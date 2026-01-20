<?php
/**
 * AtlasTech HR CRUD - Edit Employee
 * VULNERABILITY: Direct SQL concatenation and IDOR (Insecure Direct Object Reference)
 */
include "config.php";

// VULNERABILITY: No authentication check - anyone can access
// VULNERABILITY: IDOR - ID directly from GET parameter without validation
$id = $_GET['id'];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // VULNERABILITY: SQL Injection via POST parameters
    $sql = "UPDATE employees SET
        firstname='{$_POST['firstname']}',
        lastname='{$_POST['lastname']}',
        email='{$_POST['email']}',
        position='{$_POST['position']}',
        salary='{$_POST['salary']}'
        WHERE id=$id";
    $conn->query($sql);
    header("Location: index.php");
    exit;
}

// VULNERABILITY: SQL Injection via GET parameter
$result = $conn->query("SELECT * FROM employees WHERE id=$id");
$emp = $result->fetch_assoc();

if (!$emp) {
    die("Employee not found.");
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Employee - AtlasTech HR</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="glass-container">
        <header>
            <h1>✏️ Edit Employee</h1>
            <p class="subtitle">Update employee information</p>
        </header>

        <div class="form-container">
            <form method="POST">
                <div class="form-group">
                    <label for="firstname">First Name</label>
                    <input type="text" id="firstname" name="firstname" value="<?= htmlspecialchars($emp['firstname']) ?>" required>
                </div>
                
                <div class="form-group">
                    <label for="lastname">Last Name</label>
                    <input type="text" id="lastname" name="lastname" value="<?= htmlspecialchars($emp['lastname']) ?>" required>
                </div>
                
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" value="<?= htmlspecialchars($emp['email']) ?>" required>
                </div>
                
                <div class="form-group">
                    <label for="position">Position</label>
                    <input type="text" id="position" name="position" value="<?= htmlspecialchars($emp['position']) ?>" required>
                </div>
                
                <div class="form-group">
                    <label for="salary">Salary (MAD)</label>
                    <input type="number" id="salary" name="salary" value="<?= htmlspecialchars($emp['salary']) ?>" step="0.01" required>
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn btn-submit">💾 Update Employee</button>
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
