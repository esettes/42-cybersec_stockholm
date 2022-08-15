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

TARGET_SRC = /home/
APP_NAME = stockholm:v1
CONTAINER = wannacry
SOURCE = /Users/iostancu/Desktop/cursus/cybersec/stockholm
all:	build	run	exec

list:
	@echo "${BLUE}"
	docker ps -a
	@echo "${GREEN}"
	docker ps
	@echo "${YELLOW}"
	docker images

build:
	docker build -t ${APP_NAME} .

build-nc: ## Build the container without caching
	docker build --no-cache -t ${APP_NAME} .

run:
	docker run -it -d --mount type=bind,source=$(SOURCE),target=${TARGET_SRC} --name ${CONTAINER} ${APP_NAME} bash

delete:
	@echo "${BLUE}"
	docker stop ${CONTAINER}
	@echo "${GREEN}"
	docker rm ${CONTAINER}
	@echo "${YELLOW}"
	docker rmi ${APP_NAME}

exec:
	docker exec -it ${CONTAINER} bash

help:
	@echo "${BLUE}GENERAL COMMANDS:\033[2;37m"
	@echo "[make] builds main image, and run a container and execute it with bash"
	@echo "[exec] execute container with bash"
	@echo "[list] shows images and all containers"
	@echo "[delete] stops running containers, deletes containers and images"