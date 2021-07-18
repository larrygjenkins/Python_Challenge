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

## Challenges
One of the stocks represented had "0" listed for all pricing data. This meant that calculations performed by the script could result in an Overflow Error because a formula would have included dividing by 0. 

To account for this, the script included a nested If statement to validate if the yearly open price was 0. If so, the percent change was automatically assigned a value of 0.

**Nested If Statement Validating Whether Year Open Price is 0**

        If yrOpenPrice = 0 Then
            percentChange = 0
                    
        Else
            percentChange = Round((((yrClosePrice - yrOpenPrice) / yrOpenPrice) * 100), 2)
                    
        End If

This solution served this particular data set, but it would have limitations if the opening price was 0 but the closing price was not. That scenario would require a decision on how to present a percentage change when the starting value is 0. (For example, would a starting price of 0 and an ending price of 1 be represented as a 100% change?)  

## Technologies Used
* Python
* Jupyter Notebook

## Questions?
Contact me at the following locations:

* Email: <a href="mailto:larrygjenkins@gmail.com">larrygjenkins@gmail.com</a>
* GitHub: <a href="https://github.com/larrygjenkins">github.com/larrygjenkins</a>
* LinkedIn: <a href="https://www.linkedin.com/in/l-jenkins/">linkedin.com/in/l-jenkins</a>