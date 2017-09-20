import random
import sys

from collections import defaultdict

def make_ngrams(n, txt):
    ngrams = defaultdict(list)
    for i in range(len(txt)-n):
        ngrams[txt[i:i+n]].extend(txt[i+n])

    return ngrams

def markov(n, ln, txt, ngrams):
    current = ""
    mx = len(txt)-n
    while True:
        start = random.randint(0, mx)
        if " " in txt[start:]:
            idx = txt.find(" ") + 1
            if idx > mx: continue
            current = txt[idx:idx+n]
            break

    res = current
    for _ in range(ln):
        pos = ngrams[current]
        nxt = random.choice(pos)
        res = "{}{}".format(res, nxt)
        current = res[-n:]

    return res


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        txt = f.read()

    n = int(sys.argv[2])
    ln = int(sys.argv[3])

    ngrams = make_ngrams(n, txt)

    print(markov(n, ln, txt, ngrams))
