<?php
header('Content-Type: application/json');

require_once "../../config.php";

$json = file_get_contents("php://input");
$data = json_decode($json, true);

$user = trim($data['username']);
$game = trim($data['game_name']);
$check = trim($data['checksum']);
$achievement = trim($data['achievement']);

if($user == '' || $game == '' || $check == '') {
    echo json_encode(['vysledek' => 'Nekompletní údaje.']);
    exit();
}

$spojeni = mysqli_connect(dbhost, dbuser, dbpass, dbname);

$dotaz = "SELECT * FROM 1ep_eplauncher_users WHERE username = '$user'";
$data = mysqli_query($spojeni, $dotaz);

if(mysqli_num_rows($data) == 0) {
    echo json_encode(['vysledek' => 'Uživatel neexistuje.']);
    mysqli_close($spojeni);
    exit();
}

$zaznam = mysqli_fetch_assoc($data);
$user_id = $zaznam['id'];

$dotaz = "SELECT * FROM 1ep_eplauncher_games WHERE name = '$game'";
$data = mysqli_query($spojeni, $dotaz);

if(mysqli_num_rows($data) == 0) {
    echo json_encode(['vysledek' => 'Hra neexistuje.']);
    mysqli_close($spojeni);
    exit();
}

$zaznam = mysqli_fetch_assoc($data);
$sum = $zaznam['checksum'];
$game_id = $zaznam['id'];

if($check != $sum) {
    echo json_encode(['vysledek' => 'Porušena integrita hry.']);
    mysqli_close($spojeni);
    exit();
}

$dotaz = "SELECT * FROM 1ep_eplauncher_achievements WHERE game_id = '$game_id' AND name = '$achievement'";
$data = mysqli_query($spojeni, $dotaz);

if(mysqli_num_rows($data) == 0) {
    echo json_encode(['vysledek' => 'Hra nemá achievementy.']);
    mysqli_close($spojeni);
    exit();
}

$zaznam = mysqli_fetch_assoc($data);
$achievement_id = $zaznam['id'];
$castka = $zaznam['amount'];

$dotaz = "SELECT * FROM 1ep_eplauncher_achieved WHERE user_id = '$user_id' AND achievement_id = '$achievement_id'";
$data = mysqli_query($spojeni, $dotaz);

if(mysqli_num_rows($data) > 0) {
    echo json_encode(['vysledek' => 'Tento hráč již tento achievement získal.']);
    mysqli_close($spojeni);
    exit();
}

$dotaz = "INSERT INTO 1ep_eplauncher_achieved (user_id, achievement_id) VALUES ('$user_id', '$achievement_id')";

if(!mysqli_query($spojeni, $dotaz)) {
    echo json_encode(['vysledek' => mysqli_error($spojeni)]);
    mysqli_close($spojeni);
    exit();
}

$dotaz = "UPDATE 1ep_eplauncher_users SET money = money + '$castka' WHERE id = '$user_id'";

if(!mysqli_query($spojeni, $dotaz)) {
    echo json_encode(['vysledek' => mysqli_error($spojeni)]);
    mysqli_close($spojeni);
    exit();
}

echo json_encode(['vysledek' => true]);
mysqli_close($spojeni);
