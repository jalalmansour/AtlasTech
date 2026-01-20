"""
Provisioner
-----------
Configures the target server via SSH.
Installs the Vulnerable LAMP Stack and HR Application.
"""

import paramiko
import time
import logging
import os
from ..config import Config

logger = logging.getLogger("AtlasTech.Provisioner")

class Provisioner:
    def __init__(self, ip):
        self.ip = ip
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.client.connect(self.ip, username=Config.LAB_SSH_USER, password=Config.LAB_SSH_PASS)
            logger.info(f"SSH Connected to {self.ip}")
            return True
        except Exception as e:
            logger.error(f"SSH Connection failed: {e}")
            return False

    def execute(self, cmd, sudo=False):
        if sudo:
            cmd = f"echo '{Config.LAB_SSH_PASS}' | sudo -S {cmd}"
        
        logger.debug(f"Executing: {cmd}")
        stdin, stdout, stderr = self.client.exec_command(cmd)
        exit_status = stdout.channel.recv_exit_status()
        out = stdout.read().decode().strip()
        err = stderr.read().decode().strip()

        if exit_status != 0:
            logger.error(f"Command failed: {cmd}\nError: {err}")
            return None
        return out

    def deploy_vulnerable_stack(self):
        logger.info("Starting Vulnerable Stack Deployment...")
        
        # 1. Install Packages (Apache, PHP, MariaDB)
        # Note: In a real "outdated" lab, we'd pin old versions or download .debs
        # For this script, we assume the base OS has standard repos, but we configure them insecurely.
        setup_cmds = [
            "apt-get update",
            "DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 mariadb-server php php-mysql php-cli"
        ]
        
        for cmd in setup_cmds:
            self.execute(cmd, sudo=True)

        # 2. Database Setup (Weak Config)
        sql_setup = f"""
        CREATE DATABASE IF NOT EXISTS atlas_rh;
        -- WEAKNESS: Root user accessible from localhost with known pass
        ALTER USER 'root'@'localhost' IDENTIFIED BY '{Config.LAB_DB_ROOT_PASS}';
        -- WEAKNESS: App user has too many privileges
        CREATE USER IF NOT EXISTS 'atlas_app'@'%' IDENTIFIED BY '{Config.LAB_DB_APP_PASS}';
        GRANT ALL PRIVILEGES ON *.* TO 'atlas_app'@'%';
        FLUSH PRIVILEGES;
        
        USE atlas_rh;
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            ssn VARCHAR(20), -- PII Plaintext
            salary INT,
            password VARCHAR(100) -- Plaintext storage
        );
        INSERT INTO employees (name, ssn, salary, password) VALUES 
        ('Alice CEO', '123-44-555', 150000, 'alice_boss'),
        ('Bob Dev', '999-11-222', 90000, 'dev_rules');
        """
        
        # Write SQL to file and execute
        self.execute(f"echo \"{sql_setup}\" > /tmp/setup.sql")
        self.execute("mysql -u root < /tmp/setup.sql", sudo=True) # Assuming no root pass yet or handled above

        # 3. Deploy Vulnerable PHP App
        self._deploy_php_files()

        logger.info("Vulnerable Stack Deployed Successfully.")

    def _deploy_php_files(self):
        """Writes the vulnerable PHP files directly to the server"""
        web_root = "/var/www/html/hr"
        self.execute(f"mkdir -p {web_root}", sudo=True)
        self.execute(f"chown -R www-data:www-data {web_root}", sudo=True)
        self.execute(f"chmod -R 777 {web_root}", sudo=True) # WEAKNESS: World Writable

        # Vulnerable Login (SQL Injection)
        login_php = f"""<?php
        $conn = new mysqli('localhost', 'atlas_app', '{Config.LAB_DB_APP_PASS}', 'atlas_rh');
        if(isset($_POST['user'])) {{
            $user = $_POST['user']; // VULN: No sanitization
            $pass = $_POST['pass'];
            // SQL Injection Vector
            $sql = "SELECT * FROM employees WHERE name = '$user' AND password = '$pass'";
            $result = $conn->query($sql);
            if($result->num_rows > 0){{
                echo "<h1>Welcome, Admin!</h1><pre>";
                while($row = $result->fetch_assoc()) {{ print_r($row); }}
                echo "</pre>";
            }} else {{
                echo "Invalid credentials";
            }}
        }}
        ?>
        <form method='POST'>
        User: <input type='text' name='user'><br>
        Pass: <input type='password' name='pass'><br>
        <button>Login</button>
        </form>
        """
        
        # Use SFTP to write
        sftp = self.client.open_sftp()
        with sftp.file(f"/tmp/login.php", 'w') as f:
            f.write(login_php)
        sftp.close()
        
        self.execute(f"mv /tmp/login.php {web_root}/login.php", sudo=True)
