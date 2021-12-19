from flask import Flask, request, render_template
import stories

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Madlibs.html")

@app.route('/story')
def madlib():
    story = "Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    ans = {
        "place": place,
        "noun": noun,
        "verb": verb,
        "adjective": adjective,
        "plural_noun": plural_noun
    }
    s = stories.Story(["place", "noun", "verb", "adjective", "plural_noun"],story)
    new_story = s.generate(ans)

    return render_template("Stories.html", new_story=new_story)
