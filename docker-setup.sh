#!/bin/bash

get_containers()
{
	docker ps -a -q --filter "name=$1"
}

containers="$(get_containers '.demo')"

echo $containers

echo "Stop all relevant containers ..."
docker stop $containers 

echo "Remove all relevant containers ..."
docker rm $containers

echo "Pull all involved containers ..."
docker-compose pull

