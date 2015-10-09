__author__ = 'rudragouda'

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print "index start..."
print(res['created'])
print "index end..."

res = es.get(index="test-index", doc_type='tweet', id=1)
print "get start..."
print(res['_source'])
print "get end.."

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
