deps:
	pip install -r requirements.txt

run:
	gunicorn app:app

snakeviz:
	snakeviz latest.pstats
