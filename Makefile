run:
	uvicorn main:app --host="127.0.0.1" --port=5000 --log-level=debug --reload

install:
	pip install -r requirements.txt

upgrade:
	pip-upgrade requirements.txt

init:
	cp .env.example .env
	$(MAKE) install
	$(MAKE) run

test:
	pytest
