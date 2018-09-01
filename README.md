# Git repository scanner

This is a shell script that checks git properties of given directories. It
answers questions like "Which subdirectory is a git repository?" or "Which
subdirectory is a git repository with an 'origin' remote?"

## Requirements

You need `pipenv` to install the necessary dependencies in an isolated way. How
to install it depends on how you can install Python packages on your system;
usually something like

```sh
pip install python
```

does the trick. For detailed information, see the [pipenv
documentation](https://github.com/pypa/pipenv).


## Usage

The current version uses `pipenv` for module support. Before running the tool
for the first time, use

```sh
pipenv install
```

Then, to run the program, call

```sh
pipenv run python gitscan.py
```

To show detailed usage instructions:

```sh
pipenv run python gitscan.py -h
```
