
import spacy
from spacy import displacy
import pandas as pd
# Load the language model
nlp = spacy.load("en_core_web_sm")
# # nlp function returns an object with individual token information, 
# # linguistic features and relationships
sentence = "The principal opposition parties boycotted the polls after accusations of vote-rigging , and the only other name on the ballot was a little-known challenger from a marginal political party ."
doc = nlp(sentence)

print ("{:<15} | {:<8} | {:<15} | {:<20}".format('Token','Relation','Head', 'Children'))
print ("-" * 70)

for token in doc:
  # Print the token, dependency nature, head and all dependents of the token
  # if((token.dep_) == 'nsubj' or (token.dep_) =='ROOT' or (token.dep_) =='attr'):
  print ("{:<15} | {:<8} | {:<15} | {:<20}".format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children])))
  
 # Use displayCy to visualize the dependency 