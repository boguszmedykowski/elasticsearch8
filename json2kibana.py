import json
from elasticsearch import Elasticsearch


es = Elasticsearch([{"host": "localhost", "port": 9200}])
response = es.ping()
print(response)


with open("od220601.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

rows = data["rows"]

# Otwórz plik do zapisu
with open("kibana.json", "w", encoding="UTF-8") as file:

    for row in rows:
        file.write(json.dumps(row) + "\n")



# es.indices.create(index="orders")


with open("kibana.json", "r", encoding="UTF-8") as file:
    for line in file:
        record = json.loads(line)

        # Wstaw dokument do Elasticsearch
        es.index(index="orders", doc_type="_doc", document=record)
