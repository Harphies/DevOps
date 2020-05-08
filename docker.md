## A List of essential docker commands

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
