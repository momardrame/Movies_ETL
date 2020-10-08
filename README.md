# Movies Extract Transform and Load
Create a function that takes in three arguments:

# Objective
In this project, a Python script will be created to extract movies datasets from Wikipedia and Kaggle, transform the dataset and loads it.

# Resources
- Python
- Jupyter Notebook

Wikipedia data

    Kaggle metadata

    MovieLens rating data (from Kaggle)

    Create a function to turn the extracted values into a numeric value.

    [found in jupyter notebook LN 27] We’ll call it [def parse_dollars] and [def parse_dollars ] will take in a string and return a floating-point number.

    We’ll start by making a skeleton function with comments explaining each step, and then fill in the steps with actual codede.

# Assumption:

As shown in the data jupyter notebook [LN 86], it is inidcated the there are 7 instances of similar data from Wiki and MovieLens

    Similar Data from Wiki and MovieLens
    box_office : revenue
    release_date_wiki : release_data_kaggle
    title_wiki : title_kaggle
    budget_wiki : budget_kaggle
    Production company(s) : production_companies
    running_time : runtime
    Language : originale_language

# Assumption
Create a function that fills missing data and drop redundant column.

As shown in the data jupyter notebook [LN 95]:

    As shown in the data above the running_time vs the runtime, it was observed that the runtimes are very close together with the Wiki data having outliers
    Wikipedia data has more outliers in comparison to the Kaggle data
    Some Kaggle movie have 0 runtime where Wiki has data.

# Assumption

As shown in the data jupyter notebook [LN 105]

    The budget_wiki data have more outliers compared to the budget_kaggle data.
    There are movies with no data in the Kaggle column, and wiki has budget data.


## Background
## Project Overview
## Resources
## Data Source
## Machine Learning Model
## Findings and Recommendation
