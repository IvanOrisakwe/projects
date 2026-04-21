<?php
session_start();
require_once __DIR__ . '/connect.php';
require_once __DIR__ . '/auth.php';


if (!isset($_SESSION['user_id'])) { header('Location: index.php'); exit; }
if (!isAdmin()) { http_response_code(403); exit('Forbidden'); }

$id = (int)($_GET['id'] ?? 0);
if ($id > 0) {
  $del = $pdo->prepare("DELETE FROM posts WHERE id = :id");
  $del->execute([':id' => $id]);
}
header('Location: home.php');
exit;
