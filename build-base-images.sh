# BUILD_OPTIONS="--no-cache"
BUILD_OPTIONS=""
ROOT="docker/services"

services=(\
"database" \
"log" \
"queue" \
"common" \
)

for service in "${services[@]}"; do
  echo "building base image $service-base:latest ..."
  docker build -t $service-base:latest -f $ROOT/$service/Dockerfile.base $BUILD_OPTIONS .
  echo "... built base image for $service"
done