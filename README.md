# Covid Dashboard

## Contributors

* [Alan Chau](https://github.com/achau6) 
* [Alex Kuang](https://github.com/Alexk21323) 
* [Kent Phan](https://github.com/Moltenfuzzy)
* [Ryan Park](https://github.com/Park-Ryan) 
* [Kevin Ferrer](https://github.com/kferr0012)

## Summary

Covid Dashboard is a web application built to analyze a COVID-19 dataset. The goal is to help users understand statistical information about COVID-19 globally. 
<br /> <br />

![image](https://user-images.githubusercontent.com/46156230/144631184-d1cf3bf5-3532-45a3-955b-d0ebc0b61557.png)
![image](https://user-images.githubusercontent.com/46156230/144631247-b714d17f-8008-42c3-875f-4449bf6c827b.png)

## Features

- Search cases by type (Confirmed, Death, Recovered)
- Update and modify records
- Backup records to a CSV
- Data visualization
  - Statistics to show standard deviation, percentages and averages
  - Bar chart for country with most deaths

## Architecture Diagram

![GUI Design - Page 4](https://user-images.githubusercontent.com/46156230/144409514-ba1ae6f8-2add-4327-863b-a9aacf6a3744.png)

## Setup Instructions

1. Initialize Virtual Environment (optional)
2. Clone the github repository
3. Run npm install in the ./covid_dashboard/frontend directory or install manually
* pip install django, djangorestframework
* npm i react react-dom --save-dev
* npm install @material-ui/core
* npm i webpack webpack-cli --save-dev
* npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
* npm install @babel/plugin-proposal-class-properties
* npm install react-router-dom
* npm install @material-ui/icons

## Usage

1. Open three terminal tabs, one for frontend, one for backend, and one for testing
2. Backend
  * cd ./covid_dashboard
  * python3 manage.py runserver
3. Frontend
  * cd./covid_dashboard/frontend
  * npm run dev 
4. Unit Testing
  * cd ./covid_dashboard
  * python manage.py test

## Navigation
1. After running usage command, a dashboard will display
2. Look to the left side of the page where you will see 2 tabs: Dashboard and Analytics
3. Play around with the filters
4. Click the analytics tab to see graphs and statistical values

Note: Old Homepage UI is available, but not functional. 

## Data

https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset

## Final Review
1. There is unit testing in ./covid_dashboard/api/tests.py
  * The unit test uses Django-Python framework unit testing
2. Continuous Integration is available on PR to main
