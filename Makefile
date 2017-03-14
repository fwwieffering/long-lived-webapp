WORKDIR = $(shell pwd)
NAME = long-lived-webapp
HOST_PORT = 5050
REMOTE_PORT = 5050

build:
	docker build -t $(NAME):latest .

runi:
	docker run -it --rm $
run:
	docker run -d \
		-p $(HOST_PORT):$(REMOTE_PORT) \
		--name $(NAME) \
		$(NAME):latest

ssh:
	docker exec -it $(NAME) /bin/bash

repl:
	docker exec -it $(NAME) ipython

remote_watch:
	docker exec -it $(NAME) make watch

watch:
	ptw --ignore __pycahce__

tail:
	docker logs -f $(NAME)

clean:
	docker stop $(NAME)
	docker rm $(NAME)
