file = open('dots_and_dashes_easy_input.txt', 'r')
#file = open('dots_and_dashes_easy_sample_input.txt', 'r')
output = open('output.txt', 'w')

Lines = file.readlines()
 
d1 = {
'A': '.',
'B': '...',
'C': '..-',
'D': '.-.',
'E': '-',
'F': '.--',
'G': '-..',
'H': '-.-',
'I': '..',
'J': '--.',
'K': '---',
'L': '....',
'M': '...-',
'N': '..-.',
'O': '.-',
'P': '..--',
'Q': '.-..',
'R': '.-.-',
'S': '.--.',
'T': '.---',
'U': '-.',
'V': '-...',
'W': '-..-',
'X': '-.-.',
'Y': '--',
'Z': '-.--',
'.': '.....',
',': '....-',
'!': '...-.',
'?': '...--',
"'": '..-..',
'"': '..-.-',
';': '..--.',
':': '..---',
'(': '.-...',
')': '.-..-',
'[': '.-.-.',
']': '.-.--',
'{': '.--..',
'}': '.--.-',
'0': '--..',
'1': '--.-',
'2': '---.',
'3': '----',
'4': '--...',
'5': '--..-',
'6': '--.-.',
'7': '--.--',
'8': '---..',
'9': '---.-',
'+': '----.',
'-': '-----',
'*': '-.--.',
'/': '-.---',
'%': '-.-.-'
}

d2 = {}
for key in d1.keys():
    d2[d1[key]] = key

first = True
res = ''
# Strips the newline character
for line in Lines:
    if first:
        first = False
    else:
        words = line.split(' / ')
        for word in words:
            letters = word.split(' ')
            for letter in letters:
                res += d2[letter.strip()].upper()
            res += ' '
        res += '\n'
    
    
#print(res)
output.write(res)
file.close()
output.close()
