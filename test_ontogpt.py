import logging
import os
from dotenv import load_dotenv

from oaklib.utilities.apikey_manager import set_apikey_value
from ontogpt.engines.spires_engine import SPIRESEngine
from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD

load_dotenv()

logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)

model: str = "ctd.ChemicalToDiseaseDocument"
text: str = "ARICEPT is indicated for the treatment of dementia of the Alzheimer's type."
template: str = "treatment.DiseaseTreatmentSummary"
text: str = "Clozapine is indicated for the treatment of severely ill patients with schizophrenia who fail to respond adequately to standard antipsychotic treatment"

set_apikey_value("openai", os.getenv('OPENAI_APIKEY'))
set_apikey_value("bioportal", os.getenv('BIOPORTAL_APIKEY'))

engine = SPIRESEngine(template)
#print(engine)
results = engine.extract_from_text(text)
#print(results)

#from ontogpt import OntoGPT
#from ontogpt.ontologies import PersonOntology

#print("OntoGPT importado com sucesso!")

#ontogpt = OntoGPT(ontology=FOAF.Person)
#print("OntoGPT inicializado com sucesso!")

# Texto de exemplo
#texto = """
##João Silva é um engenheiro de software de 28 anos que trabalha na empresa TechCorp.
#Ele nasceu em São Paulo e atualmente mora no Rio de Janeiro.
#"""

#Extrair informações do texto
#resultado = ontogpt.extract(texto)

#Imprimir os resultados
#print("\nInformações extraídas:")
#for pessoa in resultado.pessoas:
#    print(f"Nome: {pessoa.nome}")
#    print(f"Idade: {pessoa.idade}")
#    print(f"Profissão: {pessoa.profissao}")
#    print(f"Local de nascimento: {pessoa.local_nascimento}")
#    print(f"Local de residência: {pessoa.local_residencia}")