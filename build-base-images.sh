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
  echo "-------------------------------------------------------------------------------------"
  tag="$service-base:latest"
  dockerfile_path="$ROOT/$service/Dockerfile.base"
  echo "building $tag from $dockerfile_path ..."
  docker build -t $tag -f $dockerfile_path $BUILD_OPTIONS .
  echo "... built $tag"
done