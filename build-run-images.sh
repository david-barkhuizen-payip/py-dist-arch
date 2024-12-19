# BUILD_OPTIONS="--no-cache"
BUILD_OPTIONS=""
ROOT="docker/services"

services=(\
"write_model" \
"read_model" \
"log" \
"queue" \
"read_model_sync" \
"migration" \
"merchant_pos" \
"platform_new_pmt" \
"platform_new_receipt" \
"pmt_proc_new_pmt" \
)

for service in "${services[@]}"; do
  echo "building run image $service:latest ..."
  docker build -t $service:latest -f $ROOT/$service/Dockerfile $BUILD_OPTIONS .
  echo "... built run image $service"
done