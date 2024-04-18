# --- Dado: 2 strings s e t de DNA com até mil nucleotídeos cada --- #
# --- Problema: Todas as localizações de t em s --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.readlines()

    # --- Obter as strings de DNA --- #
    s = conteudo[0].strip()
    t = conteudo[1].strip()


# --- Separar a string s em substrings com o tamanho da string t --- #
lista_strings = []
k = len(t)
for i in range(len(s)):
    # --- Obter cada pedaço da string s --- #
    pedaco = s[i:i+k]

    # --- Se o tamanho do pecaço for do mesmo tamanho de k, adicionar à lista --- #
    if len(pedaco) == k:
        lista_strings.append(pedaco)

# --- Verificar quais são as posições que estão os motivos --- #
resposta = ''
for posicao, string in enumerate(lista_strings, start=1):
    if string == t:
        resposta += f'{posicao} '

# --- Mostrar a resposta --- #
print(resposta)        
