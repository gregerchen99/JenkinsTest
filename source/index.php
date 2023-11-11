<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    /*
     * Check if password is set and is not empty
     */
    if (isset($_POST["password"]) && !empty($_POST["password"])) {
    	/*
    	 * Retrieve the password from the form and store into $password
    	 */
        $password = $_POST["password"]; 

        $isExists = False;
        $lines = file('blacklist.txt');
        /*
         * Iterate through each line of password in blacklist.txt
         */
        foreach ($lines as $line) {
        	if ($line == $password) {
        		$isExists = True;
        		break;
        	}
        }

        /*
         * Check if isExist flag is set
         */
        if ($isExists == True)
        {
        	header("Location: index.html");
        }
        else if ($isExists == False)
        {
        	?>
            <!DOCTYPE html>
        	<html lang="en">        		
                <head>
    				<title>Home</title>
				</head>
				<body>

					<h1>Home</h1>

					<p>Your password is: <?php echo $password; ?></p>

					<a href="index.html"><button type="button" id="returnButton">Return</button></a>

				</body>
        	</html>
        	<?php
        }
    }
    else
    {
    	header("Location: index.html");
    }
}
else
{
	header("Location: index.html");
}
?>
