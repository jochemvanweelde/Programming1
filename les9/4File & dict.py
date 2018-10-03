tickerSymbol={
    "YAHOO":"YHOO",
    "GOOGLE INC":"GOOG",
    "Harley-Davidson":"HOG",
    "Yamana Gold":"AUY",
    "Sotheby's":"BID",
    "inBev":"BUD"
}
def ticker(filename):
    for naam, ticker in tickerSymbol.items():
        if naam == filename:
            print("Ticker symbol:", ticker)
bedrijf = input("Enter Company name:")
ticker(bedrijf)