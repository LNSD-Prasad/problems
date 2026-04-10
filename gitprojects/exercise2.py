import spacy

nlp = spacy.blank("en")

text = "tony gave 2 $ to peter, bruce gave 5 € to steve"
doc = nlp(text)

currencies = ["$", "€", "£", "₹"]

for i, token in enumerate(doc):
    if token.text in currencies and i > 0 and doc[i-1].like_num:
        print(token.text)