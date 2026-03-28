import re
import glob
import os

files = [
    "01_INTRODUCAO_V2.md",
    "02_VISAO_GERAL_V2.md",
    "03_01_ACH01_V2_REESTRUTURADO.md",
    "03_02_ACH02_V2_REESTRUTURADO.md",
    "03_03_ACH03_V2_REESTRUTURADO.md",
    "03_04_ACH04_V2_REESTRUTURADO.md",
    "04_COMENTARIOS_GESTOR_V2.md",
    "05_CONCLUSAO_V2.md",
    "06_PROPOSTAS_ENCAMINHAMENTO_V2.md"
]
base_dir = "/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2"

para_num = 1
quadro_num = 1
tabela_num = 1

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace {§} with paragraph number
    def repl_para(m):
        global para_num
        res = f"{para_num}."
        para_num += 1
        return res
    content = re.sub(r"\{\§\}", repl_para, content)
    
    # Replace {Q} with quadro number
    def repl_quadro(m):
        global quadro_num
        res = f"{quadro_num}"
        quadro_num += 1
        return res
    content = re.sub(r"\{Q\}", repl_quadro, content)
    
    # Replace {T} with tabela number
    def repl_tabela(m):
        global tabela_num
        res = f"{tabela_num}"
        tabela_num += 1
        return res
    content = re.sub(r"\{T\}", repl_tabela, content)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
        
print(f"Total paragraphs: {para_num-1}")
print(f"Total quadros: {quadro_num-1}")
print(f"Total tabelas: {tabela_num-1}")

