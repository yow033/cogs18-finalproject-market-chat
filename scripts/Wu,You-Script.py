#!/usr/bin/python

import string
import random
import nltk

import requests
import json

news_request = requests.get(url='https://newsapi.org/v2/top-headlines?sources=the-wall-street-journal&apiKey=df21f07e419c41feb602fb9ba2a8456c')
news_dict = news_request.json()['articles']

def is_question(input_string):
    """Check if the input is a question.
   
    Parameters
    ----------
    input_string : string
        String that may contain '?'.
        
    Returns
    -------
    output_string : boolean
        Boolean that asserts whether the input contains '?'.
   """
    
    if "?" in input_string:
        output = True
    else:
        output = False
    return output 


def remove_punctuation(input_string):
    """Remove the punctuations in input string.
   
    Parameters
    ----------
    input_string : string
        String to remove punctuations.
        
    Returns
    -------
    output_string : string
        String without punctuations.
   """
    
    out_string =''
    for char in input_string:
        if not char in string.punctuation:
            out_string = out_string + char
    
    return out_string


def prepare_text(input_string):
    """Convert all the inputs to lower case string without any punctuations. 
   
    Parameters
    ----------
    input_string : string
        String that will be reorganized.
        
    Returns
    -------
    output_list : list
        List that contains all the lower case splited words of the input.
   """
    out_list=[]
    
    # Convert strings to lower case letters
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    
    # Split out the words from the string and list them as items in a list
    out_list = temp_string.split()
    return out_list


def respond_echo(input_string, number_of_echoes, spacer):
    """ Repeat input several times.
   
    Parameters
    ----------
    input_string : string
        String that to be repeated by certain nymber of times.
    
    number_of_echoes : integer
        Integer that determines how many times the input will be repeated.
    
    spacer : string 
        String to seperate input between the repetition.
        
    Returns
    -------
    echo_output : string
        String to repeat the input by the number of echos with a spacer as separator.
   """
    
    if not input_string == None:
        echo_output = (input_string+spacer)*number_of_echoes
    else:
        echo_output = None

    return echo_output


def selector(input_list, check_list, return_list):
    """ Repeat input several times.
   
    Parameters
    ----------
    input_list : list
        List that contains a list of input.
    
    check_list : list
        List that checks whether input contains certain items.
    
    return_list : list
        List contains items that will be drawn randomly.
        
    Returns
    -------
    output : string
        String to display the result of a random choice in a list given certain conditions met.
   """
    
    
    output = None
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break
    return output 


def string_concatenator(string1, string2, separator):
    """ Concatenate strings with separators.
   
    Parameters
    ----------
    string1 : string
        String to be connected with other inputs. 
    
    string2 : string
        String to be connected with other inputs.
    
    separator : string
        String to separate various inputs.
        
    Returns
    -------
    output : string
        String to display the result a series of connected inputs. 
   """
    output = string1+separator+string2
    return output



def list_to_string(input_list, separator):
    """ Concatenate items in a list and conver them to a string with separators.
   
    Parameters
    ----------
    input_list : list
        List containing items to be connected.
    
    separator : string
        String to separate various inputs.
        
    Returns
    -------
    output : string
        String to display the result a series of connected item in the input list. 
   """
    
    output = input_list[0]
    for item in input_list[1:]:
        output=string_concatenator(output, item, separator)
    return output 



def end_chat(input_list):
    """ End chat 
   
    Parameters
    ----------
    input_list : list
        List containing 'quit' to end chat.
    
    Returns
    -------
    True or False : boolean
        Boolean assures whether to end chat based on whether the input contains 'quit'.
   """
    
    if 'quit' in input_list:
        return True
    else: 
        return False


assert callable(end_chat)
assert isinstance(end_chat(['lalalala', 'have a great day!']), bool)
assert end_chat(['nope']) == False


def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two.
    
    Parameters
    ----------
    list_one : list
        List containing a set of items.
    
    list_two : list
        List containing a set of items that may be in list_one.
        
    Returns
    -------
    True or False : boolean
        Return result of whether the element in list one is in list two.
    """
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise.
    
    Parameters
    ----------
    list_one : list
        List containing a set of items.
    
    list_two : list
        List containing a set of items that may be in list_one.
        
    Returns
    -------
    element : string
        Return result of the element that are both in list one and list two.
    """
    
    for element in list_one:
        if element in list_two:
            return element
    return None


GREETINGS_IN = ['morning', 'hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ['Good Morning!', 'What can I do for you?', 'How can I help you today?', 'Want some fresh market news?', 'Nice Meeting You!', "Hello, it's nice to talk to you!", 'Nice to meet you!']

MARKETS_GREETINGS_IN = ["how's the market today", "what's the market like today?","market", 'markets' ]
MARKETS_GREETINGS_OUT = ['Political? or Deal? or Economy?']

type_news = ['political', 'deal', 'economy']
WHICH_ARTICLE = "Which % article would you like to read? (Enter the article number)"
NO_NEWS = "Sorry, there are no % headlines today!"

political_news_list = ['trump', 'jinping', 'trade', 'congress', 'sanction', 'china', 'us', 'british', 'europe', 'france', 'asia', 'africa', 'middle east', 'iran', 'iraq', 'korea', 'white house', 'law']
deal_news_list = ['merger', 'acquisition', 'investment', 'financing', 'uber', 'ge', 'amazon', 'facebook', 'lyft', 'healthcare', 'technology', 'consumer', 'real estate', 'google','yahoo', 'huawei']
economy_news_list = ['unemployment', 'gdp', 'economy', 'purchase', 'plunge', 'plummet', 'oil', 'outlook', '2019', 'next year', 'distress', 'crisis', 'market', 'workforce', 'plan']

COMP_IN = ['python', 'code', 'computer', 'algorithm', ]
COMP_OUT = ["Python is what I'm made of.", \
            "Did you know I'm made of code!?", \
            "Computers are so magical", \
            "Do you think I'll pass the Turing test?"]

PEOPLE_IN = ['turing', 'hopper', 'neumann', 'lovelace']
PEOPLE_OUT = ['was awesome!', 'did so many important things!', 'is someone you should look up :).']
PEOPLE_NAMES = {'turing': 'Alan', 'hopper': 'Grace', 'neumann': 'John von', 'lovelace': 'Ada'}

JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
JOKES_OUT = ['ha', 'haha', 'lol'] 

NONO_IN = ['matlab', 'java', 'C++']
NONO_OUT = ["I'm sorry, I don't want to talk about"]

UNKNOWN = ['Oops, such information is not available currently!']

QUESTION = "I'm too shy to answer questions. What do you want to talk about?"




def have_a_chat():
    """Main function to run our chatbot."""
    
    # Define news article lists outside loop to be able to reference when user inputs numeric choice option
    chosen_article_list = []
    article_list_indices = []
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None        
        
        # Check if the input is a question
        question = is_question(msg)
        
        # Check if the input is a number (article choice)
        isnumber = msg.isnumeric()

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            
            ## Check if the input looks like a market greeting, add a market greeting output if so
            outs.append(selector(msg, MARKETS_GREETINGS_IN, MARKETS_GREETINGS_OUT))
                
            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))
            
            # Check if the input looks like a computer thing, add a computer output if so
            if is_in_list(msg, type_news):
                
                # Define  specific news article lists inside loop to be able to reference when input is a specific news type
                political_article_list = []
                deal_article_list = []
                economy_article_list = []
                article_display = ''

                for e in news_dict:
                    article_title = e['title']
                    article_link = e['url']
                    article_summary = e['description']
                    
                    for word in political_news_list:
                        
                        # Check if a set of words are in the news article titles to determine whether it is political news
                        if word in article_title.lower():
                            political_article_list.append({'title': article_title, 'link': article_link, 'summary': article_summary })
                            
                    for word in deal_news_list:
                        
                        # Check if a set of words are in the news article titles to determine whether it is deal news
                        if word in article_title.lower():
                            deal_article_list.append({'title': article_title, 'link': article_link, 'summary': article_summary })

                    for word in economy_news_list:
                        
                        # Check if a set of words are in the news article titles to determine whether it is economy news
                        if word in article_title.lower():
                            economy_article_list.append({'title': article_title, 'link': article_link, 'summary': article_summary })
               
                # Chechk if the input contains news type that users want to read more about
                if "political" in msg:
                    
                    # Check if the news article list today for political news is empty
                    if len(political_article_list) != 0: 
                        for index, article in enumerate(political_article_list):
                            
                            # Assign an Index number to every news in the list and store this to be able to check later if an option was chosen
                            article_list_indices.append(str(index + 1)) 
                            article_display += ( '(' + str(index + 1) + ') ' + article['title'] + '\n')
                        outs.append(WHICH_ARTICLE.replace('%', 'political') + ' \n' + article_display)
                        
                        # store article list to be able to reference it later
                        chosen_article_list = political_article_list 
                    else:
                        outs.append(NO_NEWS.replace('%', 'political'))
                elif "deal" in msg:
                    
                    # Check if the news article list today for deal news is empty
                    if len(deal_article_list) != 0: 
                        for index, article in enumerate(deal_article_list):
                            
                            # Assign an Index number to every news in the list and store this to be able to check later if an option was chosen
                            article_list_indices.append(str(index + 1)) 
                            article_display += ( '(' + str(index + 1) + ') ' + article['title'] + '\n')
                        outs.append(WHICH_ARTICLE.replace('%', 'deal') + ' \n' + article_display)
                        
                        # store article list to be able to reference it later                        
                        chosen_article_list = deal_article_list 
                    else:
                        outs.append(NO_NEWS.replace('%', 'deal'))                
                elif "economy" in msg:
                    
                    # Check if the news article list today for economy news is empty
                    if len(economy_article_list) != 0: 
                        for index, article in enumerate(economy_article_list):
                            
                            # Assign an Index number to every news in the list and store this to be able to check later if an option was chosen
                            article_list_indices.append(str(index + 1)) 
                            article_display += ( '(' + str(index + 1) + ') ' + article['title'] + '\n')
                        outs.append(WHICH_ARTICLE.replace('%', 'economy') + ' \n' + article_display)
                        
                        # store article list to be able to reference it later
                        chosen_article_list = economy_article_list 
                    else:
                        outs.append(NO_NEWS.replace('%', 'economy'))
        
            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION
            
        if not out_msg and isnumber:
            if is_in_list(msg, article_list_indices):
                option_str = ''.join(msg)
                option_int = int(option_str)
                article_index = option_int - 1
                chosen_article = chosen_article_list[article_index]
                
                outs.append(chosen_article['title'] + '\n\n Summary: ' + chosen_article['summary'] + '\n\n Read more: ' + chosen_article['link'])
                
                options = list(filter(None, outs))
                if options:
                    out_msg = random.choice(options)

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)


have_a_chat()