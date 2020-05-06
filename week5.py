numbers = [3, 1, 4, 9, 4]
def mymin(numbers):
    least = numbers[0]
    for i in numbers:
        if i < least:
            least = i
    return least

words = ['box', 'bologna', 'bats', 'best']

def long(words, n):
    big = []
    for word in words:
        if len(word) > n:
            big.append(word)
    return big

def firstlong(words, n):
    for word in words:
        if len(word) > n:
            return word

def histogram(numbers, char):
    for n in numbers:
        print(char*n)

def odd_even(numbers):
    odds = []
    evens = []
    for n in numbers:
        if n%2 != 0:
            odds.append(n)
        else:
            evens.append(n)
    return odds+evens

def allit(words):
    first_letter = words[0][0].lower()
    for w in words[1:]:
        if w[0].lower() != first_letter:
            return False
        else:
            return True

def anti_allit(words):
    firsts = [words[0][0]].lower()
    for w in words[1:]:
        if w[0].lower() in firsts:
            return False
        else:
            firsts.append(w[0])
    return True

def addpairs(L):
    pairs = []
    for n in L[:]:
        L.remove(n)
        for n2 in L:
            add= n + n2
            pairs.append(add)
    return pairs

def endings(word):
    cut = []
    for i in range(len(word)):
        scraps = word[i:]
        cut.append(scraps)
    return cut

def vhistogram(numbers, char):
    height = max(numbers)
    width = range(len(numbers))
    change = height 
    for h in range(height, 0, -1):
        for n in numbers:
            if n >= h:
                print(char, end='')
            else:
                print(' ', end='')
        print()

def larger_than_both(numbers):
    out = []
    for i in range(1, len(numbers)-1):
        if numbers[i] > numbers[i+1] and numbers[i] > numbers[i-1]:
            out.append(numbers[i])
    print(out)

def progress(string):
    words = string.split()
    record = 0
    found = []
    for word in words:
        if len(word) > record:
            found.append(word)
            record = len(word)
    return ', '.join(found)

def midchars(strings):
    startchars = []
    endchars = []
    result = []
    for s in strings:
        startchars.append(s[0])
        endchars.append(s[-1])
        for c in s[1:-1]:
            if c not in startchars and c not in endchars and c not in result:
                result.append(c)
    copy = result[:]
    for letter in copy:
        if letter in startchars or letter in endchars:
            result.remove(letter)
    return ''.join(sorted(result))

