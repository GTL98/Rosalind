## Problema: Uma string s de DNA com no máximo 1000 pb.
## Resultado: Quatro inteiros (separado por espaços) representando
## respectivamente a quantidade de vezes em que os ncleotídeos 'A', 'C', 'G' e
## 'T' aparecem na string s.

# Importar a biblioteca
from Bio.Seq import Seq

# Indicar o arquivo usado
arquivo = 'rosalind_ini.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    # Transformar a string em um objeto Seq
    sequencia = Seq(doc.read())

# Contar quantos nucleotídeos de cada tipo há na sequência
nuc_a = sequencia.count('A')
nuc_c = sequencia.count('C')
nuc_g = sequencia.count('G')
nuc_t = sequencia.count('T')

# Mostrar a resposta_peptideo
print(nuc_a, nuc_c, nuc_g, nuc_t)
