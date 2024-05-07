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
}

$spojeni = mysqli_connect(dbhost, dbuser, dbpass, dbname);

$dotaz = "SELECT * FROM 1ep_eplauncher_users WHERE username = '$username'";
$data = mysqli_query($spojeni, $dotaz);

mysqli_close($spojeni);

if(mysqli_num_rows($data) == 0) {
    echo json_encode(['vysledek' => 'Uživatel neexistuje.']);
    exit();
}

$zaznam = mysqli_fetch_assoc($data);
$hash = $zaznam['password'];

if(!password_verify($password, $hash)) {
    echo json_encode(['vysledek' => 'Špatné heslo.']);
    exit();
}

echo json_encode(['vysledek' => TRUE]);
