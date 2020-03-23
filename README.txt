Loading individual ingredients:
	-- Actual name of the product
	-- Category for what it roughly is (flour, Sugar, ...) Plural when appropriate
	-- Tags to specify what kind (flour : wheat, rice, ...)
	-- when multiple categories of product have same WF, add multiple tags and remove addn lines as needed
	-- nes - not especially specified OR Not Elsewhere Specified

Dictionary needed for aliasing foods!


Process from website to ingredient display:
	-- Extract ingredients list and directions using python tool
	-- Parse ingredients with nyt ingredient tagger 
	-- Generate objects
	-- Get WF data
	-- Display

Possible methods for extracting ingredients:
### My fav?: ###
	-- ripping out all script... and extracting raw text
	-- matching every line against a dictionary file for cooking and extracting those lines w/ best matches
		-01- 
	-- hoping it'll work xD

