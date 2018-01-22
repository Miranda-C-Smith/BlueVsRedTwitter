#!/usr/bin/env python
import twitter
import csv
import sys

#Program downloads the users FRIENDS and gives them a score based on how many
#Red or blue people they are following based on list in
#RedUserInfo.csv and BlueUserInfo.csv


# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '824794440409706496-CGUoqhcZpfk4lOcblNVG1OuubwaCqZp'
ACCESS_SECRET = 'Mgd7wctkwI3nNUL6RHD4Cqjg9HVngccRrynoWfEsTUzlJ'
CONSUMER_KEY = '72haUMMgwOXNNGXXz4G0N7B9m'
CONSUMER_SECRET = 'zSx800UtH7OUTkVUMw2uORB39o1aP59uZgmXMWo8AZpoFkNgJQ'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET,
                  sleep_on_rate_limit=True)

def readUserInfocsv(filename):
    userIDs = []
    with open(filename, "r" ,encoding='utf-8') as f:
        reader = csv.reader(f)
        count =0 
        for row in reader:
            if count > 0:
                userIDs.append(row[0])
            count +=1
    #print(userIDs)
    return userIDs
            
def readUserInfoAndFriends(filename):
    users = {}
    with open(filename, "r" ,encoding='utf-8') as f:
        count = 0
        for row in f.read().split("\n"):
            if count ==0:
                count+=1
                continue
            if row:
                friends = row.split(" ")[1:]
                username = row.split(" ")[0]
                users[username]=friends
    return users
    

def main():
    
    #print( "found %d friends" % (len(query["ids"])))
    redGS = readUserInfocsv("RedUserInfo.csv")
    blueGS = readUserInfocsv("BlueUserInfo.csv")
    #query = api.GetFriends(screen_name = twitterHandle )
    #print("length " + str(len(query)))

    redUsers = readUserInfoAndFriends("Friend_List_Red.txt")
    blueUsers = readUserInfoAndFriends("Friend_List_Blue.txt")

    redOutfile = open("RedGovScores.tsv", "w")
    blueOutfile = open("BlueGovScores.tsv", "w")
    
    for user, friends in redUsers.items():
        redscore =0
        bluescore =0
        redOutfile.write(user)
        for friend in friends:
            if(str(friend) in redGS):
                redscore +=1
            if(str(friend) in blueGS):
                bluescore +=1
        redOutfile.write("\t" + str(redscore) + "\t" + str(bluescore) +"\n" )

    for user, friends in blueUsers.items():
        redscore =0
        bluescore =0
        blueOutfile.write(user)
        for friend in friends:
            if(str(friend) in redGS):
                redscore +=1
            if(str(friend) in blueGS):
                bluescore +=1
        blueOutfile.write("\t" + str(redscore) + "\t" + str(bluescore) +"\n" )

    redOutfile.close()
    blueOutfile.close()
    #for friend in query:
    #    #print(friend.id)
    #    if(str(friend.id) in redUsers):
    #        redscore +=1
    #    if(str(friend.id) in blueUsers):
    #        bluescore +=1
    #print("redscore {} \nbluescore {}".format(redscore, bluescore))
    
if __name__ == '__main__':
    main()
