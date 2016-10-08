del bbs.sqlite
rd /s/q migrations

python app.py db init
python app.py db migrate
python app.py db upgrade