__author__ = 'rudragouda'

from elasticsearch import Elasticsearch

es = Elasticsearch()

# body = [
#     {"title": "First", "text":  "Just trying this out..."},
#     {"title": "Second", "text":  "Just trying this out..."},
#     {"title": "Third", "text":  "Just trying this out..."},
#     {"title": "Fourth", "text":  "Just trying this out..."},
#     {"title": "Fifth", "text":  "Just trying this out..."},
#     {"title": "Sixth", "text":  "Just trying this out..."},
#     {"title": "Seventh", "text":  "Just trying this out..."},
#     {"title": "Eighth", "text":  "Just trying this out..."},
#     {"title": "Ninth", "text":  "Just trying this out..."},
#     {"title": "Tenth", "text":  "Just trying this out..."},
#     {"title": "Eleven", "text":  "Just trying this out..."},
#     {"title": "Twelve", "text":  "Just trying this out..."},
#     {"title": "Thirteen", "text":  "Just trying this out..."},
#     {"title": "Fourteen", "text":  "Just trying this out..."},
#     {"title": "Fifteen", "text":  "Just trying this out..."},
#     {"title": "Sixteen", "text":  "Just trying this out..."},
#     {"title": "Seventeen", "text":  "Just trying this out..."},
#     {"title": "Eighteen", "text":  "Just trying this out..."},
#     {"title": "Ninteen", "text":  "Just trying this out..."},
#     {"title": "Twenty", "text":  "Just trying this out..."}
# ]
#
# for i in range(len(body)):
#     res = es.index(index="index-1-20", doc_type='doc-1-20', body=body[i])


res = es.search(index="index-1-20", doc_type="doc-1-20", body={"query": {"match_all": {}}, "from": 5,"size": 5})
for item in res['hits']['hits']:
    print item
