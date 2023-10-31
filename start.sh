
# su airflow
# usermod -aG docker $USER                  # to add myself to docker group
# chgrp docker /usr/local/bin/docker-compose     # to give docker-compose to docker group,
# chmod 750 /usr/local/bin/docker-compose

#teardown
docker-compose down --remove-orphans
echo "BLA"

#start
docker-compose up -d --build

LOL=`docker-compose logs`
echo "$LOL"

#RESULT=`ls -la`
RESULT=`whoami`
RESULT="THIS LOG SHOULD CHANGE"
echo "$RESULT"

#echo "Type 'docker-compose down' to tear-down"
#echo "Type 'docker-compose logs -f' to show logs."