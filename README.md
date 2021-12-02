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

## Data

https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset

## Contributors

* Alan Chau
* Alex Kuang
* Kent Phan
* Ryan Park
* Kevin Ferrer

