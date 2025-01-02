#!/usr/bin/env bash

# BUILD_OPTIONS="--no-cache"
BUILD_OPTIONS=""
ROOT="docker/services"

services=("write_model" \
"read_model" \
"log" \
"queue" \
"read_model_sync" \
"migration" \
"merchant_pos_new_checkout" \
"platform_new_pmt" \
"platform_new_receipt" \
"pmt_proc_new_pmt" \
"iss_bank_new_pmt" \
"test")

for service in "${services[@]}"; do
  tag="$service:latest"
  dockerfile_path="$ROOT/$service/Dockerfile"
  echo "building $tag from $dockerfile_path ..."
  docker build -t $tag -f $dockerfile_path $BUILD_OPTIONS .
  echo "... built $tag"
done