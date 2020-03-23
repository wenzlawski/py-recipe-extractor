from requests import get
import re
from urllib3.util import parse_url

html = [
#				"http://www.foodnetwork.co.uk/recipes/flourless-french-apple-tarts.html",
#				"https://www.jamieoliver.com/recipes/bread-recipes/christmas-tree-camembert/",
#				"https://tasty.co/recipe/one-pot-garlic-parmesan-pasta",
				"https://www.bbcgoodfood.com/recipes/chicken-pasta-bake"
			 ]

import urllib3

http = urllib3.PoolManager()
for page in html:
	with open("pages/" + parse_url(page).host + ".html", "w") as f:
		f.write(str(http.request('get', page).data))
