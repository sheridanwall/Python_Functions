#!/usr/bin/env python
# coding: utf-8

# ## homework 4.2: investigating lists and dictionaries using functions
# 
# In this assignment I will ask you to pick five relatively short texts (poems, paragraphs, short essays, song lyrics, whatever interests you). The main thing is to make sure that each text is around 10 - 20 lines or sentences long. Below, I have selected five poems by Wallace Stevens. In each cell I have made a variable that contains each poem, and then I pass that poem through a function called `text_to_dict` that makes a dictionary for each poem. The dictionary contains the title of the poem, the full text as one string, and a list that contains each line of the poem. The function will also make lists of sentences instead of lines if you want to investigate a prose text (sentence by sentence) instead of a poem (line by line).
# 
# There are two parts of this assignment. 
# 
# **Part 1**, which should be easy, is to replace the poems with texts of your own choice--and choose to split them by lines or sentences. 
# 
# **Part 2** is to write functions that and investigate your texts. If you want to focus on the functions first, you can go straight to Part 2 and use the poems I have chosen. You can then go back and enter your own texts--your functions should work no matter what text you've chosen.
# 

# In[32]:


#Run this cell toImport regular expressions
#And to initialize the all texts list that will contain all of your dictionaries of text
import re
all_texts = []


# ** understanding the text_to_dict function**
# 
# You don't have to completely understand this function to use it, but you do need to understand its parameters. It takes three parameters:
# * `title` is a string you need to write inside function's parameters
# * `text` is the variable that holds the entire text
# * `poem` True/False parameter --if it is true it will split your text by line (`\n`) 
#  	If it is false it will split your text by sentence ('[.?!])
# 
# If you look at the function you will see that it builds a dictionary with the following fields:
# * `title` is the title of the text
# * `text_as_string` is the full text as a string
# * `lines` is a list of lines or sentences
# 
# It returns a dictionary with those fields.

# In[33]:


def text_to_dict(title,text,poem):
    dict_of_this_text = {}
    dict_of_this_text['title'] = title
    dict_of_this_text['text_as_string'] = text
    if poem:
        text_to_list = text.strip().split('\n')
    else:
        text_to_list = re.split(r"[.?!]",text)
    dict_of_this_text['lines'] = text_to_list
    return dict_of_this_text


# In[34]:


#please note: the regular expression I am using to split by sentences
#is highly flawed, it is borderline impossible to write a regular expression 
#that splits 100% perfectly by sentence, but feel free to use this.


# ## Part One
# 
# The next five cells are exactly the same. They define five different texts, and then they pass each text through the `text_to_dict` function. And then they add the resulting dictionary to the all_texts list. 
# 
# In the five cells below enter your five selected texts.
# 
# **You should do no coding at any point** until the very last cell before part two.

# In[35]:


#To change the text, just put a new text between the quotation mark
text0 = '''
When I think about myself,
I almost laugh myself to death,
My life has been one great big joke,
A dance that's walked
A song that's spoke,
I laugh so hard I almost choke
When I think about myself.

Sixty years in these folks' world
The child I works for calls me girl
I say "Yes ma'am" for working's sake.
Too proud to bend
Too poor to break,
I laugh until my stomach ache,
When I think about myself.

My folks can make me split my side,
I laughed so hard I nearly died,
The tales they tell, sound just like lying,
They grow the fruit,
But eat the rind,
I laugh until I start to crying,
When I think about my folks.
'''
#Remember: you need to type the title into the first parameter
#If you want to split by line choose True for the third parameter
#If you want to split by sentence, choose False
transform_it = text_to_dict("When I think about myself",text0,True)
all_texts.append(transform_it)


# In[36]:


all_texts


# In[37]:


text1 = '''
There are places I'll remember
All my life, though some have changed
Some forever, not for better
Some have gone and some remain

All these places had their moments
With lovers and friends, I still can recall
Some are dead and some are living
In my life, I've loved them all

But of all these friends and lovers
There is no one compares with you
And these memories lose their meaning
When I think of love as something new

Though I know I'll never lose affection
For people and things that went before
I know I'll often stop and think about them
In my life, I love you more
'''
transform_it = text_to_dict("In My Life",text1,True)
all_texts.append(transform_it)


# In[38]:


text2 = '''
Green was the color of the grass
Where I used to read at Centennial Park
I used to think I would meet somebody there
Teal was the color of your shirt
When you were sixteen at the yogurt shop
You used to work at to make a little money

Time, curious time
Gave me no compasses, gave me no signs
Were there clues I didn't see?
And isn't it just so pretty to think
All along there was some
Invisible string
Tying you to me?

A string that pulled me
Out of all the wrong arms, right into that dive bar
Something wrapped all of my past mistakes in barbed wire
Chains around my demons
Wool to brave the seasons
One single thread of gold
Tied me to you
'''
transform_it = text_to_dict("Invisible String",text2,True)
all_texts.append(transform_it)


# In[39]:


all_texts[2]['lines'][4]


# In[40]:


text3 = '''
Here on the edge of hell
Stands Harlem—
Remembering the old lies, 
The old kicks in the back,
The old "Be patient"
They told us before.

Sure, we remember.
Now when the man at the corner store
Says sugar's gone up another two cents,
And bread one,
And there's a new tax on cigarettes—
We remember the job we never had,
Never could get,
And can't have now
Because we're colored.

So we stand here
On the edge of hell
in Harlem
And look out on the world
And wonder
What we're gonna do
In the face of what
We remember.
'''
transform_it = text_to_dict("Harlem",text3,True)
all_texts.append(transform_it)


# In[41]:


text4 = '''
They said of him, about the city that night, 
that it was the peacefullest man's face ever beheld there. 
Many added that he looked sublime and prophetic. 
One of the most remarkable sufferers by the same axe -a woman - 
had asked at the foot of the same scaffold, not long before, 
to be allowed to write down the thoughts that were inspiring her. 
If he had given any utterance to his, and they were prophetic, 
they would have been these:

It is a far, far better thing that I do, 
than I have ever done; 
it is a far, far better rest that I go to, 
than I have ever known.
'''
transform_it = text_to_dict("Tale of Two Cities",text4,True)
all_texts.append(transform_it)


# Run the two cells below to confirm that first, you only have five texts in the all_texts list, and next, look at the all_texts list to see the dictionary inside it. 

# In[42]:


len(all_texts)


# In[43]:


all_texts


# In the cell below, loop through all_texts and print out the title of each text. (This is the only code you need to write for Part One.)

# In[44]:


for text in all_texts:
    print(text['title'])


# ## Part Two:  searching within lists and dictionaries
# In this part, we will be searching through each text and printing out a desired result. The searches, including loops and printing should all be defined in the function. The second cell should just have a function call that executes the function. I have written an example function and call for the first search. For each function that you write you should copy the function from the previous question and modify it so what does what I ask for.
# 
# For the first five functions, there are no parameters passed to the functions--the calls will just execute the function. Go step-by-step and take your time.

# In[45]:


def get_lengths():
    for text in all_texts:
        print(text['title'])
        print(len(text['text_as_string']))
        print("------------")


# In[46]:


get_lengths()


# Question 1
# Now write a function that gets the **line count for each poem** (or sentence count for each piece of prose). This function is going to be very similar to the last one. Instead of accessing the whole text via text['text_as_string'] which is a string, you need to access the list of lines/sentences and get the length of that list. Everything else should be the same.

# In[47]:


def get_line_count():
    for text in all_texts:
        print(text['title'])
        print(len(text['lines']))
    print("------------")


# In[48]:


get_line_count()


# Question 2
# Now write a function that prints out **one random line or sentence from each text**. Again, this function will look much the same as the last ones, but instead of getting numbers you need to get actual lines. I have included the necessary import and an example of how to get random integers. Basically, for each text you need to get one element from the list of lines/ sentences with a random number between 0 and the length of the list.

# In[49]:


from random import randint

def show_random_lines():
    for text in all_texts:
        random_num = randint(0,13)
        print(text['title'])
        print(text['lines'][random_num])
        print('-----------')


# In[50]:


show_random_lines()


# Question 3
# This is a little bit different--instead of printing out something from each text, I want you to **print the entire text of the longest text**. Remember in the first function, I printed out the length of each text. Well, you need to test for the longest text as you loop through and when you're done looping through print out the one that is longest.
# 
# **Major hints!**: To do this you will need two **tracking variables** set before the loop runs: A numerical one that tracks the longest length (the number), and string variable remembers the actual text that has that length.
# 
# Like this: longest_length = 0 and longest_text = ""
# 
# When you loop through, you need to test if each text was longer than the last one, and if it is longer--you update longest_length and longest_text to reflect the highest length, and the actual text. When the loop is over you then print out that longest_text string.

# In[51]:


def longest_text():
    longest_length = 0
    longest_text = ''
    for text in all_texts:
        if len(text['lines']) > longest_length:
            longest_length = len(text['lines'])
            longest_text = text['lines']
    print(longest_text)


# In[52]:


longest_text()


# Question 4
# This is kind of a combination of the first two functions--write a function that gets the **average line/sentence length for each text**.

# In[53]:


def average_line_length():
    for text in all_texts:
        print(text['title'])
        average = (len(text['text_as_string']))/(len(text['lines']))
        print(average)


# In[54]:


average_line_length()


# Question 5
# **Print the longest line/sentence in each text**. 
# This is similar to question 3--but your two tracking variables (longest_length and longest_line) need to be placed right before the inside loop--and then you print the lines each time the inside loop ends.

# In[55]:


def longest_line_in_each():
    for text in all_texts:
        print(text['title'])
        longest_line = 0
        longest_line_text = ''
        for line in text['lines']:
            if len(line) > longest_line:
                longest_line=len(line)
                longest_line_text= line
        print(longest_line_text)


# In[56]:


longest_line_in_each()


# Question 6
# **Print the shortest single line/sentence out of all of the texts that is greater than zero**
# This is the tricky-ish: You need to place the tracking variables outside the loop (like question 4, but the loop through all of the lines, test for the shortest one (greater than 0).

# In[57]:


def shortest_of_all_lines():
    shortest_line = 10000
    shortest_line_text = ''
    for text in all_texts:
        print(text['title'])
        for line in text['title']:
            if len(line) < shortest_line and len(line) != 0:
                shortest_line = len(line)
                shortest_line_text = line
            print(shortest_line_text)
# I can't think of another way to do this structurally, but I keep getting different answers and all of them are incorrect    


# In[58]:


shortest_of_all_lines()


# ## searching with regular expressions
# In the functions below you will search all the texts using regular expressions. The first few of these functions should not be too challenging--you just need to adjust the regular expression inside the function. At points it gets a little more complex as you have to control the looping through the lists and dictionaries.

# In[59]:


def get_this_word(word):
    my_regex = r"\b" + word + r"\b"
    for text in all_texts:
        result = [line for line in text['lines'] if re.search(my_regex, line, re.IGNORECASE)]
        if len(result) > 0:
            print(text['title'])
            [print(line) for line in result]
            print("------------")
            


# In[60]:


get_this_word('the')


# Question 7
# Print out the lines that **start** with the word entered.  You just need to adjust the regular expression here.

# In[93]:


def line_starts_with(word):
    my_regex = r"^" + word + r"\s.*"
    for text in all_texts:
        result = [line for line in text['lines'] if re.search(my_regex, line, re.IGNORECASE)]
        if len(result) > 0:
            print(text['title'])
            [print(line) for line in result]
            print("------------")
            
    


# In[94]:


line_starts_with('the')


# In[95]:


line_starts_with('they')


# Question 8
# Print out the lines that **end** with the word entered.  You just need to adjust the regular expression here.

# In[91]:


def line_ends_with(word):
    my_regex = r"(.*)\s" + word + r"$"
    for text in all_texts:
        result = [line for line in text['lines'] if re.search(my_regex, line, re.IGNORECASE)]
        if len(result) > 0:
            print(text['title'])
            [print(line) for line in result]
            print("------------")
            


# In[92]:


line_ends_with('me')


# Question 9
# Print out **how many times the word was found in each text.** In this case, instead of the list comprehension, you want to run a re.findall() on the string of the text (not the list) and then count the number of elements in the list of results.
# 
# Hint: use the original function at the beginning of this section, and make the proper adjustments to the variable "result"

# In[214]:


def how_many_times(word):
    my_regex = r"\b" + word + r"\b"
    for text in all_texts:
        result = re.findall(my_regex, text['text_as_string'], re.IGNORECASE)
        if len(result) > 0:
            print(text['title'])
            print(len(result))
            print("------------")
            
    


# In[223]:


how_many_times('in')


# Question 10
# Print out **the text that has the highest occurrence of the word** you searched for. This is similar to the last function, but here you need tracking variables like you had in Question 3.
# 

# In[263]:


def text_with_most_occurance_of(word):
    my_regex = r"\b" + word + r"\b"
    occurrences = 0
    occurrences_text = ""
    for text in all_texts:
        result = re.findall(my_regex, text['text_as_string'], re.IGNORECASE)
        if len(result) > occurrences and len(result) != 0:
            occurrences = len(result)
            occurrences_text = text['text_as_string']
    print(text['title'])
    print(occurrences_text)
        
        
    
    


# In[264]:


text_with_most_occurance_of('the')


# Question 11
# Print out **lines containing words of the length asked**. We are sort of back to basics here, you just need to modify the regular expression of the first function (get_this_word(word)) so that it can take a number parameter for the length of characters in a word.

# In[346]:


def lines_with_words_this_length(word):
    my_regex = r"\b\w{"+word+r"}\b"
    for text in all_texts:
        result = [line for line in text['lines'] if re.search(my_regex, line, re.IGNORECASE)]
        if len(result) > 0:
            print(text['title'])
            [print(line) for line in result]
            print("------------")


# In[347]:


lines_with_words_this_length('10')


# **Final question:** in this cell, describe two functions that you would like to write, not ones that you're able to write, but ones you think would be useful or interesting or fun--or might bring greater insight into a corpus of text. If you feel like trying to write it, go-ahead!

# 1. I think it might be interesting to find all of the end line punctuation marks specifically to investigate how the text's author chose to divide each line.
#     This might also give us some insight into the connotation of each text. 
# 2. I would also like to learn how to search for multiple words at a time, especially those that show up in tandem in each text. 

# **Bonus question:** Write a function that counts word frequency: that is, it returns a dictionary with each unique word and its count, sorted by the most frequent. Note, this is highly stack-overflowable -- Python has some built in ways of doing this. If you're doing this, you might as well try to do it on your own. But it's up to you!

# In[265]:


# I know you really wanted us to attempt this, but I'm so overwhelmed with homework that I need to get this assignment off my plate. I will turn it in now without the this questions and will circle back tomorrow if I'm able to!


# In[ ]:




