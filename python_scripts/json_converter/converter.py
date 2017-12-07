import json
import pprint
# Sets a nice level of indent for pprint
pp = pprint.PrettyPrinter(indent=4)

# Create a JSON converted class object
class JSON_convert:

	def __init__(self, json_1):
			with open(json_1) as json_file:
				self.json_converted = json.load(json_file)


# Import named file here - file in same dir as python script
json_file_1 =  'example.json'

# Makes a variable of the converted JSON file
converted = JSON_convert(json_file_1).json_converted

# Example print statements to drill into the JSON
# print the keys of the converted json
print('*' * 25)
pp.pprint(converted.keys())
# print the keys of the tracks document within the json
print('*' * 25)
pp.pprint(converted['tracks'].keys())
# print the first item in the items array from tracks
print('*' * 25)
print('Number of items: {}'.format(len(converted['tracks']['items'])))
print('*' * 25)
pp.pprint(converted['tracks']['items'][0])
print('*' * 25)
