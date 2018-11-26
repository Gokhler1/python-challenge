import os

import csv

csvpath = "election_data.csv"

candidates=[]
unique_candidates=[]
total_votes=[]
total_percent=[]
candidates_votes= []


with open(csvpath, newline="") as csvfile:
    election = csv.reader(csvfile,delimiter=",")
    vote_counter = 0
    header = next(election)
    for raw in election:
        vote_counter = vote_counter+1
        candidates.append(raw[2])

    for candidate in candidates:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
    total_candidates= len(unique_candidates)

    for x in unique_candidates:
        total_votes.append(0)

    total=0
    for y in candidates:
          candidate_index =unique_candidates.index(y)
          total_votes[candidate_index] +=1
    for z in total_votes:
        total= total + z
    for w in total_votes:
        total_percent.append(w/total)
    max_votes = max(total_votes)
    max_index = total_votes.index(max_votes)
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(vote_counter))
    print("-------------------------")
    results = zip(unique_candidates,total_percent,total_votes)
    for result in results:
        print(result[0]+ ": " + str(round((result[1]*100),3))+ " % (" + str(result[2])+ ")")
    print("-------------------------")
    print("winner: "+unique_candidates[max_index])
    print("-------------------------")
