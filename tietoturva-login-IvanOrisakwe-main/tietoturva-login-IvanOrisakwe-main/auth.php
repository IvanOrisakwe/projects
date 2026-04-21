<?php
if (session_status() !== PHP_SESSION_ACTIVE) { session_start(); }

if (!function_exists('currentUserId')) {
  function currentUserId() { return $_SESSION['user_id'] ?? null; }
}
if (!function_exists('currentRole')) {
  function currentRole() { return $_SESSION['role'] ?? 'user'; }
}
if (!function_exists('isAdmin')) {
  function isAdmin() { return currentRole() === 'admin'; }
}
if (!function_exists('isModerator')) {
  function isModerator() { return currentRole() === 'moderator'; }
}
if (!function_exists('canEditPost')) {
  function canEditPost($authorId) {
    return isAdmin() || isModerator() || ($authorId == currentUserId());
  }
}
if (!function_exists('canDeletePost')) {
  function canDeletePost($authorId) {
    return isAdmin(); // only admins delete
  }
}
