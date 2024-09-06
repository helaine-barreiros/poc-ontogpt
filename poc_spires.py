from ontogpt import OntoGPT
from ontogpt.ontologies import BaseOntology
from pydantic import BaseModel, Field
from typing import List

# Definindo nossa ontologia para máquina de estados
class Estado(BaseModel):
    nome: str
    descricao: str = ""

class Transicao(BaseModel):
    origem: str
    destino: str
    evento: str
    acao: str = ""

class MaquinaDeEstados(BaseOntology):
    nome: str
    estados: List[Estado] = Field(default_factory=list)
    transicoes: List[Transicao] = Field(default_factory=list)
    estado_inicial: str
    estados_finais: List[str] = Field(default_factory=list)

# Inicializando o OntoGPT com nossa ontologia personalizada
ontogpt = OntoGPT(ontology=MaquinaDeEstados)

# Texto descritivo de uma máquina de estados
texto = """
Máquina de Estados: Controle de Semáforo

Estados:
1. Verde: Permite o fluxo de tráfego.
2. Amarelo: Alerta os motoristas para se prepararem para parar.
3. Vermelho: Interrompe o fluxo de tráfego.

Estado Inicial: Verde

Estados Finais: Nenhum (a máquina opera continuamente)

Transições:
- De Verde para Amarelo: Após 60 segundos, muda para amarelo.
- De Amarelo para Vermelho: Após 5 segundos, muda para vermelho.
- De Vermelho para Verde: Após 55 segundos, muda para verde.

Ações:
- Ao entrar em Verde: Acende a luz verde.
- Ao entrar em Amarelo: Acende a luz amarela.
- Ao entrar em Vermelho: Acende a luz vermelha.
"""

# Extrair informações do texto
resultado = ontogpt.extract(texto)

# Imprimir os resultados
print(f"Máquina de Estados: {resultado.nome}")
print("\nEstados:")
for estado in resultado.estados:
    print(f"- {estado.nome}: {estado.descricao}")

print(f"\nEstado Inicial: {resultado.estado_inicial}")

print("\nEstados Finais:")
if resultado.estados_finais:
    for estado in resultado.estados_finais:
        print(f"- {estado}")
else:
    print("Nenhum estado final (máquina opera continuamente)")

print("\nTransições:")
for transicao in resultado.transicoes:
    print(f"- De {transicao.origem} para {transicao.destino}:")
    print(f"  Evento: {transicao.evento}")
    if transicao.acao:
        print(f"  Ação: {transicao.acao}")