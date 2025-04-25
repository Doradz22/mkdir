from flask import Flask, render_template,request
import csv
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

# Setup Google Sheets Connection Once
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name('config/doradz-sheets-key.json', scope)
client = gspread.authorize(creds)

# Function to Save Data
def save_to_google_sheets(data_list, sheet_id):
    sheet = client.open_by_key(sheet_id).sheet1
    sheet.append_row(data_list)


# Function to Save to CSV
def save_to_csv(data, filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)

    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(data.keys())
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

        # Save to CSV
        save_to_csv(data, 'data/client_submissions.csv')

        # Convert to list for Google Sheets
        data_list = list(data.values())
        save_to_google_sheets(data_list, '1eed_gVpZ-5dYSZGoCCSk8ebr4fqZpYPRK-sgnj6Z8po')

        return render_template('thank_you.html')

    return render_template('client_form.html')



@app.route('/contactinfo/model', methods=['GET', 'POST'])
def model_form():
    if request.method == 'POST':
        age = int(request.form['age'])

        if age < 18:
            return render_template('underage.html')

        data = {
            'Name': request.form['name'],
            'Age': request.form['age'],
            'Experience': request.form['experience'],
            'Permission to Post': request.form['permission'],
            'Agreed to Terms': 'Yes',
            'Availability': request.form['availability']
        }

        # Save to CSV
        save_to_csv(data, 'data/model_submissions.csv')

        # Convert to list for Google Sheets
        data_list = list(data.values())
        save_to_google_sheets(data_list, '1HcRtwlGQ1SLmuFtB-K7K3gciDsHh5UoDCnjneO-7hQ4')

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


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')




if __name__ == '__main__':
    app.run(debug=True)


    
