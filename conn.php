<?php
$conn = mysqli_connect("localhost","root","","email")
if (!$con)
{
die('Could not connect: ' . mysql_error());
}

$sql="INSERT INTO details VALUES('$_POST[email]')";
if (!mysqli_query($con,$sql))
{
die('Error: ' . mysqli_error());
}
echo "1 Record Added";
mysqli_close($con);
?>