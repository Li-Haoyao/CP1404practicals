from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
app.secret_key = 'IT@JCUA0Zr98j/3yXa R~XHH!jmN]LWX/,?RT'

@app.route('/')
def home():
    """Home page route."""
    return render_template("home.html")

@app.route('/about')
def about():
    """About page route."""
    return "I am still working on this"

@app.route('/search', methods=['GET', 'POST'])
def search():
    """Search page route."""
    if request.method == 'POST':
        search_term = request.form.get('search', '').strip()
        if not search_term:
            return render_template("search.html", error="Please enter a search term")
        session['search_term'] = search_term
        return redirect(url_for('results'))
    return render_template("search.html")

@app.route('/results')
def results():
    """Results page route."""
    search_term = session.get('search_term')
    if not search_term:
        return redirect(url_for('search'))

    page = get_page(search_term)
    return render_template("results.html", page=page, search_term=search_term)

def get_page(search_term):
    """Get a Wikipedia page safely."""
    try:
        # Try getting exact page
        return wikipedia.page(search_term)

    except wikipedia.exceptions.PageError:
        # Page not found → get random
        title = wikipedia.random()
        return wikipedia.page(title)

    except wikipedia.exceptions.DisambiguationError as e:
        # Ambiguous → choose first VALID option
        for option in e.options:
            try:
                return wikipedia.page(option)
            except:
                continue

        # If all fail, fallback
        return wikipedia.page(wikipedia.random())

if __name__ == '__main__':
    app.run(debug=True)