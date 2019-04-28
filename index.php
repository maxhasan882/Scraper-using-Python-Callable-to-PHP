<?php
ini_set('max_execution_time', 0);
$command = escapeshellcmd('C:/xampp/htdocs/WEBS/hello.py');
$output = shell_exec($command);
#$mystring = exec('python hello.py', $output);
echo "Done.....!";
var_dump($output);
include "new.php"
?>