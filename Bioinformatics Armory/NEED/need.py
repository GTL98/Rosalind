## Problema: Dois IDs GenBank. Gap open = 10 & Gap extension = 1.
## Resultado: O valor máximo do alinhamento global entre as sequeências de DNA
## dos IDs GenBank.

# Importar as bibliotecas
from Bio import SeqIO
from Bio import Align
from Bio import Entrez
from Bio.Align import substitution_matrices

# Informar o arquivo usado
arquivo = 'rosalind_need.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    ids_sequencias = doc.read().split()

# Informar o email para o Entrez
Entrez.email = 'teste@example.com'

# Acessar o banco de dados
identificador = Entrez.efetch(db='nucleotide', id=ids_sequencias, rettype='fasta')

# Criar uma lista_pedacos com todos os registros encontrados
registros = list(SeqIO.parse(identificador, 'fasta'))

# Separar as sequências de DNA de cada registro
sequencia_1 = registros[0].seq
sequencia_2 = registros[1].seq

# Configurar o alinhamento
alinhador = Align.PairwiseAligner()
matriz = substitution_matrices.load('NUC.4.4') # matriz de substituição de DNA
alinhador.substitution_matrix = matriz
alinhador.open_gap_score = -10
alinhador.extend_gap_score = -1
pontuacao = alinhador.score(sequencia_1, sequencia_2)

# Mostrar a resposta_peptideo
print(pontuacao)
