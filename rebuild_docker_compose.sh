sudo docker ps | grep techtok_backend | awk '{ print $1;}' | xargs sudo docker kill
sudo docker-compose build
sudo docker-compose -f docker-compose.yml up -d
docker_id=`sudo docker ps | grep techtok_backend | awk '{ print $1; }'`
sudo docker exec -it $docker_id bash 
