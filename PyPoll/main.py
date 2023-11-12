import os
import csv

#Listing all my paths
electiondoc = r"C:\Users\tadip\OneDrive\Documents\BAC\Data Analytics\Module 3 - Python\python-challenge\PyPoll\Resources\election_data.csv"
analysis = r"C:\Users\tadip\OneDrive\Documents\BAC\Data Analytics\Module 3 - Python\python-challenge\PyPoll\Analysis\Election Results.txt"
#Since the data is not seperated in colomns, we create lists to store them.
ballotID = []
county = []
candidate =[]
#Read the election_data.csv file
with open(electiondoc, 'r', encoding = "UTF-8") as f: 
    csvreader = csv.reader(f,delimiter=",")

    #ensure we do not read/include the header
    header = next(csvreader)

    #Below, we are filling the lists with data from the csv file. This step creates columns.
    for row in csvreader:
        #Add Ballot ID
        ballotID.append(row[0])

        #Add county
        county.append(row[1])

        #Add candidate
        candidate.append(row[2])
    
    #Find the total votes
    totalvotes = len(ballotID)
    print(totalvotes)

    #Create a list of all the candidates. The loop won't add the name if it was already added once.
    all_candidates = []

    for name in candidate:
        if name not in all_candidates:
            all_candidates.append(name)
    print(all_candidates)
    
    #Find Charles' total of votes and percentage.
    counter = 0
    for i in candidate:
        if i == "Charles Casper Stockham":
            counter += 1
    charles_count = counter
    print(charles_count)
    charles_vote = round(charles_count/totalvotes *100,3)
    print(charles_vote)

    #Find Diane's total of votes and percentage.
    counter2 = 0
    for i in candidate:
        if i == "Diana DeGette":
            counter2 += 1
    diane_count = counter2
    print(diane_count)
    diane_vote = round(diane_count/totalvotes *100,3)
    print(diane_vote)

    #Find Charles' total of votes.
    counter3 = 0
    for i in candidate:
        if i == "Raymon Anthony Doane":
            counter3 += 1
    raymon_count = counter3
    print(raymon_count)
    raymon_vote = round(raymon_count/totalvotes *100,3)
    print(raymon_vote)

    #Find the winner.
    if charles_vote > diane_vote:
        winner = all_candidates[0]
    elif diane_vote > raymon_vote:
        winner = all_candidates[1]
    else:
        winner = all_candidates[2]
    print(winner)

#Creating the txt file to display the analysis.
with open(analysis, "w") as f:
    writer = csv.writer(f)
    #Write the title.
    writer.writerow(["Election Results"])
    #Write the rest of the rows.
    writer.writerow(["-----------------------------------------"])
    writer.writerow([f"Total Votes: {totalvotes}"])
    writer.writerow(["-----------------------------------------"])
    writer.writerow([f"{all_candidates[0]}:{charles_vote}% ({charles_count})"])
    writer.writerow([f"{all_candidates[1]}:{diane_vote}% ({diane_count})"])
    writer.writerow([f"{all_candidates[2]}:{raymon_vote}% ({raymon_count})"])
    writer.writerow(["-----------------------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-----------------------------------------"])
