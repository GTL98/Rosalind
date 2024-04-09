# --- Fornecido: Uma string s de até 10.000 letras --- #
# --- Problema: O número de ocorrências de cada palavra em s, separadas por espaço --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter as informações do arquivo --- #
    conteudo = txt.read().split()

# --- Criar um dicionário para armazenar as palavras --- #
dic_palavras = {}

# --- Colocar as palavras como chave do dicionário --- #
for palavra in conteudo:
    # --- Colocar o valor a quantidade de vezes que a palavra aparece no arquivo como valor --- #
    dic_palavras[palavra] = conteudo.count(palavra)

# --- Escrever no formato correto a saída --- #
for chave, valor in dic_palavras.items():
    print(chave, valor)

