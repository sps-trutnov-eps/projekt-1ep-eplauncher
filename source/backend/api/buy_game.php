<?php
header('Content-Type: application/json');

require_once "../../config.php";

// prijeti dat z requestu
$json = file_get_contents("php://input");
$data = json_decode($json, true);

$username = trim($data['username']);
$password = trim($data['password']);
$game_id = trim($data['game_id']);

$spojeni = mysqli_connect(dbhost, dbuser, dbpass, dbname);

// kontrola jmena a hesla
if($username == '' || $password == '') {
    echo json_encode(['vysledek' => 'Nevyplněné údaje.']);
    mysqli_close($spojeni);
    exit();
}

$dotaz = "SELECT * FROM 1ep_eplauncher_users WHERE username = '$username'";
$data = mysqli_query($spojeni, $dotaz);

if(mysqli_num_rows($data) == 0) {
    echo json_encode(['vysledek' => 'Uživatel neexistuje.']);
    mysqli_close($spojeni);
    exit();
}

$user = mysqli_fetch_assoc($data);
$hash = $user['password'];

if(!password_verify($password, $hash)) {
    echo json_encode(['vysledek' => 'Špatné heslo.']);
    mysqli_close($spojeni);
    exit();
}

// kontrola predchoziho vlastnictvi hry
$user_id = $user['id'];

$dotaz = "SELECT * FROM 1ep_eplauncher_owned WHERE user_id = '$user_id' AND game_id = '$game_id'";
$data = mysqli_query($spojeni, $dotaz);

if(mysqli_num_rows($data) > 0) {
    echo json_encode(['vysledek' => 'Uživatel již hru vlastní.']);
    mysqli_close($spojeni);
    exit();
}

// kontrola dostatku financi
$cash = $user['money'];

$dotaz = "SELECT * FROM 1ep_eplauncher_games WHERE id = '$game_id'";
$data = mysqli_query($spojeni, $dotaz);

$game = mysqli_fetch_assoc($data);
$price = $game['price'];

if($cash < $price) {
    echo json_encode(['vysledek' => 'Nedostatek financí.']);
    mysqli_close($spojeni);
    exit();
}

// koupit hru
$dotaz = "UPDATE 1ep_eplauncher_users SET money = money - '$price' WHERE id = '$user_id'";
mysqli_query($spojeni, $dotaz);

$dotaz = "INSERT INTO 1ep_eplauncher_owned (user_id, game_id) VALUES ('$user_id', '$game_id')";
mysqli_query($spojeni, $dotaz);

echo json_encode(['vysledek' => TRUE]);
mysqli_close($spojeni);
