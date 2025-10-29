from typing import List, Optional, Dict
from random import random
import json
import time
from playsound3 import playsound

FILES = [
    'data/inoue-donaire-1.txt',
    'data/jirov-toney.txt',
    'data/miscellaneous.txt'
]
VOICE = 'Neural2-D'
START = 'START'
END = 'END'

Sequence = List[str]
Frequencies = Dict[str, int]
Chain = Dict[str, Frequencies]

def build_chain(combos: List[Sequence]) -> Chain:
    chain = {}

    for combo in combos:
        last_output = START
        n = len(combo)

        for i, action in enumerate(combo + [END]):
            output = END if action == END else action[0]

            if last_output not in chain:
                chain[last_output] = {output: 1}
            else:
                if output not in chain[last_output]:
                    chain[last_output][output] = 1
                else:
                    chain[last_output][output] += 1

            last_output = output

    return chain

def resample(freqs: Frequencies) -> str:
    total = sum(freqs.values())

    freq_target = random() * total
    freq_sum = 0

    for action, freq in freqs.items():
        freq_sum += freq

        if freq_sum >= freq_target:
            return action

def generate(chain: Chain) -> Sequence:
    combo = [resample(chain[START])]

    while (next_action := resample(chain[combo[len(combo) - 1]])) != END:
        combo.append(next_action)

    return combo

###
# build and export chain
combos = []
for file_name in FILES:
    with open(file_name) as f:
        combos += [combo.split() for combo in f.read().strip().split('\n')]

with open('chain.json', 'w') as f:
    chain = build_chain(combos)
    json.dump(chain, f)
###

# ###
# # import chain
# with open('chain.json') as f:
#     chain = json.load(f)
# ###

###
# start the "flow" game
mp3s = { # for orthodox
    # '1': ,
    # '2': 'cross',
    # '3': 'left-hook',
    # '4': 'right-hook',
    # '5': 'left-uppercut',
    # '6': 'right-uppercut'
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six'
}
action = START

while True:
    action = resample(chain[action])

    if action == END:
        action = START

        print()
        time.sleep(random() + 1)
    else:
        print(action, end=' ', flush=True)
        playsound(f'{VOICE}/{mp3s[action]}.mp3')
###
