from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.allrecipes.com/recipe/162760/fluffy-pancakes/?internalSource=hub%20recipe&referringContentType=Recipe%20Hub')

scraper.title()
scraper.total_time()
scraper.yields()
print(scraper.ingredients())
print(dir(scraper))
scraper.instructions()
scraper.image()
scraper.links()
