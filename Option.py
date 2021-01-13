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


def GetMaximumCallAtStrike(records):
    records.loc[(records['DownloadDate'] == records['DownloadDate'].max()) & (records['openInterest'] == records['openInterest'].max())]  
    print records
    return records 

def run(underlying, optiontype):    
    queryStr = ''' set nocount on  
                    select *
                    from OptionChain where underlying = '{}'and OptionType = '{}'
                    order by DownloadDate desc, openInterest desc, changeinOpenInterest                   
                    ''' 
                    
    query = queryStr.format(underlying, optiontype)  
    df = fetch(query)
    GetMaximumCallAtStrike(df)


if __name__ == '__main__':
    run('ACC', 'CE')
