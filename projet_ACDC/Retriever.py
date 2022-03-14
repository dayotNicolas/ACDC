import urllib.request
import csv, json

urlMainFile = "https://www.data.gouv.fr/fr/organizations/sante-publique-france/datasets-resources.csv"
MainCsvFilePath = "datas/CSV/mainCsv.csv"
urllib.request.urlretrieve(urlMainFile, MainCsvFilePath)

# todo : manipuler le main file csv pour récupérer les urls des fichiers qui nous interesses et construire le dict urlList avec.

urlList = {
    "https://static.data.gouv.fr/resources/indicateurs-de-lactivite-epidemique-taux-dincidence-de-lepidemie-de-covid-19-par-metropole/20220307-191013/sg-metro-opendata-2022-03-07-19h10.csv" : "datas/CSV/sg-metro-opendata-2022-03-07-19h10.csv",
    "https://static.data.gouv.fr/resources/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/20220311-190146/vacsi-v-dep-2022-03-11-19h01.csv" : "datas/CSV/vacsi-v-dep-2022-03-11-19h01.csv",
    "https://static.data.gouv.fr/resources/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/20220311-190143/vacsi-v-fra-2022-03-11-19h01.csv" : "datas/CSV/vacsi-v-fra-2022-03-11-19h01.csv",
    "https://static.data.gouv.fr/resources/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/20220310-190135/covid-hosp-ad-age-2022-03-10-19h01.csv" : "datas/CSV/covid-hosp-ad-age-2022-03-10-19h01.csv",
    "https://static.data.gouv.fr/resources/donnees-de-vaccination-relatives-aux-professionnels-et-resident-en-ehpad-et-usld/20220311-190133/vacsi-prof-dep-2022-03-11-19h01.csv" : "datas/CSV/vacsi-prof-dep-2022-03-11-19h01.csv",
    "https://static.data.gouv.fr/resources/donnees-de-certification-electronique-des-deces-associes-au-covid-19-cepidc/20200518-185536/covid-cedc-quot.csv" : "datas/CSV/covid-cedc-quot.csv"
}

JsonDict = {
    "datas/CSV/sg-metro-opendata-2022-03-07-19h10.csv" : "datas/JSON/evolution_taux_incidence.json",
    "datas/CSV/vacsi-v-dep-2022-03-11-19h01.csv" : "datas/JSON/vaccin_cage_date.json",
    "datas/CSV/vacsi-v-fra-2022-03-11-19h01.csv" : "datas/JSON/vaccin_date.json",
    "datas/CSV/covid-hosp-ad-age-2022-03-10-19h01.csv" : "datas/JSON/hospitalisation_age.json",
    "datas/CSV/vacsi-prof-dep-2022-03-11-19h01.csv" : "datas/JSON/vaccin_pro_poucentage_dep.json",
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