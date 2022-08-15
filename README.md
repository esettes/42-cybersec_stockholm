# Stockholm

<br>

Program that recursively encrypts and decrypts local files starting from the indicated directory.

````
        █▀ ▀█▀ █▀█ █▀▀ █▄▀ █░█ █▀█ █░░ █▀▄▀█
        ▄█ ░█░ █▄█ █▄▄ █░█ █▀█ █▄█ █▄▄ █░▀░█
                ──▄────▄▄▄▄▄▄▄────▄───
                ─▀▀▄─▄█████████▄─▄▀▀──
                ─────██─▀███▀─██──────
                ───▄─▀████▀████▀─▄────
                ─▀█────██▀█▀██────█▀──  
````

<br>

The program runs inside a Docker container. The creation and execution of the environment is automated with Makefile.

An image must first be created.

````bash
make build
````
And then the container gets up and runs.

````bash
make
````

The container has been built on Debian. The program was in `cd /home/` with the infection folder.

You can type `make help` to see more avaible commands.

<br>

## Crypt files

Encrypt files using:

````
./stock.py
````

<br>

It can recieve flags and decrypt the files with the encryption key.

````bash
./stock.py -r key.key
````

`./stock -help` to see more avaible flags

<br>

The encryption/decryption key is named 'key.key'. You can generate a different key with the `./generatekey.py` command (in /utils folder).
