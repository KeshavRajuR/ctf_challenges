<?php 
include("mydatabase.php");
if(isset($_POST["useremail"]) && isset($_POST["userpassword"]))
{
	$user_email=$_POST["useremail"];
	$user_password = $_POST["userpassword"];
	$hash = md5(crypt($user_password,'salted'));
        $stmt=$conn->prepare("select email,password from users where email=? and password=?");
        $stmt->bind_param("ss",$user_email,$hash);
        $stmt->execute();
        $result = $stmt->get_result();
        $num_rows = $result->num_rows;
        if($num_rows > 0)
	{
		session_start();
		$_SESSION["loggedin"]=$email;
		header("location: homepage.php");
	}
	else
	{
		echo '<script>alert("Invalid username or password");window.location.href="/loginpage.php";</script>';
	}
}
else
{?>
