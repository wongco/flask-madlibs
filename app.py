from stories import Story
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

story_options = {
    "first_story":
    '''Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.''',
    "second_story":
    '''A long time ago in {place}, there was a microsized {adjective} {noun}. It wished to {verb} {plural_noun}.'''
}


@app.route('/')
def dropdown_form():
    """ dropdown form - creates down down option for story type - then sends you to inputs"""
    return render_template("dropdown.html", stories=story_options)


@app.route('/form')
def madlib_form():
    """ input forms for taking all the user information for the madlibs """
    current_story = request.args.get("selection")
    return render_template("madlibform.html", current_story_data=current_story)


@app.route('/story')
def display_story():
    """ displays current story template with inputs from user """

    # grab current_story_selection from landing page
    current_story = request.args.get('current_story')

    # defines instance of story type
    story = Story(["place", "noun", "verb", "adjective", "plural_noun"],
                  story_options[current_story])

    # create the answers for our story
    answer = {
        "place": request.args.get('place'),
        "noun": request.args.get('noun'),
        "verb": request.args.get('verb'),
        "adjective": request.args.get('adjective'),
        "plural_noun": request.args.get('plural_noun')
    }

    # create story string from story generate method
    result = story.generate(answer)
    print(result)

    # render template with our story display html
    return render_template("displaystory.html", complete_story_string=result)
