import StringIO
import io
import pandas as pd
import requests
import datetime
import clr

optionExtensionsToCheck = ('0PE', '0CE', '5PE', '5CE')

def CalculateCharges(file):
    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    df = pd.read_csv(stream)
    df['TotalPrice'] = df.apply(lambda row: (row['Qty.'] * row['Avg. Price']), axis=1)

    def CalculateBrokerage(row):
        if row['Instrument'].endswith(optionExtensionsToCheck):
            return 20
        else:    
            value = row['Qty.'] * row['Avg. Price'] * 0.0001
            if value > 20:
                return 20
            else:
                return value

    def CalculateTransactionCharges(row):
        if row['Instrument'].endswith(optionExtensionsToCheck):
            return row['Qty.'] * row['Avg. Price'] * 0.0005
        else:
            return row['Qty.'] * row['Avg. Price'] * 0.0000325

    def CalculateSTT(row):
        tradetype = row['Type']
        if tradetype == 'sell' or tradetype == 'SELL':
            if row['Instrument'].endswith(optionExtensionsToCheck):
                return row['Qty.'] * row['Avg. Price'] * 0.0005
            else:
                return row['Qty.'] * row['Avg. Price'] * 0.00025

        else:
            return 0



    df['Brokerage'] = df.apply(CalculateBrokerage, axis=1)
    df['Txn Charges'] = df.apply(CalculateTransactionCharges, axis=1)
    df['Gst.'] = df.apply(lambda row: ((row['Brokerage'] + row['Txn Charges']) * 0.18), axis=1)
    df['SebiCharges'] = df.apply(lambda row: (row['Qty.'] * row['Avg. Price'] * 0.00002), axis=1)
    df['STT'] = df.apply(CalculateSTT, axis=1)
    return df