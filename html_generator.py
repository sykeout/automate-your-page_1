

# // Title List Builder //
# Loop through concepts, copy titles, append them to list of titles

def get_title(concepts):
    title_list = []
    for concept in concepts:
        title = concept[concept.find('TITLE:')+7 : concept.find('DESCRIPTION:')-1]
        title_list.append(title)
    return title_list
# Finally working, freaking heck!



# // Description List Builder //
# Loop through concepts, copy descriptions, append them to list of descriptions

def get_description(concepts):
    description_list = []
    for concept in concepts:
        description = concept[concept.find('DESCRIPTION:')+13 :]
        description_list.append(description)
    return description_list
# Also working. Boomtown!


# // CONCEPT FINDER //
# Find number of concepts in text, create list with this number of elements, break text into concepts and place within list elements.

def concept_finder(text):
    n = text.count('TITLE:')
    concepts = [[] for i in range(n)]
    count = 0
    for e in concepts:
        while count < len(concepts):
            next_concept_start = text.find('TITLE:')
            next_concept_end = text.find('TITLE:', next_concept_start + 1)
            if next_concept_end >= 0:
                concepts[count] = text[next_concept_start:next_concept_end]
            else:
                next_concept_end = len(text)
                concepts[count] = text[next_concept_start:]
            text = text[next_concept_end:]
            count +=1
    return concepts
# Seems to work. Yipee!



# // HTML WRITER //
# Take title element from title_list, and description element from corresponding position in description_list and place them within
# HTML for as many concepts as there are.
# Then add closing div tags

def html_generate(text):
    count = 0
    title = get_title(concept_finder(text))
    description = get_description(concept_finder(text))
    top_tags = '''
    <div class="concept">
        <div class="title">
        '''
    middle_tags = '''
        </div>
        <div class="description">
        '''
    bottom_tags = '''
        </div>
    </div>'''
    for s in title:
        print top_tags + title[count] +  middle_tags + description[count] + bottom_tags
        count +=1
# painted myself into a corner by using lists instead of strings like Andy. Fun learning though :-)


# // Andy's test text to use //

TEST_TEXT = """TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true."""



