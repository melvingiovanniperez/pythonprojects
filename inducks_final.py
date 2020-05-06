from nltk.corpus import stopwords

story_to_hero = {}
with open('inducks_herocharacter.isv') as ref:
    next(ref)
    for line in ref:
        line = line.split('^', 2)
        story_to_hero[line[0]] = line[1]

stopWords = set(stopwords.words('english'))
punctuation = '-.()—,"'


def get_words(title):
    title = title.lower().split()
    result = []
    for word in title:
        if word not in stopWords:
            newword = ''
            for c in word:
                if c not in punctuation:
                    newword += c
            if newword != '':
                result.append(newword)
    return result


chacode_to_cha = {}
with open('inducks_charactername.isv') as names:
    next(names)
    for line in names:
        line = line.split('^', 5)
        if line[1] == 'en' and line[3] == 'Y':
            chacode_to_cha[line[0]] = line[2]

def is_english_title(line):
    if line[0] in 'ADWS':
        return True

story_dict = {}
with open('inducks_story.isv') as storyref:
    next(storyref)
    for line in storyref:
        if is_english_title(line):
            storycode, b, c, d, e, storytitle, f = line.split('^', 6)
            if storytitle != '':
                story_dict[storycode] = storytitle

hero_to_wordfreqs = {}
herocodes = story_to_hero.values()

for story in story_to_hero:
    hero = story_to_hero[story]
    if hero not in hero_to_wordfreqs:
        hero_to_wordfreqs[hero] = {}
    if story in story_dict:
        title = story_dict[story]
        words = get_words(title)
        for word in words:
            if word not in hero_to_wordfreqs[hero]:
                hero_to_wordfreqs[hero][word] = 1
            else:
                hero_to_wordfreqs[hero][word] += 1


for code in chacode_to_cha:
    if code in hero_to_wordfreqs and len(hero_to_wordfreqs[code]) > 0:
        most_fre_words = hero_to_wordfreqs[code]
        fre_words_ordered = sorted(most_fre_words,
                                   key=most_fre_words.get, reverse=True)[:5]
        print(f'Top words for {chacode_to_cha[code]}')
        for word in fre_words_ordered:
            print(f'     {hero_to_wordfreqs[code][word]:>3} {word}')
