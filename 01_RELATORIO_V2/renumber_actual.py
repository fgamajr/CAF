import re
import os

files = [
    "00_RESUMO_EXECUTIVO_V2.md",
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
fig_num = 1

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    
    # We skip Resumo Executivo from paragraph numbering (it usually is unnumbered or independent)
    # The bug report says: "Namespace collision in paragraph numbering (Resumo §1 vs. Intro §1)"
    # We should NOT number Resumo Executivo lines. The Intro starts at 1.
    is_resumo = (filename == "00_RESUMO_EXECUTIVO_V2.md")
    
    for line in lines:
        # Match paragraph number at the beginning: "X. " where X is digits
        if not is_resumo:
            m = re.match(r'^(\d+)\.\s+(.*)', line)
            if m:
                # This looks like a numbered paragraph
                # Wait, what if it's a numbered list inside a paragraph? Usually those don't start at the very margin, or they are numbered sequentially but restart.
                # In TCU, main paragraphs always start with a number at the beginning of the line.
                line = f"{para_num}. {m.group(2)}"
                para_num += 1
                
        # Match Quadros
        line = re.sub(r'\*\*Quadro \d+\*\*', lambda m: f"**Quadro {quadro_num}**", line)
        
        # Match Tabelas
        line = re.sub(r'\*\*Tabela \d+\*\*', lambda m: f"**Tabela {tabela_num}**", line)
        
        new_lines.append(line)
        
        # Increment if we just matched a Quadro/Tabela title
        if "**Quadro " in new_lines[-1] and "—" in new_lines[-1] and re.match(r'^\*\*Quadro \d+\*\*', new_lines[-1]):
            quadro_num += 1
        elif "**Tabela " in new_lines[-1] and "—" in new_lines[-1] and re.match(r'^\*\*Tabela \d+\*\*', new_lines[-1]):
            tabela_num += 1
            
    with open(path, "w", encoding="utf-8") as f:
        f.write('\n'.join(new_lines))

print(f"Total paragraphs: {para_num-1}")
print(f"Total quadros: {quadro_num-1}")
print(f"Total tabelas: {tabela_num-1}")

