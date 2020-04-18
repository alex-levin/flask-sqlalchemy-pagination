from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
print(os.path.join(basedir, 'pages.db'))
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
# https://docs.sqlalchemy.org/en/13/core/engines.html#sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Alex\\Documents\\Projects\\flask-sqlalchemy-pagination\\pages.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pages.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# db.create_all()

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/?highlight=pagination#flask_sqlalchemy.Pagination
class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    

@app.route('/thread/<int:page_num>')
def thread(page_num):
        # If error_out is True (default) - will display 404 if page doesn't exist
        # If error_out is False - will display blank page if page doesn't exist
        threads = Thread.query.paginate(per_page=5, page=page_num, error_out=True)
        return render_template('index.html', threads=threads)
        
        
if(__name__ == '__main__'):
    app.run(debug=True)