<html>
	<head>
		<title>
			Auth App 
		</title>
		<style>
			*{
				font-size:40px;
				text-align:center;
				font-family:Cambria;
			}
			body{
				background-color:lightblue;
			}
		</style>
	</head>
	<body>
		<h1> Signup Page </h1>
		<a href="/"> Existing Users Click Here </a>
		<br><br>
		<form method="POST">
			<input type="text"	name="un"	placeholder="Enter username"	required/>	<br><br>
			<input type="password"	name="pw"	placeholder="Enter password"	required/>	<br><br>
			<input type="password"	name="cpw"	placeholder="Confirm Password"	required/>	<br><br>
			<input type="Submit"	value="Register"/>
		</form>
			<h2> {{ msg }} </h2>
	</body>
</html>
