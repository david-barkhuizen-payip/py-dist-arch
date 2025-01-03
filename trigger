#!/usr/bin/env bash

export $(cat dev.env | xargs)

echo

curl \
    -H "Content-Type: application/json" \
    -d '{}' \
    -X POST ${TRIGGER_PROTOCOL}://localhost:${TRIGGER_EXT_PORT}/merchant_pos_new_checkout

echo
echo