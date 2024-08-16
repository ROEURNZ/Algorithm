<?php
function addOneToBinary($binaryStr) {
    // Initialize the result string and carry
    $result = '';
    $carry = 1;  // We are adding one, so the initial carry is 1

    // Loop through the binary string from the end to the beginning
    for ($i = strlen($binaryStr) - 1; $i >= 0; $i--) {
        $char = $binaryStr[$i];
        if ($char == '0') {
            if ($carry) {
                $result = '1' . $result;
                $carry = 0;
            } else {
                $result = '0' . $result;
            }
        } else {  // $char == '1'
            if ($carry) {
                $result = '0' . $result;
                $carry = 1;  // Still need to carry over
            } else {
                $result = '1' . $result;
            }
        }
    }

    // If there's still a carry left after the loop, prepend '1' to the result
    if ($carry) {
        $result = '1' . $result;
    }

    return $result;
}

// Input from the user
echo "Enter a binary string: ";
$handle = fopen("php://stdin", "r");
$n = trim(fgets($handle));
fclose($handle);

$result = addOneToBinary($n);
echo "The binary representation of $n + 1 is $result\n";
