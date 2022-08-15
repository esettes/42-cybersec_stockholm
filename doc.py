#!/usr/bin/python3.9
from os import system
import sys
import argparse
import subprocess
from argparse import RawTextHelpFormatter

img_name = 'stockholm:v1'
container_name = 'wannacry'
dockerpath = './docker/Dockerfile'

target_src = '/home'

blue_ = '\033[0;34m'
lila_ = '\033[0;35m'
cyan_ = '\033[36m'
green_ = '\033[32m'
yellow_ = '\033[0;33m'
red_ = '\033[0;31m'
end_ = '\033[37m'

def main(argv):
    args = MainArguments()
    if args.list: DockerList()
    if args.build: BuildImage()
    if args.exec: Execute()
    if args.runexec: RunContainer(); Execute()
    if args.delete: DeleteContainer()
    if args.deleteall: DeleteContainer(); DeleteImage()
    return

def BuildImage():
    system('docker build -f ' + dockerpath + ' . -t ' + img_name)

def Execute():
    system('docker exec -it ' + container_name + ' bash')

def RunContainer():
    subprocess_ = subprocess.run(['pwd'], stdout=subprocess.PIPE, text=True)
    mount_src = subprocess_.stdout
    system('docker run -it -d --mount ' + \
        'type=bind,source=' + mount_src +',target='+ target_src + ' --name ' \
            + container_name + ' ' + img_name + ' bash')

def DeleteContainer():
    try:
        system('docker stop ' + container_name)
        system('docker rm ' + container_name)
    except SystemError:
        ErrorMssg("Can't stop/remove '" + container_name + "'. Maybe forcing it?")
        return
    ConfirmationMssg(container_name + ' stopped and deleted')

def DeleteImage():
    try:
        system('docker rmi ' + img_name)
    except SystemError:
        ErrorMssg("Can't remove image '" + img_name +"'. Maybe forcing?")
        return
    ConfirmationMssg(img_name + ' deleted')

def DockerList():
    print(lila_ + "> Running containers: ")
    system('docker ps -a')
    print(cyan_ + "> Existing but stopped containers: ")
    system('docker ps')
    print(yellow_ + "> Docker images: ")
    system('docker images')

def MainArguments():
    head = blue_ + """
      ▀▄▀      ▄     ▄  ▄▀█ █░█ ▀█▀ █▀█
    ▄███████▄  ▀██▄██▀  █▀█ █▄█ ░█░ █▄█
  ▄█████▀█████▄  ▄█   
  ███████▀████████▀    █▀█ █▄█ █▀▄ █▀█ █▀▀
   ▄▄▄▄▄▄███████▀      █▀▀ ░█░ █▄▀ █▄█ █▄▄
""" + end_ + """
  Simple docker automation with debian:11 image. 
  Steps:
     Configure the main variables: 'img_name', 'container_name'. The 
    'target_src' by default is /home/, but you can change it too.
    [ ./doc.py -b ]    Build the image if it's not created.
    [ ./doc.py -re]    Run and execute a container_name based on builded image.

    [ ./doc.py -d]     Delete container or [ ./doc.py -da] to delete container
                       and image.
    Use more than one flag at once it's not allowed. 
"""+blue_+"""-------------------------------------------------------------------------------""" + end_
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, \
        description=head)
    group = parser.add_mutually_exclusive_group()
    #parser.add_argument('-p','--pull', action='store_true', help="Downloads the official debian image from docker hub.")
    group.add_argument('-b','--build', action='store_true', \
        help="Create docker image.")
    group.add_argument('-e','--exec', action='store_true', \
        help="Execute container.")
    group.add_argument('-re','--runexec', action='store_true', \
        help="Run and execute container.")
    group.add_argument('-l','--list', action='store_true', \
        help="List all docker images and containers.")
    group.add_argument('-d','--delete', action='store_true', \
        help="Stop container_name and delete it.")
    group.add_argument('-da','--deleteall', action='store_true', \
        help="List all docker images and containers.")
    args = parser.parse_args()
    return args

def ConfirmationMssg(s):
    print(green_ + "[OK] " + end_ + s)

def ErrorMssg(s):
    print(red_ + "[ERROR] " + end_ + s)

if __name__ == '__main__':
    main(sys.argv)