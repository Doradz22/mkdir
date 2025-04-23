from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/contactinfo')
def contactinfo():
    return render_template('contactinfo.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/portfolio/weddings')
def weddings():
    return render_template('weddings.html')

@app.route('/portfolio/portraits')
def portraits():
    return render_template('portraits.html')

@app.route('/portfolio/studio')
def studio():
    return render_template('studio.html')

@app.route('/portfolio/events')
def events():
    return render_template('events.html')

@app.route('/portfolio/all')
def all_portfolio():
    return render_template('all_portfolio.html')



if __name__ == '__main__':
    app.run(debug=True)
