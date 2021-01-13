from flask import Flask, send_file, Response
from flask import request, jsonify, flash, redirect, url_for, make_response
from sqlalchemy import create_engine
from json import dumps
import StringIO
import pandas as pd
import requests
import datetime
import clr
from charges import CalculateCharges
import constants
from flask_cors import CORS
from fetchFrame import fetch
import Option

ALLOWED_EXTENSIONS = set(['csv'])
optionExtensionsToCheck = ('0PE', '0CE', '5PE', '5CE')
app = Flask(__name__)
CORS(app)
app.secret_key = "super secret key"

@app.route('/', methods=['GET'])
def home():
    return '''<p><strong>Please select the Stock: </strong><select name="cars"></select></p>
<p><button type="button">Fetch.</button></p>'''


@app.route('/brokerage', methods=['POST'])
def brokerage():
    '''
    This is to calculate the brokerage
    :return: CSV file
    '''
    try:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']  # type: csv
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            df = CalculateCharges(file)       
            output = StringIO.StringIO()
            df.to_csv(output)

            return Response(output.getvalue(), mimetype="text/csv")

    except Exception as e:
        print(e)
        return '''<h1>Error</h1><p>error while reading excel</p>'''

@app.route('/fnostocks', methods=['GET'])
def NiftyfnoStockNames():
    return jsonify(constants.NIFTY_FNO_STOCKS)


@app.route('/optionchain/<underlying>/<optiontype>', methods=['GET'])
def getOptionChain(underlying, optiontype):   
     
    queryStr = ''' set nocount on  
                    select *
                    from OptionChain where underlying = '{}'and OptionType = '{}'
                    order by DownloadDate desc, openInterest desc, changeinOpenInterest                   
                    ''' 
                    
    query = queryStr.format(underlying, optiontype, optiontype)
  
    df = fetch(query)
    result = Option.GetMaximumCallAtStrike(df);
    
    return Response(df.to_json(orient='records'), mimetype="application/json")  

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS      


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)