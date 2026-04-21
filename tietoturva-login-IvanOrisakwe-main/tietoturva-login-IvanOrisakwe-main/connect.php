<?php
$host = 'localhost';
$db   = 'topi_2253';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
    if (basename($_SERVER['SCRIPT_NAME']) === 'connect.php') {
        echo "✅ Connection successful!";
    }
} catch (PDOException $e) {
    if (basename($_SERVER['SCRIPT_NAME']) === 'connect.php') {
        echo "❌ Connection failed: " . $e->getMessage();
    }
    throw $e;
}
