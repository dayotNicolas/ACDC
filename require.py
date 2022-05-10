import os

os.chdir('./project_ACDC')

pathdatas = './datas'
pathdatascsv = './datas/CSV'
pathdatasjson = './datas/JSON'
# Check whether the specified path exists or not

isExist = os.path.exists(pathdatas)
isExist2 = os.path.exists(pathdatascsv)
isExist3 = os.path.exists(pathdatasjson)

if not isExist:
    os.makedirs(pathdatas)

if not isExist2:
    os.makedirs(pathdatascsv)

if not isExist3:
    os.makedirs(pathdatasjson)

os.system('pip install -r ../requirements.txt')
os.system('python ./Retriever.py')



