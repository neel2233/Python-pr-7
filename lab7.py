import json
import sys

if len(sys.argv) == 1:
    fileName = input("Введите имя json файла: ") + ".json"
elif len(sys.argv) == 2:
    fileName = sys.argv[1]
else:
    fileName = ""

if fileName != "":
    with open(fileName, "r") as jsonFile:
        jsonDict = json.load(jsonFile)
        for CSVName in jsonDict.keys():
            with open(f"{CSVName}.csv", "w") as CSVFile:
                colNames = list(jsonDict[CSVName][0].keys())
                CSVFile.write(";".join(colNames) + "\n")
                for row in jsonDict[CSVName]:
                    rowList = []
                    for col in colNames:
                        rowList.append(row[col])
                    CSVFile.write(";".join(list(map(str, rowList))) + "\n")

