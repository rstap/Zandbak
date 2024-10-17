from ast import Store
from rdflib import Graph
# Example 1
# #initialize a graph
# g=Graph()

# #parse in a RDF file graph dbpedia Berlin
# g.parse('http://dbpedia.org/resource/Berlijn')

# #loop through each triple in the graph (subj, pred, obj)
# for index, (sub, pred, obj) in enumerate(g):
#     print(sub, pred, obj)
#     if index == 50:
#         break
#     # end if

# # print size of the graph
# print(f'graph has {len(g)} facts')

# # print entire graph in RDF Turtle formal
# # print(g.serialize(format="turtle").decode('u8'))

# example 2
from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD

# create a Graph
# g=Graph()

# roel=URIRef("http://example.org/roel")

# # add triples using Store's add() method
# g.add((roel, RDF.type, FOAF.Person))
# g.add((roel, FOAF.nick, Literal("orlando", lang="en")))
# g.add((roel, FOAF.name, Literal("Roel Stap")))
# g.add((roel, FOAF.mbox, Literal("mailto:roel.stap@gmail.com")))

# # add another person
# shyla=URIRef("http://example.org/shyla")
# g.add((shyla, RDF.type, FOAF.Person))
# g.add((shyla, FOAF.nick, Literal("shyla", datatype=XSD.string)))
# g.add((shyla, FOAF.name, Literal("shyla Sharples")))
# g.add((shyla, FOAF.mbox, Literal("mailto:shyla@example.org")))

# #iterate over de graph and print
# for s, p, o in g:
#     print(s, p, o)

# #for each foaf:person in the grpah print out their nicknames
# for person in g.subjects(RDF.type, FOAF.Person):
#     for nick in g.objects(person, FOAF.nick):
#         print(nick)

# #Bind the FOAF namespace to a prefix form ore readable output
# g.bind("foaf", FOAF)

# #Print al the data in the n3 format
# print(g.serialize(format="n3"))

# exemple 3
import rdflib
#initialize a Graph
g=rdflib.Graph()

#Parse in an RDF file graph the Web
g.parse('http://dbpedia.org/resource/Python_(programming_language)')

print(len(g))

