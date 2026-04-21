<?php if (!isset($_SESSION['user_id'])) { return; } ?>
<h3>Uusi posti</h3>
<form method="post" action="send-post.php" autocomplete="off">
  <p><input type="text" name="title" placeholder="Otsikko" required></p>
  <p><textarea name="body" placeholder="Sisältö" rows="5" required></textarea></p>
  <p><button type="submit">Send</button></p>
</form>
