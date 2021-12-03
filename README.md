# Covid Dashboard

## Summary

Covid Dashboard is a web application built to analyze a COVID-19 dataset. The goal is to help users understand statistical information about COVID-19 globally. 

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

1. Open two terminal tabs, one for frontend and one for backend
2. Backend
  * cd ./covid_dashboard
  * python3 manage.py runserver
3. Frontend
  * cd./covid_dashboard/frontend
  * npm run dev 
4. Unit Testing
  * ./covid_dashboard
  * python manage.py test

## Navigation
1. After running usage command, a homepage will display
2. Look to the left side of the page where you will see 3 tabs: Dashboard, Analytics, and Old Homepage
3. Click on Old Homepage to be brought to new page
  * The new polish feature/improvement was to implement the new Homepage, but there was not even time to fully 
    get it working and flesh out
4. Play around with the filters

## Data

https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset

## Contributors

* Alan Chau
* Alex Kuang
* Kent Phan
* Ryan Park
* Kevin Ferrer

## Final Review
1. There is unit testing in ./covid_dashboard/api/tests.py
  * The unit test uses Django-Python framework unit testing
2. Continuous Integration
