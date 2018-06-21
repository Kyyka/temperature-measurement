<!DOCTYPE html>
<html lang="en">
<head>
    <title>Home Temperature</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="bootstrap/css/bootstrap.css">
    <script src="boostrap/js/bootstrap.min.js"></script>
</head>
<body>

    <div class="jumbotron text-center" class="border border-white">
        <h1>Home Temperature</h1>
        <p>Outdoor and indoor temperatures</p>
    </div>

    <div class="container text-center">
        <div class="row">
            <div class="col-6">
                <h5>Outside temperature</h5>
                <p><?php echo shell_exec("python3 /var/www/html/outside.py"); ?></p>
            </div>
        </div>

        <div class="row">
            <div class="col-6">
                <h5>Inside temperature</h5>
                <p><?php echo shell_exec("python3 /var/www/html/inside.py"); ?></p>
            </div>
        </div>
    </div>

</body>
</html>