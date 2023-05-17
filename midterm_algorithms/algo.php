<?php

$x = explode(" ", readline());

$n = (int)$x[0];
$m = (int)$x[1];

$Fake_hs = explode(" ", readline());
$hs = [];

foreach ($Fake_hs as $value) {
    $hs[] = (int)$value;
}

$string = str_split(readline());

/////////////////////////////////////////////////

function right_to_left()
{
    global $hs;

    for ($i = count($hs) - 1; $i >= 0; $i--) {
        if ($hs[$i] < max(array_slice($hs, $i))) {
            $hs[$i] += 1;
        }
    }
}


function left_to_right()
{
    global $hs;

    for ($i = 0; $i <= count($hs) - 1; $i++) {
        if ($hs[$i] < max(array_slice($hs, 0, $i + 1))) {
            $hs[$i] += 1;
        }
    }
}


/////////////////////////////////////



foreach ($string as $char) {
    if ($char == "R") {
        right_to_left();
    } else {
        left_to_right();
    }
}

# 1 3 1 3 1
# 1 3 2 3 1
# 2 3 2 3 1

# 

echo implode(" ", $hs);
