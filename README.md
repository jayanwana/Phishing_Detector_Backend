<div id="top"></div>

<div align="center">
 
  <h3 align="center">Backend For Phishing Email Detector</h3>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[Phishing Email Detector](https://phishing-detector-backend-7sgvu.ondigitalocean.app/)

This is a simple backend API meant to expose a pre-trained Catboost model, 
allowing it to accept emails and make predictions on if the Email is a 
phishing email or not based on the textual features of the email. 
The Catboost model was trained with a sample dataset comprising 9,000 
phishing and non-phishing emails, with and accuracy of 98.83% on the test dataset.
The model was tuned using nested cross-validation techniques and based of the results of this, 
the hyper-parameters were selected.  
The front-end of this application is a simple Chrome Browser extension that can be found [Here]()


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This application was built with the following libraries and frameworks

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
* [Gunicorn](https://gunicorn.org/)
* [Catboost.ai](https://catboost.ai/en/docs/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This app is currently hosted on the Digital Ocean App Platform 
[Here](https://phishing-detector-backend-7sgvu.ondigitalocean.app/). 
However, the repository can be easily cloned and run locally with the following steps.


### Prerequisites

* Python 3
  ```sh
  python --version
  ```
* Pipenv 
  ```sh
  pip install pipenv
  ```
* git

### Installation

All project dependencies are listed in the Pipfile of the project

1. Clone the repo
   ```sh
   git clone https://github.com/jayanwana/Phishing_Detector_Backend.git
   ```
2. Move into the local repository directory that was just cloned
   ```sh
   cd Phishing_Detector_Backend
   ```
3. Install python packages
   ```sh
   pipenv install
   ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
After installation, run the application with  
    ```
    python app.py
    ```
or 
    ```
    python3 app.py
    ```
or ```
    flask run
    ```  
_For more examples, please refer to the [Documentation](https://flask.palletsprojects.com/en/2.0.x/)_

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

John Anwana - john2.anwana@live.uwe.ac.uk

Project Link: [https://github.com/jayanwana/Phishing_Detector_Backend.git](https://github.com/jayanwana/Phishing_Detector_Backend.git)

<p align="right">(<a href="#top">back to top</a>)</p>

</div>
