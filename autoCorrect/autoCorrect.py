import pandas
f = pandas.read_csv(r'C:\Users\user\vscode\FacebookHackathon\autoCorrect\dictionary.tsv', sep='\t', header=None)
d = {}
for row in f.itertuples():
    d[row[1]] = row[2]
inp = pandas.read_csv(r'C:\Users\user\vscode\FacebookHackathon\autoCorrect\autocorrect_easy_sample_input.txt')

for word in inp.itertuples():
    if word[1] in d.keys():
        print("IN")
    else:
        print("OUT")