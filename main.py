import re
import pprint
import matplotlib.pyplot as plt

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
def run_mft_search(filename: str, search: str):
    print(f"MFT searching for {search}..")
    with open(filename) as speech_file:
        word_count = {}
        # populate categories with zeroes
        for regex in regexes:
            word_count.update({ regex[0]: 0 })

        for line in speech_file:
            if search in line:
                for word in line.split():
                    for regex in regexes:
                        match = re.findall(regex[1], word)  
                        if match != None and len(match) != 0:  
                            # print("MATCH:", match)
                            if not regex[0] in word_count:
                                word_count.update({ regex[0]: 1 })
                            else:
                                word_count[regex[0]] += 1
                    for k, v in word_count.items():
                        mft_counts.update({ CATEGORIES[k]: v })
    
    plt.gcf().subplots_adjust(bottom=0.275)
    plt.xticks(rotation=45, ha='right')
    plt.bar(mft_counts.keys(), mft_counts.values())    
    f = filename.replace(".txt", "") + search.replace(":", "")
    plt.title(f"{search} Moral Foundation Frequency")
    plt.ylabel("Frequency")
    plt.xlabel("Moral Foundations")
    plt.yticks(range(0, 51, 5))
    plt.savefig(f"{f}.png")
    plt.clf()

    with open(f"{f}.csv", "w") as output:
        for k, v in mft_counts.items():
            output.write(f"{k},{v}\n")

    pprint.pprint(mft_counts)
    print("TOTAL:", sum([v for v in mft_counts.values()]))

run_mft_search("speeches/kennedynixon1960.txt", "KENNEDY:")
run_mft_search("speeches/kennedynixon1960.txt", "NIXON:")

run_mft_search("speeches/carterford1976.txt", "CARTER:")
run_mft_search("speeches/carterford1976.txt", "FORD:")

run_mft_search("speeches/carterreagan1980.txt", "CARTER:")
run_mft_search("speeches/carterreagan1980.txt", "REAGAN:")

run_mft_search("speeches/bushclintonperot1992.txt", "BUSH:")
run_mft_search("speeches/bushclintonperot1992.txt", "CLINTON:")
run_mft_search("speeches/bushclintonperot1992.txt", "PEROT:")

run_mft_search("speeches/bushkerry2004.txt", "BUSH:")
run_mft_search("speeches/bushkerry2004.txt", "KERRY:")

run_mft_search("speeches/obamaromney2012.txt", "OBAMA:")
run_mft_search("speeches/obamaromney2012.txt", "ROMNEY:")

run_mft_search("speeches/clintontrump2016.txt", "CLINTON:")
run_mft_search("speeches/clintontrump2016.txt", "TRUMP:")

run_mft_search("speeches/bidentrump2020.txt", "BIDEN:")
run_mft_search("speeches/bidentrump2020.txt", "TRUMP:")

run_mft_search("speeches/harristrump2024.txt", "HARRIS:")
run_mft_search("speeches/harristrump2024.txt", "TRUMP:")
