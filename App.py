
import pandas
import csv 
import json 

while True:
    val = input ('Enter 1 for CSV, 2 for JSON and 3 for XML').lower()
    if val =='1':
        dataframe = pandas.read_csv("HW.txt",delimiter="\t")
        dataframe.to_csv("myCSV.csv", encoding='utf-8', index=False)
    elif val == '2':
        dataframe = pandas.read_csv("HW.txt",delimiter="\t")
        dataframe.to_csv("CSVtoJSON.csv", encoding='utf-8', index=False)
        def csv_to_json(csvFilePath, jsonFilePath):
            jsonArray = []
            with open(csvFilePath, encoding='utf-8') as csvf: 
                csvReader = csv.DictReader(csvf) 
                for row in csvReader: 
                    jsonArray.append(row)
            with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
                jsonString = json.dumps(jsonArray, indent=4)
                jsonf.write(jsonString)
        csvFilePath = r'CSVtoJSON.csv'
        jsonFilePath = r'Myjson.json'
        csv_to_json(csvFilePath, jsonFilePath)
    elif  val == '3':
        dataframe = pandas.read_csv("HW.txt",delimiter="\t")
        dataframe.to_csv("CSVtoXML.csv", encoding='utf-8', index=False)
        csvFile = 'CSVtoXML.csv'
        xmlFile = 'myXML.xml'
        csvData = csv.reader(open(csvFile))
        xmlData = open(xmlFile, 'w')
        xmlData.write('<csv_data>' + "\n")
        rowNum = 0
        for row in csvData:
            if rowNum == 0:
                tags = row
                for i in range(len(tags)):
                    tags[i] = tags[i].replace(' ', '_')
            else: 
                xmlData.write('<row>' + "\n")
                for i in range(len(tags)):
                    xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
                xmlData.write('</row>' + "\n")
            rowNum +=1
        xmlData.write('</csv_data>' + "\n")
        xmlData.close()
    else:
        quit()
