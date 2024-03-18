run:
	uvicorn app.application:app --host="127.0.0.1" --port=5000 --log-level=debug --reload

install:
	pip install -r requirements.txt

upgrade:
	pip-upgrade requirements.txt

init:
	$(MAKE) install
	pip install httpx
	$(MAKE) test
	
test:
	pytest ./app/tests.py
