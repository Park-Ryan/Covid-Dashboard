import * as React from 'react';
import Paper from '@material-ui/core/Paper';
import {
  ArgumentAxis,
  ValueAxis,
  Chart,
  BarSeries,
} from '@devexpress/dx-react-chart-material-ui';
import { modalClasses } from '@mui/material';
import { CountryData } from './data/CountryData';
  
  
export default function BarChart(props) {
  // const [mostDeaths, setMostDeaths] = React.useState(JSON.parse(props.mostDeaths));
// Sample data
console.log("from BarChart")
// console.log(mostDeaths);
const data = [
  { argument: 'Monday', value: 30 },
  { argument: 'Tuesday', value: 20 },
  { argument: 'Wednesday', value: 10 },
  { argument: 'Thursday', value: 50 },
  { argument: 'Friday', value: 60 },
];
// let data = []
// function createData(country, deaths){
//   return{
//     country, 
//     deaths,
//   }
// }
// for (let i= 0; i< mostDeaths.length; i++)
// {
//   data.push(createData(mostDeaths[i]["Country"], mostDeaths[i]["Types"]["Deaths"]));
// }
// console.log("from BarChart")

console.log(data)
return (
    <Paper>
    <Chart
      data={data}
    >
      <ArgumentAxis />
      <ValueAxis />
      {/* <BarSeries valueField="deaths" argumentField="country" /> */}
      <BarSeries valueField="value" argumentField="argument" />
    </Chart>
  </Paper>
);
}