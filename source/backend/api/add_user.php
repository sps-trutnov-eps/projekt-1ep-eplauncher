<?php
header('Content-Type: application/json');

require_once "../../config.php";

$json = file_get_contents("php://input");
$data = json_decode($json, true);

$username = trim($data['username']);
$password = trim($data['password']);

if($username == '' || $password == '') {
    echo json_encode(['vysledek' => 'Nevyplněné údaje.']);
    exit();
} else {
    $password = password_hash($password, PASSWORD_BCRYPT);
}

$spojeni = mysqli_connect(dbhost, dbuser, dbpass, dbname);

$dotaz = "INSERT INTO 1ep_eplauncher_users (username, password) VALUES ('$username', '$password')";

if(!mysqli_query($spojeni, $dotaz)) {
    echo json_encode(['vysledek' => mysqli_error($spojeni)]);
} else {
    echo json_encode(['vysledek' => TRUE]);
}

mysqli_close($spojeni);
