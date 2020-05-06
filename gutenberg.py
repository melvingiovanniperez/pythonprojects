from nltk.corpus import gutenberg

def firstdict(filename):
    d = {}
    for line in gutenberg.sents(filename):
        if line[0] not in d:
            d[line[0]] = 1
        else:
            d[line[0]] += 1
    return d 

def top_ten(d):
    d = sorted(d, key=d.get, reverse = True)
    return d[:10]
    
