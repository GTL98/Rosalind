# --- Fornecido: Uma string s de DNA com até 1000 nucleotídeos --- #
# --- Problema: A quantidade de cada nucleotídeo em s, separado por espaço. A ordem é adenina (A), citosina (C), guanina (G) e timina (T) --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    s = txt.read()

# --- Contar quantas adeninas há em s --- #
A = s.count('A')

# --- Contar quantas citosinas há em s --- #
C = s.count('C')

# --- Contar quantas guaninas há em s --- #
G = s.count('G')

# --- Contar quantas timinas há em s --- #
T = s.count('T')

# --- Mostrar a resposta --- #
print(f'{A} {C} {G} {T}')
