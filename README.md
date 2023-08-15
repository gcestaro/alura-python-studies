# Demo project with some Python studies

## Install requirements
- Run: ```pip3 install -r requirements.txt```

## Unit tests
- Run tests locally: ```python3 -m pytest -v```
- Run tests with coverage: ```python3 -m pytest --cov=unit_tests/tests```
  - With ```source``` defined in ```.coveragerc```, just run: ```python3 -m pytest --cov```
  - With ```addopts``` defined in ```pytest.ini```, just run: ```python3 -m pytest```
- Check coverage report - missing terms: ```python3 -m pytest --cov=unit_tests/tests --cov-report term-missing```
- Check coverage report - html: ```python3 -m pytest --cov=unit_tests/main --cov-report html```
- Check coverage report - xml: ```python3 -m pytest --junitxml report.xml```