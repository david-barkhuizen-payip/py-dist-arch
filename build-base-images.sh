# BUILD_OPTIONS="--no-cache"
BUILD_OPTIONS=""
ROOT="docker/services"

services=(\
"common" \
"database" \
"log" \
"queue" \
"read_model_sync" \
"migration" \
"btc_price" \
"create_buy_order" \
"fetch_buy_orders" \
)

for service in "${services[@]}"; do
  echo "building base image $service-base:latest ..."
  docker build -t $service-base:latest -f $ROOT/$service/Dockerfile.base $BUILD_OPTIONS .
  echo "... built base image for $service"
done