import os
import csv
#create path
path = os.path.join("C:\\Users\\User\\Documents\\Data_Bootcamp\\Module_3\\Challenge\\Starter_Code\\Starter_Code\\PyPoll\\Resources","election_data.csv")
output_path = os.path.join("C:\\Users\\User\\Documents\\Data_Bootcamp\\Module_3\\Challenge\\Starter_Code\\Starter_Code\\PyPoll\\Resources","Py_Poll_Results.txt")
#variables
total_votes = 0
candidate_list = []
candidate_votes = {}
winnning_candidate = ""
percentage_of_votes = 0
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headerskip = next(csvreader)
    for row in csvreader:
#calculating total votes
        total_votes = total_votes + 1
#unique value for candidate
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
#cacluating votes
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Print results
with open(output_path, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        if (votes > percentage_of_votes):
            percentage_of_votes = votes
            winnning_candidate = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winnning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)



        