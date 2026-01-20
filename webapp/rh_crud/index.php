<?php
include "config.php";
$result = $conn->query("SELECT * FROM employees");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AtlasTech HR Portal</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="glass-container">
        <header>
            <h1>🏢 AtlasTech HR Portal</h1>
            <p class="subtitle">Employee Management System</p>
        </header>

        <nav class="actions">
            <a href="add.php" class="btn btn-primary">➕ Add Employee</a>
        </nav>

        <main>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Full Name</th>
                        <th>Email</th>
                        <th>Position</th>
                        <th>Salary (MAD)</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while($row = $result->fetch_assoc()): ?>
                    <tr>
                        <td><?= $row['id'] ?></td>
                        <td class="name-cell"><?= $row['firstname'] . " " . $row['lastname'] ?></td>
                        <td><?= $row['email'] ?></td>
                        <td><?= $row['position'] ?></td>
                        <td class="salary"><?= number_format($row['salary'], 2) ?></td>
                        <td class="actions-cell">
                            <a href="edit.php?id=<?= $row['id'] ?>" class="btn btn-edit">✏️ Edit</a>
                            <a href="delete.php?id=<?= $row['id'] ?>" class="btn btn-delete" onclick="return confirm('Are you sure you want to delete this employee?')">🗑️ Delete</a>
                        </td>
                    </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
        </main>

        <footer>
            <p>© 2024 AtlasTech Solutions - Internal Use Only</p>
        </footer>
    </div>
</body>
</html>
