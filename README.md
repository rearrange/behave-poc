Python Behave and Selenium POC
==============

This is a proof-of-concepts in setting up Python Behave with Selenium as a test automation framework.

Installation:
----------
This project has been created with Python 3.9.4 on Windows, and browser used is Google Chrome v91.0.4472.77.
There's no need to install ChromeDriver separately since this project includes [WebDriverManager](https://pypi.org/project/webdriver-manager/) library for automatic web driver detection.
- Clone this repository: 
```
git clone https://github.com/rearrange/behave-poc.git
```
- Create virtual environment for this project: 
```
python -m venv venv
```
- Install the required library 
```
pip install -r requirements.txt
```

Running:
----------
To run all the test and features: 
```
behave
```

To run the test and have the output generated as HTML:
```
behave -f html -o report.html
```