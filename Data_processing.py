import pandas as pd
from collections import Counter

#### Clean main data and set up metrics
### Variable list
#   total_mechanic = [] : list of all mechanics used in all games, with duplication
#   total_category = [] : list of all categories used in all games, with duplication
#   total_family = []   : list of all families used in all games, with duplication

#   unique_mechanic = [] : list of unique mechanics
#   unique_category = [] : list of unique categories
#   unique_family = []   : list of unique families
#   unique_designer = [] : list of unique designers/teams

#   k_mechanic = int : number of unique mechanics
#   k_category = int : number of unique categories
#   k_family = int   : number of unique families

#   dict_mechanic_occur = {} : a dictionary of unique mechanics and their occurrences in all games

### Read excel file
##  Read the main database
df = pd.read_excel(r'Publisher Specific_RAW.xlsx')

##  Read the category and mech list
#   mechanism list
df_mechanism = pd.read_excel(r'category and mech list.xlsx', sheet_name='list of mechanism')
#   category list
df_category = pd.read_excel(r'category and mech list.xlsx', sheet_name='list of category')

### CLEAN UP COLUMN VALUES
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
##  find k for mechanic from Prof. Chen's list
#   combine all mechanic into a list
total_mechanic = []
for mechanic in df_mechanism['mechanism']:
    total_mechanic.append(mechanic)

#   count k for mechanic
unique_mechanic = Counter(total_mechanic).keys()
k_mechanic = len(unique_mechanic)

##  find k for category from Prof. Chen's list
#   combine all category into a list
total_category = []
for category in df_category['category']:
    total_category.append(category)

#   count k for category
unique_category = Counter(total_category).keys()
k_category = len(unique_category)

##  find k for mechanic from main database
#   combine all mechanic into a list
# total_mechanic = []
# for mechanic in df['mechanic']:
#     total_mechanic = total_mechanic + mechanic

#   count k for mechanic
# unique_mechanic = Counter(total_mechanic).keys()
# k_mechanic = len(unique_mechanic)

##  find k for category from main database
#   combine all category into a list
# total_category = []
# for category in df['category']:
#     total_category = total_category + category

#   count k for category
# unique_category = Counter(total_category).keys()
# k_category = len(unique_category)

##  find k for family from main database
#   combine all family into a list
# total_family = []
# for family in df['family']:
#     total_family = total_family + family

#   count k for family
# unique_family = Counter(total_family).keys()
# k_family = len(unique_family)

##  make a dict of mechanics and their occurrences in all games
#   count occurrences of each mechanic and append to a list
mechanic_occur = []
for mechanic in unique_mechanic:
    x = total_mechanic.count(mechanic)
    mechanic_occur.append(x)

#   combine the list of unique mechanics and the list of their occurrences in a dict
dict_mechanic_occur = dict(zip(unique_mechanic, mechanic_occur))
#print(dict_mechanic_occur)

##  make a dict of categories and their occurrences in all games
#   count occurrences of each category and append to a list
category_occur = []
for category in unique_category:
    x = total_category.count(category)
    category_occur.append(x)

#   combine the list of unique mechanics and the list of their occurrences in a dict
dict_category_occur = dict(zip(unique_category, category_occur))
#print(dict_category_occur)

### Save to excel file
df.to_excel("Publisher Specific_CLEAN.xlsx")

# ===============================================================================================================

#### CONSTRUCT A DESIGNER_SPECIFIC DATAFRAME
### construct a designer_specific dataframe from all publishers
##  construct designer column
#   combine all designer into a list
total_designer = []
for designer in df['designer']:
    total_designer.append(designer)

#   remove blank value from list of designers/teams
total_designer = [x for x in total_designer if x]

#   make a list of unique designers/teams
unique_designer = [list(x) for x in set(tuple(x) for x in total_designer)]

##  acquire mechanisms used by each designer/team
#   go through main dataframe and acquire mechanisms, categories and families
df_designer = pd.DataFrame(columns=['designer', 'mechanic', 'category', 'family'])
a = 0
for designer in unique_designer:
    list_mechanism = []
    list_category = []
    list_family = []
    for index, x in enumerate(df['designer']):
        if x == designer:
            list_mechanism = list_mechanism + df.iloc[index]['mechanic']
            list_category = list_category + df.iloc[index]['category']
            list_family = list_family + df.iloc[index]['family']
    df_designer.loc[a, 'designer'] = designer
    df_designer.loc[a, 'mechanic'] = list_mechanism
    df_designer.loc[a, 'category'] = list_category
    df_designer.loc[a, 'family'] = list_family
    a = a + 1

#   new col with count of mechanism, categories and families for each designer/team
for index, x in enumerate(df_designer['mechanic']):
    df_designer.at[index, 'number_mechanic'] = len(x)
for index, x in enumerate(df_designer['category']):
    df_designer.at[index, 'number_category'] = len(x)
for index, x in enumerate(df_designer['family']):
    df_designer.at[index, 'number_family'] = len(x)

# ===============================================================================================================

#### Calculate diversity scores for each designer/team, from all publishers
### CALCULATE DIVERSITY SCORE d = y/z
### calculate y = 1 - x
### x = (1/A)^2 + (1/B)^2 + ... + (1/N)^2
### A, B,.. N are the occurrences of A, B,... N mechanics in each game

##  find y for mechanism
for index, mechanic_used in enumerate(df_designer['mechanic']):
    unique_mechanic_designer = list(set(mechanic_used))

    x = 0
    for mechanic in unique_mechanic_designer:
        a = mechanic_used.count(mechanic)
        x += (a / len(mechanic_used)) ** 2

    y = 1 - x

    z = 1 - 1 / k_mechanic

    d = y / z

    df_designer.at[index, 'mechanic_diversity'] = d

##  find y for category
for index, category_used in enumerate(df_designer['category']):
    unique_category_designer = list(set(category_used))

    x = 0
    for category in unique_category_designer:
        a = category_used.count(category)
        x += (a / len(category_used)) ** 2

    y = 1 - x

    z = 1 - 1 / k_category

    d = y / z

    df_designer.at[index, 'category_diversity'] = d

### Save to excel file
df_designer.to_excel("Designer Specific_all publishers.xlsx")

### CALCULATE CATEGORY_DIVERSITY SCORE d = y/z
### calculate y = 1 - x
### x = (1/A)^2 + (1/B)^2 + ... + (1/N)^2
### A, B,.. N are the occurrences of A, B,... N categories in each game

##  find y
# for index, category_used in enumerate(df['category']):
#     x = 0
#     for category in category_used:
#         a = dict_category_occur.get(category)
#         x += (a/len(total_category))**2
#     y = 1 - x
#
#     z = 1 - 1/len(total_category)
#
#     d = y/z
#
#     df.at[index, 'category_diversity'] = d

