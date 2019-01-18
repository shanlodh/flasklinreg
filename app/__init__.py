from flask import Flask
from sklearn.externals import joblib
import os


BASEDIR = os.path.dirname(os.path.abspath(__file__))
linreg_deserialized = joblib.load(BASEDIR + '/mlmodels/linreg.joblib')
app = Flask(__name__)


from app import routes

if __name__ == "__main__":
    print (BASEDIR)
    if(linreg_deserialized):
        print("model deserialized successfully")