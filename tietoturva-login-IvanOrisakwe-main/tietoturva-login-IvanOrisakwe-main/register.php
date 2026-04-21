<?php
session_start();
?>
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>Create user</title>
<style>
  body {font-family: system-ui, Arial, sans-serif; max-width: 600px; margin: 2rem auto; padding: 0 1rem;}
  label {display:block; margin:.5rem 0 .25rem;}
  input {width:100%; padding:.5rem; margin-bottom:.75rem;}
  button {padding:.5rem 1rem; cursor:pointer;}
  .msg {margin: .5rem 0; color: #d00;}
</style>
<h1>Create user</h1>

<?php if (!empty($_GET['e'])): ?>
  <p class="msg"><?= htmlspecialchars($_GET['e']) ?></p>
<?php endif; ?>

<form method="post" action="register_handler.php" autocomplete="off">
  <label>Username</label>
  <input name="username" required>

  <label>Real name</label>
  <input name="real_name" required>

  <label>Password</label>
  <input name="password" type="password" required minlength="6">

  <button type="submit">Create account</button>
</form>

<p><a href="login.php">Back to login</a></p>
</html>
