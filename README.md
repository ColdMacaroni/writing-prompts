# writing-prompts
A python script that takes prompts from r/writingprompts

It stores the writing promps in a file in /tmp. File is updated if you change the parameters.

# Example usage
First run: `writing-prompt top 50 week`

This will populate a file in /tmp with the top 50 posts of this week in r/writingprompts

While this file exists you can call `writing-prompt` without arguments and it will get a random prompt from the file in /tmp

If you'd like to update this file, you can either delete it **and then** call `writing-prompt` with the same arguments.

Here's a one liner to do this. `/tmp/writingprompts.txt` is the default path. You can change it by editing the `temp_file()` function in `writing_prompts.py`. Replace it here with the new path if you've done so already.

`wp_args=$(head -n 1 /tmp/writingprompts.txt); rm /tmp/writingprompts.txt && sh -c "writing-prompt $wp_args"`



Or run `writing-prompt` with different arguments. If they are the same as the ones defined in the file (first line), it will pick one from there.

An update function/arguments will be added soon

