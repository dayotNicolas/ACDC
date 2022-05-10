#bash
pip install -r requirements.txt

cd project_ACDC/
mkdir "datas"

cd datas/
mkdir "CSV"
mkdir "JSON"

cd ../
python Retriever.py

