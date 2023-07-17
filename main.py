from flask import Flask, request
from flask import render_template

from app.analyzer_json import check_data
from app.settings import *
from app.models import db
from app.models import DataJson

app = Flask(
    __name__,
    template_folder='templates/app',
)


def main():
    with db:
        db.create_tables([DataJson])

    app.secret_key = os.getenv('KEY_FLASK')
    app.run(host=HOST, port=PORT_DB, Hdebug=DEBUG)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        file_content = file.read()

        if file_content:
            check_data(file_content)
            if check_data(file_content):
                return render_template('message_success.html')
            else:
                return render_template('message_error.html')
        else:
            return render_template('message_error.html')
    return render_template('index.html')


@app.route('/table', methods=['GET'])
def table_view():
    data = DataJson.select()
    return render_template('table_view.html', data=data)


if __name__ == '__main__':
    main()
