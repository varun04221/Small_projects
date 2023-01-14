#Made by VARUN KUMAR | Roll No:2022563 | IIIT-DELHI

import csv
import requests

api_key='fae375fabd85c09a46c4405b106b88dd'

#getting details from User for importing details
while True:
    country=input("Please Enter the Name of Your Country[REQUIRED]:")
    country.lower()
    country=country.replace(" ","_")
    if requests.get("https://restcountries.com/v2/name/"+country).status_code==200:
        break
    else:
        print("Please Enter A Valid Country Name!!!")
singer=input("Please Enter the name of a artist or bypass it using enter/return:")
singer.lower()



needof=True

#if user does not enter a artist name
if singer=="":
    print("You have not entered any artist so we are adding most played tracks as per your country.")
    url='http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks&country={}&api_key={}&format=json'.format(country,api_key)


    #if country exist in last fm data
    if requests.get(url).status_code==200:
        rdata=requests.get(url)
        rdata=rdata.json()
        header=["Name of the song","Artist","Link to play song","Play Count"]
        rows=[]
        for i in rdata["tracks"]["track"]:
            l=[]
            l.append(i["name"])
            l.append(i["artist"]["name"])
            l.append(i['url'])
            l.append(i["listeners"])
            rows.append(l)
    #if country does not exist in last fm data
    else:
        print("Sorry!!! Country:{} does not exist in database".format(country))
        needof=False

#If user enters a artist name
else:
    url='http://ws.audioscrobbler.com/2.0/?method=artist.search&artist={}&api_key={}&format=json'.format(singer,api_key)

    #if artist exist in last fm data
    if requests.get(url).status_code==200 and len(requests.get(url).json()["results"]["artistmatches"]["artist"])>0:
        rdata=requests.get(url)
        rdata=rdata.json()
        n=1
        select_artist={}
        for i in rdata["results"]["artistmatches"]["artist"]:
            print(n,i["name"])
            select_artist[n]=[i["mbid"],i['name']]
            n+=1
        
        n=int(input("Please Enter the number corresponding to your Selected Artist[PLEASE SELECT FIRST OCCURENCE IF THERE ARE MULTIPLE ENTERIES WITH SIMILIAR NAME FOR BEST RESULTS]{If It does not work please try another option}:"))
        mbid=select_artist[n][0]
        name=select_artist[n][1]
        #url to get tracks of artist when mbid is not specified
        if mbid=="":
            url='http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={}&api_key={}&format=json'.format(name,api_key)
        else:
            url='http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={}&mbid={}&api_key={}&format=json'.format(name,mbid,api_key)
        #proceeding forward with the details of artist
        rdata=requests.get(url)
        rdata=rdata.json()
        header=["Name of the song","Artist","Link to play song","Play Count"]
        rows=[]
        for i in rdata["toptracks"]["track"]:
            l=[]
            l.append(i["name"])
            l.append(name)
            l.append(i["url"])
            l.append(i["playcount"])
            rows.append(l)
        
    #if artist not in last fm data
    else:
        print("Sorry No Matching Results...")
        needof=False

#Working with CSV File
if needof:
    file=open("music.csv",'w')
    writer=csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
    file.close()
    print("Please check your current Directory a file name music.csv is added to it with songs")
    print("It may be Possible that some Songs are not playable {Links Not Working Properly} because I am Using free version of API.")