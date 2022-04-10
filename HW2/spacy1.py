
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
        if (token.dep_=='nsubj' and  token.text in qq['S'][i] ):
            S_flag = True

        elif (token.dep_=='dobj' and  token.text in qq['O'][i] ):
            O_flag = True

        elif (token.dep_=='ROOT' and  token.text in qq['V'][i] ):
            V_flag = True
    if(S_flag and O_flag and V_flag):
        sublabel.append(1)
    else:
        sublabel.append(0)

dict = {'id': subid, 'label': sublabel} 
df = pd.DataFrame(dict) 
df.to_csv('submission.csv',index = None)

