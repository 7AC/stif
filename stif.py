#!/usr/bin/env python

''' Posts info from Google Finance to Notification Center '''

import argparse
import sys
import googlefinance
import pync


def get_quotes(symbol):
    """Get a quote and notify"""
    quote = googlefinance.getQuotes(symbol)[0]
    url = 'https://www.google.com/finance?q=' + symbol
    subtitle = quote['LastTradePrice']
    text = quote.get('Change') or quote['LastTradeTime']
    pync.Notifier.notify(text, title=symbol.upper(),
                         subtitle=subtitle, sender='com.apple.stocks',
                         activate='com.apple.Safari', open=url)


def main():
    ''' Parses command-line arguments '''
    parser = argparse.ArgumentParser()
    parser.add_argument('symbol', metavar='KEYWORD', nargs=1,
                        help='ticker symbol')
    args = parser.parse_args()
    get_quotes(args.symbol[0])


if __name__ == "__main__":
    sys.exit(main())
