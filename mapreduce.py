# Open file
file = open("log.txt", "r")

# Read all words
data = file.read().split()

# Mapper phase
mapped = []

for word in data:
    mapped.append((word, 1))

print("Mapper Output:")
print(mapped)

# Reducer phase
result = {}

for key, value in mapped:
    if key in result:
        result[key] += value
    else:
        result[key] = value

print("\nReducer Output:")

for key in result:
    print(key, result[key])



    # ---------------- THEORY ----------------

# MapReduce is a programming model used for processing large datasets
# in distributed computing environments such as Hadoop.
# It divides processing into two main phases:
# 1) Mapper Phase
# 2) Reducer Phase

# Mapper:
# The mapper reads input data and converts it into key-value pairs.
# Example:
# ERROR -> (ERROR, 1)

# Reducer:
# The reducer combines similar keys and performs aggregation.
# Example:
# (ERROR,1), (ERROR,1) -> ERROR 2

# In this experiment, a log file is processed using MapReduce concepts.
# The program counts how many times each word/log type appears in the file.

# Distributed processing means multiple systems can process different
# parts of data simultaneously, making big data processing faster.

# ---------------- CODE EXPLANATION ----------------

# open("log.txt", "r")
# Opens the log file in read mode.

# file.read()
# Reads complete file content.

# split()
# Splits text into separate words using spaces.

# mapped = []
# Creates an empty list to store mapper output.

# mapped.append((word,1))
# Creates key-value pair for every word.

# Example:
# INFO -> (INFO,1)

# result = {}
# Dictionary used for reducer output.

# if key in result:
# Checks whether word already exists in dictionary.

# result[key] += value
# Increases count if key already exists.

# else:
# Creates new key if word appears first time.

# print()
# Displays mapper and reducer outputs.

# ---------------- VIVA QUESTIONS ----------------

# Q1. What is MapReduce?
# MapReduce is a programming model used for distributed processing
# of large datasets.

# Q2. What is Mapper?
# Mapper processes input data and generates key-value pairs.

# Q3. What is Reducer?
# Reducer combines mapper outputs and generates summarized results.

# Q4. What is distributed processing?
# Processing data using multiple systems simultaneously.

# Q5. Why is MapReduce important?
# It helps process very large datasets efficiently.

# Q6. What is the output of Mapper?
# Key-value pairs.

# Q7. What is the output of Reducer?
# Final summarized/count result.

# Q8. Why is Hadoop used?
# Hadoop is used for storage and distributed processing of big data.

# Q9. What is key-value pair?
# A data format consisting of a key and its associated value.

# Q10. Which data structure is used in reducer phase here?
# Dictionary.