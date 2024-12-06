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
                mft_dictionary.update({ line[0]: CATEGORIES[line[1]] })
            else:
                # 1:many mapping of word to mfts
                mft_dictionary.update({ line[0]: ", ".join([CATEGORIES[mapping] for mapping in line[1:]])})

speech = input("Enter a speech file: ")

with open(speech) as speech_file:
    for line in speech_file:
        for category, foundation in CATEGORIES.items():
            word_count = 0
            for stem, mfoundation in mft_dictionary.items():
                if foundation == mfoundation:
                    regex = re.compile(stem.replace('*', '+'))
                    match = re.findall(regex, line)  
                    if match != None and len(match) != 0:  
                        print("MATCH:", match)
                        word_count += len(match) # TODO should it be 1? this will have duplicates
            mft_counts.update({ foundation: word_count })

pprint.pprint(mft_counts)
