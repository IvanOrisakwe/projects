<?php
session_start();
require __DIR__ . '/connect.php';

function back($msg) {
  header('Location: register.php?e=' . urlencode($msg));
  exit;
}

$username = trim($_POST['username'] ?? '');
$realName = trim($_POST['real_name'] ?? '');
$password = $_POST['password'] ?? '';
$role     = trim($_POST['role'] ?? ''); // optional

if ($username === '' || $realName === '' || $password === '') {
  back('All fields are required.');
}
if (strlen($password) < 6) {
  back('Password must be at least 6 characters.');
}

$check = $pdo->prepare('SELECT 1 FROM users WHERE username = :u');
$check->execute([':u' => $username]);
if ($check->fetch()) {
  back('Username is already taken.');
}

$hash = password_hash($password, PASSWORD_DEFAULT);
if (!in_array($role, ['admin','moderator','user'], true)) {
  $role = 'user';
}

$ins = $pdo->prepare('INSERT INTO users (username, realname, role, password_hash) VALUES (:u, :n, :r, :h)');
$ins->execute([':u'=>$username, ':n'=>$realName, ':r'=>$role, ':h'=>$hash]);

// auto-login
$stmt = $pdo->prepare('SELECT id, username, realname, role FROM users WHERE username = :u');
$stmt->execute([':u' => $username]);
$user = $stmt->fetch();

$_SESSION['user_id']  = $user['id'];
$_SESSION['username'] = $user['username'];
$_SESSION['realname'] = $user['realname'];
$_SESSION['role']     = $user['role'];

header('Location: home.php');
exit;
