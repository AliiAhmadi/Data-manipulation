<?php

$date = $_POST['date'];
// $date = readline();


$date = new DateTime($date);

$today = new DateTime("2023-05-13");

if ($date < $today) {
    echo "gone";
} else {
    $interval = $today->diff($date);

    echo $interval->days;
}
