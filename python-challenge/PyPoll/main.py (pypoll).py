#PyPoll
#import OS
import os
#import csv
import csv
#create list for total votes, candidates, list of candidates, percentages, and votes
total_votes =[]
whole_list = []
candidate_list = []
percentages = []
votes = []
#csv path to get to data file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
#Open actual path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first and skip it
    csv_header = next(csvreader, None)
    #go through data
    for element in csvreader:
        #count how many votes there are
        total_votes.append(element[0])
        #add the 2nd place to a list of candidates
        whole_list.append(element[2])
        #create loop make a list of unique candidates
        if element[2] not in candidate_list:
            #add new names to unique candidate list
            candidate_list.append(element[2])
#create a loop for the unique list
for x in candidate_list:
    #count how many times that unique candidate is in the complete candidate list ie "voted for"
    votes.append(whole_list.count(x))
#create a loop for the length of the votes
for i in range(int(len(votes))):
     #calculate percentages for each candidate by having the candidates votes/total votes and adding it to a list 
     percentages.append(round(votes[i]/len(total_votes), 5)*100)
#create a loop to go through percentage list
for i in range(len(percentages)):
    #add % to each item in the percentages list
    percentages[i] = str(percentages[i]) + str("%")
#tie all of the results together by zipping it 
results = list(zip(candidate_list, percentages,votes))        
#calculate who got the max votes by getting the position of the votes list with the max number 
max_votes = votes.index(max(votes))
#get the winner by corresponding the index of the max votes with the candidate list
winner = candidate_list[max_votes]
#print results to terminal
print("Election Results")
print("-----------------------------")
count = str(len(total_votes))
print(f"Total Votes:", count)
print("------------------------------")
#loop through the results for each candidate to get their stats
for candidate in results:
    #print out candidate and their stats
    print(candidate)
print("---------------------------------")
print(f"Winner: " + winner)

#open a new file to store data collected
with open("pypoll_final.txt","w",newline="") as newfile:
    #write all of the results to the new file
    newfile.write("Election Results \n")
    newfile.write("----------------------------- \n")
    newfile.write(f"Total Votes: {count} \n")
    newfile.write("------------------------------ \n")
    newfile.write(f"{results} \n")
    newfile.write("------------------------------- \n")
    newfile.write(f"Winner: {winner} \n")
    newfile.write("-------------------------------")