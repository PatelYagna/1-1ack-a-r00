# Life Expectancy Analysis via Water, Air, and Sanitation Quality Metrics
Authors: Daniel Huynh, Jacob Pham, Johnny Diep, and Yagna Patel

## Problem
We are addressing the problem of correlating environmental factors like water, air, and sanitation quakity  with life expectancy in various populations. 
By analyzing these metrics, we aim to determine the weights of each factor and understand their contribution to life expectancy.

## Statement
This information can be used to develop and implement public health interventions that improve environmental conditions and
promote health and well-being. 
Goverments can use this model to plan their budgets and health efforts arrcordingly to ensure the welfare of their people and so organizations
can more specifically focus their efforts within a country. 

## Usage
To use this program, follow these steps:

1. Ensure that you have the necessary CSV files (`Population using safely managed drinking water.csv`, `Population using safely managed sanitation services.csv`, `Concentration of fine particulate matter.csv`, `Life expectancy.csv`) in the same directory as `main.py`.
2. Run the `main.py` file.
3. The program will prompt you to choose from the following options:
   - Calculate life expectancy: This option allows you to input weights for water access, sanitation, and pollution to estimate life expectancy.
   - Look up a country's statistics: This option allows you to enter a country name and retrieve its corresponding statistics.
   - Quit
4. Follow the on-screen instructions and input the required information.
5. The program will provide the estimated life expectancy or display the statistics for the chosen country.
6. Additionally, the program produces a global map with countries that are color-coordinated with life expectancy.
   
## Additional Details
- The program reads data from the CSV files to extract important dates and values for each metric.
- It calculates the weights of each metric using the provided data and numpy, running the algorithm to find the inverse of the matrix. 
- The resulting weights can be used to estimate life expectancy and generate a world map based on the calculated life expectancies.
- The program uses the PyGal library to create visualizations, specifically a world map showing life expectancy based on clean water access, sanitation,
  and pollution weights.

## Limits
- Time limit didn't allow us to fully create the program we had in mind.
- Only three metrics are used to calculate the weight on life expectancy.
- The CSV files don't have statistics/metrics for every country. Additionally,
  some countries only have statistics for two metrics but may be missing one or vice versa.

## Strengths
- The program can be scaled quickly to accommodate a larger data set. This requires adding more rows/columns in the matrix.
- Adding a larger data set will also make it more accurate because the weights would be more evenly distributed.

## Exapansions
- Analyze other metrics like diseases and health spending to improve model accruacy
- Analyze other types of necessary contributers to life expectancy. 

## Complexity
**Time Complexity for Each Function and Operation** 
- `translate_country_name_to_abbreviation` function: O(1)
- `worldRender` function: O(n)
- `read_csv` function: O(n)
- `weight_of_environmental_factors` function: O(n)
- `questions` function: O(1)
- `main` function:  O(n)
- 'metrics' function: O(n)
- Numpy Operations Time Complexities:
	- Inverse (pinv) operation: O(n^3) because its not a perfect matrix.
	- Matrix multiplication (@) operation: O(n^3)

**Space Complexity for Each Function and Operation** // not accurate.
- `country_dictionary`: O(n).
- `translate_country_name_to_abbreviation`: O(1)
- `worldRender`: space complexity: O(n), where n is the number of countries in the `country_dictionary`.
- `read_csv` space complexity: O(n)
- `weight_of_environmental_factors`: O(m), where m is the number of countries in the `country_dictionary`.
- Numpy Operations Space Complexity:
  - numpy operations have space complexity proportional to the size of the input matricies being processed.

## Citations
- World Health Organization. (n.d.).
  Life expectancy at birth (years).
  World Health Organization.
  https://www.who.int/data/gho/data/indicators/indicator-details/GHO/life-expectancy-at-birth-(years)
- World Health Organization. (n.d.-b).
  Population using safely managed sanitation services (%).
  World Health Organization.
  https://www.who.int/data/gho/data/indicators/indicator-details/GHO/population-using-safely-managed-sanitation-services-(-)
- World Health Organization. (n.d.-b).
  Population using safely managed drinking-water services (%).
  World Health Organization.
  https://www.who.int/data/gho/data/indicators/indicator-details/GHO/population-using-safely-managed-drinking-water-services-(-) 
- World Health Organization. (n.d.-e).
  SDG indicator 11.6.2 concentrations of fine particulate matter (PM2.5).
  World Health Organization.
  https://www.who.int/data/gho/data/indicators/indicator-details/GHO/concentrations-of-fine-particulate-matter-(pm2-5) 
