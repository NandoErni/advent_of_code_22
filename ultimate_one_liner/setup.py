import os
from pathlib import Path
import shutil

parent_path = Path(os.getcwd()).parent.absolute()
all_dirs = sorted([dir for dir in os.listdir(parent_path) if dir.startswith('day')])

INPUT_DIR = 'inputs'

if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)

for dir in all_dirs:
    input_path = os.path.join(parent_path, dir, 'input.txt')
    if not os.path.exists(input_path):
        continue
    new_input = os.path.join(INPUT_DIR, f'{dir}_input.txt')
    print(f'{input_path} -> {new_input}')

    shutil.copyfile(input_path, new_input)

ultimate_one_liners = []
for dir in all_dirs:
    input_path = os.path.join(parent_path, dir, 'one_line.py')
    new_input = os.path.join(INPUT_DIR, f'{dir}_input.txt')

    with open(input_path, 'r') as fili:
        file_content = fili.read().replace('input.txt', new_input).replace('Part ', f'Day {dir[-2:]} Part ')
        if file_content.strip() == '':
            continue
        ultimate_one_liners.extend(file_content.split('\n'))

ultimate_one_liner = " or ".join(ultimate_one_liners)
improved_ultimate_one_liner = f'exec("".join(map(chr, {str(list(map(ord, " or ".join(ultimate_one_liners))))})))'

with open("one_line.py", "w") as text_file:
    text_file.write(ultimate_one_liner)

with open("one_line_improved.py", "w") as text_file:
    text_file.write(improved_ultimate_one_liner)