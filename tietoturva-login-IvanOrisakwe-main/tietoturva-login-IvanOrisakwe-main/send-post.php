<?php
session_start();
if (!isset($_SESSION['user_id'])) { header('Location: index.php'); exit; }

require __DIR__ . '/connect.php';

$title  = trim($_POST['title'] ?? '');
$body   = trim($_POST['body'] ?? '');
$author = $_SESSION['user_id'];

if ($title === '' || $body === '') {
  header('Location: home.php'); exit;
}

$stmt = $pdo->prepare("INSERT INTO posts (title, body, author, posted) VALUES (:t, :b, :a, CURRENT_DATE())");
$stmt->execute([':t'=>$title, ':b'=>$body, ':a'=>$author]);

header('Location: home.php');
exit;
