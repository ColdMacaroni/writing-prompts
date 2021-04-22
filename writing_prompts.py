#!/bin/python
# Prints a random writing prompt from r/writingprompts
# Takes the top 100 of today
# TODO: Add options to select from

# Sample api link
# https://old.reddit.com/r/WritingPrompts/top.json?sort=top&t=day&count=100

from random import choice
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


def write_wp_temp(listing, limit, timeframe, back=False):
    prompts = process_prompts(listing, limit, timeframe)

    with open(temp_file(), 'w+') as txt:
        # Add current details
        txt.write(' '.join([listing, limit, timeframe]))
        txt.write('\n')

        for prompt in prompts:
            txt.write(prompt)
            txt.write('\n')

    if back:
        return prompts


def temp_file():
    return '/tmp/writingprompts.txt'


def get_prompt(listing, limit, timeframe):
    try:
        raise Exception()
        # Try to open the temp file with prompts
        with open(temp_file(), 'r') as txt:
            identifier, *prompts = txt.readlines()

    except FileNotFoundError:
        identifier, *prompts = write_wp_temp(listing,
                                             limit,
                                             timeframe,
                                             back=True)

    # Compare first line and call write_wp if they arent the same
    if identifier != ' '.join([listing, limit, timeframe]):
        identifier, *prompts = write_wp_temp(listing,
                                             limit,
                                             timeframe,
                                             back=True)

    # Return a random prompt
    return choice(prompts)


if __name__ == "__main__":
    # Code
    print(len(process_prompts('top', '100', 'day')))
