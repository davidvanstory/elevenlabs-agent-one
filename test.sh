# curl -X POST http://localhost:8000/agent/take-note \
#   -H "Content-Type: application/json" \
#   -d '{ "note": "Roses are red and violets are blue." }'

curl http://localhost:8000/agent/get-note
