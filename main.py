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

speech = input("Enter a speech file: ")

with open(speech) as speech_file:
    for line in speech_file:
        print(line)

    with open('dict.txt') as f:
        for line in f:
            line: str = line.strip().split()
            if len(line) > 0:
                print(line)
