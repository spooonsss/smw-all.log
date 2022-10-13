import os
import os.path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

all_log = open('../all.log', 'rt').read()

split = all_log.split('\norg ')

for bank, text in enumerate(split[1:]):
    with open(f'bank_{bank:02X}.asm', 'wt') as outputfile:
        outputfile.write('org ')
        outputfile.write(text)
