import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
# print(csvpath)

# Creating empty array for each candidate, candidate votes received, and election winner
candidates = []
candidate_votes_received = []
winner = []

# Creating variable to hold number of votes cast for each candidate
candidate0_votes = 0
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0

# Creating variable for total number of votes cast
num_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
#   Cycles through each row in the csv file (after the header) and calculates total number of votes and array of candidates.
    for row in csvreader:
        num_votes += 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
        
        if row[2] == candidates[0]:
            candidate0_votes += 1
        
        elif row[2] == candidates[1]:
            candidate1_votes += 1
        
        elif row[2] == candidates[2]:
            candidate2_votes += 1
        
        elif row[2] == candidates[3]:
            candidate3_votes += 1

# creating variable for percentage of vote cast for each candidate
candidiate0_percent_vote = format(((candidate0_votes/num_votes)*100), '.3f')
candidiate1_percent_vote = format(((candidate1_votes/num_votes)*100), '.3f')
candidiate2_percent_vote = format(((candidate2_votes/num_votes)*100), '.3f')
candidiate3_percent_vote = format(((candidate3_votes/num_votes)*100), '.3f')

# Takes candidates votes received and puts them in array that corresponds to their index in candidates list array
candidate_votes_received.append(candidate0_votes)
candidate_votes_received.append(candidate1_votes)
candidate_votes_received.append(candidate2_votes)
candidate_votes_received.append(candidate3_votes)

# Finds the highest value in the candidate_votes_received array
max_votes = (max(candidate_votes_received))

# Finds the index of the highest value in the candidate_votes_received array
winner_index = candidate_votes_received.index(max_votes)

# Using the index from the prevoius array, populates the winner array with the winning candidates name
winner.append(candidates[winner_index])

# Prints onscreen election results
print(f'Election Results')
print(f'-----------------------------')
print(f'Total Votes: {num_votes}')
print(f'-----------------------------')
print(f'{candidates[0]}: {candidiate0_percent_vote}% ({candidate0_votes})')
print(f'{candidates[1]}: {candidiate1_percent_vote}% ({candidate1_votes})')
print(f'{candidates[2]}: {candidiate2_percent_vote}% ({candidate2_votes})')
print(f'{candidates[3]}: {candidiate3_percent_vote}% ({candidate3_votes})')
print(f'-----------------------------')
print(f'Winner: {winner[0]}')
print(f'-----------------------------')

# Defines path for output text file
output_file = os.path.join('..', 'PyPoll', 'Analysis', 'election_results_analysis.txt')

# Prints analysis to .txt file in Analysis folder
with open(output_file, "w") as textfile:
    textfile.writelines(f'Election Results\n')
    textfile.writelines(f'-----------------------------\n')
    textfile.writelines(f'Total Votes: {num_votes}\n')
    textfile.writelines(f'-----------------------------\n')
    textfile.writelines(f'{candidates[0]}: {candidiate0_percent_vote}% ({candidate0_votes})\n')
    textfile.writelines(f'{candidates[1]}: {candidiate1_percent_vote}% ({candidate1_votes})\n')
    textfile.writelines(f'{candidates[2]}: {candidiate2_percent_vote}% ({candidate2_votes})\n')
    textfile.writelines(f'{candidates[3]}: {candidiate3_percent_vote}% ({candidate3_votes})\n')
    textfile.writelines(f'-----------------------------\n')
    textfile.writelines(f'Winner: {winner[0]}\n')
    textfile.writelines(f'-----------------------------\n')
