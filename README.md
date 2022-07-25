### Stockholm

<br>

Program that encrypts and decrypts local files.

<br>

You can init your docker(school) with a [custom 42 school script](https://github.com/alexandregv/42toolbox/blob/master/init_docker.sh)

<br>

After this, check that the proyect is in your user directory and `cd stockholm` into it.
Then execute:

`make`

This builds the image, runs the container and executes it with bash. You can type `make help` to see avaible commands.

<br>

Now we are in Debian 11, `cd /home/` and here is the script and the test directory (infection).

Encrypt files using:

`./stock.py`

<br>

It can recieve flags and decrypt the files with the encryption key.

`./stock -help` to see the avaible flags

<br>

The encryption/decryption key is in *utils* directory (key.key). You can generate a different key with the
`./crypt.py` command.
