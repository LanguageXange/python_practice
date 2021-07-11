from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)



@app.route('/<string:page_name>')
def page(page_name):
    return render_template(f'{page_name}.html')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_success', methods=['POST', 'GET'])
def yeah():
    if request.method == 'POST':
        try:

            data = request.form.to_dict()
            #print(data)
            write(data)
            write_to_csv(data)
            return render_template('submit.html', user=data["username"])
        except:
            return 'something went wrong!'
    else:
        return 'oooops request method is not POST!'
        
def write(data):
    with open('db.txt',mode='a') as mydb:
        email = data['useremail']
        name = data['username']
        mydb.write(f'\n\n - Contact {email} for User:{name}')


def write_to_csv(data):
    with open('database.csv', mode='a') as spreadsheet:
         email = data['useremail']
         name = data['username']
         csv_writer = csv.writer(spreadsheet, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
         csv_writer.writerow([email,name])

