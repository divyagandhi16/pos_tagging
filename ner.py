import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp('Apple is looking at buying U.K. startup for $1 billion')

for ent in doc.ents:
    print(f"Entity: {ent.text} | Label: {ent.label_} | Description: {spacy.explain(ent.label_)}")