from nltk.corpus import gutenberg
emma = gutenberg.sents('austen-emma.txt')

def print_sents_with_word(word):
    printed = []
    for line in emma:
        if word in line:
            print(line)

def find_shortest_sent(word):
    sents = []
    for line in emma:
        for w in line:
            if w == word:
                sents.append(line)
    least = sents[0]
    for i in sents:
        if len(i) < len(least):
            least = i
    return least

def conc3(word):
    for line in emma:
        for w in range(len(line)):
            if line[w] == word:
                if w-3 > 0:
                    print(line[w-3:w+4])
                else:
                    print(line[:w+3])
        
