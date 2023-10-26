USER=$(whoami)

#teardown
docker-compose down --remove-orphans

#start
docker-compose -f docker-compose.yml up -d --build
echo "$(docker-compose logs -f)"

#echo "Type 'docker-compose down' to tear-down"
#echo "Type 'docker-compose logs -f' to show logs."