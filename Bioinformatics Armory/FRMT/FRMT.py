# --- Fornecido: Conjunto de n (n <= 10) de IDs do GenBank --- #
# --- Problema: A menor sequência com o ID no formato FASTA --- #

# --- Importar as bibliotecas --- #
from Bio import SeqIO
from Bio import Entrez

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter os IDs --- #
    lista_ids = txt.read().split(' ')

# --- Indicar um e-mail aleatório --- #
Entrez.email = 'your.email@example.com'

# --- Realizar a busca no banco de dados de nucleotídeos --- #
busca = Entrez.efetch(
    db='nucleotide',
    id=lista_ids,
    rettype='fasta'
    )

# --- Dar um valor infinito como início para análise --- #
menor_seq = float('inf')

# --- Criar uma lista para armazenar as entradas --- #
entradas = []

# --- Ler o resultado da busca --- #
for registro in list(SeqIO.parse(busca, 'fasta')):
    # --- Verificar se o tamanho da sequência atual é menor do que a anterior --- #
    if len(registro) < menor_seq:
        menor_seq = len(registro.seq)
        # --- Criar a string do formato FASTA --- #
        fasta = f'''>{registro.description}
{registro.seq}'''
        entradas.append(fasta)

# --- Mostrar a resposta --- #
print(entradas[-1])
