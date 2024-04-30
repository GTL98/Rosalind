# --- Dado: Dois números inteiros positivos n (<=40) e k (<=5) --- #
# --- Problema: O número total de coelhos depois de n meses gerando k pares de novos coelhos --- #

# --- Criar a função para o cálculo da sequência de Fibonacci --- #
def fibo(n: int, k: int) -> int:
    """
    Função responsável pelo cálculo da sequência de Fibonacci.
    :param n: Meses.
    :param k: Pares de coelhos.
    :return: Quantidade total de coelhos após n meses.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1, k) + k * fibo(n-2, k)


# --- Informar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter n e k --- #
    conteudo = txt.read().split()
    n = int(conteudo[0])
    k = int(conteudo[1])

# --- Montar a resposta --- #
resposta = fibo(n, k)

# --- Mostrar a resposta --- #
print(resposta)
