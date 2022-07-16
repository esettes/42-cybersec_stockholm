# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iostancu <iostancu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/16 17:25:10 by iostancu          #+#    #+#              #
#    Updated: 2022/07/16 17:59:33 by iostancu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

MOUNT_SRC = /Users/${USER}/stockholm
TARGET_SRC = /home/
APP_NAME = stockholm
CONTAINER = wannacry

list:
	docker ps -all
	docker images
	docker network ls

build:
	docker build -t ${APP_NAME} .

build-nc: ## Build the container without caching
	docker build --no-cache -t ${APP_NAME} .

run:
	docker rm -fv ${CONTAINER} && docker run -it -d --mount type=bind,source=${MOUNT_SRC},target=${TARGET_SRC} --name ${CONTAINER} ${APP_NAME}:1 bash

exec:
	docker exec -it ${CONTAINER} bash
