#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv

def load_trades_file(filename):
    buys = {}
    sells = {}
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['major'] == 'btc':
                if row['type'] == 'buy':
                    buys[row['timestamp']] = {
                            'price': float(row['rate']),
                            'amount': float(row['amount'])
                    }
                elif row['type'] == 'sell':
                    sells[row['timestamp']] = {
                            'price': float(row['rate']),
                            'amount': float(row['amount'])
                    }
    return buys, sells

def average_price(buys, sells):
    total_btc_buys = 0.
    total_btc_sells = 0.
    total_mxn_buys = 0.
    total_mxn_sells = 0.
    for timestamp, buy in buys.items():
        total_btc_buys += buy['amount']
        total_mxn_buys += buy['amount'] * buy['price']
    for timestamp, sell in sells.items():
        total_btc_sells -= sell['amount']
        total_mxn_sells -= sell['amount'] * sell['price']
    return (total_mxn_buys + total_mxn_sells)/ (total_btc_buys + total_btc_sells)

def total_btc(buys, sells):
    total_btc_buys = 0.
    total_btc_sells = 0.
    for timestamp, buy in buys.items():
        total_btc_buys += buy['amount']
    for timestamp, sell in sells.items():
        total_btc_sells -= sell['amount']
    return total_btc_buys + total_btc_sells

filename='/home/i0rch/Downloads/bitso.com-trade-10302024-14684423122665280162.csv'
if __name__ == '__main__':
    buys, sells = load_trades_file(filename)
    print('total BTC: {}'.format(total_btc(buys, sells)))
    print('average buys: {}'.format(average_price(buys,{})))
    print('average sells: {}'.format(average_price({}, sells)))
    print('average price: {}'.format(average_price(buys, sells)))

