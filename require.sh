#bash
chmod 766 requirements.txt
pip install -r requirements.txt

cd project_ACDC/
mkdir "datas"

cd datas/
mkdir "CSV"
mkdir "JSON"

cd ../
chmod 766 Retriever.py
python Retriever.py

