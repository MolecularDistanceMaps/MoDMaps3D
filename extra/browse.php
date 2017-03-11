<?php
	$root = __DIR__."/../maps";
	//print_r(glob($root.'/*'));
	$output="";
	foreach (glob($root.'/*') as $file) {
	    $file = realpath($file);
	    $link = substr($file, strlen($root) + 1);
	    $output.=$link."#";
	}
	echo substr($output,0,strlen($output)-1);
?>