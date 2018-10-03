programmingDict = {
    "Henk": 6.3,
    "Jan": 9.1,
    "Klaas": 9.8,
    "Patricia": 7.5,
    "Jim": 10.0,
    "Jochem": 8.5,
    "Geert": 8.4,
    "Ans": 4.2
}
print("De cijfers hoger dan een 9.0 zijn:")
for cijferNaam, cijferHoog in programmingDict.items():
    if cijferHoog > 9.0:
        print(cijferNaam, "heeft een", cijferHoog, "gehaald!")