<?php
session_start();
require_once __DIR__ . '/connect.php';


$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $username = trim($_POST['username'] ?? '');
  $password = $_POST['password'] ?? '';

  if ($username === '' || $password === '') {
    $error = 'Please enter username and password.';
  } else {
    // NOTE: If later you drop the legacy 'password' column, remove it from SELECT and fallback code.
    $stmt = $pdo->prepare('SELECT id, username, realname, role, password_hash, password FROM users WHERE username = :u');
    $stmt->execute([':u' => $username]);
    $user = $stmt->fetch();

    $ok = false;
    if ($user) {
      if (!empty($user['password_hash'])) {
        $ok = password_verify($password, $user['password_hash']);
      } elseif (isset($user['password']) && $user['password'] !== '') {
        // legacy fallback (remove after migration + dropping column)
        $ok = hash_equals($user['password'], $password);
      }
    }

    if ($ok) {
      $_SESSION['user_id']  = $user['id'];
      $_SESSION['username'] = $user['username'];
      $_SESSION['realname'] = $user['realname'];
      $_SESSION['role']     = $user['role'] ?? 'user';
      header('Location: home.php');
      exit;
    } else {
      $error = 'Invalid username or password.';
    }
  }
}
?>
<!doctype html>
<html lang="fi">
<meta charset="utf-8">
<title>Login</title>
<style>
  body {font-family: system-ui, Arial, sans-serif; max-width: 600px; margin: 2rem auto; padding: 0 1rem;}
  label {display:block; margin:.5rem 0 .25rem;}
  input {width:100%; padding:.5rem; margin-bottom:.75rem;}
  button, input[type=submit] {padding:.5rem 1rem; cursor:pointer;}
  .error {color:#d00; margin:.5rem 0;}
</style>
<h1>Login</h1>

<?php if ($error): ?>
  <p class="error"><?= htmlspecialchars($error) ?></p>
<?php endif; ?>

<form method="post" autocomplete="off">
  <label>Username</label>
  <input name="username" required>

  <label>Password</label>
  <input name="password" type="password" required>

  <input type="submit" value="Sign in">
</form>

<p>Don’t have an account? <a href="register.php">Create one</a></p>
</html>
