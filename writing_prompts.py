#!/bin/python
# Prints a random writing prompt from r/writingprompts
# Takes the top 100 of today by default

# Sample api link
# https://old.reddit.com/r/WritingPrompts/top.json?sort=top&t=day&count=100

from sys import argv
from random import choice
from requests import get


def get_reddit(subreddit,listing,limit,timeframe):
    # Taken from https://www.jcchouinard.com/documentation-on-reddit-apis-json/

    # subreddit = writingprompts
    # listing = controversial, best, hot, new, random, rising, top
    # limit = 100
    # timeframe = hour, day, week, month, year, all

    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'

        request = get(base_url, headers = {'User-agent': 'writingprompts-yank'})

    except:
        print('An Error Occured')

    return request.json()


def process_prompts(listing, limit, timeframe):
    posts = get_reddit('writingprompts', listing, limit, timeframe)
    prompts = []

    # This is to avoid things like mod posts
    # link_flair_text
    acceptable_flairs = ['Writing Prompt',
                         'Established Universe',
                         'Simple Prompt']

    # Loop through the posts
    for child in posts['data']['children']:
        post = child['data']

        if post['link_flair_text'] in acceptable_flairs:
            # Remove tag. e.g. "[WP] "
            prompts.append(post['link_flair_text'] + ': ' + post['title'][5:])

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
        # Try to open the temp file with prompts
        with open(temp_file(), 'r') as txt:
            identifier, *prompts = txt.readlines()

    except FileNotFoundError:
        identifier, *prompts = write_wp_temp(listing,
                                             limit,
                                             timeframe,
                                             back=True)

    # Compare first line and call write_wp if they arent the same
    # identifier comes with \n if read from file
    if identifier.replace('\n', '') != ' '.join([listing, limit, timeframe]):
        identifier, *prompts = write_wp_temp(listing,
                                             limit,
                                             timeframe,
                                             back=True)

    # Return a random prompt. Getting rid of newline
    return choice(prompts).replace('\n', '')


def wp_help():
    print("""Invalid arguments.
You must provide 3 arguments: listing, limit, timeframe. (In that order)

Valid listings: controversial, best, hot, new, random, rising, top
Limit is the amount of posts you want. Any positive int > 0 will do.
Valid timeframes: hour, day, week, month, year, all

e.g. "{} top 25 week" this would print out a random writing prompt out of the top rated 25 posts this week.
""".format(argv[0]))


if __name__ == "__main__":
    # TODO: Add a function that updates the tmp file with the same parameters
    try:
        if 'help' in argv or 'h' in argv or (len(argv) > 1 and len(argv) < 4):
            wp_help()

        # [0] is filename
        elif len(argv) > 3:
            print(get_prompt(argv[1], argv[2], argv[3]))

        else:
            # Call with last arguments
            with open(temp_file(), 'r') as txt:
                # Get first line
                arguments = txt.readline()
                arguments = arguments.replace('\n', '')

                arguments = arguments.split(' ')
                print(get_prompt(*arguments))

    except:
        wp_help()

