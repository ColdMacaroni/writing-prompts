#!/bin/python
# Prints a random writing prompt from r/writingprompts
# Takes the top 100 of today
# TODO: Add options to select from

# Sample api link
# https://old.reddit.com/r/WritingPrompts/top.json?sort=top&t=day&count=100

import random
import requests

def get_reddit(subreddit,listing,limit,timeframe):
    # Taken from https://www.jcchouinard.com/documentation-on-reddit-apis-json/

    # subreddit = writingprompts
    # listing = controversial, best, hot, new, random, rising, top
    # limit = 100
    # timeframe = hour, day, week, month, year, all

    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?\
                     limit={limit}&\
                     t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'writingprompts-yank'})
    except:
        print('An Error Occured')
    return request.json()


def process_prompts(listing, limit, timeframe):
    posts = get_reddit('writingprompts',listing,limit,timeframe)
    prompts = []

    # link_flair_text
    flair = 'Writing Prompt'
    # Loop through the posts
    for child in posts['data']['children']:
        print(child)
        print()
        # Add 'title' to prompts if flair is 'Writing Prompt'. Removing [WP] from it

if __name__ == "__main__":
    # Code
    print(process_prompts('top', '100', 'day'))
