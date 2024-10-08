

from flask import Flask, render_template, request
import random

app= Flask (__name__)

def get_word(word_type):
    words= {
        'noun' : ['dog','car','banana','mountain','cookie'],
        'verb' : ['run','jump','eat','sleep','drive'],
        'adjective' : ['big','yellow', 'quick','lazy', 'funny'],
        'adverb' : ['quickly','lazily','happily','sadly'],
        'place' : ['park', 'restaurant','school','zoo','museum'],
    }
    return random.choice(words[word_type])

def create_story():
    
    story_template=(
            "(Today I went to the {place} and I saw a very {adjective} {noun}."
            "It was {adverb} {verb}ing around! I couldn't believe my eyes, so I decided to "
            "{verb} along with it. What a day!"
    )

    story = story_template.format(
        
        place=get_word('place'),
        noun=get_word('noun'),
        adjective=get_word('adjective'),
        adverb=get_word('adverb'),
        verb=get_word('verb'),

    )
    return story

@app.route('/')

def home ():
        return create_story()

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000)