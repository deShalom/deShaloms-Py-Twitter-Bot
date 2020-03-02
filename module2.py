import tweepy
import time
import schedule
import xml.dom.minidom
import random
import xml.etree.ElementTree as ET

#----Parsing XML data in
tree = ET.parse('')
root = tree.getroot()

titles = [item.find('Text').text for item in root.findall('Tweet')]

#----This works collects random tweet from the XML
def collectTweet():
    rnum = (random.randint(0,len(titles)-1))
    tweetText = titles[rnum]
    return tweetText

