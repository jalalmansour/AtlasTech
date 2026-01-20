<?php
/**
 * AtlasTech HR CRUD - Add Employee
 * VULNERABILITY: Direct SQL concatenation (SQL Injection possible)
 */
include "config.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // VULNERABILITY: No input sanitization - SQL Injection vector
    $sql = "INSERT INTO employees (firstname, lastname, email, position, salary)
            VALUES (
                '{$_POST['firstname']}',
                '{$_POST['lastname']}',
                '{$_POST['email']}',
                '{$_POST['position']}',
                '{$_POST['salary']}'
            )";
    $conn->query($sql);
    header("Location: index.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Employee - AtlasTech HR</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="glass-container">
        <header>
            <h1>➕ Add New Employee</h1>
            <p class="subtitle">Fill in the employee details below</p>
        </header>

        <div class="form-container">
            <form method="POST">
                <div class="form-group">
                    <label for="firstname">First Name</label>
                    <input type="text" id="firstname" name="firstname" placeholder="Enter first name" required>
                </div>
                
                <div class="form-group">
                    <label for="lastname">Last Name</label>
                    <input type="text" id="lastname" name="lastname" placeholder="Enter last name" required>
                </div>
                
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" placeholder="employee@atlastech.ma" required>
                </div>
                
                <div class="form-group">
                    <label for="position">Position</label>
                    <input type="text" id="position" name="position" placeholder="e.g. Software Developer" required>
                </div>
                
                <div class="form-group">
                    <label for="salary">Salary (MAD)</label>
                    <input type="number" id="salary" name="salary" placeholder="15000.00" step="0.01" required>
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn btn-submit">💾 Save Employee</button>
                    <a href="index.php" class="btn btn-cancel">← Cancel</a>
                </div>
            </form>
        </div>

        <footer>
            <p>© 2024 AtlasTech Solutions - Internal Use Only</p>
        </footer>
    </div>
</body>
</html>
