from flask import Flask, render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')







@app.route('/contactinfo')
def contactinfo():
    return render_template('contact_landing.html')

@app.route('/contactinfo/client', methods=['GET', 'POST'])
def client_form():
    if request.method == 'POST':
        # Dito natin hahawakan yung submitted data later
        name = request.form['name']
        email = request.form['email']
        shoot_type = request.form['shoot_type']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        hours = request.form['hours']
        permission = request.form['permission']
        notes = request.form['notes']

        # For now, simple print or redirect
        print(f"New Client: {name}, {email}, {shoot_type}")

        return render_template('thank_you.html')

    return render_template('client_form.html')


@app.route('/contactinfo/model', methods=['GET', 'POST'])
def model_form():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        experience = request.form['experience']
        permission = request.form['permission']
        agree = request.form.get('agree')
        availability = request.form['availability']

        # Age check (basic handling for now)
        if age < 18:
            return render_template('underage.html')

        if not agree:
            return "<h2>You must agree to the terms to proceed.</h2>"

        print(f"Model: {name}, Age: {age}, Experience: {experience}")

        return render_template('thank_you.html')

    return render_template('model_form.html')






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
