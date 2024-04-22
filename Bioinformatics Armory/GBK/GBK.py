# --- Fornecido: O gênero de uma espécie seguido de duas datas no formaro AAAA/MM/DD --- #
# --- Problema: A quantidade de entradas de nucleotídeos GenBank do gênero durante o período informado --- #

# --- Importar a biblioteca --- #
from Bio import Entrez

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteudo do arquivo --- #
    conteudo = txt.readlines()

    # --- Obter o gênero --- #
    genero = conteudo[0].strip()

    # --- Obter a data inicial --- #
    data_inicial = conteudo[1].strip()

    # --- Obter a data final --- 3
    data_final = conteudo[2].strip()

# --- Indicar um e-mail aleatório --- #
Entrez.email = 'your.email@example.com'

# --- Realizar a busca no banco de dados --- #
busca = Entrez.esearch(
    db='nucleotide',
    term=f'"({genero}"[Organism]) AND ("{data_inicial}"[Publication Date]:"{data_final}"[Publication Date])'
    )

# --- Ler a busca --- #
registro = Entrez.read(busca)

# --- Saber quantas entradas há --- #
quantidade = registro['Count']

# --- Mostrar a resposta --- #
print(quantidade)
