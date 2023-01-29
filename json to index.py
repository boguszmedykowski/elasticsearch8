from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document, Text, Integer
import json

# połączenie z Elasticsearch
es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
# print(es.ping())


with open("tabelatest.json", "r") as file:
    data = json.load(file)
    file.close()

for row in data['rows']:
    es.index(index="orders", document=row)




# # Create an index
# # es.indices.create(index="orders")

