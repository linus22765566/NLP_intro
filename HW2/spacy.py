
import spacy
import pandas as pd
import csv

qq = pd.read_csv('data.csv')

# load english language model
nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])
subid = []
sublabel = []
for i in range(len(qq)):
    S_flag = False
    V_flag = False
    O_flag = False
    text = qq['sentence'][i]
    subid.append(qq['id'][i])
    # create spacy 
    doc = nlp(text)

    for token in doc:
        # print(token.text,'->',token.pos_)
        if (token.dep_=='nsubj' and qq['S'][i] == token.dep_):
            S_flag = True

        elif (token.dep_=='dobj'and qq['O'][i] == token.dep_):
            O_flag = True

        elif (token.dep_=='ROOT'and qq['V'][i] == token.dep_):
            V_flag = True
    if(S_flag and O_flag and V_flag):
        sublabel.append(1)
    else:
        sublabel.append(0)

dict = {'id': subid, 'label': sublabel} 
df = pd.DataFrame(dict) 
df.to_csv('submission.csv',index = None)

