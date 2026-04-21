<?php
session_start();
if (!isset($_SESSION['user_id'])) { header('Location: index.php'); exit; }
require_once __DIR__ . '/connect.php';
require_once __DIR__ . '/auth.php';

?>
<!DOCTYPE html>
<html lang="fi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Super foorumi</title>
</head>
<body>
  <h1>Super foorumi</h1>
  <p>
    Tervetuloa
    <?= htmlspecialchars($_SESSION['realname'] ?? $_SESSION['username'] ?? '') ?>
    (<?= htmlspecialchars($_SESSION['role'] ?? 'user') ?>)
    <a href="logout.php"><button>Kirjaudu ulos</button></a>
  </p>

  <?php
    include __DIR__ . '/posts.php';
    include __DIR__ . '/post-form.php';
  ?>
</body>
</html>
