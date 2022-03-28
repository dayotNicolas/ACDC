import urllib.request
import csv, json
import re

urlMainFile = "https://www.data.gouv.fr/fr/organizations/sante-publique-france/datasets-resources.csv"
MainCsvFilePath = "datas/CSV/mainCsv.csv"
urllib.request.urlretrieve(urlMainFile, MainCsvFilePath)

# todo : test si le fichier de csv principal est déja stocké, et l'effacer si c est le cas

# todo : manipuler le main file csv pour récupérer les urls des fichiers qui nous interesses et construire le dict urlList avec.
with open(MainCsvFilePath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=';')
    ListMatchToSort1 = []
    ListMatchToSort2 = []
    ListMatchToSort3 = []
    ListMatchToSort4 = []
    ListMatchToSort5 = []
    ListMatchToSort6 = []
    for row in csvReader:
        if re.search("indicateurs-de-lactivite-epidemique-taux-dincidence-de-lepidemie-de-covid-19-par-metropole.*sg-metro-opendata",row[9]) is not None:
            splitTitle = row[10].split('-')
            if len(splitTitle) == 7:
                ListMatchToSort1.append(row[9])

        if re.search("donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1.*vacsi-v-dep",row[9]) is not None:
            ListMatchToSort2.append(row[9])

        if re.search("donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1.*vacsi-v-fra",row[9]) is not None:
            ListMatchToSort3.append(row[9])
        
        if re.search("donnees-hospitalieres-relatives-a-lepidemie-de-covid-19.*covid-hosp-ad-age",row[9]) is not None:
            ListMatchToSort4.append(row[9])

        if re.search("donnees-de-vaccination-relatives-aux-professionnels-et-resident-en-ehpad-et-usld.*vacsi-prof-dep",row[9]) is not None:
            ListMatchToSort5.append(row[9])

        if re.search("donnees-de-certification-electronique-des-deces-associes-au-covid-19-cepidc.*covid-cedc-quot",row[9]) is not None:
            ListMatchToSort6.append(row[9])

    urlList = {}
    ListMatchToSort1.sort()
    urlList[ListMatchToSort1[-1]] = "datas/CSV/sg-metro-opendata.csv"
    ListMatchToSort2.sort()
    urlList[ListMatchToSort2[-1]] = "datas/CSV/vacsi-v-dep.csv"
    ListMatchToSort3.sort()
    urlList[ListMatchToSort3[-1]] = "datas/CSV/vacsi-v-fra.csv"
    ListMatchToSort4.sort()
    urlList[ListMatchToSort4[-1]] = "datas/CSV/covid-hosp-ad-age.csv"
    ListMatchToSort5.sort()
    urlList[ListMatchToSort5[-1]] = "datas/CSV/vacsi-prof-dep.csv"
    ListMatchToSort6.sort()
    urlList[ListMatchToSort6[-1]] = "datas/CSV/covid-cedc-quot.csv"

# urlList = {
#     "https://static.data.gouv.fr/resources/indicateurs-de-lactivite-epidemique-taux-dincidence-de-lepidemie-de-covid-19-par-metropole/20220307-191013/sg-metro-opendata-2022-03-07-19h10.csv" : "datas/CSV/sg-metro-opendata-2022-03-07-19h10.csv",
#     "https://static.data.gouv.fr/resources/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/20220311-190146/vacsi-v-dep-2022-03-11-19h01.csv" : "datas/CSV/vacsi-v-dep-2022-03-11-19h01.csv",
#     "https://static.data.gouv.fr/resources/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/20220311-190143/vacsi-v-fra-2022-03-11-19h01.csv" : "datas/CSV/vacsi-v-fra-2022-03-11-19h01.csv",
#     "https://static.data.gouv.fr/resources/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/20220310-190135/covid-hosp-ad-age-2022-03-10-19h01.csv" : "datas/CSV/covid-hosp-ad-age-2022-03-10-19h01.csv",
#     "https://static.data.gouv.fr/resources/donnees-de-vaccination-relatives-aux-professionnels-et-resident-en-ehpad-et-usld/20220311-190133/vacsi-prof-dep-2022-03-11-19h01.csv" : "datas/CSV/vacsi-prof-dep-2022-03-11-19h01.csv",
#     "https://static.data.gouv.fr/resources/donnees-de-certification-electronique-des-deces-associes-au-covid-19-cepidc/20200518-185536/covid-cedc-quot.csv" : "datas/CSV/covid-cedc-quot.csv"
# }

JsonDict = {
    "datas/CSV/sg-metro-opendata.csv" : "datas/JSON/evolution_taux_incidence.json",
    "datas/CSV/vacsi-v-dep.csv" : "datas/JSON/vaccin_cage_date.json",
    "datas/CSV/vacsi-v-fra.csv" : "datas/JSON/vaccin_date.json",
    "datas/CSV/covid-hosp-ad-age.csv" : "datas/JSON/hospitalisation_age.json",
    "datas/CSV/vacsi-prof-dep.csv" : "datas/JSON/vaccin_pro_poucentage_dep.json",
    "datas/CSV/covid-cedc-quot.csv" : "datas/JSON/deces_age_region.json"
}

for cle, valeur in urlList.items():
   urllib.request.urlretrieve(cle, valeur)


def takeCSVMakeJSON(CSVPath, JSONPath):
    data = {}
    with open(CSVPath) as csvFile:
        if CSVPath == "datas/CSV/sg-metro-opendata-2022-03-07-19h10.csv":
            csvReader = csv.DictReader(csvFile, delimiter=',')
        else :
            csvReader = csv.DictReader(csvFile, delimiter=';')
        id = 0
        for rows in csvReader:
            #print(rows)
            data[id] = rows
            id += 1

    with open(JSONPath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

for cle, valeur in JsonDict.items():
    takeCSVMakeJSON(cle, valeur)