### Stockholm

<br>

Program that encrypts and decrypts local files.

<br>

You can init your docker(school) with a [custom 42 school script](https://github.com/alexandregv/42toolbox/blob/master/init_docker.sh)

<br>

After this, check that the proyect is in your user directory and `cd stockholm` into it.
Then start to build the container. First mount the image:

`make build`

Mount the directories, this gets the proyect folder and puts ir in the image home directory.

`make run`

And finally execute the container!

`make exec`

Now we are in Debian 11, `cd /home/` and here is the script and the test directory (infection).

Encrypt files using:

`./stock.py`

<br>

It can recieve flags and decrypt the files with the encryption key.

<br>

[ -help ][ h ] Shows avaible flags for the program.

[ -silent ][ s ] Silences the file encryption process.

[ -reverse ][ r ] Decrypt files using it along with decryption key [ ./ramon.py -reverse + [key] ]

[ -version ][ v ] Shows program version.
