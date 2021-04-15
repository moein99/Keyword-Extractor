# KeyWord Extractor

## Installation
Clone the repo:
```
git clone https://github.com/moein99/Keyword-Extractor.git
cd keyword-extractor
```
Make a virtual environment (your python version MUST be 3.8+):
```bash
virtualenv -p python3.8 .venv
```
Activate it:
```
source .venv/bin/activate
```
Install requirements:
```
pip install -r requirements.txt
```
One of the dependencies (perke) needs some resource files that are already provided in this repo. Copy them:
```
mkdir $(python get_perke_resources_dir.py)
cp -r resources/* $(python get_perke_resources_dir.py)
```
Run migrations:
```
python manage.py migrate
```
Run server:
```
python manage.py runserver
```
## API
```
end-point: keyword_extractor/api/extract
data:
{
    text: put a document in this field
    method: one of the following algorithms -> text, position, multipartite, topic, single
    num_of_keywords: top n keywords
}
```
