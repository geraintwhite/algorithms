import sys


commands = {
    'LDA': '0000',
    'STA': '0001',
    'LDAN': '0010',
    'ADD': '0011',
    'SUB': '0100',
    'MLT': '0101',
    'DIV': '0110',
    'JF': '0111',
    'JB': '1000',
    'JFE': '1001',
    'JBE': '1010',
    'CLO': '1011',
    'PAN': '1100',
    'PAC': '1101',
    'NOP': '1110',
    'END': '1111'
}

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = 'program.txt'

with open(file_name, 'r') as f:
    output = []
    for line in f.read():
        parts = line.split(' ')
        output.append(commands[parts[0]] + parts[1])

with open(file_name, 'w') as f:
    for line in output:
        f.write(line + '\r\n')