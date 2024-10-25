from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')  
def my_home():
    return render_template('index.html')   #Using flask –app <app_name> run#


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/blog/2020/dogs')  
# def blog2():
#     return 'This is blog in breadcrumbs under blog under 2020, then dogs' 

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

#This function saves the contact information to CSV file
def write_to_csv(data):
  with open('database.csv', mode='a', newline='') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods =['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong"






#to run the debug mode on
if __name__=='__main__':
    app.run(debug=True)
