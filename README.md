## Introduction

Sample python app to learn the concepts of type hinting and more specifically setting up a cicd pipeline with pre commit so that any bugs are identified during pre commit itself.

### Project structure

root/
│
├── src/
│   └── app/
│       ├── __init__.py
│       ├── calculator.py
│       └── users.py
│
├── tests/
│   ├── test_calculator.py
│   └── test_users.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements-dev.txt
└── README.md