temp = []
dew = []
wind = []

# Open file
file = open("sample_weather.txt", "r")

# Read line by line
for line in file:

    # Split values
    values = line.split()

    # Store values
    temp.append(float(values[0]))
    dew.append(float(values[1]))
    wind.append(float(values[2]))

# Calculate averages
avg_temp = sum(temp) / len(temp)

avg_dew = sum(dew) / len(dew)

avg_wind = sum(wind) / len(wind)

# Print output
print("Average Temperature:", avg_temp)

print("Average Dew Point:", avg_dew)

print("Average Wind Speed:", avg_wind)



# ---------------- THEORY ----------------

# Weather data analysis is used to process and analyze
# environmental parameters such as temperature,
# dew point, and wind speed.

# In this experiment, a text file containing weather data
# is read using Python file handling techniques.

# The data is processed line by line and values are extracted
# using the split() function.

# The extracted values are converted into numerical format
# using float() and stored in separate lists.

# Average temperature, average dew point,
# and average wind speed are then calculated.

# This experiment demonstrates:
# - File handling
# - Data processing
# - Statistical calculations
# - Basic data analytics concepts

# Weather data analysis is widely used in:
# - Climate monitoring
# - Forecasting systems
# - Environmental studies
# - Data analytics applications

# ---------------- CODE EXPLANATION ----------------

# temp = []
# Creates empty list for storing temperatures.

# dew = []
# Creates empty list for storing dew point values.

# wind = []
# Creates empty list for storing wind speed values.

# open("weather.txt", "r")
# Opens weather file in read mode.

# next(file)
# Skips first/header line of file.

# for line in file:
# Reads file line by line.

# line.split()
# Splits values using spaces.

# Example:
# "30 20 10"
# becomes:
# ['30', '20', '10']

# float(values[0])
# Converts string into decimal number.

# temp.append()
# Stores temperature values in temp list.

# dew.append()
# Stores dew point values in dew list.

# wind.append()
# Stores wind speed values in wind list.

# sum(temp)
# Calculates total of all temperatures.

# len(temp)
# Calculates total number of temperature values.

# sum(temp)/len(temp)
# Calculates average temperature.

# print()
# Displays final calculated averages.

# ---------------- VIVA QUESTIONS ----------------

# Q1. What is file handling?
# File handling means reading and writing files using programming languages.

# Q2. Why is split() used?
# split() is used to separate values from each line.

# Q3. Why is float() used?
# float() converts string values into numerical values.

# Q4. How is average calculated?
# Average = sum of values / total number of values.

# Q5. What is weather data analysis?
# Weather data analysis means processing and analyzing
# weather parameters such as temperature and wind speed.

# Q6. Why are lists used in this program?
# Lists are used to store multiple values.

# Q7. What does next(file) do?
# It skips the first/header line of the file.

# Q8. What type of file is used here?
# Text file (.txt)

# Q9. Why is file processing important?
# It helps analyze large amounts of stored data efficiently.

# Q10. Which statistical operation is performed here?
# Average calculation.