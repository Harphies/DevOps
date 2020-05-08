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

# Execute a command on a running container

docker exec [container name][commands]

# check for OS details

cat /etc/_release_

# run a command in background

-d command

# run a container for certain time

docker run -d [container name] sleep [time duration]
Note: -d means run in the background

# running a command on a container

e.g docker run -d ubuntu sleep 1000

# Steps to run a command in a running container

1.  identify the container with docker ps command
2.  docker exec [container id][command]
    exmple command here is cat /etc/_release_

## Docker Run commands

1.  TAG
2.  attach and detach mode
3.  STDIN (standard input) for docker container to listen to a standard input of the host.
    using the '-i' command

# Note: the underlying host where docker is installed is called docker host/docker engine

4.  PORT MAPPING (-p for PORT specifier)

# Note: every container have an IP assignedd by default.

# Note: A user can access a container via the port number.

# Note users outside of the host can't access the container with the asigned IP on the host, because it's local.

# Note: you can run different instances of your application by mapping them with different host.

# Note: You can't map a port more than once on the docker host.

5.  VOLUME MAPPING (-v)

## Advanced Docker Run Commands
