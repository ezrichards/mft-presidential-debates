import re
import pprint

# Presidential Debate-Moral Foundations Theory Cleaner
CATEGORIES = {
    '01': 'HarmVirtue',
    '02': 'HarmVice',
    '03': 'FairnessVirtue',
    '04': 'FairnessVice',
    '05': 'IngroupVirtue',
    '06': 'IngroupVice',
    '07': 'AuthorityVirtue',
    '08': 'AuthorityVice',
    '09': 'PurityVirtue',
    '10': 'PurityVice',
    '11': 'MoralityGeneral'
}

# stores word stems -> moral foundations
mft_dictionary = {}

# stores moral foundations -> appearance count
mft_counts = {}

with open('dictionary.txt') as f:
    for line in f:
        line: str = line.strip().split()
        if len(line) > 0:
            if len(line) == 2:
                # 1:1 mapping of word to mft
                mft_dictionary.update({ line[0]: line[1] })
            else:
                # 1:many mapping of word to mfts
                mft_dictionary.update({ line[0]: ",".join([mapping for mapping in line[1:]])})

speech = input("Enter a speech file: ")

regexes = []
for category, foundation in CATEGORIES.items():
    r = []
    for stem, mfoundation in mft_dictionary.items():
        for mf in mfoundation.split(","):
            if category == mf:
                r.append(stem.replace("*", ".*"))
    regex = re.compile('\\b(' + '|'.join(r) + ')')
    regexes.append([category, regex])

# pprint.pprint(regexes)

with open(speech) as speech_file:
    for line in speech_file:
        word_count = {}
        for word in line.split():
            for regex in regexes:
                match = re.findall(regex[1], word)  
                if match != None and len(match) != 0:  
                    print("MATCH:", match)
                    if not regex[0] in word_count:
                        word_count.update({ regex[0]: 1 })
                    else:
                        word_count[regex[0]] += 1
            for k, v in word_count.items():
                mft_counts.update({ CATEGORIES[k]: v })

pprint.pprint(mft_counts)
