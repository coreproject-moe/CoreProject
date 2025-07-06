<?php
    $user_id = end(explode("/", $url));
    $db = pg_connect(
    "host=localhost port=5432 dbname={{ database_name }} user={{ database_user }} password={{ database_password }}"
    );
    $query =
    "SELECT "user".id AS user_id, "user".last_login AS user_last_login, "user".is_superuser AS user_is_superuser, "user".username AS user_username, "user".first_name AS user_first_name, "user".last_name AS user_last_name, "user".email AS user_email, "user".is_staff AS user_is_staff, "user".is_active AS user_is_active, "user".discriminator ASuser_discriminator, "user".avatar AS user_avatar,"user".avatar_provider AS user_avatar_provider, "user".ip AS user_ip,"user".date_joined AS user_date_joined FROM "user" WHERE "user".id = $user_id";
    $result = pg_query($db, $query);
    $row = pg_fetch_assoc($result);
    echo 'User not found $row["id"]';
?>

User not found {{ user_id }}
