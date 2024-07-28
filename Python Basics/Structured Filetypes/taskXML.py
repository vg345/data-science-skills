# import Element Tree and parse the XML file
import xml.etree.ElementTree as ET
tree = ET.parse('movie.xml') 
root = tree.getroot()

# find movie elements and print all its child tags. 
for movie in root.iter('movie'):
    for child in movie:
        print(child.tag, child.attrib)

# Iterate over the description tags and print out the text.
for description in root.iter('description'):
    print(description.text)

# use itertext to print description of all movies
print(''.join(root.itertext()))

# counting the favorite and not favorite movies
count_true = 0
count_false = 0
for movie in root.iter('movie'):
    # not all attributes are formatted the same way. So I used lower() to fix that.
    if movie.attrib['favorite'].lower() == 'true':
        count_true += 1
    else:
        count_false += 1

# print output in a clear way
print(f"The file has a list of {count_true} movies that are favorites and {count_false} movies that are not.")