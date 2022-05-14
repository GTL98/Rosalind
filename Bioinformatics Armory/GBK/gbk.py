## Problema: O nome do gênero de uma espécie com duas datas no formato
## AAAA/M/D.
## Resultado: O número de entradas de Nucleotide GenBank para esse gênero
## no período das datas informadas.

# Importar a biblioteca
from Bio import Entrez

# Indicar o arquivo usado
arquivo = 'rosalind_gbk.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')

# Informar o gênero
genero = conteudo[0]

# Informar as datas de pesquisa
inicio = conteudo[1]
fim = conteudo[2]

# Informar o email para o NCBI
Entrez.email = 'teste@example.com'

# Armazenar o termo a ser procurado
termo = f'"{genero}"[Organism] AND ({inicio}[Publication Date]: {fim}[Publication Date])'

# Pesquisar no banco de dados
identificador = Entrez.esearch(db='nucleotide', term=termo)

# Ler a pesquisa no banco de dados
pesquisa = Entrez.read(identificador)

# Mostrar a resposta_peptideo
print(pesquisa['Count'])
