clear

export $(cat dev.env | xargs) &&  docker-compose -f docker-compose.yml --env-file dev.env up 