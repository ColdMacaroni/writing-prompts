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
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'

        request = requests.get(base_url, headers = {'User-agent': 'writingprompts-yank'})

    except:
        print('An Error Occured')

    return request.json()


def process_prompts(listing, limit, timeframe):
    posts = get_reddit('writingprompts', listing, limit, timeframe)
    prompts = []

    # This is to avoid things like mod posts
    # link_flair_text
    acceptable_flairs = ['Writing Prompt', 'Established Universe']

    # Loop through the posts
    for child in posts['data']['children']:
        post = child['data']

        if post['link_flair_text'] in acceptable_flairs:
            prompts.append(post['title'].replace('[WP] ', ''))

    return prompts


def get_prompt(listing, limit, timeframe):

    wp_tmp_file = '/tmp/writingprompts.txt'
    try:
        # Try to open the temp file with prompts
        with open(wp_tmp_file, 'r') as txt:
            prompts = txt.readlines()

    except:
        with open(wp_tmp_file, 'w+') as txt:
            prompts = process_prompts(listing, limit, timeframe)

            # Add current details
            txt.write(' '.join(listing, limit, timeframe))
            txt.write('\n')




if __name__ == "__main__":
    # Code
    print(len(process_prompts('top', '100', 'day')))
