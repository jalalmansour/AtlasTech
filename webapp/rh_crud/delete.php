<?php
/**
 * AtlasTech HR CRUD - Delete Employee
 * VULNERABILITY: No CSRF protection, SQL Injection, IDOR
 */
include "config.php";

// VULNERABILITY: Directly using user input in SQL query
$id = $_GET['id'];

// VULNERABILITY: SQL Injection - id not sanitized
$conn->query("DELETE FROM employees WHERE id=$id");

header("Location: index.php");
exit;
?>
