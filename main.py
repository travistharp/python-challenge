import os
import csv

# path to data file
election_data_csv = os.path.join('resources','election_data.csv')

#set up lists to hold values
#list of candidates names
candidates = []
#list of votes-- one name is one vote
candidates_votes = []
#total number of votes- count of rows
vote_total_all = 0


#open and read the csv file
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #read csv file- count rows(total votes), find candidate names and count votes
    for row in csvreader:

        #All votes- count +1 for each row
        vote_total_all += 1

        #read candidate name from csv file- check if the name is in the list or not
        candidate_name = row[2]

        #if candidate in in the list, add a vote to that candidate
        if candidate_name in candidates:
            candidate_list = candidates.index(candidate_name)
            candidates_votes[candidate_list] = candidates_votes[candidate_list] + 1

         #if candidate is not in the list, add them (append) to the list and add a vote  
        else:
            candidates.append(candidate_name)
            candidates_votes.append(1)

#voting result calculations
percent_vote = []
#find candidate with most votes
winner_name = 0
winner_votes = candidates_votes[0]


for value in range(len(candidates)):
    #percentage of vote
    percent = candidates_votes[value]/vote_total_all*100
    percent_vote.append(percent)
    #find the candidate with the most votes
    if candidates_votes[value] > winner_votes:
        winner_votes = candidates_votes[value]
        winner_name = value

winner_winner = candidates[winner_name]

#export the results to a text file
export = open("election_results.txt", "w+")
export.write("Election Results:")
export.write(f'Total Votes: {vote_total_all}')
for value in range(len(candidates)):
    export.write(f'{candidates[value]} : {percent_vote[value]}% ({candidates_votes[value]})')
export.write(f'Winner: {winner_winner}')
export.close

#print results

print('Election Results')
print('------------------------------------')
print(f'Total Votes: {vote_total_all}')
print('------------------------------------ ')
for value in range(len(candidates)):
    print(f'{candidates[value]} : {percent_vote[value]}% ({candidates_votes[value]})')
print('-------------------------------------')
print(f'Winner: {winner_winner}')
print('------------------------------------')
print("Better than the Iowa election")
