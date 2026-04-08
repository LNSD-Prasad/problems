import spacy
nlp=spacy.load("en_core_web_sm")
doc=nlp("DR.strange loves pov bhaji of mumbai.Hulk loves chaat of delhi")
for sentnce in doc.sents:
    print(sentnce)
    for word in sentnce:
        print(word)
