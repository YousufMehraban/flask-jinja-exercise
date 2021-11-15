from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
# story = Story(answers)


@app.route('/')
def homepage():
    return render_template('form.html')

@app.route('/story')
def show_story():
    
    text = story.generate(request.args)
    return render_template('story.html', text = text)



    
    
    
    
    
    
    # place = request.args['place']
    # noun = request.args['noun']
    # verb = request.args['verb']
    # adjective = request.args['adjective']
    # plural_noun = request.args['plural_noun']
