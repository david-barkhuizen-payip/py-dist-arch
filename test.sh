export $(cat dev.env | xargs)

echo

curl \
    -H "Content-Type: application/json" \
    -d '{}' \
    -X POST ${TEST_PROTOCOL}://localhost:${TEST_EXT_PORT}/checkout

echo
echo