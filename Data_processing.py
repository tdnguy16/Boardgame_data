import pandas as pd
from collections import Counter

### Read excel file
df = pd.read_excel(r'Publisher Specific_RAW.xlsx')

### CEALN UP COLUMN VALUES
##  New column with list of designer names
#   Remove special characters from string, leave only names separated by commas
for index, x in enumerate(df['designer']):
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace("'", '')

    # Turn string into name list
    x = list(x.split(','))

    # Remove space at beginning and end of list element
    y = []
    for name in x:
        y.append(name.strip())

    # Remove blank from name lists
    while "" in y:
        y.remove("")

    # Replace old string of names with new list
    df.at[index, 'designer'] = y

##  New column with list of artist names
#   Remove special characters from string, leave only names separated by commas
for index, x in enumerate(df['artist']):
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace("'", '')

    # Turn string into name list
    x = list(x.split(','))

    # Remove space at beginning and end of list element
    y = []
    for name in x:
        y.append(name.strip())

    # Remove blank from name lists
    while "" in y:
        y.remove("")

    # Replace old string of names with new list
    df.at[index, 'artist'] = y

##  New column with list of publisher
# Remove special characters from string, leave only names separated by commas
for index, x in enumerate(df['publisher']):
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace("'", '')

    # Turn string into name list
    x = list(x.split(','))

    # Remove space at beginning and end of list element
    y = []
    for name in x:
        y.append(name.strip())

    # Remove blank from name lists
    while "" in y:
        y.remove("")

    # Replace old string of names with new list
    df.at[index, 'publisher'] = y

##  New column with list of category
# Remove special characters from string, leave only names separated by commas
for index, x in enumerate(df['category']):
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace("'", '')

    # Turn string into name list
    x = list(x.split(','))

    # Remove space at beginning and end of list element
    y = []
    for name in x:
        y.append(name.strip())

    # Remove blank from name lists
    while "" in y:
        y.remove("")

    # Replace old string of names with new list
    df.at[index, 'category'] = y

##  New column with list of mechanic
#   Remove special characters from string, leave only names separated by commas
for index, x in enumerate(df['mechanic']):
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace("'", '')

    # Turn string into name list
    x = list(x.split(','))

    # Remove space at beginning and end of list element
    y = []
    for name in x:
        y.append(name.strip())

    # Remove blank from name lists
    while "" in y:
        y.remove("")

    # Replace old string of names with new list
    df.at[index, 'mechanic'] = y

##  New column with list of family
#   Remove special characters from string, leave only names separated by commas
for index, x in enumerate(df['family']):
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace("'", '')

    # Turn string into name list
    x = list(x.split(','))

    # Remove space at beginning and end of list element
    y = []
    for name in x:
        y.append(name.strip())

    # Remove blank from name lists
    while "" in y:
        y.remove("")

    # Replace old string of names with new list
    df.at[index, 'family'] = y

### COUNT NUMBER OF VALUES FOR EACH GAME AND SAVE TO NEW COLUMNS
##  New column of number of designers for each game
for index, x in enumerate(df['designer']):
    df.at[index, 'number_designer'] = len(x)

##  New column of number of artists for each game
for index, x in enumerate(df['artist']):
    df.at[index, 'number_artist'] = len(x)

##  New column of number of publishers for each game
for index, x in enumerate(df['publisher']):
    df.at[index, 'number_publisher'] = len(x)

##  New column of number of category for each game
for index, x in enumerate(df['category']):
    df.at[index, 'number_category'] = len(x)

##  New column of number of mechanic for each game
for index, x in enumerate(df['mechanic']):
    df.at[index, 'number_mechanic'] = len(x)

##  New column of number of family for each game
for index, x in enumerate(df['family']):
    df.at[index, 'number_family'] = len(x)

### CALCULATE METRICS
##  find k for mechanic
#   combine all mechanic into a list
total_mechanic = []
for mechanic in df['mechanic']:
    total_mechanic = total_mechanic + mechanic

#   count k for mechanic
unique_mechanic = Counter(total_mechanic).keys()
k_mechanic = len(unique_mechanic)
print(k_mechanic)

##  find k for category
#   combine all category into a list
total_category = []
for category in df['category']:
    total_category = total_category + category

#   count k for category
unique_category = Counter(total_category).keys()
k_category = len(unique_category)
print(k_category)

##  find k for family
#   combine all family into a list
total_family = []
for family in df['family']:
    total_family = total_family + family

#   count k for family
unique_family = Counter(total_family).keys()
k_family = len(unique_family)
print(k_family)

##  make a dict of mechanics and their occurrences in all games
#   count occurrences of each mechanic and append to a list
mechanic_occur = []
for mechanic in unique_mechanic:
    x = total_mechanic.count(mechanic)
    mechanic_occur.append(x)

#   combine the list of unique mechanics and the list of their occurrences in a dict
dict_mechanic_occur = dict(zip(unique_mechanic, mechanic_occur))


### Save to excel file
df.to_excel("Publisher Specific_CLEAN.xlsx")
