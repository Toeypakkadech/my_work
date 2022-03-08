<html>
<head>

<meta charset="UTF-8">
</head>

<body>


<form action="" method="POST">
   รหัสพนักงาน<input type="text" name="txtEmpNum"  placeholder="รหัสพนักงาน"><br>
  ชื่อพนักงาน<input type="text" name="txtEmpName"  placeholder="ชื่อพนักงาน"><br>
   <select name = "ddlPosition" id = "ddlPosition">
   <option value="">Chosse Position</option>
    <option value="Managing Director">Managing Director</option>
    <option value="Manager">Manager</option>
    <option value="Supervisor">Supervisor</option>
    <option value="Clerk">Clerk</option>
    <option value="Saleman">Saleman</option>
   </select>
    <br>
<input type="submit" value="ตกลง" >
<input type="reset" value="ยกเลิก" >
</form>

</body>
</html>
<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "temployee";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
if(empty($_POST['txtEmpNum'])){
	
	echo "<script language=\"JavaScript\">";
	echo "alert('คุณยังไม่ได้กรอกข้อมูลรหัสพนักงาน')";
	echo "</script>";
}
elseif(empty($_POST['txtEmpName'])){
    echo "<script language=\"JavaScript\">";
	echo "alert('คุณยังไม่ได้กรอกชื่อพนักงาน')";
	echo "</script>";
}
elseif(empty($_POST['ddlPosition'])){
    echo "<script language=\"JavaScript\">";
	echo "alert('คุณยังไม่ได้กรอกตำแหน่งพนักงาน')";
	echo "</script>";
}
else {
    $txtEmpNum = trim($_POST['txtEmpNum']);
	$txtEmpName = trim($_POST['txtEmpName']);
    $Position = trim($_POST['ddlPosition']);
    $sl = "INSERT INTO `employee`(`EmpNum`, `EmpName`, `Position`) 
            VALUES ('$txtEmpNum', '$txtEmpName', '$Position');";
    $slq = mysqli_query($conn, $sl);
    if ($slq){
        echo "เพื่มข้อมูลสำเร็จ";
        mysqli_close($conn);
    }
    else{
        echo "เพิ่มข้อมูลไม่สำเร็จ";
    }
}

?>
