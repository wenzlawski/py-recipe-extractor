from loadFood import fromDB


class Food:
    def __init__(self, name, quantity, unit="", loadWF=False):
        self.name = name
        # need self.tags for special types (fresh, dried, etc); if no tag passed, init as "base"
        if unit in ["g", "kg", ""]:
            # TODO: Problem with foods that come in pieces, not kg
            if unit == "g":
                self.unit = "kg"
                self.quantity = quantity / 1000
            else:
                self.unit = unit
                self.quantity = quantity
        else:
            raise ValueError("Bad unit!")
        if loadWF:
            fromDB([self])

    def __str__(self):
        return str(self.quantity) + self.unit + " " + self.name

    def addDetails(self, details):
        self.allWF = details[0]
        self.totalWF = details[1]

    def getAllWF(self):
        pass


class Recipe:
    def __init__(self, ingredients, name=""):
        self.name = name
        # ingredients are Food objected w/ name, quantity, unit and tag (dried, fresh, ...)
        self.ingredients = fromDB(ingredients)

    def __str__(self):
        return ", ".join([ingredient.__str__() for ingredient in self.getIngredients()])

    def getIngredients(self):
        return self.ingredients.copy()

    def getIngredientsWF(self):
        return [ingredient.allWF() for ingredient in self.getIngredients()]

    def getWF(self, WFtype="all"):
        totalWF = 0
        for ingredient in self.getIngredients():
            totalWF += ingredient.totalWF()
