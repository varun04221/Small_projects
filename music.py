#Made by VARUN KUMAR | IIIT-DELHI

import csv
import requests
from math import ceil

api_key='fae375fabd85c09a46c4405b106b88dd'

#getting details from User for importing details
sing=input("Please Enter the name of a singer or bypass it using enter/return:")
sing.lower()
fill=True
if sing=="":
    fill =False
if not fill:
    lyricist=""
    while lyricist=="":
        lyricist=input("Please Enter the name of a writer or bypass it using enter/return:")
        if lyricist=="":
            print("You have to provide the name of lyricist if you are not providing the name of the singer!!!")
else:
    lyricist=input("Please Enter the name of a writer or bypass it using enter/return:")
singer=sing+" "+lyricist.lower()


needof=True
url='http://ws.audioscrobbler.com/2.0/?method=artist.search&artist={}&api_key={}&limit={}&format=json'.format(singer,api_key,10)

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
        url='http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={}&api_key={}&format=json'.format(name,api_key,500)
    else:
        url='http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={}&mbid={}&api_key={}&format=json'.format(name,mbid,api_key,500)
    #proceeding forward with the details of artist
    if "toptracks" in requests.get(url).json():
        pdata=requests.get(url)
        pdata=pdata.json()
        total=int(pdata["toptracks"]["@attr"]["total"])
        if total<=1000:
            pages=1
        else:
            pages=ceil(total/1000)
        rows=[]
        header=["Name of the song","Singer","Lyricist/Writer","Link to play song","Play Count"]
        print("Please Wait...")

        for i in range(1,pages+1):
            if mbid=="":
                url='http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={}&api_key={}&limit={}&page={}&format=json'.format(name,api_key,1000,i)
            else:
                url='http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={}&mbid={}&api_key={}&limit={}&page={}&format=json'.format(name,mbid,api_key,1000,i)
            

            rdata=requests.get(url)
            rdata=rdata.json()
            
            for i in rdata["toptracks"]["track"]:
                l=[]
                l.append(i["name"])
                if sing!="":
                    l.append(sing)
                else:
                    l.append("Not Found")
                if lyricist!="":
                    l.append(lyricist)
                else:
                    l.append("Not Found")
                l.append(i["url"])
                l.append(i["playcount"])
                rows.append(l)
    else:
        print("Sorry No songs found")
        needof=False
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
