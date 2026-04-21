<?php
session_start();
require_once __DIR__ . '/connect.php';
require_once __DIR__ . '/auth.php';


if (!isset($_SESSION['user_id'])) { header('Location: index.php'); exit; }

$id = (int)($_GET['id'] ?? $_POST['id'] ?? 0);
if ($id <= 0) { header('Location: home.php'); exit; }

$stmt = $pdo->prepare("SELECT id, title, body, author FROM posts WHERE id = :id");
$stmt->execute([':id' => $id]);
$post = $stmt->fetch();
if (!$post) { header('Location: home.php'); exit; }

if (!canEditPost($post['author'])) {
  http_response_code(403);
  exit('Forbidden');
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $title = trim($_POST['title'] ?? '');
  $body  = trim($_POST['body']  ?? '');
  if ($title === '' || $body === '') {
    $error = 'Title and body are required.';
  } else {
    $upd = $pdo->prepare("UPDATE posts SET title = :t, body = :b WHERE id = :id");
    $upd->execute([':t'=>$title, ':b'=>$body, ':id'=>$id]);
    header('Location: home.php'); exit;
  }
}
?>
<!doctype html>
<meta charset="utf-8">
<title>Edit post</title>
<h1>Edit post</h1>

<?php if (!empty($error)): ?>
  <p style="color:#d00"><?= htmlspecialchars($error) ?></p>
<?php endif; ?>

<form method="post">
  <input type="hidden" name="id" value="<?= (int)$post['id'] ?>">
  <p><label>Title<br>
    <input name="title" value="<?= htmlspecialchars($post['title']) ?>" required></label></p>
  <p><label>Body<br>
    <textarea name="body" rows="6" required><?= htmlspecialchars($post['body']) ?></textarea></label></p>
  <p><button type="submit">Save</button> <a href="home.php">Cancel</a></p>
</form>
