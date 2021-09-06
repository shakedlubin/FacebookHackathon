import soundfile as sf 
data, samplerate = sf.read(hard.ex.flac)

'''
ile = open('dots_and_dashes_medium_input.txt', 'r')
#file = open('dots_and_dashes_medium_sample_input.txt', 'r')
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


for line in Lines:
    if first:
        first = False
    else:
        len1 = -1
        len2 = -1
        len3 = -1
        curr = 0
        
        ind = line.find("+")
        for i in range(ind,len(line)):
            l = line[i]
            if l=="+":
                curr += 1
            elif curr!=0:
                if curr<len1 or len1==-1:
                    len1 = curr
                elif curr>len2 or len2==-1:
                    len2 = curr
                curr=0
        
        curr = 0
        ind = line.find("-")
        for i in range(ind,len(line)):
            l = line[i]
            if l=="-":
                curr += 1
            elif curr!=0:
                if curr>len3 or len3==-1:
                    len3 = curr
                curr=0
        
                    
        line = line.replace("-"*len3, ' / ')
        line = line.replace('-'*len2, ' ')
        line = line.replace('-'*len1, '*')
        line = line.replace("+"*len2, '-')
        line = line.replace("+"*len1, '.')
        line = line.replace('*', '')

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
'''

