#! /bin/bash

echo "Testing HTML Output with a get"
curl http://127.0.0.1:8000/HTTP

echo "Testing JSON Output with a get"
curl http://127.0.0.1:8000/HTTP -H "Accept: application/json"

echo "Testing HTML Output with a post"
curl http://127.0.0.1:8000/HTTP -X POST

echo "Testing JSON Output with a post"
curl http://127.0.0.1:8000/HTTP -H "Accept: application/json" -X POST