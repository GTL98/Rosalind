# --- Dado: Seis números que não excedem 20.000, onde cada número representa a quantidade de indivíduo de um genótipo --- #
# --- Problema: O número de descendentes que possuam ao menos 1 alelo dominante, assumindo que cada indivíduo gere exatamente 2 descendentes --- #

# --- Informar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter cada genótipo --- #
    conteudo = txt.read().split()
    AA_AA = int(conteudo[0])
    AA_Aa = int(conteudo[1])
    AA_aa = int(conteudo[2])
    Aa_Aa = int(conteudo[3])
    Aa_aa = int(conteudo[4])
    aa_aa = int(conteudo[5])

# --- Calcular chances de passar a menos 1 alelo dominante --- #
d_AA_AA = AA_AA * 1
d_AA_Aa = AA_Aa * 1
d_AA_aa = AA_aa * 1
d_Aa_Aa = Aa_Aa * 0.75
d_Aa_aa = Aa_aa * 0.5
d_aa_aa = aa_aa * 0

# --- Total de descendentes com no mínimo 1 alelo dominante --- #
d_total = (d_AA_AA + d_AA_Aa + d_AA_aa + d_Aa_Aa + d_Aa_aa + d_aa_aa) * 2

# --- Mostrar a resposta --- #
print(d_total)
