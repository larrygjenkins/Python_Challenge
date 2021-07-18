# Python_Challenge
![GitHub Contributors](https://img.shields.io/github/contributors/larrygjenkins/larrygjenkins.github.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Description
The goal of this project was to use Python to work on two distinct scenarios: 
1. Analyzing financial records for a company.
2. Determing the winner of a local election and the breakdown of votes by candidate. 

## Requirements
The financial analysis required a script to calculate and display the following information: 

* The total number of months included in the dataset.
* The net total amount of "profit/loss" over the entire time period.
* The changes in profit/loss over the entire time period and the average of those changes.
* The greatest increase in profit (date and amount) over the time period. 
* The greatest decrease in losses (date and amount) over the time period.
* In addition to displaying these results, they were also exported to a text file.

The election analysis required a script to calculate and display the following information: 

* The total number of votes cast.
* A complete list of all candidates who received votes.
* The percentage of votes received by each candidate.
* The total number of votes received by each candidate. 
* The winner of the election based on popular vote.
* In addition to displaying these results, they were also exported to a text file.

## Repository Organization
The repository contains two folders: PyBank for the financial analysis and PyPoll for the election analysis. 

Within each folder is a main.py file (which contains the Python script), a MainWorkingCopy.ipynb (which contains the Jupyter Notebook used to create each Python script), a Resources folder with the original dataset in csv format, and an Analysis folder containing the text file output of each analysis.

## Challenges
### Financial Analysis
For the financial analysis, the profit/loss data was retrieved from a csv file, which required the values be converted from strings before any calculations could occur. To accomplish this, values were first added to an empty array and then converted to integers.

**For each row in the csv file (after the header), months and values were added to the appropriate array**

    for row in csvreader:
        months.append(row[0])
        values.append(row[1])

**Items in the value array were then converted to integers**

    for i in range(0, len(values)):
        values[i] = int(values[i])

Another loop was used to calculate the change in value each month, and those values were then added to an empty array (monthly_change).

**Finds the change from one integer to the next in the values array**

    for i in range(1, len(values)):
        monthly_change.append(values[i]-values[i-1])

### Election Analysis
For the election analysis, an initial requirement was to determine the number of votes cast in the election. After creating a variable for num_votes and settings its value to 0, the script used a loop to increment the value of the num_votes variable for each row after the header row. 

**Loop used to calculate totl number of votes cast**

    for row in csvreader:
        num_votes += 1

An if statement within this loop was used to create a list of candidates who received votes. 

**When a unique candidate name is found, it is added to the "candidates" array**

        if row[2] not in candidates:
                candidates.append(row[2])

Additionally, a secondary if statement was used to calculate the number of votes each candidate received. 

**Variables assigned to each candidate increase by 1 each time the candidate's name appears**

        if row[2] == candidates[0]:
            candidate0_votes += 1
            
        elif row[2] == candidates[1]:
            candidate1_votes += 1
            
        elif row[2] == candidates[2]:
            candidate2_votes += 1
        
        elif row[2] == candidates[3]:
            candidate3_votes += 1

In the code example above, the candidate's vote variable corresponds to their index within the "candidates" array. This index was used to assign vote totals, calculate the percentage of votes received for each candidate, and determine the election winner based on popular votes received.   

## Technologies Used
* Python
* Jupyter Notebook

## Questions?
Contact me at the following locations:

* Email: <a href="mailto:larrygjenkins@gmail.com">larrygjenkins@gmail.com</a>
* GitHub: <a href="https://github.com/larrygjenkins">github.com/larrygjenkins</a>
* LinkedIn: <a href="https://www.linkedin.com/in/l-jenkins/">linkedin.com/in/l-jenkins</a>