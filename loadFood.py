def fromDB(foods):
		"""
		Takes list of Food objects, searches the DB and adds WF details
		input: foods - List of Food objects
		output: foods - List of Food objects w/ WF added
		"""
    DBfile = openDB()

    for line in DBfile:
        line = line.split(",")
        for food in foods:
            if food.name in line[0]:
                for tag in food.tags:
                    if tag in line[1]:
                        food.addDetails(formatDetails(line))

    return foods


def openDB():
    return open("FoodResourcesSORTED.csv")

def formatDetails(line):
    wfParts = list[2].split(";")
    return list([int(num) for num in wfParts if num.isnumeric()], int(list[-1]))
# Formats input line so it can easily be added to details
# Format: list( [ int,int,int ] ,int)
