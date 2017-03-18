#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author: Obi Uchenna David <daviduchenna@outlook.com>.
"""CLI Bobo
  ___  _   _                                 _           
 / _ \| |_| |__  _ __ ___  ___  ___ ___   __| | ___  ___ 
| | | | __| '_ \| '__/ _ \/ _ \/ __/ _ \ / _` |/ _ \/ __|
| |_| | |_| | | | | |  __/  __/ (_| (_) | (_| |  __/\__ \
 \___/ \__|_| |_|_|  \___|\___|\___\___/ \__,_|\___||___/
Gets Latest News,Gist and more from your favourite Sites

Required: Python 2.4 or later
"""
import feedparser
import argparse
from colorama import init
import sys
from colorama import Fore, Back, Style
import time
import re
import requests

PUNCH_FEED_URL = 'http://punchng.com/feed/' #punch
VANGUARD_FEED_URL = 'http://www.vanguardngr.com/feed/' #vanguard
THE_NATION_FEED_URL = 'http://thenationonlineng.net/feed/' #nation
THE_SUN_FEED_URL = 'http://sunnewsonline.com/feed/' #sun
SAHARA_REPORTERS_FEED_URL = 'http://saharareporters.com/feeds/latest/feed' #sahara
GUARDIAN_FEED_URL = 'http://guardian.ng/feed/' #guardian
TECHPOINT_FEED_URL = 'https://techpoint.ng/feed/' #techpoint
TECHCABAL_FEED_URL = 'http://techcabal.com/feed/' #techcabal
LINDA_IKEJI_FEED_URL = 'https://www.blogger.com/feeds/9174986572743472561/posts/default' #lindaikeji
BELLA_NAIJA_FEED_URL = 'https://www.bellanaija.com/feed/?alt=xml' #bellanaija
LAUGHS = 'http://laughs.com.ng/feeds' #nigerian jokes

JOKES_URL = 'https://api.icndb.com/jokes/random'
FOOTBALL_API_URL = 'http://api.football-data.org/'
#ID Changes Every Season Tho
PREMIER_LEAGUE = 426
BUNDESLIGA = 430
SERIE_A = 438
CHAMPIONS_LEAGUE = 440
news_list = [PUNCH_FEED_URL,VANGUARD_FEED_URL,THE_NATION_FEED_URL,THE_SUN_FEED_URL,SAHARA_REPORTERS_FEED_URL,GUARDIAN_FEED_URL,
             TECHPOINT_FEED_URL,TECHCABAL_FEED_URL,LINDA_IKEJI_FEED_URL,BELLA_NAIJA_FEED_URL]

init()

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def spin():
    spinner = spinning_cursor()
    for _ in range(100):
        sys.stdout.write(spinner.next())
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')


def clean_html_tags(raw_html):
    """Clean the HTML tags from response"""
    clean = re.compile('<.*?>')
    clean_text = re.sub(clean, '', raw_html)
    return clean_text

class News:
    def __init__(self,source='all'):
        pass

    def latest_news(self,source):
        '''Gets latest news from a particular feed url '''
        url = news_list[source-1]

        try:
            feed = feedparser.parse(url)
        except KeyboardInterrupt:
            sys.exit(1)

        data = []
        print(Fore.LIGHTYELLOW_EX+"Latest feeds from "+feed.feed.title+"\n"+feed.feed.description)
        print(Fore.LIGHTYELLOW_EX+feed.feed.link)
        # print(Fore.CYAN+feed.feed.published)
        print("\n")
        for i in range(0,len(feed.entries)-1):
            data.append(feed.entries[i].title)

        return data

    def read_story(self,source,story):
        '''Read a news story from the source '''
        url = news_list[source - 1]

        try:
            feed = feedparser.parse(url)
        except KeyboardInterrupt:
            sys.exit(1)

        print(Fore.LIGHTYELLOW_EX + "Latest feeds from " + feed.feed.title + "\n" + feed.feed.description)
        print(Fore.LIGHTYELLOW_EX + feed.feed.link)
        # print(Fore.CYAN+feed.feed.published)
        print("\n")

        try:
            return feed.entries[story]
        except IndexError:
            '''No such news story'''
            print(Fore.RED+"NO SUCH NEWS STORY !!!!")
            sys.exit(1)

    def random(self):
        pass


class Tips:
    def __init__(self):
        pass

    def random(self):
        pass


class Jokes:
    def __init__(self):
        pass

    def random(self):
        """
        Gets a single random joke from the API
        :return: A String Containing the joke
        """

        jokes = requests.get(JOKES_URL)
        return jokes.json()['value']['joke']
        pass


class StackOverflow:
    def __init__(self):
        pass


class Soccer:
    def __init__(self):
        pass

    def fixtures(self,competition):

        pass


def main():
    desc = 'CLIBobo keeps you in touch with the world, getting your news, gist, jokes, sport info and more from your terminal'
    parser = argparse.ArgumentParser(prog='clibobo', description=desc,epilog='')
    news_choices = [
    '[1] PUNCH',
    '[2] VANGUARD',
    '[3] THE NATION',
    '[4] THE DAILY SUN',
    '[5] SAHARA REPORTERS',
    '[6] GUARDIAN',
    '[7] TECHPOINT',
    '[8] TECHCABAL',
    '[9] LINDA IKEJI',
    '[10] BELLA NAIJA'
    ]
    news_group = parser.add_argument_group('News','Options for news')
    news = news_group.add_argument('-n','--news', type=int, help='pass source to\
    get latest news from '+str(news_choices),choices=range(1,11))
    news_group.add_argument('-s','--story',type=int,help='the story of the news item to read')

    jokes_group = parser.add_argument_group('Jokes','Options for jokes')
    jokes_group.add_argument('-j','--jokes',help='gets a random joke',action='store_true')

    # sports_group = parser.add_argument_group('Sports','Options for sport')
    # sports_group.add_argument('-f','--football',help='gets football \
    # news and information',choices=['fixtures','table'])
    # available_options = ""
    # sports_group.add_argument('-o',metavar='team/player/competition',help='What to find football info on')


    # parser.print_help()

    args = parser.parse_args()

    if args.news:
        if args.story:
            spin()
            newsfeed = News()
            response = newsfeed.read_story(args.news,args.story)
            print(Fore.RED+response.title)
            print("\n")
            try:
                print(Fore.BLUE+clean_html_tags(response.summary_detail.value))
            except AttributeError:
                print(Fore.BLUE + clean_html_tags(response.summary))
            print("\nRead more @ "+response.link)

            pass
        else:
            newsfeed = News()
            spin()
            response = newsfeed.latest_news(args.news)
            for i in range(0,len(response)):

                print(Fore.RED+"[%i] " %i+Fore.BLUE+response[i])

    elif args.jokes:
        print(u'\U0001f604')
        jokes = Jokes()
        print(jokes.random())
        pass

    # elif args.football:
    #     pass

    else:
        parser.print_usage()


    print(Style.RESET_ALL)
    sys.exit()
