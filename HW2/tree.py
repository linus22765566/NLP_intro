
import spacy
from spacy import displacy
import pandas as pd
# Load the language model
nlp = spacy.load("en_core_web_sm")
qq = pd.read_csv('data.csv')

subid = []
count = 0
sublabel = []
text = ""
for i in range(len(qq)):
    S_flag = True
    V_flag = False
    O_flag = False
    possible_S = []
    possible_O = []
    V_children = []
    Verb = ""
    if(text != qq['sentence'][i]):
        text = qq['sentence'][i]
        count += 1
    subid.append(qq['id'][i])
    print('now id = ',qq['id'][i])
    # create spacy 
    doc = nlp(text)

    for token in doc:
        # print(token.text,'->',token.pos_)
        if (token.dep_=='nsubj'):
            possible_S.append(token.text)

        elif (token.dep_=='dobj' and token.head.text in qq['V'][i]):
            O_flag = True

        elif (token.dep_=='ROOT' and token.text in qq['V'][i]):
            V_children = [str(child) for child in token.children]
            V_flag = True
    # do conclusion

    for Ss in possible_S:
        if (str(Ss) in V_children) and (str(Ss) in qq['S'][i]):
            S_flag = True
    if(S_flag and O_flag and V_flag):
        sublabel.append(1)
    else:
        sublabel.append(0)
    if count == 10:
      break
dict = {'id': subid, 'label': sublabel} 
df = pd.DataFrame(dict) 
df.to_csv('submission.csv',index = None)


# # nlp function returns an object with individual token information, 
# # linguistic features and relationships
# doc = nlp(sentence)

# print ("{:<15} | {:<8} | {:<15} | {:<20}".format('Token','Relation','Head', 'Children'))
# print ("-" * 70)

# for token in doc:
#   # Print the token, dependency nature, head and all dependents of the token
#   # if((token.dep_) == 'nsubj' or (token.dep_) =='ROOT' or (token.dep_) =='attr'):
#   print ("{:<15} | {:<8} | {:<15} | {:<20}".format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children])))
  
 # Use displayCy to visualize the dependency 