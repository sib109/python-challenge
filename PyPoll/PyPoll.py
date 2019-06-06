#Import relevant packages
import os
import csv
import operator
#Initialize variables
#Holds unique candidate list
candidate=[]
#Holds all votes polled by all candidates
candidate_vote=[]
#Holds vote summary
vote_summary={}
#Open input poll data file
#Define filepath. If in same folder as code, no need for full path entry
csvpath=os.path.join('pypoll.csv')
#Open file in filepath
with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip the header
    next(csvreader)
    for row in csvreader:
#Create votes data
        candidate_vote.append(row[2])
        if row[2] not in candidate:
#Creates candidate data
            candidate.append(row[2])
#Vote count function
def candidate_vote_count (candidate_name):
    count = 0
    for row in candidate_vote:
         if row == candidate_name:
            count+=1
    return count
#Put the summaryresults in a dictionary
for i in candidate:
    vote_summary.update({i:candidate_vote_count(i)})
#Sort the results in descending order to give winner
vote_summary_sorted = sorted(vote_summary.items(), key=operator.itemgetter(1))
vote_summary_sorted.reverse()
#Print on screen and Write on output file
print("Election Results")
output_file = open("PyPoll.txt","w")
output_file.write("Election Results \n" "--------------------------\n")
print("--------------------------")
print("Total Votes: " + str(len(candidate_vote)))
output_file.write("Total Votes: " + str(len(candidate_vote)))
print("--------------------------")
output_file.write("\n--------------------------\n")
for key, value in vote_summary_sorted:
    print(key +": " + "{:.3f}".format(100*float(value)/float(len(candidate_vote))) + "% (" + str(value) + ")")
    output_file.write(key +": " + "{:.3f}".format(100*float(value)/float(len(candidate_vote))) + "% (" + str(value) + ")\n")
print("--------------------------")
output_file.write("\n--------------------------\n")
print("Winner:"+" "+vote_summary_sorted[0][0])
output_file.write("Winner:"+" "+vote_summary_sorted[0][0])
print("--------------------------")
output_file.write("\n--------------------------")
