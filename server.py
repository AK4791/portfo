from flask import Flask, url_for, render_template, request, redirect
import csv
from pathlib import Path

app = Flask(__name__)

# print(url_for('static',filename="/assets/apple-icon-180x180.png"))

# href="./assets/apple-icon-180x180.png"


@app.route('/')
def base():
    return render_template('index.html')

# <form action = 'submit_form' method = 'post'>
# send button
# </form>

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# FLASK_APP
# FLASK_ENV
# render_template(url,**Kwargs)
# request
# redirect()

@app.route('/<string:page>')
def dynamicpage(page):
    return render_template(page)


def write2csv(filename, datarow):
    path = Path('database')
    if (not path.exists()):
        path.mkdir()
    path = path.joinpath('stg1.csv')
    # path.touch()
    #addheaders = not file.exists()
    with open(path, mode='w+', newline='') as csvfile:
        # dialect = csv.Sniffer().sniff(csvfile.readline())
        # csvfile.seek(0)

        # csv_write = csv.writer(csvfile, delimiter=',',
        #                        quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_write = csv.DictWriter(csvfile, datarow.keys())
        try:
            if not csv.Sniffer().has_header(csvfile.read(10)):
                csvfile.seek(0)
                csv_write.writeheader()
            else:
                csvfile.seek(0)
        except:
            csv_write.writeheader()
        csv_write.writerow(datarow)
        # csv_write.writerow(['Name', 'email', 'Subject', 'Message'])

        # csv_write.writerow(datarow)

    # with open(datarow)


@app.route('/submitted', methods=['GET', 'POST'])
def submition():
    if request.method == 'POST':
        data = request.form.to_dict()
        # print("huh", data, data['name'])

        write2csv('database/stg1.csv', datarow=data)
        return render_template('/acknowledgecontact.html', varName=data['name'])
        # return 'Acknwledged'
