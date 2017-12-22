
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup
import urllib.request
import sys
import csv

# Change this to indicate which types you want to create flash cards for
supported_types = ['presentIndicative', 'preteritIndicative','imperfectIndicative', 'presentSubjunctive']
# Possible types are
# Indicative
#    presentIndicative
#    preteritIndicative
#    imperfectIndicative
#    conditionalIndicative
#    futureIndicative
# Subjunctive
#    presentSubjunctive
#    imperfectSubjunctive
#    imperfectSubjunctive2
#    futureSubjunctive
# Imperative
#    imperative
#    negativeImperative
# Continious Progressive
#    presentContinuous
#    preteritContinuous
#    imperfectContinuous
#    conditionalContinuous
#    futureContinuous
# Perfect
#    presentPerfect
#    preteritPerfect
#    pastPerfect
#    conditionalPerfect
#    futurePerfect
# Perfect Subjunctive
#    presentPerfectSubjunctive
#    pastPerfectSubjunctive
#    futurePerfectSubjunctive

def find_extract_html_el(verb):
    URL_BASE = "http://www.spanishdict.com/conjugate/"
    quoted_verb = urllib.parse.quote(verb)
    url = URL_BASE + quoted_verb    
    response = urllib.request.urlopen(url)
    data = response.read()
    soup = BeautifulSoup(data, "html.parser")
    main_cont = soup.find('div', attrs={'class':'main-container'})
    conjug = main_cont.find('div', attrs={'class':'conjugation'})
    if conjug == None:
        return None
    card = conjug.find('div', attrs={'class':'card'})
    return card

def extract_conjugations(card):   
    # <div class="card">
    #    <div class="vtable-header"> 
    #    <div class="vtable-wrapper">
    #    The two divs above contain conjugations for different tense for the same mood, e.g. indicative, subjunctive, etc
    # </div>

    current_mood = None
    dicts = {}
    # Initialize the dictionaries
    for sup_type in supported_types:
        dicts[sup_type] = {}

    for card_div in card.children:
        if (card_div.name != 'div') or card_div.get('class') == None:
            continue
        div_classes = card_div['class']
        if 'vtable-header' in div_classes:
            mood = card_div.find('a').find('span').text
            current_mood = mood
        elif 'vtable-wrapper' in div_classes:
            # Iterate over all tenses
            for tr in card_div.table.children:
                if tr.name != 'tr' or tr.get('class') == None or 'vtable-head-row' in tr.get('class'):
                    pass
                else:
                    # Iterate over all the pronouns
                    pronoun = tr.td.text
                    for pronoun_td in tr.children:
                        if pronoun_td.name != 'td' or pronoun_td.get('class') == None or 'vtable-pronoun' in pronoun_td.get('class'):
                            pass
                        else:
                            if (pronoun_td.div.div == None): # If for this pronoun, there doesnt exist a conjugation
                                continue
                            mood_tense = pronoun_td.div.div['data-tense'] # e.g. presentIndicative, preteritIndicative
                            conjug_word = pronoun_td.div.div.text
                            correct_dict = dicts.get(mood_tense)
                            if correct_dict == None and mood_tense in supported_types:
                                print("Error trying to get a dictionary for type {}".format(mood_tense))
                                # TODO exit?? print the word we are trying to processs?
                            elif correct_dict != None:
                                correct_dict[pronoun] = conjug_word
    return dicts


# In[9]:


def process_word(verb):
    html_el = find_extract_html_el(verb)
    if html_el == None:
        print("Could not process verb '{}'".format(verb))
        return
    dicts = extract_conjugations(html_el)
    for mood_tense in supported_types:
        newfilename = '{}.txt'.format(mood_tense)
        with open(newfilename, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter='\n')
            curr_dict = dicts[mood_tense]
            if curr_dict == None:
                print("Cant find a dict for {}".format(mood_tense))
                continue
            for pronoun in curr_dict:
                flashcard = "{} {}\t {}".format(pronoun, verb, curr_dict[pronoun])
                writer.writerow([flashcard])
    print("Processed verb '{}'".format(verb))

def find_conjugations(textfile):
    try:
        with open(textfile, 'r') as input_file:
            reader = csv.reader(input_file, delimiter='\n')
            for word in reader:
                if len(word) > 1:
                    print("There is more than one word at each line. Those will not be processed\n")
                process_word(word[0])       
    except FileNotFoundError:
        print("Could not find file {} in current directory".format(textfile))


# In[10]:


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <text file with \\n separated words>\n".format(sys.argv[0]))
    else:
        find_conjugations(sys.argv[1])
        print("Done processing")


# In[ ]:





# In[ ]:




