FastAPI + SQLAlchemy + Dependency Injector Example
==================================================

   - make init
   - make run

Build the Docker image:
   - docker-compose build

Run the docker-compose environment:
   - docker-compose up

##### Test
   docker-compose run --rm webapp py.test webapp/tests.py --cov=webapp


<i> This is a `FastAPI <https://fastapi.tiangolo.com/>`
`SQLAlchemy <https://www.sqlalchemy.org/>`
`Dependency Injector <https://python-dependency-injector.ets-labs.org/>`_ example application. </i>