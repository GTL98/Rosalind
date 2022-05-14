## Problema: Uma coleção de n entradas de IDs do GenBank (n =< 10).
## Resultado: A menor sequência associada com o ID no formato FASTA.

# Importar as bibliotecas
from Bio import SeqIO
from Bio import Entrez

# Listas usadas
lista_tamanho_seq = []

# Indicar o arquivo usado
arquivo = 'rosalind_frmt.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    lista_ids = doc.read().split()

# Informar o email
Entrez.email = 'teste@example.com'

# Acessar o banco de dados
identificador = Entrez.efetch(db='nucleotide', id=lista_ids, rettype='fasta')

# Criar uma lista_pedacos com todos os registros encontrados
registros = list(SeqIO.parse(identificador, 'fasta'))

# Loop para obter o tamanho da menor sequência
for registro in registros:
    lista_tamanho_seq.append(len(registro.seq))

# Obter o índice do menor valor da lista_pedacos "lista_tamanho_seq"
menor_valor_sequencia = min(lista_tamanho_seq)
indice_menor_valor = lista_tamanho_seq.index(menor_valor_sequencia)

# Mostrar a resposta_peptideo
print(f'>{registros[indice_menor_valor].description}')
print(registros[indice_menor_valor].seq)
