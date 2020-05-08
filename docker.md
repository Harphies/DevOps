## A List of essential docker commands

[More docker commands](https://vmokshagroup.com/blog/steps-to-build-run-and-manage-docker/)
[Useful Link](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf)
[Docker comprehensive cheat sheet](https://phoenixnap.com/kb/list-of-docker-commands-cheat-sheet)
[Docker By Examples](https://www.slideshare.net/CodeOps/docker-by-example-basics)
**docker images** : List available docker Images

**docker build** : Build a docker images

**docker commit** : create an image from a container

**docker push** : Push an Image or a repository to a registry

**docker rename** : Rename a container

**docker port** : List port mapping or a specific mapping for the container

**docker restart** : restart a container

**docker save** : save one or more images to a tar archive (streamed to STDOUT by default)

**docker search** : search the docker hub for images

**docker services** : manage the docker services

**docker stack** : Manage Docker stacks

**docker start** : start one or more stopped containers

**docker swarm** : Manage Docker swam

**docker tage** : Tag an image into a repository

**docker top** : display the running processes of a container

**docker unpause** : Unpause all processes within one or more container

**docker update** : Update the configuration of one or more containers

**docker version** : show the docker version information

**docker volume** : Manage docker volumes

**docker wait** : Wait until a container stop, then print its exit code
**docker run [container name]** : run a container from an Image

**docker ps** : List all containers

**docker ps -a** : List all running containers/ History of all runned containers

**docker stop [Name of the container]** : stop running a container

Note: use 'docker ps' to get all the list of docker containers you have and search for the name/id of the docker container to stop

**docker rm [name of container]** : remove a container

**docker images** : List of the Images

**docker rmi [Name of the image]** : Remove an image

Note: Before deleting an image ensure there is no dependent container running out if it.
Note: delete all dependent container to remove image

**docker pull [Image name]** : download an Image from the docker hub registry.

**docker exec [container name][commands]** : Execute a command on a running container

**cat /etc/_release_** : check for OS details

**-d command** : run a command in background

**docker run -d [container name] sleep [time duration]** : run a container for a certain time
Note: -d means run in the background

**e.g docker run -d ubuntu sleep 1000** : running a command on a container

## Steps to run a command in a running container

- identify the container with docker ps command
- docker exec [container id][command]
  exmple command here is cat /etc/_release_

## Docker Run commands

- TAG
- attach and detach mode
- STDIN (standard input) for docker container to listen to a standard input of the host.
  using the '-i' command
- PORT MAPPING (-p for PORT specifier)
- VOLUME MAPPING (-v)

## Some useful Notes

- Every container have an IP assignedd by default.
- A user can access a container via the port number.
- Users outside of the host can't access the container with the asigned IP on the host, because it's local.
- The underlying host where docker is installed is called docker host/docker engine
- You can run different instances of your application by mapping them with different host.
- You can't map a port more than once on the docker host.

## Advanced Docker Run Commands
