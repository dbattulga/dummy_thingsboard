USER=$(whoami)

sudo usermod -aG docker $USER                  # to add myself to docker group
sudo chgrp docker /usr/local/bin/docker-compose     # to give docker-compose to docker group,
sudo chmod 750 /usr/local/bin/docker-compose

#teardown
docker-compose down --remove-orphans

#start
docker-compose -f docker-compose.yml up -d --build
# RESULT=`docker-compose logs`

RESULT=`ls -la`
echo "$RESULT"

#echo "Type 'docker-compose down' to tear-down"
#echo "Type 'docker-compose logs -f' to show logs."