import spacy as sp
from collections import Counter

nlp = sp.load('en_core_web_sm')

sentence1 = nlp('I have seen a bear. I can’t bear this pain.')

for token in sentence1:
 print(f'{token.text:10}{token.pos_:10}')
 if not token.is_punct and not token.is_space:
    cnts = Counter(token.pos_ )

print(cnts)
