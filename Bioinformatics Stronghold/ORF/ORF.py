# --- Dado: Uma string de DNA com até mil nucleotídeos --- #
# --- Problema: Toda possível proteína que pode ser traduzida de cada possível ORF --- #

# --- Importar as biblioteca --- #
from Bio import SeqIO
from Bio.Seq import Seq

# --- Informar o arquivo --- #
arquivo = ''

# --- Obter a sequência e a sequência reversa complementar --- #
sequencia = ''
sequencia_rev_comp = ''
for registro in SeqIO.parse(arquivo, 'fasta'):
    sequencia = registro.seq
    sequencia_rev_comp = registro.seq.reverse_complement()

# --- Separar em códons a sequência --- #
codons = [sequencia[i:i+3] for i in range(len(sequencia)) if len(sequencia[i:i+3]) == 3]

# --- Separar em codons a sequência reversa complementar --- #
codons_rev_comp = [sequencia_rev_comp[i:i+3] for i in range(len(sequencia_rev_comp)) if len(sequencia_rev_comp[i:i+3]) == 3]

# --- Traduzir as possívels proteínas --- #
orfs = []
for posicao, codon in enumerate(codons):
    # --- Obter a posição do códon ATG --- #
    if codon == 'ATG':
      orf = sequencia[posicao:].translate()
      if '*' in orf:
          orfs.append(orf)

# --- Traduzir as possíveis proteínas da sequência reversa complementar --- #
for posicao, codon in enumerate(codons_rev_comp):
    # --- Obter a posição do códon ATG --- #
    if codon == 'ATG':
        orf = sequencia_rev_comp[posicao:].translate()
        if '*' in orf:
            orfs.append(orf)

# --- Criar uma lista para as respostas --- #
respostas = []

# --- Descobrir onde estão os stop codons --- #
for orf in orfs:
    stop_codon = orf.index('*')

    # --- Obter a proteína gerada da ORF --- #
    proteina = orf[0:stop_codon]

    # --- Adicionar a lista de respostas caso a proteína não esteja nela --- #
    if proteina not in respostas:
        respostas.append(proteina)

# --- Mostrar as respostas --- #
for resposta in respostas:
    print(resposta)
