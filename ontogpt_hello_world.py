from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD

# Crie um grafo RDF para representar nossa ontologia simples
g = Graph()

# Defina um namespace para nosso exemplo
ex = URIRef("http://example.org/")

# Crie URIRefs para os recursos que queremos usar
Greeting = URIRef(ex + "Greeting")

# Adicione algumas triplas à nossa ontologia
g.add((Greeting, RDF.type, FOAF.Person))
g.add((Greeting, FOAF.name, Literal("Hello World", datatype=XSD.string)))

# Função para simular uma consulta OntoGPT
def ontogpt_query(graph, query):
    # Neste exemplo simples, apenas retornamos o nome associado à saudação
    for _, _, o in graph.triples((Greeting, FOAF.name, None)):
        return o

# Use a função de consulta para obter nossa saudação
greeting = ontogpt_query(g, "What is the greeting?")

# Imprima a saudação
print(greeting)
