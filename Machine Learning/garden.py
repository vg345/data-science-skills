# import and load nlp
import spacy
nlp = spacy.load('en_core_web_sm')

# garden path sentences
gardenpathsentences = ['Time flies like an arrow; fruit flies like a banana.','The man whistling tunes pianos.', 'Mary gave the child the dog bit a Band-Aid.', 'That Jill is never here hurts.', 'The cotton clothing is made of grows in Mississippi.']

# tokenize each line and perform named entity recognition on them
for line in gardenpathsentences:
    nlp_gps = nlp(line)
    print(line)
    print([(i, i.label_) for i in nlp_gps.ents])

# explain entities
print('GPE: ', spacy.explain("GPE"))
print('FAC: ', spacy.explain("FAC"))

## Looked up GPE. It's a category for places: countries, cities, states. Associated with 'Mississippi.' Makes sense
## Looked up FAC. Category includes buildings, airports, other physical structures on the map. Not associated with anything in these words but this was in the example file with 'Filmware Awards' 
# which does not make sense since that term should be either an event or a thing. Especially in the context of someone recieving 5 awards, it makes no sense for it to be categorized as a piece fo architecture.