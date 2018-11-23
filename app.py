from stories import Story
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

story_options = [
    {
        "title":
        "first_story",
        "words": ["place", "noun", "verb", "adjective", "plural_noun"],
        "template":
        """Once upon a time in a long-ago {place}, there lived large    {adjective} {noun}. It loved to {verb} {plural_noun}."""
    },
    {
        "title":
        "second_story",
        "words": ["place", "noun", "verb", "adjective", "plural_noun"],
        "template":
        """A long time ago in {place}, there was a microsized {adjective} {noun}. It wished to {verb} {plural_noun}."""
    },
    {
        "title":
        "third_story",
        "words": ["verb_past_tense", "adjective", "plural_noun"],
        "template":
        """Last year, there was a small {adjective} cookie. It {verb_past_tense} into several {plural_noun}."""
    }
]


@app.route('/')
def dropdown_form():
    """ dropdown form - creates down down option for story type - then sends you to inputs"""

    titles = [story["title"] for story in story_options]
    return render_template("dropdown.html", titles=titles)


@app.route('/form')
def madlib_form():
    """ input forms for taking all the user information for the madlibs """
    current_story_title = request.args.get("title-selection")

    # find index of story matching current story title
    target_story_index = -1
    for story in story_options:
        if current_story_title == story.get("title"):
            target_story_index = story_options.index(story)
            break

    request_words = story_options[target_story_index]["words"]

    return render_template(
        "madlibform.html",
        current_story_title=current_story_title,
        request_words=request_words)


@app.route('/story')
def display_story():
    """ displays current story template with inputs from user """

    # grab current_story_selection from landing page
    current_story_title = request.args.get('current_story_title')

    # find index of story matching current story title
    target_story_index = -1
    for story in story_options:
        if current_story_title == story.get("title"):
            target_story_index = story_options.index(story)
            break

    # defines instance of story type
    story = Story(story_options[target_story_index]["words"],
                  story_options[target_story_index]["template"])

    # word template list of current story
    template_words = story_options[target_story_index]["words"]

    # dictionary comp - create the answers for our story
    answer = {word: request.args.get(word) for word in template_words}

    # create story string from story generate method
    story_string = story.generate(answer)

    # render template with our story display html
    return render_template(
        "displaystory.html", complete_story_string=story_string)
