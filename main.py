
"""
Daniel McCarragher
CS 108
Final project

World Smoking stats from 1980-2012 broken down by gender and country *This was originally for the whole world. The data was overhwelming, so I manipulated it to include the North american countries and the world data
https://corgis-edu.github.io/corgis/csv/smoking/

Question #1 :#For this question, I had to calculate the average for daily cigarrettes and manipulate the data to add a new column that contained this data in the csv file. Then with the variables below, I was able to create a simple bar chart that showed on average over a 32 year span from 1980-2012, how each country and the world is consuming cigarrettes. 

Question #2: I had to seperate the USA data from the rest of the data within the csv file. Once I was able to store the data in variables, I then was able to use the imported module to create a simple scatterplot showing the trend of total smokers in the US.

Question #3: This scatterplot depicts the change over time in the increase and/or decrease in individuals who smoke. As we can see from the data, in general, male population is tending to increase, while women tend to stay the same, even slightly decrease.
"""


#import modules
import matplotlib.pyplot as plt
#open and read csv file
with open("smoking.csv") as textFile:
    statList = textFile.readlines()[1:]
#create empty lists for variables
countryList = []
yearList = []
dailycigaretteAvg = []
SmokersTotal = []

#split headers apart to seperate data. split using the , in between each header
for line in statList:
    
    Country, Year, Daily_cigarettes_smoked, Data_Percentage_Male, DataPercentage_Female, DataPercentageTotal, Smokers_Total, Total_Femal_Smokers, Total_Male_Smokers, dailycigaretteAverage = line.split(",") 
  #add the empty lists to the 
    countryList.append(Country)
    yearList.append(Year)
    dailycigaretteAvg.append(float(dailycigaretteAverage))
    SmokersTotal.append(int(Smokers_Total))
  #Print the questions and header. Also is asking for the users input on which question they would like to answer
print("Welcome to my Final Project!")
print()
print("NA Vs. World Smoking Statistics")
print("-------------------------")
print("Which question would you like to answer?")
print()
print("1 - Which country, on average, smokes the most cigarrettes daily from 1980-2012?")
print()
print("2 - For the United States, since 1980 - 2012, is the number of smokers increasing or decreasing?")
print()
print("3 - Do men or women tend to consume more cigarettes? *According to World Data")
print()

#create a while loop to keep asking for input until user gives an input that is acceptable
while True:
    userinput = input("Your Selection: ")

    if not userinput.isnumeric():
        print("Input must not contain letters")
    elif userinput > "3":
        print("Input must be 1, 2, or 3.")
    else:
        break
print()      
print("You have selected question", userinput,"!")
#For this question, I had to calculate the average for daily cigarrettes and manipulate the data to add a new column that contained this data in the csv file. Then with the variables below, I was able to create a simple bar chart that showed on average over a 32 year span from 1980-2012, how each country and the world is consuming cigarrettes. 
if userinput == "1":

  
  countryList = ["United States", "Canada", "World"]
  dailycigaretteAvg = [27.5, 24.9, 18.1]
  values = [27.5, 24.9, 18.1]
# Create the plot
  fig, ax = plt.subplots()
  ax.bar(countryList, dailycigaretteAvg)

# Add the values to the bars
  for i, v in enumerate(values):
    ax.text(i, v + 1, str(v), ha='center',   fontweight='bold')

# Set the labels and title
  plt.xlabel("Country")
  plt.ylabel("Average number of cigarettes smoked per day")
  plt.title("Smoking statistics by Country - Avg from 1980-2012")

# Set the maximum value of the y-axis to 35
  ax.set_ylim([0, 35])

# Display the plot
  plt.show()
#User input for question 2. For this question, I had to seperate US data from the rest of the csv file. Then, had to create new empty lists for the data that included the years and the total number of smokers in the US. 
if userinput =="2":
  #create empty lists for variables
  usa_years = []
  usasmokers = []

# Loop through rows and separate USA data
  for row in statList:
    Country, Year, Daily_cigarettes_smoked, Data_Percentage_Male, DataPercentage_Female, DataPercentageTotal, Smokers_Total, Total_Femal_Smokers, Total_Male_Smokers, dailycigaretteAverage = row.split(",") 
    #loop trough each row and see if the country is equal to United states
    if Country == 'United States':
        usasmokers.append(int(Smokers_Total))
        usa_years.append(int(Year))

# Create scatter plot with the lists from above. Addinig axis labels as well.
  plt.scatter(usa_years, usasmokers)
  plt.title('USA Smokers from 1980 to 2012')
  plt.xlabel('Year')
  plt.ylabel('Smokers (millions)')
  plt.show()

#User input for question 3
if userinput == "3":
  #create empty lists
  world_years = []
  world_male_smokers = []
  world_female_smokers = []

for row in statList:
    Country, Year, Daily_cigarettes_smoked, Data_Percentage_Male, DataPercentage_Female, DataPercentageTotal, Smokers_Total, Total_Female_Smokers, Total_Male_Smokers, daily_cigarette_average = row.split(",")
#This scatterplot depicts the change over time in the increase and/or decrease in individuals who smoke. As we can see from the data, in general, male population is tending to increase, while women tend to stay the same, even slightly decrease.
    if Country == "World":
        world_years.append(int(Year))
        world_male_smokers.append(int(Total_Male_Smokers))
        world_female_smokers.append(int(Total_Female_Smokers))

# Create scatter plot with thhe defined vairables above. Including axis labels
plt.scatter(world_years, world_male_smokers, label='Male')
plt.scatter(world_years, world_female_smokers, label='Female')
plt.title('Total Male vs Female Smokers Around the World')
plt.xlabel('Year')
plt.ylabel('Number of Smokers (millions)')
plt.legend()
plt.show()
