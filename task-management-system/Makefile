# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smagniny <santi.mag777@student.42madrid    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 04:38:53 by smagniny          #+#    #+#              #
#    Updated: 2025/09/09 17:11:11 by smagniny         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# exportar .env (crearlo segun .env.sample para usar este makefile)
include .env
export

all: up

up:
	docker-compose up -d --build

down:
	docker-compose down

logs:
	docker-compose logs -f

py:
	docker-compose exec backend_django python

sh:
	docker-compose exec backend_django bash
	
sql:
	docker-compose exec database_postgres psql -U ${POSTGRES_USER} -d ${POSTGRES_DB_NAME}

django:
	docker-compose build backend_django
	docker-compose up -d backend_django

re: clean up

clean:
	if [ $$(docker images -qa | grep backend_django) ]; then docker rmi backend_django; fi
	if [ $$(docker images -qa | grep database_postgres) ]; then docker rmi database_postgres; fi

