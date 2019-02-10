import os
import csv
#path to collect the data from file
pollCSV = os.path.join('Resources', 'election_data.csv')
#path for output
output_path = os.path.join('election_analysis.txt')
#set variables
total_votes = []
candidates = []
votes = {}


total_votes = 0
winning_count = 0
winning_candidate = ""

#open and read CSV
with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for i in csvreader:
        #calculate total votes
        total_votes = total_votes + 1
        #candidate name
        candidate_name = i[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            #counting the canditates votes
            votes[candidate_name] = 0

        votes[candidate_name] = votes[candidate_name] + 1
        #getting the percentages
        for results in votes:
            vote_count = votes.get(results)
            vote_percentage = float(vote_count) / float(total_votes) *100
            voter_output = f"{results}: {vote_percentage:.3f}% ({vote_count})\n"
        #veryfing the winner
            if (vote_count > winning_count):
                winning_count = vote_count
                winning_candidate = results



        

        
    


#print results
print("Election Results")
print("----------------------------")
print("Total Votes:" + str(total_votes))
print("----------------------------")
print(voter_output, end="")
print("----------------------------")
print(f"Winner: {winning_candidate}")

#output to a text file
with open(output_path, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("----------------------------")
    txt_file.write("Total Votes:" + str(total_votes))
    txt_file.write("----------------------------")
    txt_file.write(voter_output)
    txt_file.write("----------------------------")
    txt_file.write(f"Winner: {winning_candidate}")