## Problema: Dois inteiros positivos n & k, onde 100 >= n > 0 e 10 >= k > 0
## Resultado: O número total das permutações P(n, k) em módulo de 1.000.000

# Importar a biblioteca
import pyperclip

# Informar o arquivo usado
arquivo = 'rosalind_pper.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    inteiros = doc.read().strip().split()
    n = int(inteiros[0])
    k = int(inteiros[1])

# Saber a diferença de entre n & k, isso indica quantos "espaços" há para multiplicar
diferenca = n - k

# Calcular o valor de quantas permutações podem ser feitas com n valores agrupados com tamanho k
x = 1
for i in range(diferenca, n):
    # O '+1' serve para evitar a contagem a partir do zero, como é o padrão do Python
    x *= i+1

# Saber o valor em módulo
resposta = x % 10**6

# Para facilitar a entrega da resposta, ela será copiada
pyperclip.copy(resposta)
