# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iostancu <iostancu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/16 17:25:10 by iostancu          #+#    #+#              #
#    Updated: 2022/08/04 16:22:55 by iostancu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

BLUE	=\033[0;35m
GREEN	=\033[0;36m
YELLOW	=\033[0;33m

<<<<<<< HEAD
TARGET_SRC = /home/
APP_NAME = stockholm:v1
CONTAINER = wannacry
SOURCE = /Users/iostancu/Desktop/cursus/cybersec/stockholm
all:	build	run	exec
=======

TARGET_SRC = /home/
APP_NAME = stockholm:v1
CONTAINER = wannacry
MOUNT_SRC = $(shell pwd)
DOCKER_PATH = './docker/Dockerfile'

all:	run	exec
>>>>>>> 3e5e839a6b0af94bb7af4abceaac7767686211ab

list:
	@echo "${BLUE}"
	docker ps -a
	@echo "${GREEN}"
	docker ps
	@echo "${YELLOW}"
	docker images

build:
	docker build -f ${DOCKER_PATH} -t ${APP_NAME} .

build-nc: ## Build the container without caching
	docker build -f ${DOCKER_PATH} --no-cache -t ${APP_NAME} .

run:
<<<<<<< HEAD
	docker run -it -d --mount type=bind,source=$(SOURCE),target=${TARGET_SRC} --name ${CONTAINER} ${APP_NAME} bash
=======
	docker run -f ${DOCKER_PATH} --rm -it -d --mount type=bind,source=${MOUNT_SRC},target=${TARGET_SRC} --name ${CONTAINER} ${APP_NAME} bash
>>>>>>> 3e5e839a6b0af94bb7af4abceaac7767686211ab

delete:
	@echo "${BLUE}"
	docker stop -f ${DOCKER_PATH} ${CONTAINER}
	@echo "${GREEN}"
	docker rm -f ${DOCKER_PATH} ${CONTAINER}
	@echo "${YELLOW}"
	docker rmi -f ${DOCKER_PATH} ${APP_NAME}

exec:
	docker exec -it ${CONTAINER} bash

help:
	@echo "${BLUE}GENERAL COMMANDS:\033[2;37m"
	@echo "[make] builds main image, and run a container and execute it with bash"
	@echo "[exec] execute container with bash"
	@echo "[list] shows images and all containers"
	@echo "[delete] stops running containers, deletes containers and images"