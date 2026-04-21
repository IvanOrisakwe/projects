<?php
require_once __DIR__ . '/connect.php';
require_once __DIR__ . '/auth.php';


$sql = "SELECT p.id, p.title, p.body, p.posted, p.author, u.realname
        FROM posts p
        JOIN users u ON u.id = p.author
        ORDER BY p.id DESC";
$rows = $pdo->query($sql)->fetchAll();
?>
<ul>
  <hr>
  <?php foreach ($rows as $row): ?>
    <li>
      <h3><?= htmlspecialchars($row['title']) ?></h3>
      <p><i><?= htmlspecialchars($row['posted']) ?> – <?= htmlspecialchars($row['realname']) ?></i></p>
      <p><?= nl2br(htmlspecialchars($row['body'])) ?></p>

      <?php if (canEditPost($row['author'])): ?>
        <a href="edit-post.php?id=<?= (int)$row['id'] ?>">Edit</a>
      <?php endif; ?>

      <?php if (canDeletePost($row['author'])): ?>
        &nbsp;|&nbsp;
        <a href="delete-post.php?id=<?= (int)$row['id'] ?>"
           onclick="return confirm('Delete this post?');">Delete</a>
      <?php endif; ?>
      <hr>
    </li>
  <?php endforeach; ?>
</ul>
