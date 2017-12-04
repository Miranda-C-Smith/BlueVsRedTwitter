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
                userIDs.append(row[2])
            count +=1
    #print(userIDs)
    return userIDs
            
        

def main(twitterHandle = "jaredpolis"):
    
    #print( "found %d friends" % (len(query["ids"])))
    redUsers = readUserInfocsv("RedUserInfo.csv")
    blueUsers = readUserInfocsv("BlueUserInfo.csv")
    query = api.GetFriends(screen_name = twitterHandle )
    print("length " + str(len(query)))
    redscore =0
    bluescore =0
    #print(redUser)
    for friend in query:
        #print(friend.id)
        if(str(friend.id) in redUsers):
            redscore +=1
        if(str(friend.id) in blueUsers):
            bluescore +=1
    print("redscore {} \nbluescore {}".format(redscore, bluescore))
    
if __name__ == '__main__':
    main()
