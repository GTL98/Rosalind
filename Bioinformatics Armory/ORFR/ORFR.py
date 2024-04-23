# --- Dado: Uma string de DNA com até mil nucleotídeos --- #
# --- Problema: A maior proteína possível traduzida de uma ORF --- #

# --- Importar a biblioteca --- #
from Bio.Seq import Seq

# --- Informar o arquivo --- #
arquivo = '
# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.read()

    # --- Obter a sequência --- #
    sequencia = Seq(conteudo)

    # --- Obter a sequência reversa complementar --- #
    sequencia_rev_comp = Seq(conteudo).reverse_complement()

# --- Separar em códons a sequência --- #
codons = []
for i in range(len(sequencia)):
    # --- Obter o códon --- #
    codon = sequencia[i:i+3]

    # --- Verificar se o códon possui 3 nucleotídeos --- #
    if len(codon) == 3:
        codons.append(codon)


# --- Separar em códons a sequência reversa_complementar --- #
codons_rev_comp = []
for i in range(len(sequencia_rev_comp)):
    # --- Obter o códon --- #
    codon = sequencia_rev_comp[i:i+3]

    # --- Verificar se o códon possui 3 nucleotídeos --- #
    if len(codon) == 3:
        codons_rev_comp.append(codon)
    

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

# --- Criar uma lista para as proteinas --- #
proteinas = []

# --- Descobrir onde estão os stop codons --- #
for orf in orfs:
    stop_codon = orf.index('*')

    # --- Obter a proteína gerada da ORF --- #
    proteina = orf[0:stop_codon]

    # --- Adicionar a lista de respostas caso a proteína não esteja nela --- #
    if proteina not in proteinas:
        proteinas.append(proteina)

# --- Encontrar a maior proteína --- #
maior_proteina = sorted(
    proteinas,
    key=lambda x: len(x)
    )

# --- Mostrar a resposta --- #
print(maior_proteina[-1])
