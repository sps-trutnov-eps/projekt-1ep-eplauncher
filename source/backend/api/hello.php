<?php
header('Content-Type: application/json');

$hello = [
    'message' => 'Hello there!',
];

echo json_encode($hello);
