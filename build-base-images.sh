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
"merchant_pos" \
"platform_new_pmt" \
"iss_bank_new_pmt" \
"platform_new_receipt" \
"pmt_proc_new_pmt" \
)

for service in "${services[@]}"; do
  echo "building base image $service-base:latest ..."
  docker build -t $service-base:latest -f $ROOT/$service/Dockerfile.base $BUILD_OPTIONS .
  echo "... built base image for $service"
done