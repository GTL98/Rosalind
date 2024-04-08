# --- Fornecido: Dois números interos positivos a e b menor do que 1000 --- #
# --- Problema: O inteiro correspondente ao quadrado da hipotenusa do triângulo, cujo os lados são a e b --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.read()

    # --- Obter o primeiro número --- #
    a = int(conteudo.split(' ')[0])

    # --- Obter o segundo número --- #
    b = int(conteudo.split(' ')[1])

# --- Encontrar a hipotenusa do triângulo --- #
h = (a**2 + b**2)

# --- Mostrar a respota --- #
print(h)
