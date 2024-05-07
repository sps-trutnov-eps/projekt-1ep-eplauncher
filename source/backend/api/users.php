<?php
header('Content-Type: application/json');

require_once "../../config.php";

$spojeni = mysqli_connect(dbhost, dbuser, dbpass, dbname);

$dotaz = "SELECT * FROM 1ep_eplauncher_users";
$data = mysqli_query($spojeni, $dotaz);

mysqli_close($spojeni);

$users = [];

while($zaznam = mysqli_fetch_assoc($data)) {
    $users[] = $zaznam;
}

echo json_encode($users);
