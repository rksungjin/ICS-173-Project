import csv
import sys

inputfile = "C:/Users/RK/OneDrive/Desktop/Coding/211.csv"
outputfile = "211-summary-agg.csv"
from categories import categoryMap

zipcodes = {}
categories = {}
# We know the names of the zip code and category columns
zipfield = "Contact Zip Code"
taxonomyfield = "Taxonomy: AIRS Term"

with open(inputfile, "r", encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    #lines = dict();
    for line in csv_reader:
        zipcode = line[zipfield]
        # Capture all values for a zipcode in a dict in a dict of zipcodes
        if not (zipcode in zipcodes):
            zipcodes[zipcode] = dict()
        taxonomyKey = line[taxonomyfield]
        if taxonomyKey in categoryMap:
           taxonomy = categoryMap.get(taxonomyKey) or "Other"
        else: 
            taxonomy = "Other"
        categories[taxonomy] = 1
        if not taxonomy in zipcodes[zipcode]:
            zipcodes[zipcode][taxonomy] = 0
        zipcodes[zipcode][taxonomy] = zipcodes[zipcode][taxonomy] + 1

# For demo purposes, uncomment this line to only use 5 of the categories
#categories = list(categories)[0:4]

# The first column name is the zipcode
headernames = ['zipcode']
# Create column names for each taxonomy/category
for category in list(categories):
    headernames.append( category )

# Write the extract file
with open(outputfile, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Write column headers
    writer.writerow( headernames )

    # Get the zipcodes
    for zip, contents in zipcodes.items():
        # The first output column is the zipcode
        valuelist = [zip]
        # Add a column for each category
        for category in list(categories):
            count = 0
            if category in contents:
                count = contents[category]
            valuelist.append( count )
        writer.writerow( valuelist )
