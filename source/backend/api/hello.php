<?php
header('Content-Type: application/json');

$data = [
    'text' => 'Hello there!',
];

echo json_encode($data);
