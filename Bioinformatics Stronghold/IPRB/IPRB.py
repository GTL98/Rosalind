## Problema: Três inteiros positivos, representando a população contendo k+m+n organismos, onde:
## k são os homozigotos dominantes, m os heterozigotos e n os homozigotos recessivos
## Resultado: A probabilidade de dois organismos aleatórios gerarem um indivíduo com um alelo dominante.
## Assumindo que quaisquer dois organismos possam se encontrar

# Informar o arquivo usado
arquivo = 'rosalind_iprb.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    inteiros = [int(num) for num in doc.read().split()]
    populacao = sum(inteiros)
    k = inteiros[0]  # homozigoto dominante
    m = inteiros[1]  # heterozigoto
    n = inteiros[2]  # homozigoto recessivo

# A chance de um homozigoto recessivo encontrar um homozigoto recessivo
r_r = (n/populacao) * ((n-1)/(populacao-1))

# A chance de um heterozigoto encontrar um heterozigoto
h_h = (m/populacao) * ((m-1)/(populacao-1))

# A chance de um heterozigoto encontrar um homozigoto recessivo
h_r = (m/populacao) * (n/(populacao-1)) + (n/populacao) * (m/(populacao-1))

# A chance to indivíduo gerado ser homozigoto recessivo
# O valor "1/4" serve para informar o número de indivíduos gerados quando
# dois heterozigotos se encontram
# O valor "1/2" serve para informar o número de indivídos gerados quando
# dois homozigotos recessivos se encontram
recessivo = r_r + (h_h * 1/4) + (h_r * 1/2)

# Saber a probabilidade do indivíduo ter ao menos 1 alelo dominante
dominante = 1 - recessivo

# Mostrar a resposta
print(f'{dominante:.5f}')
