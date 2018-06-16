<!DOCTYPE html>
<html lang="en">
<head>
    <title>Home Temperature</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
</head>
    <body>
        <div class="container h-100 text-center">
            <div class="row h-100 justify-content-center align-items-center">
                
                <div class="card">
                    <img class="card-img-top" src="..." alt="Card image cap">
                        <div class="card-body">
                            <h5 class="card-title">Outside temperature</h5>
                            <p class="card-text"><?php echo shell_exec("python3 /var/www/html/outside.py"); ?></p>
                        </div>
                </div>

                <div class="card">
                    <img class="card-img-top" src="..." alt="Card image cap">
                        <div class="card-body">
                            <h5 class="card-title">Inside temperature</h5>
                            <p class="card-text"><?php echo shell_exec("python3 /var/www/html/inside.py"); ?></p>
                        </div>
                </div>

            </div>
        </div>

        <!--<div class="container h-100 d-flex justify-content-center text-center">
                <div class="col-lg-4 mx-auto">
                    <div class="card">
                        <div class="card-body">
                        <h3 class="card-title">Outside temperature</h3>
                        <p class="card-text"><?php echo shell_exec("python3 /var/www/html/outside.py"); ?></p>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 mx-auto">
                    <div class="card">
                        <div class="card-body">
                        <h3 class="card-title">Inside temperature</h3>
                        <p class="card-text"><?php echo shell_exec("python3 /var/www/html/inside.py"); ?></p>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 mx-auto">
                    <h3>Inside temperature</h3>
                    <p><?php echo shell_exec("python3 /var/www/html/inside.py"); ?></p>
                </div>

        </div> -->

        <!--    if (isset($_REQUEST["outside"])){
                echo shell_exec("python3 /var/www/html/outside.py");
            }
            
            if (isset($_REQUEST["inside"])){
                echo shell_exec("python3 /var/www/html/inside.py");
            }
            header("refresh:10;");
            echo("Outside temperature is: ");
            echo shell_exec("python3 /var/www/html/outside.py");
            echo("<br>"."Inside temperature is: ");
            echo shell_exec("python3 /var/www/html/inside.py");
        -->

    </body>
</html>