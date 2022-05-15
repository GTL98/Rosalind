## Problema: Dois inteiros positivos a & b, cada um menor do que 1000.
## Resultado: O inteiro correspondente ao quadrado da hipotenusa do triângulo
## de comprimento ab.

# Indicar o arquivo usado
arquivo = 'rosalind_ini2.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    # Ler o arquivo
    numeros = doc.read().split()
    # Criar uma lista_pedacos dos números que estão no arquivo
    lista_numeros = [int(num) for num in numeros]

# Separar em duas variáveis os dois números
a = lista_numeros[0]
b = lista_numeros[1]

# Calcular a hipotenusa
hipotenusa = a**2 + b**2

# Mostrar o valor da variável
print(hipotenusa)
