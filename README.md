# writing-prompts
A python script that takes prompts from r/writingprompts

It stores the writing promps in a file in /tmp. File is updated if you change the parameters.

# Example usage
First run: `writing-prompt top 50 week`

This will populate a file in /tmp with the top 50 posts of this week in r/writingprompts

While this file exists you can call `writing-prompt` without arguments and it will get a random prompt from the file in /tmp

If you'd like to update this file, run `writing-prompt update`. It will update the file with the same arguments as when it was made

