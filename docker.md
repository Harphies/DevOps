## A List of essential docker resources

[More docker commands](https://vmokshagroup.com/blog/steps-to-build-run-and-manage-docker/)

[Useful Link](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf)

[Docker comprehensive cheat sheet](https://phoenixnap.com/kb/list-of-docker-commands-cheat-sheet)

[Docker By Examples](https://www.slideshare.net/CodeOps/docker-by-example-basics)

## Docker Essentials

- Running Docker containers
- Creating a DockerFile
- Creating Docker Image from a DockerFile
- Buiding a Docker Image from DockerFile
- Pushing a Docker Image to the Docker hub repository
- Docker compose
  - It is used to run large application that contain multiple services [docker-compose.yml]
  - it consist of list of services in the yml file
  - bring the application up by running 'docker-compose up' command
  - Docker Swarm
- Networking In Docker
- Docker Hosts

## Creating a docker Image steps

- Dockerfile : Create a dockerfile in the current directory of that project
- Use Dockerfile commands to specify all the needed steps to run the application
  - FROM : specify a base image
  - COPY
  - RUN
  - ENTRYPOINT
- docker build . -t [name of the image]: run 'docker build .' to build the dockerfile in the current directory
- docker run [image name] : test the just created image
- docker login : Loggin to the docker hub registry
- docker push [image name] : push the newly created image to the docker hub

## YAML Files

- it used to represent configuration data
- Equal number of spaces
- YAML File use a dictionary

# Why you Need Docker

- Compatability and dependency issues
- Long setup time accross different platform
- Different Development/Testing/Production

# What can docker do

- Containerized Applications that can run on different platforms with thier own libraries and dependencies.
- Run each service with its own dependencies in separate containers.

# A few things to know about docker

- Containers are completely Isolated environment that can have their own Process/services, Networking Interfaces and Mount
- There are different types of containers but docker uses LSC containers.
- Docker hub is the registry where all contanarized applications are hosted.
- Docker Image is a package/template used to create one or more containers.
- Docker container are runing Instances of Image that are Isolated and have their own environment and set of process
- Think of Docker Image and container like an OOP Image is the class and container are Instances of the class having thier separate attributes.
- [Go here for more](https://hackernoon.com/docker-commands-the-ultimate-cheat-sheet-994ac78e2888)

## A List of essential docker commands

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
