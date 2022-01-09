import numpy as np
import pandas as pd
import random
from collections import defaultdict
import spacy as sp
import re

load_model = sp.load("en_core_web_sm")
# Custom tokenizer
load_model.tokenizer.rules = {key: value for key, value in load_model.tokenizer.rules.items() if "'" not in key and "’" not in key and "‘" not in key}
assert [t.text for t in load_model("can't")] == ["can't"]
assert [t.text for t in load_model("don't")] == ["don't"]
assert [t.text for t in load_model("won't")] == ["won't"]
assert [t.text for t in load_model("I'm")] == ["I'm"]


def get_words(file_path) -> list:
    t = open(file_path, "r")
    x = t.read()
    txt = x.lower()
    l = txt.split()
    return l


def get_ngrams(words, size) -> list:
    l = []
    if size == 0:
        return l
    else:
        for i in range(len(words) - size + 1):
            l.append(tuple(words[i:i+size]))
        return l    


def get_counts(n_grams) -> dict:
    res = defaultdict(lambda: defaultdict(lambda: 1))
    for i in range(len(n_grams) - 1):
        res[n_grams[i]][n_grams[i + 1]] = res[n_grams[i]][n_grams[i + 1]] + 1
    return res


def generate_gram(counts, context) -> tuple:
    k = list(counts[context].keys())
    if k:
        d = counts[context].values()
        probabilities = []
        s = sum(d)
        for i in d:
            probabilities.append(i / s)
        word = k[np.random.choice(len(k), p=probabilities)]
        return word
    else:
        return ()


def generate_sentence(counts, context, length=10) -> list:
    l = []
    for i in range(length + 1):
        j = generate_gram(counts, context)
        l.append(j)
        context = j
    return l


def stringify(sentence) -> list:
    return " ".join("".join(gram[0]) for gram in sentence)


def insert_newlines(sentence):
    a = sentence.split()
    ret = ''
    every = 10

    # Line breaks every 5 to 13 words
    for i in range(0, len(a), every):
        every=random.randint(5, 13)
        # Capitlize first word per line
        ret += (' '.join(a[i:i+every])).capitalize() + '\n'
    return ret


def fix_grammar(lines):
    # Capitalize first letter of sentences
    lines = '. '.join(i.capitalize() for i in re.split('\.\s', re.sub('^\s+', '', lines)))
    lines = re.sub('[()]', '', lines)
    lines = lines.replace('"', '')
    doc = load_model(lines)
    tagged_sent = [(w.text, w.tag_) for w in doc]

    # Capitalize I's
    normalized_sent = [w.capitalize() if w == "i" or w == "i'm" or w == "i'll" or w == "i'd" or t in ["PROPN"] else w for (w,t) in tagged_sent]
    normalized_sent[0] = normalized_sent[0].capitalize()
    lines = re.sub(" (?=[\.,'!?:;])", "", ' '.join(normalized_sent))
    lines = re.sub(r"(\A\w)|"+ "(?<!\.\w)([\.?!] )\w|",
            lambda x: x.group().upper(), 
            lines)

    return lines


class Generator:
    def __init__(self, corpus_name):
        words = get_words(corpus_name)
        n_grams = get_ngrams(words, 2)
        counts = get_counts(n_grams)        
        
        # generate text
        context = n_grams[np.random.choice(len(n_grams))]
        sentence = generate_sentence(counts, context, length=random.randint(25, 60))
        fixed = fix_grammar(stringify(sentence))
        self.lines = insert_newlines(fixed)
    
    def __str__(self):
        return self.lines
