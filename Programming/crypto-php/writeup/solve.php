<?php
	$hash = 'e7925ce09ec0eac25293ead97f7bdaf0';
	$salt = 'salted';
	$wordlist = fopen("rockyou.txt","r");
	while(! feof($wordlist))
	{
		$str = trim(fgets($wordlist));
		$new_hash = md5(crypt($str, $salt));
		if($hash == $new_hash)
		{
			echo "Flag Found: flag{". $str."}\n";
			fclose($wordlist);
			exit(0);
		}
	}
	fclose($wordlist);
?>
