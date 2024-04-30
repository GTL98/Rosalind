# --- Dado: Três inteiros positivos (k, m, n). k são homozigotos dominantes, m são heterozigotos e n são homozigotos recessivos --- #
# --- Problema: A probabilidade de dois indivíduos se encontrarem e gerar um organismo com um alelo dominante --- #

# --- Informar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter a população de cada genótipo --- #
    conteudo = txt.read().split()
    k = int(conteudo[0])
    m = int(conteudo[1])
    n = int(conteudo[2])

    # --- Obter a população --- #
    populacao = k + m + n

# --- A chance de um homozigoto recessivo encontrar um homozigoto recessivo --- #
r_r = (n/populacao) * ((n-1)/(populacao-1))

# --- A chance de um heterozigoto encontrar um heterozigoto --- #
h_h = (m/populacao) * ((m-1)/(populacao-1))

# --- A chance de um heterozigoto encontrar um homozigoto recessivo --- #
h_r = (m/populacao) * (n/(populacao-1)) + (n/populacao) * (m/(populacao-1))

# --- A chance to indivíduo gerado ser homozigoto recessivo --- #
recessivo = r_r + (h_h * 1/4) + (h_r * 1/2)

# --- Saber a probabilidade do indivíduo ter ao menos 1 alelo dominante --- #
dominante = 1 - recessivo

# --- Mostrar a resposta --- #
print(f'{dominante:.5f}')
