# SysReview 


## SysReview - A systematic review web application

SysReview is a Systematic Review Application. The purpose of this application is to enable researchers to perform a systematic review using PubMed. A systematic review consists of a number of stages, which need to be recorded:  Query Construction, Abstract Pool Evaluation and then Document Pool Evaluation. The API to use is provided by E-Utilities which gives access to the [PubMed API.](http://www.ncbi.nlm.nih.gov/home/api.shtml "PubMed API")

## Motivation

This application was created for the University of Glasgow Computing Science Web App Development course. 

## Installation

  * **1.** Create new directory in your workspace.

  * **2.** Open a terminal and navigate to new directory

  * **3.** Clone repository by using command 
   
        git clone https://github.com/Alistair401/10C.git

  * **4.** We would recommend creating a virtual directory at this stage and workon that environment. 

  * **5.** Set up your virtual environment using the [requirements.txt](../master/requirements.txt) using the command 
        
        pip install -r requirements.txt

  * **6.** To deploy the app locally navigate to the SysReview directory then run the command 
   
        python manage.py runserver

  * **7.** To lanuch the SysReview application open a web browser and go to
   
        http://localhost:8000/

## Pubmed API Reference

Further reading on the Pubmed API can found [here.](http://www.ncbi.nlm.nih.gov/books/NBK25500/ "Pubmed API")

## Tests

**STILL TO DO**

## Contributors

   **Group 10c**
   
   * Alistair Miles
   * David Haughton
   * Iain Lafferty
   
## GitHub Accounts

  * **Alistair401:**   Alistair Miles 2125558m
  * **2080734h:**      David Haughton 2080734h
  * **Glasian:**       Iain Lafferty  9905142l

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
