#!/usr/bin/env bash

export $(cat dev.env | xargs)

echo

curl \
    -H "Content-Type: application/json" \
    -d '{"currency_amt":888,"currency":"ZAR"}' \
    -X POST ${TEST_PROTOCOL}://localhost:${TEST_EXT_PORT}/

echo
echo