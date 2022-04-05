
import spacy


# load english language model
nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])

text = "The nation 's health maintenance organizations were required to tell the federal government by midnight Monday whether they plan to continue providing health insurance to Medicare recipients next year , raise premiums , or reduce benefits ."

# create spacy 
doc = nlp(text)

for token in doc:
    if (token.dep_=='nsubj'):
        print(token.text)
    # extract object
    elif (token.dep_=='dobj'):
        print(token.text)