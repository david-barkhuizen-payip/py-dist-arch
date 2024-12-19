# BUILD_OPTIONS="--no-cache"
BUILD_OPTIONS=""
ROOT="docker/services"

services=(\
"write_model" \
"read_model" \
"log" \
"create_buy_order" \
"fetch_buy_orders" \
"queue" \
"read_model_sync" \
"migration" \
"btc_price" \
)

for service in "${services[@]}"; do
  echo "building run image $service:latest ..."
  docker build -t $service:latest -f $ROOT/$service/Dockerfile $BUILD_OPTIONS .
  echo "... built run image $service"
done