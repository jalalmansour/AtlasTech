<?php
/**
 * AtlasTech HR CRUD - Login Page
 * VULNERABILITY: SQL Injection authentication bypass
 * VULNERABILITY: Passwords stored/compared in plaintext
 */
session_start();
include "config.php";

$error = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    // VULNERABILITY: Direct SQL concatenation - Authentication bypass possible
    // Payload: admin'-- or ' OR '1'='1
    $sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
    $result = $conn->query($sql);
    
    if ($result && $result->num_rows > 0) {
        $user = $result->fetch_assoc();
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        $_SESSION['role'] = $user['role'];
        header("Location: index.php");
        exit;
    } else {
        $error = "Invalid username or password";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - AtlasTech HR Portal</title>
    <link rel="stylesheet" href="style.css">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        
        .login-container {
            width: 100%;
            max-width: 420px;
        }
        
        .login-logo {
            font-size: 4rem;
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .error-message {
            background: rgba(239, 68, 68, 0.9);
            color: white;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            text-align: center;
        }
        
        .demo-credentials {
            background: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1.5rem;
            font-size: 0.85rem;
            color: rgba(255, 255, 255, 0.8);
        }
        
        .demo-credentials h4 {
            color: white;
            margin-bottom: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="glass-container login-container">
        <header>
            <div class="login-logo">🔐</div>
            <h1>AtlasTech HR</h1>
            <p class="subtitle">Employee Management Portal</p>
        </header>

        <?php if ($error): ?>
        <div class="error-message">
            ⚠️ <?= htmlspecialchars($error) ?>
        </div>
        <?php endif; ?>

        <div class="form-container">
            <form method="POST">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" name="username" placeholder="Enter your username" required>
                </div>
                
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" placeholder="Enter your password" required>
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn btn-primary" style="width: 100%;">🔑 Sign In</button>
                </div>
            </form>
        </div>

        <div class="demo-credentials">
            <h4>📋 Demo Credentials</h4>
            <p>Admin: admin / admin123<br>
            HR User: hr_user / hr2024</p>
        </div>

        <footer>
            <p>© 2024 AtlasTech Solutions</p>
        </footer>
    </div>
</body>
</html>
