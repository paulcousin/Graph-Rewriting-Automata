This repository contains the source code of the website [paulcousin.github.io/graph-rewriting-automata](https://paulcousin.github.io/graph-rewriting-automata/).

It was made using [Jupyter Book](https://jupyterbook.org/) and uses of the code present in the following repositories :
* [paulcousin/gra-python](https://github.com/paulcousin/gra-python)
* [paulcousin/gra-mathematica](https://github.com/paulcousin/gra-mathematica)

### Building the Jupyter Book from a virtual environment
In your terminal, run the following commands.
```
python3 -m venv .venv	
```
```
source .venv/bin/activate
```
```
pip install -r requirements.txt
```
```
jupyter-book build .
```
To deactivate the virtual environment, simply run :
```
deactivate
```