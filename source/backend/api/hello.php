<?php
header('Content-Type: application/json');

$data = [
    'zprava' => 'Hello there!',
];

echo json_encode($data);
