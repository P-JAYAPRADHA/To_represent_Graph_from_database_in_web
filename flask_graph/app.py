from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("<path which you saved service account key>")
firebase_admin.initialize_app(cred, {'databaseURL': '<your firebase databse url>'})
ref = db.reference('books/books')

datas = ref.get()

app = Flask(__name__)

@app.route('/')
def home():
    

    labels = list(datas.keys())
    values = list(datas.values())
    return render_template('graph.html', labels = labels, values = values)
if __name__ == "__main__":
    app.run(debug= True)


