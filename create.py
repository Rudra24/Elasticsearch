__author__ = 'rudragouda'

from elasticsearch import Elasticsearch

es = Elasticsearch()

doc1 = {
    'author': 'Author name here...',
    'text': 'Enter the text here...',
}

#res = es.get(index="index-ka-naam", doc_type="document-ka-naam", id='1234')
res = es.search(index="index-ka-naam", doc_type="document-ka-naam", body={"query": {"match_all": {}},})

# print(res['created'])


# res = es.get(index="test-index", doc_type='tweet', id=1)
print res

# es.indices.refresh(index="test-index")
#
# res = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
