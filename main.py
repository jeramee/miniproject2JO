# INF601 - Advance Programming with Python
# Jeramee Oliver
# Mini Project 2

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.

# (5/5 points) Proper import of packages used.
import re
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
sns.set() # apply the default seaborn theme

# Now your matplotlib plots will be styled with seaborn's default theme
# which in my opinion looks better than matplotlib's default theme

# Start of program
# Create our charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

df = pd.read_csv('US-Presidents.csv')

column_names = df.columns.tolist()
# print(column_names)

net_worth = df['Net worth((millions of 2022 US$))']

# print(net_worth)

comparison_table = df[['Age', 'Net worth((millions of 2022 US$))', 'Political party[11]', 'Years in office', 'IQ']]
# print(comparison_table)

# print(df['Education'])

term = df['Years in office']
# print(term)  # if you want to print and see the contents of term


# Sanitized the data from the years.
def calculate_years(term):
    years = re.findall(r'\d{4}', term)
    start_year = years[0]

    if len(years) < 2:
        if "present" in term.lower():
            end_year = datetime.now().year
        else:
            end_year = start_year
    else:
        end_year = years[1]

    total_years = int(end_year) - int(start_year)
    return total_years

# Use the calculate_years function on 'Years in office' column
df['Total Years'] = df['Years in office'].apply(calculate_years)

# print out the results
# print(df['Total Years'])


df['IQ'] = df['IQ'].fillna('120')
df['IQ'] = df['IQ'].apply(lambda x: max(map(int, re.findall(r'\d+', x))))
# print(df['IQ'])

column_names = df.columns.tolist()
# print(column_names)

# The regex \D+ means "one or more non-digit characters".
df['Net worth((millions of 2022 US$))'] = df['Net worth((millions of 2022 US$))'].str.replace('\D+', '', regex=True)

# Convert to integer
df['Net worth((millions of 2022 US$))'] = df['Net worth((millions of 2022 US$))'].astype(int)

# print(df['Net worth((millions of 2022 US$))'])


df['Education'] = df['Education'].apply(lambda x: 0 if 'No formal education' in x else 1 if 'did not graduate' in x else 2)
# print(df['Education'])

# In this line, we first split the string on spaces, take the first part,
# then use a regex to replace all non-numeric characters with an empty string,
# and finally, convert the result to integers.
df['Age'] = df['Age'].str.split(' ').str[0].replace('\D+', '', regex=True).astype(int)

# print(df['Age'])



# Code for Comparing Networth to Age
plt.figure(figsize=(10,6))
plt.scatter(df['Age'], df['Net worth((millions of 2022 US$))'])
plt.xlabel('Age')
plt.ylabel('Net worth((millions of 2022 US$))')
plt.title('Comparing Net worth with Age')
plt.savefig('charts/networth_vs_age.png')  # save the plot as a png file in "charts" directory
# Clears plot had trouble with that
plt.show()


# Code for Comparing Networth to Political Party
color_dict = {'Democratic': 'blue', 'Republican': 'red'}

# Sort dataframe by 'Net worth((millions of 2022 US$))'
df = df.sort_values('Net worth((millions of 2022 US$))', ascending=True)

plt.figure(figsize=(10,6))

for party, color in color_dict.items():
    plt.scatter(df[df['Political party[11]'] == party]['Political party[11]'],
                df[df['Political party[11]'] == party]['Net worth((millions of 2022 US$))'],
                color=color)

plt.xlabel('Political party[11]')
plt.ylabel('Net worth((millions of 2022 US$))')
plt.title('Comparing Net worth with Political Party')
plt.savefig('charts/networth_vs_political_party.png') # save the plot as a png file in "charts" directory
# Clears plot had trouble with that
plt.show()

# Code for Comparing Networth to IQ
plt.figure(figsize=(10,6))
plt.scatter(df['IQ'], df['Net worth((millions of 2022 US$))'])
plt.xlabel('IQ')
plt.ylabel('Net worth((millions of 2022 US$))')
plt.title('Comparing Net worth with IQ')
plt.savefig('charts/networth_vs_IQ.png')
plt.show()

# Code for Comparing Networth to Education
plt.figure(figsize=(10,6))
plt.scatter(df['Education'], df['Net worth((millions of 2022 US$))'])
plt.xlabel('Education in a scale from 0-2 from lowest to highest')
plt.ylabel('Net worth((millions of 2022 US$))')
plt.title('Comparing Net worth with Education')
plt.savefig('charts/networth_vs_Education.png')
plt.show()

# Code for Comparing Networth to Number of Years in office
plt.figure(figsize=(10,6))
plt.scatter(df['Total Years'], df['Net worth((millions of 2022 US$))'])
plt.xlabel('Number of Years in Office')
plt.ylabel('Net worth((millions of 2022 US$))')
plt.title('Comparing Net worth with Years in office')
plt.savefig('charts/networth_vs_Years.png')
plt.show()

print('Your program has completed running. Please collect your documents in the charts folder master.')
