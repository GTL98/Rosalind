## Problema: Conjunto de nucleotídeos no formato FASTA
## Resultado: ID da string com mais discrepância entre elas

# Importar as bibliotecas
from Bio import Phylo
from Bio.Align.Applications import ClustalOmegaCommandline

# Indicar o arquivo usado
arquivo = 'rosalind_clus.txt'

# Infomar o caminho do Clustal Omega
caminho_clustal_omega = r'D:\Clustal Omega\clustalo.exe'

# Informar o arquivo da saída da árvore guia
arquivo_arvore = 'rosalind_clus.dnd'

# Linha de comando do ClustalW
# guidetree_out: arquivo onde será armazenada a árvore guia
# force: se o arquivo já existir, sobrescrever as informações
clustal_omega_cline = ClustalOmegaCommandline(caminho_clustal_omega, infile=arquivo,
                                              guidetree_out=arquivo_arvore, force=True)

# Gerar os arquivos de alinhamento e árvore filogenética
stdout, stderr = clustal_omega_cline()

# Criar a árvore filogenética
arvore = Phylo.read(arquivo_arvore, 'newick')

# Mostrar a resposta_peptideo
Phylo.draw_ascii(arvore)
