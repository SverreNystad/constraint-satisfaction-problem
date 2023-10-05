# Constraint Satisfaction Problems

<div align="center">

![Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/USERNAME/REPONAME/build_and_test.yml)
[![codecov.io](https://codecov.io/github/USERNAME/REPONAME/coverage.svg?branch=main)](https://codecov.io/github/USERNAME/REPONAME?branch=main)
![GPT-dungeon-master top language](https://img.shields.io/github/languages/top/USERNAME/REPONAME)
![GitHub language count](https://img.shields.io/github/languages/count/USERNAME/REPONAME)
[![Project Version](https://img.shields.io/badge/version-0.0.1-blue)](https://img.shields.io/badge/version-0.0.1-blue)

</div>

<details>
  <summary> <b> Table of Contents </b> </summary>
  <ol>
    <li>
    <a href="#constraint-satisfaction-problems"> Constraint Satisfaction Problems </a>
    </li>
    <li>
      <a href="#Introduction">Introduction</a>
    </li>
    </li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Installation">Installation</a>
      <ul>
        <li><a href="#Prerequisites">Prerequisites</a></li>
        <li><a href="#Setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#Tests">Tests</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Introduction
This is the sudoku solver. It uses CSP to solve the sudoku. The creators of this application have both never solved a sudoku, but with the power of CSP, we can solve any sudoku. Enjoy the application and have fun solving Sudokus.

The application is built with Flask and pure javascript. The CSP is implemented in python. The CSP is a backtracking algorithm. To learn more about CSP look here [CSP](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem) and our [Assignment](docs/Assignment%203%20Constraint%20Satisfaction%20Problems.pdf).

## Picture of the application:
![frontend](docs\images\application.png)


## Usage

```bash
flask run
```

## Installation
To install the PROJECT NAME, one needs to have all the prerequisites installed and set up, and follow the setup guild. The following sections will guide you through the process.
### Prerequisites
- Python 3.9 or higher
  

### Setup
1. Clone the repository
```bash
git clone https://github.com/SverreNystad/constraint-satisfaction-problem.git
cd constraint-satisfaction-problem
```
2. Create a virtual environment
    #### On Windows:
    ```bash
    python3 -m venv venv
    source venv/Scripts/activate
    ```
    #### On macOS and Linux: 
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages
```bash
pip install -r requirements.txt
```
## Tests
To run all the tests, run the following command in the root directory of the project:
```bash
pytest --cov
coverage html # To generate a coverage report
```
If you do not want to run api tests, run the following command instead:
```bash
pytest -m "not apitest" --cov
```

### License
Licensed under the [MIT License](LICENSE). Because this is a template repository, you need to change the license if you want to use it for your own project.

