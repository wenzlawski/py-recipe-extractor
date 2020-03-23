from food import Food
from loadFood import fromDB

class Recipe:
    def __init__(self, ingredients):
        self.ingredients = fromDB(ingredients) # ingredients are Food objected w/ name, quantity, unit and tag (dried, fresh, ...)

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
        return totalWF
