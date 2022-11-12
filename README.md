# PROJECT INSTALLATION

* Install [pyenv](https://github.com/pyenv/pyenv)
* Create virtual env for project
```
pyenv install 3.10.4
pyenv virtualenv selenium 3.10.4
pyenv local selenium
pyenv activate selenium
```
* install python deps
```
pip install requirements/requirements.txt
```
* Install chrome webdriver

See [documentation](https://selenium-python.readthedocs.io/installation.html#drivers).
It's better to use your package manager for it (pacman, apt-get and etc)
* To start test
```
pytest
```

*Note:*
* To start certain test
```
pytest -k <test name>
```
