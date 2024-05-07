# --- Dado: Números n (<=100) e m (<=20) positivos --- #
# --- Problema:  O número total de pares de coelhos que permanecerão após o enésimo mês se todos os coelhos viverem m meses. --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o valor de n e m --- #
    conteudo = txt.read().split()
    n = int(conteudo[0])
    m = int(conteudo[1])

# --- Criar a lista que armazenará a sequência de Fibonacci --- #
coelhos = [1, 1]

# --- Iniciar no segundo mês, pois é aí que começam a procriar --- #
meses = 2

while meses < n:
    if meses < m:
        coelhos.append(coelhos[-2] + coelhos[-1])
    elif meses == m:
        coelhos.append(coelhos[-2] + coelhos[-1] - 1)
    else:
        coelhos.append(coelhos[-2] + coelhos[-1] - coelhos[-(m + 1)])
    meses += 1

# --- Mostrar a resposta --- #
print(coelhos[-1])
