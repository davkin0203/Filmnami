# Movie Site

## Setup 

This project uses [PipEnv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/) to manage dependencies.

Before running this project, install [PipEnv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/) and add it to your PATH. 

After Pip is installed, navigate to the root directory of this project (the directory containing this file), and run 
`pipenv install`, which will add all dependencies listed in the `Pipfile`.

Finally, set the selected python interpreter to the one created by Pipenv. If you are using vs code, open the command palette (`cmd + shift + p`) and select `Python: Select Interpreter`. You should select the `Pipenv` environment with the name `[ProjectName]-<someid>` (i.e. `MovieWebsite-2ffKhDdy`).

You should now be able to run the project using the run configuration `Python: Django`. If you want to run from the commandline, run `pipenv run python3 manage.py runserver`