from flask import Flask, render_template
from flask import request
import csv
import os


app = Flask(__name__)





def save_to_csv(data, filename):
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(data.keys())  # Write header once
        writer.writerow(data.values())






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
        data = {
            'Name': request.form['name'],
            'Email': request.form['email'],
            'Shoot Type': request.form['shoot_type'],
            'Date': request.form['date'],
            'Time': request.form['time'],
            'Location': request.form['location'],
            'Hours': request.form['hours'],
            'Permission to Post': request.form['permission'],
            'Notes': request.form['notes']
        }

        save_to_csv(data, 'data/client_submissions.csv')
        return render_template('thank_you.html')

    # Pag GET request (pag open pa lang ng form)
    return render_template('client_form.html')



@app.route('/contactinfo/model', methods=['GET', 'POST'])
def model_form():
    if request.method == 'POST':
        age = int(request.form['age'])

        # ✅ Check if under 18
        if age < 18:
            return render_template('underage.html')

        data = {
            'Name': request.form['name'],
            'Age': age,
            'Experience': request.form['experience'],
            'Permission to Post': request.form['permission'],
            'Agreed to Terms': 'Yes',
            'Availability': request.form['availability']
        }

        save_to_csv(data, 'data/model_submissions.csv')
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
