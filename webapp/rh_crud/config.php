<?php
/**
 * AtlasTech HR CRUD - Configuration
 * VULNERABILITY: Credentials stored in plain text
 */
$host = "localhost";
$db   = "RH";
$user = "RH";
$pass = "StrongPassword123";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Database connection failed: " . $conn->connect_error);
}
?>
