def indef(text):
    vowels = 'aeiouAEIOU'
    if text[0] in vowels:
        return 'an ' + text
    else:
        return 'a ' + text

def parens(s):
    sent = ''
    for l in s:
        sent += '('+l+')'
    return sent

def wordtriangle(word):
    for i in range(1, len(word)+1):
        print(word[0:i])

def cutstrings(s, i):
    return s[i:]+s[0:i]

def firstdigit(string, default):
    number= '0123456789'
    for c in string:
        if c in number:
            return int(c)
    return default 

def upcase_firsts(s):
    out = ''
    upcase_next = True 
    for char in s:
        if upcase_next:
            out = out + char.upper()
            upcase_next = False
        else:
            out = out + char
        if char == ' ':
            upcase_next = True
    return out

def is_palindrome(s):
    lgt = len(s)
    for i in range(int(lgt/2)):
        if s[i].lower() != s[lgt-1-i].lower():
            return False
    return True

def countmatch(s1, s2):
    if len(s1) <= len(s2):
            short = s1
    if len(s1) > len(s2):
            short = s2
    for i in range(len(short)):
        if s1[i] != s2[i]:
            return i
    return len(short)
            
def grid(s):
    for i in range(0, len(s)):
       print(s[i:]+s[0:i])
