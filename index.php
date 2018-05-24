<html>
    <body>

        <form>
            <input type="submit" name="outside" value="Outside" />
            <input type="submit" name="inside" value="Inside" />
        </form>

        <?php
            /*if (isset($_REQUEST["outside"])){
                echo shell_exec("python3 /var/www/html/outside.py");
            }
            
            if (isset($_REQUEST["inside"])){
                echo shell_exec("python3 /var/www/html/inside.py");
            }*/
            header("refresh:10;");
            echo("Outside temperature is: ");
            echo shell_exec("python3 /var/www/html/outside.py");
            echo("<br>"."Inside temperature is: ");
            echo shell_exec("python3 /var/www/html/inside.py");
        ?>

    </body>
</html>