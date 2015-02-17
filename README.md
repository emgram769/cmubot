# cmubot
A snapchat bot.

## Set up

Use python 2.7. cmubot will read from the `credentials.txt` file to log your bot in.  You can generate the file in bash:

    echo [username] > credentials.txt
    echo [password] >> credentials.txt

There are a bunch of dependencies that python will likely complain about.  Install these.

## Usage

    python cmubot.py

## QR Codes

A plain text QR code will be decoded and interpretted as `action:frequency`.  The `action` will simply be the name of a file (.png will silently be appended), and the `frequency` will be the interval between each snap, calculated as 15 * 2 ** `frequency` seconds.

This means that the image file `action`.png will be read from the directory and sent to the user who sent the QR code at intervals specified by `frequency`.  An example use case would be updating the image file to reflect the weather forecast every hour, thereby giving the user weather updates.  The update to the image file can be done by any other program, and should not be done by editing the `cmubot.py` file itself.  `mario.png` is included in the repo to demonstrate this.  Generate a QR code with the text `mario:5`, send a picture of it to cmubot, and you will recieve the picture of mario every 8 minutes.
