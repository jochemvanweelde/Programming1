import datetime
outfile = open('hardlopers.txt', '')
def strftime():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")
    naam = input("Wat is de naam van de hardloper?")
    outfile.write(s)
    outfile.write(naam)
    outfile.write('\n')
strftime()