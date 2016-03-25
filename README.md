# SysReview 

## Table of Contents
1. [Introduction](#intro) - Brief overview of the SysReview web application
2. [Motivation](#Motivation) - Why SysReview was developed
3. [Installation](#Installation) - How to set up SysReview on your local environment
4. [Populate SysReview](#Populate SysReview) - View the test data you can populate SysReview with.
    * [Populate instructions](#Populate instructions) - How to use the populate script
5. [Pubmed API Reference](#Pubmed API Reference) - Online PubMed API reference book
6. [Tests](#Tests) - Pre-written tests to execute on SysReview
7. [Contributors](#Contributors) - List of the project contributors
8. [Contributors GitHub Accounts](#Contributors GitHub Accounts) - Github details for each contributor
9. [License](#License) - MIT license 

<div id='intro'/>
# Introduction
##### SysReview - A systematic review web application

SysReview is a Systematic Review Application. The purpose of this application is to enable researchers to perform a systematic review using PubMed. A systematic review consists of a number of stages, which need to be recorded:  Query Construction, Abstract Pool Evaluation and then Document Pool Evaluation. The API to use is provided by E-Utilities which gives access to the [PubMed API.](http://www.ncbi.nlm.nih.gov/home/api.shtml "PubMed API")

<div id='Motivation'/>
## Motivation

This application was created for the University of Glasgow Computing Science Web App Development course. 

<div id='Installation'/>
## Installation

 1. Open a terminal and navigate to your workspace
 2. Clone repository by using command: ``` git clone https://github.com/Alistair401/10C.git ```
 3. We would recommend creating a virtual directory at this stage and ``` workon <virtualenv> ```
 4. Set up your virtual environment using the [requirements.txt](../master/requirements.txt) using the command: ```  pip install -r requirements.txt ```
 5. To deploy the app locally navigate to the SysReview directory then run the command: ```python manage.py runserver```
 6. To launch the SysReview application open a web browser and go to: ```http://localhost:8000/```

<div id='Populate SysReview'/>
## Populate SysReview

You can use the SysReview application and create your own data or you can populate the database with our test data by running the [populate_sysreview.py](../master/SysReview/populate_sysreview.py) file.

The population script will create 3 users with passwords set to their username, each user will have 3 reviews and 2 oof each users reviews will have querys created.

User | Review | Query
--- | --- | ---
<sub>**jill**</sub> | <sub>Interventions for preventing falls in older people living in the community*</sub> | <sub>(((((((((((((Interventions ) AND preventing ) AND accidental falls) OR accidental) AND older) AND persons) OR people) AND life) OR living) AND residence characteristics) OR residence) AND characteristics) OR residence characteristics) OR community </sub>
<sub>**jill**</sub> | <sub>Exercise for depression*</sub> | <sub>(((((exercise) AND depressive disorder) OR depressive) NOT disorder) OR depressive disorder) OR depression </sub>
<sub>**jill**</sub> | <sub>Early skin-to-skin contact for mothers and their healthy newborn infants*</sub> | <sub>**No Query Created**</sub>
<sub>**bob**</sub> | <sub>Neuraminidase inhibitors for preventing and treating influenza in healthy adults and children*</sub> | <sub>((((((((((((((((((neuraminidase) AND antagonists and inhibitors) OR antagonists) AND inhibitors) OR antagonists and inhibitors) OR inhibitors) AND preventing) AND therapy) OR treating) AND influenza) human OR) influenza AND) human OR) human influenza OR) influenza AND) healthy AND) adult AND) child OR) children </sub>
<sub>**bob**</sub> | <sub>Interventions for preventing obesity in children*</sub> | <sub>((((((((Interventions) AND preventing) AND pediatric obesity) OR pediatric) AND obesity) OR pediatric obesity) OR obesity) AND children) OR obesity in children</sub>
<sub>**bob**</sub> | <sub>Interprofessional education: effects on professional practice and health care outcomes*</sub> | <sub>**No Query Created**</sub>
<sub>**jen**</sub> | <sub>Interprofessional collaboration: effects of practice-based interventions on professional practice and healthcare outcomes*</sub> | <sub>((((((((((((((((((((Interprofessional) AND cooperative behavior) OR cooperative) AND behavior) OR cooperative behavior) OR collaboration) AND effects) AND practice based) AND interventions) AND professional practice) OR professional practice) OR professional) AND practice) OR professional practice) AND delivery of health care) OR delivery) AND health) AND care) OR delivery of health care) OR healthcare) AND outcomes </sub>
<sub>**jen**</sub> | <sub>Risk assessment tools for the prevention of pressure ulcers*</sub> | <sub>((((((((((((((((risk assessment) OR risk) AND assessment) OR risk assessment) AND tools) AND prevention and control) OR prevention) AND control) OR prevention and control) OR prevention) AND pressure ulcer) OR pressure) AND ulcer) OR pressure ulcer) OR pressure) AND ulcers) OR pressure ulcers </sub>
<sub>**jen**</sub> | <sub>Midwife-led continuity models versus other models of care for childbearing women*</sub> | <sub>**No Query Created**</sub>
<sub>_*Systematic example review titles taken from http://www.cochranelibrary.com/cochrane-database-of-systematic-reviews/ only the titles used no other aspect or content of reviews used_</sub>

<div id='Populate instructions'/>
##### Populate instructions

1. In your terminal navigate to the sysreview directory
2. Run the command: ``` python populate_sysreview.py ```
3. The script should run and display a message followed by ```Starting SysReview population script...```
4. The terminal will display the info in the table above and once finshed SysReview will be populated with the data objects described.

<div id='Pubmed API Reference'/>
## Pubmed API Reference

Further reading on the Pubmed API can found [here.](http://www.ncbi.nlm.nih.gov/books/NBK25500/ "Pubmed API")

<div id='Tests'/>
## Tests

Some basic tests included in tests.py are:
   
   **Model Tests**
   
   * ResearcherMethodTests
         *test_unicode_researcher_representation
   * ReviewMethodTests
   * QueryMethodTests
   * paperMethodTests
   * IndexViewTests
   * CreateReviewFormTests

<div id='Contributors'/>
## Contributors

   **Group 10c**
   
   * Alistair Miles
   * David Haughton
   * Iain Lafferty

<div id='Contributors GitHub Accounts'/>
## Contributors GitHub Accounts

  * **Alistair401:**   Alistair Miles 2125558m
  * **2080734h:**      David Haughton 2080734h
  * **Glasian:**       Iain Lafferty  9905142l

<div id='License'/>
## [License](../master/license)

The MIT License (MIT)

Copyright (c) 2016 SysReview WAD2 Project by group 10c (Alistair Miles, David Haughton and Iain Lafferty)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
