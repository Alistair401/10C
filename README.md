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

 1. Create new Directory in your workspace
 2. Open a terminal and navigate to new directory
 3. Clone repository by using command: ``` git clone https://github.com/Alistair401/10C.git ```
 4. We would recommend creating a virtual directory at this stage and ``` workon <virtualenv> ```
 5. Set up your virtual environment using the [requirements.txt](../master/requirements.txt) using the command: ```  pip install -r requirements.txt ```
 6. To deploy the app locally navigate to the SysReview directory then run the command: ```python manage.py runserver```
 7. To launch the SysReview application open a web browser and go to: ```http://localhost:8000/```

<div id='Populate SysReview'/>
## Populate SysReview

You can use the SysReview application and create your own data or you can populate the database with our test data by running the [populate_sysreview.py](../master/SysReview/populate_sysreview.py) file.

The population script will create 3 users with passwords set to their username, each user will have 3 reviews and 2 oof each users reviews will have querys created.

User | Review | Query
--- | --- | ---
jill | Interventions for preventing falls in older people living in the community | Interventions[All Fields] AND preventing[All Fields] AND (accidental falls[MeSH Terms] OR (accidental[All Fields] AND falls[All Fields]) OR accidental falls[All Fields] OR falls[All Fields]) AND older[All Fields] AND (persons[MeSH Terms] OR persons[All Fields] OR people[All Fields]) AND (life[MeSH Terms] OR life[All Fields] OR living[All Fields]) AND (residence characteristics[MeSH Terms] OR (residence[All Fields] AND characteristics[All Fields]) OR residence characteristics[All Fields] OR community[All Fields])
jill | Exercise for depression | (exercise[MeSH Terms] OR exercise[All Fields]) AND (depressive disorder[MeSH Terms] OR (depressive[All Fields] AND disorder[All Fields]) OR depressive disorder[All Fields] OR depression[All Fields] OR depression[MeSH Terms])
jill | Early skin-to-skin contact for mothers and their healthy newborn infants | **No Query Created**
bob | Neuraminidase inhibitors for preventing and treating influenza in healthy adults and children | (neuraminidase[MeSH Terms] OR neuraminidase[All Fields]) AND (antagonists and inhibitors[Subheading] OR (antagonists[All Fields] AND inhibitors[All Fields]) OR antagonists and inhibitors[All Fields] OR inhibitors[All Fields]) AND preventing[All Fields] AND (therapy[Subheading] OR therapy[All Fields] OR treating[All Fields]) AND (influenza, human[MeSH Terms] OR (influenza[All Fields] AND human[All Fields]) OR human influenza[All Fields] OR influenza[All Fields]) AND healthy[All Fields] AND (adult[MeSH Terms] OR adult[All Fields] OR adults[All Fields]) AND (child[MeSH Terms] OR child[All Fields] OR children[All Fields])
bob | Interventions for preventing obesity in children | Interventions[All Fields] AND preventing[All Fields] AND (pediatric obesity[MeSH Terms] OR (pediatric[All Fields] AND obesity[All Fields]) OR pediatric obesity[All Fields] OR (obesity[All Fields] AND children[All Fields]) OR obesity in children[All Fields])
bob | Interprofessional education: effects on professional practice and health care outcomes | **No Query Created**
jen | Interprofessional collaboration: effects of practice-based interventions on professional practice and healthcare outcomes | (Interprofessional[All Fields] AND (cooperative behavior[MeSH Terms] OR (cooperative[All Fields] AND behavior[All Fields]) OR cooperative behavior[All Fields] OR collaboration[All Fields])) AND (effects[All Fields] AND practice-based[All Fields] AND interventions[All Fields] AND (professional practice[MeSH Terms] OR (professional[All Fields] AND practice[All Fields]) OR professional practice[All Fields]) AND (delivery of health care[MeSH Terms] OR (delivery[All Fields] AND health[All Fields] AND care[All Fields]) OR delivery of health care[All Fields] OR healthcare[All Fields]) AND outcomes[All Fields])
jen | Risk assessment tools for the prevention of pressure ulcers | (risk assessment[MeSH Terms] OR (risk[All Fields] AND assessment[All Fields]) OR risk assessment[All Fields]) AND tools[All Fields] AND (prevention and control[Subheading] OR (prevention[All Fields] AND control[All Fields]) OR prevention and control[All Fields] OR prevention[All Fields]) AND (pressure ulcer[MeSH Terms] OR (pressure[All Fields] AND ulcer[All Fields]) OR pressure ulcer[All Fields] OR (pressure[All Fields] AND ulcers[All Fields]) OR pressure ulcers[All Fields])
jen | Midwife-led continuity models versus other models of care for childbearing women | **No Query Created**

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

**STILL TO DO**

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
