## Problema: Uma string s de DNA com no máximo 10 kb e uma string de
## aminoácidos traduzida de s.
## Resultado: O índice do código genético usado para a tradução (se houver
## múltiplas respostas pode ser retornado qualquer uma).


# Importar a biblioteca
from Bio.Seq import Seq

# Indicar o arquivo usado
arquivo = 'rosalind_ptra.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')

# Separar a sequêcia de DNA e de aminoácidos
sequencia_dna = Seq(conteudo[0])
sequencia_aa = Seq(conteudo[1])

# Verificar qual tabela de tradução é a correta para a sequência de AA
# Saiba mais em: http://www.bioinformatics.org/JaMBW/2/3/TranslationTables.html
for tabela in range(1, 16):
    if tabela == 7 or tabela == 8:
        pass
    else:
        traducao = sequencia_dna.translate(to_stop=True, table=tabela)
        if traducao == sequencia_aa:
            print(tabela)
            break
