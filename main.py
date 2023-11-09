'''
Project Name: Life Expectany Analysis via Water, Air and Sanitation Quality Metrics

Authors: Daniel Huynh, Jacob Pham, Johnny Diep, and Yagna Patel

Mission Statement:
We use metrics such as water quality, air quality, and sanitation to correlate them with life expectancy in order to find the weight of 
each environmental factor contributing to lower life expectancy in certain populations. This information can be used to develop and 
implement public health interventions that improve environmental conditions and promote health and well-being.
'''

#Imports
import pygal
from pygal.style import Style 
import csv
import numpy as np

# PyGal needs these abbreviations
# list of all countries that have the 3 factors listed down.
# we can turn this into a for loop.
def translate_country_name_to_abbreviation(country_name):
	country_codes = {
		'United Republic of Tanzania': 'tz',
		'Kuwait': 'kw',
		'Singapore': 'sg',
		'Democratic Republic of the Congo': 'cd',
		'Ethiopia': 'et',
		'Kiribati': 'ki',
		'Uganda': 'ug',
		'Malawi': 'mw',
		"Lao People's Democratic Republic": 'la',
		'Togo': 'tg',
		'Nepal': 'np',
		'Madagascar': 'mg',
		'Guinea-Bissau': 'gw',
		'Senegal': 'sn',
		'Lesotho': 'ls',
		'Zimbabwe': 'zw',
		'Nigeria': 'ng',
		'Cambodia': 'kh',
		'Tonga': 'to',
		'Sao Tome and Principe': 'st',
		'Mongolia': 'mn',
		'Ghana': 'gh',
		'Fiji': 'fj',
		"Côte d’Ivoire": 'ci',
		'Mexico': 'mx',
		'Dominican Republic': 'do',
		'Gambia': 'gm',
		'Philippines': 'ph',
		'Lebanon': 'lb',
		'Peru': 'pe',
		'Suriname': 'sr',
		'Myanmar': 'mm',
		'Viet Nam': 'vn',
		'Bangladesh': 'bd',
		'Iraq': 'iq',
		'Chad': 'td',
		'Central African Republic': 'cf',
		'Samoa': 'ws',
		'Honduras': 'hn',
		'Paraguay': 'py',
		'Bhutan': 'bt',
		'Ecuador': 'ec',
		'Georgia': 'ge',
		'Azerbaijan': 'az',
		'Albania': 'al',
		'Colombia': 'co',
		'Morocco': 'ma',
		'Algeria': 'dz',
		'Kyrgyzstan': 'kg',
		'Tunisia': 'tn',
		'Serbia': 'rs',
		'Russian Federation': 'ru',
		'Uzbekistan': 'uz',
		'The former Yugoslav Republic of Macedonia': 'mk',
		'Costa Rica': 'cr',
		'Romania': 'ro',
		'Armenia': 'am',
		'Jordan': 'jo',
		'Montenegro': 'me',
		'Brazil': 'br',
		'Ukraine': 'ua',
		'Sierra Leone': 'sl',
		'Poland': 'pl',
		'Belarus': 'by',
		'Italy': 'it',
		'Malaysia': 'my',
		'Lithuania': 'lt',
		'Portugal': 'pt',
		'Ireland': 'ie',
		'Bulgaria': 'bg',
		'Latvia': 'lv',
		'Qatar': 'qa',
		'Switzerland': 'ch',
		'Estonia': 'ee',
		'United States of America': 'us',
		'Hungary': 'hu',
		'Czechia': 'cz',
		'Slovenia': 'si',
		'New Zealand': 'nz',
		'Japan': 'jp',
		'Chile': 'cl',
		'Austria': 'at',
		'Bahrain': 'bh',
		'Greece': 'gr',
		'Norway': 'no',
		'Republic of Korea': 'kr',
		'Canada': 'ca',
		'Slovakia': 'sk',
		'France': 'fr',
		'Israel': 'il',
		'Luxembourg': 'lu',
		'Spain': 'es',
		'Finland': 'fi',
		'Belgium': 'be',
		'Sweden': 'se',
		'Cyprus': 'cy',
		'Malta': 'mt',
		'United Kingdom of Great Britain and Northern Ireland': 'gb',
		'Germany': 'de',
		'Denmark': 'dk',
		'Netherlands': 'nl',
	}
	if country_name in country_codes:
		return country_codes[country_name]

# function to create a global map with life expectancy based on clean water access, sanitation levels, and pollution weights.
def worldRender(country_dictionary, inverse_with_life, mean_age):
	custom_style = Style( 
	colors=('#cc0000', '#f1c232', '#6aa84f', '#3d85c6', '#674ea7'))

	# stylizes and creates appropriate label for world map
	worldmap_chart = pygal.maps.world.World(style=custom_style)
	worldmap_chart.title = 'Life Expectancy Based on Clean Water Access, Sanitation, and Pollution Weights'

	# countries are sorted into separate categories based on the life expectancy.
	rank_dictionary = {}
	rank_dictionary0to70 = {}
	rank_dictionary70to75 = {}
	rank_dictionary75to80 = {}
	rank_dictionary80to85 = {}
	rank_dictionary85to100 = {}


	# loops through the country_dictionary and calculates the life expectancy. Life expectancy and country are recorded in one of the categories
	for country in country_dictionary:
		if len(country_dictionary[country]) == 4:
			abbreviation = translate_country_name_to_abbreviation(country)

			water = float(country_dictionary[country][0])
			sanitation = float(country_dictionary[country][1])
			pollution = float(country_dictionary[country][2])

			# this require manual input from a user. The inputs are the weight of water, sanitation, and pollution.
			# 
			est_life = float((water * inverse_with_life[0][0]) - (sanitation * inverse_with_life[1][0]) - (pollution * inverse_with_life[2][0])) + mean_age

			rank = float(est_life)
			rank_dictionary[abbreviation] = rank

			# ranking system developed to correlate countries and color with their respective weights/life expectancy.
			if rank <= 69:
				rank_dictionary0to70[abbreviation] = rank
			if rank > 69 and rank <= 75:
				rank_dictionary70to75[abbreviation] = rank
			if rank > 75 and rank <= 79:
				rank_dictionary75to80[abbreviation] = rank
			if rank > 79 and rank <= 85:
				rank_dictionary80to85[abbreviation] = rank
			if rank > 85:
				rank_dictionary85to100[abbreviation] = rank

	# creates the visuals using the categorized dictionary on the world map
	worldmap_chart.add('<69', rank_dictionary0to70)
	worldmap_chart.add('69-74', rank_dictionary70to75)
	worldmap_chart.add('75-79', rank_dictionary75to80)
	worldmap_chart.add('80-85', rank_dictionary80to85)
	worldmap_chart.add('>85', rank_dictionary85to100)

	worldmap_chart.render()
	worldmap_chart.render_to_file('world_map.svg')
	print('World_Map.svg Generated!')

# function for reading the csv file to find the important dates and the right values for each metric.
def read_csv(country_dictionary):
	with open('Population using safely managed drinking water.csv') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
		for line in data:
			if (line[12] == 'Total') and (line[9] == '2019'):
				country_dictionary[line[7]] = []
				country_dictionary[line[7]].append(line[29])

	with open('Population using safely managed sanitation services.csv') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
		for line in data:
			if (line[12] == 'Total') and (line[9] == '2019'):
				try:
					country_dictionary[line[7]].append(line[29])
				except:
					country_dictionary[line[7]] = []
					country_dictionary[line[7]].append(line[29])

	with open('Concentration of fine particulate matter.csv') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
		for line in data:
			if (line[12] == 'Total') and (line[9] == '2019'):
				#values = line[29].split()
				try:
					country_dictionary[line[7]].append((float(line[23])/12)*100)
				except:
					country_dictionary[line[7]] = []
					country_dictionary[line[7]].append((float(line[23])/12)*100)

	with open('Life expectancy.csv') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
		for line in data:
			if (line[9] == '2019') and (line[12] == 'Both sexes') and (line[1] == 'Life expectancy at birth (years)'):
				try:
					country_dictionary[line[7]].append(line[29])
				except:
					country_dictionary[line[7]] = []
					country_dictionary[line[7]].append(line[29])



# function for calculating the weightes of each metric.
def weight_of_environmental_factors(country_dictionary):
	t = 0
	factors = 0
	life_expectancy = 0
	mean_age = 0
	counter = 0
	#Find mean_age
	for country in country_dictionary:
		if len(country_dictionary[country]) == 4:
			mean_age += float(country_dictionary[country][3])
			counter += 1
	mean_age = mean_age / counter
	for country in country_dictionary:
		# check if the country data has the expected format (four values: water, air, sanitation, and life expectancy)
		if len(country_dictionary[country]) == 4:
			if t == 0:
				# extract and convert the factor values for the current country and place them in an matrix.
				factors = np.array([float(country_dictionary[country][0]),
									float(country_dictionary[country][1]),
									-float(country_dictionary[country][2])], dtype='float64')

				# extract and convert the values and create a matrix
				life_expectancy = np.array([float(country_dictionary[country][3]) - mean_age],dtype='float64')
				t += 1

			else:
				a = np.array([float(country_dictionary[country][0]),
							float(country_dictionary[country][1]),
							-float(country_dictionary[country][2])],dtype='float64')
				b = np.array([float(country_dictionary[country][3])- mean_age],dtype='float64')

				factors = np.vstack([factors, a])
				life_expectancy = np.vstack([life_expectancy, b])

	return factors, life_expectancy, mean_age

# find the percent error of the prediction
def metrics(country_dictionary, inverse_with_life, mean_age):
	difference = 0
	counter = 0
	total = 0
	# iterate through countries that have all four factors
	for country in country_dictionary:
		if len(country_dictionary[country]) == 4:
			# formula for percent error
			difference = ((((inverse_with_life[0][0] * float(country_dictionary[country][0])) - (inverse_with_life[1][0] * float(country_dictionary[country][1])) - (inverse_with_life[2][0] * float(country_dictionary[country][2])) + mean_age)) - float(country_dictionary[country][3])) * 100
			difference = difference / float(country_dictionary[country][3])
			total += abs(difference)
			counter += 1
	# return the percent error for actual vs our model's calculated life expectancies 
	print(f'Average Percent Error: {(total / counter):.2f} %')


# interactive menu for estimating life expectancy and looking up country statistics.
def questions(country_dictionary, inverse_with_life, mean_age):
	while True:

		# print out menu and ask for user input.
		print("\nMenu:")
		print("1. Calculate life expectancy")
		print("2. Look up a country's statistics")
		print("3. Quit")

		try:
			#Gets user input
			user_choice = int(input("Enter Input: "))
			if user_choice == 1:
				# input the weights of each metric. used to calculate the est life.
				water = float(input('What percentage of the population has access to safely managed water?: '))
				sanitation = float(input('What percentage of the population has access to safely managed sanitation?: '))
				pollution = float(input('What is the percentage of pollution relative to U.S. National Ambient Air Quality Standard (12.0 µg/m^3):?: '))

				# calculations
				print(f'Water:{water}%')
				print(f'Sanitation:{sanitation}%')
				print(f'Pollution:{pollution} ')

				est_life = (water * inverse_with_life[0][0]) - (sanitation * inverse_with_life[1][0]) - (pollution * inverse_with_life[2][0]) + mean_age
				print(f'The expected life expectancy is: {est_life}')

			elif user_choice == 2:
				# ask for country name
				try:
					country_name = input('What country would you like to look up?: ')
					# look up the country's statistics
					print(f'''
							Percent of population with access to safely managed water: 
							{country_dictionary[country_name][0]}% 
							Percent of population with access to safely managed sanitation services:
							{country_dictionary[country_name][1]}%
							Percentage of pollution relative to U.S. National Ambient Air Quality Standard (12.0 µg/m^3):
							{country_dictionary[country_name][2]}
							Life Expectancy (years):
							{country_dictionary[country_name][3]}''')
				except:
					print('Not a valid country')

			#ends the program
			elif user_choice == 3:
				print('Goodbye')
				break
			# input validation.
			else:
				print("Invalid Input!")
		# catch Error in user input
		except TypeError or ValueError:
			print('Invalid Input')

def main():
	# dictionary to store the data
	country_dictionary = {}
	read_csv(country_dictionary)


	factors, life_expectancy, mean_age = weight_of_environmental_factors(country_dictionary)
	# rest of your code for calculations and user input
	inverse = np.linalg.pinv(factors) 
	inverse_with_life = inverse @ life_expectancy #the @ is matrix multiplicaiton

	# calling function to create the map.
	worldRender(country_dictionary, inverse_with_life, mean_age)
	metrics(country_dictionary, inverse_with_life, mean_age)
	# calling function for interactive menu for estimating life expectancy and looking up country statistics.
	questions(country_dictionary, inverse_with_life, mean_age)

if __name__ == "__main__":
	main()