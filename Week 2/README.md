## [Week 2] TTU ACM Weekly Software Development Club Short Course - Practical Python

This week, we'll be covering:
- How to use Python's built-in package manager Pip
- How to create and setup a virtual environment for a new project
- Client-server architecture
- Flask "Hello World!" and necessary objects/methods
- How to package Python projects into modules
- Git/GitHub

### Pip

#### What?
- Installs external Python dependencies from the Python Package Index ([PyPI](https://pypi.org/)) or repositories under software version control.

#### How? (Most of the time)
- Installation: `python -m pip install $PACKAGE_NAME`
- Uninstallation: `python -m pip uninstall $PACKAGE_NAME`
- Upgrade: `python -m pip install -U $PACKAGE_NAME`


### Pipenv

#### What?
- An open-source project for created fresh instances of Python for projects.

#### Why?
- Prevents collisions in globally installed package versions. 
- Gives you a fresh copy of Python to start with.
- Allows you to easily setup your project from a new machine (Pipfile).

#### How?
1. Install pipenv using pip
    - `python -m pip install pipenv`
2. Create a new virtual environment in the current directory.
    - `pipenv shell`
3. Install dependencies into the new Pipenv virtual environment
    - `pipenv install $PACKAGE_NAME`


### Pushing to a GitHub Repository
1. git config --global user.name "Your Name"
2. git config --global user.email "Your GitHub Email"
3. (Type your GitHub password into the prompt)
4. git init
5. git add .
6. git commit -m "Initial commit"
7. Create a new GitHub Repository on https://github.com
8. git remote add origin $REPOSITORY_URL
9. git push -u origin master
10. Refresh the repository! :eyes:
11. Make changes
12. git add .
13. git commit -m "I changed something!"
14. git push
15. Refresh the repository! :eyes:
