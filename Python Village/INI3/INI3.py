# --- Fornecido: Uma string s de no máximo 200 caracteres e quatro números inteiros a, b, c, d --- #
# --- Problema: As substrings de s[a:b] e s[c:d] --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.readlines()

    # --- Obter a string --- #
    s = conteudo[0]

    # --- Obter os números --- #
    numeros = conteudo[1].split(' ')
    a = int(numeros[0])
    b = int(numeros[1])
    c = int(numeros[2])
    d = int(numeros[3])

# --- Obter o as substrings --- #
sub_s_1 = s[a:b+1]
sub_s_2 = s[c: d+1]

# --- Mostrar a resposta --- #
print(f'{sub_s_1} {sub_s_2}')
