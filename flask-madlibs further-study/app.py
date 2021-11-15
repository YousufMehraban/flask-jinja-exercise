from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('form.html', words=story.prompts)

@app.route('/story')
def show_story():
    
    text = story.generate(request.args)
    return render_template('story.html', text = text)



