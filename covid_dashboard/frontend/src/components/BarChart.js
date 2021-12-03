// import * as React from 'react';
// import Paper from '@material-ui/core/Paper';
// import {
//   ArgumentAxis,
//   ValueAxis,
//   Chart,
//   BarSeries,
//   Title
// } from '@devexpress/dx-react-chart-material-ui';
// import { modalClasses } from '@mui/material';
// import { CountryData } from './props.data/CountryData';
  
  
// export default function BarChart(props) {
// const [mostDeaths, setMostDeaths] = React.useState(JSON.parse(props.mostDeaths));
// const [type, setType] = React.useState(props.type);
// // Sample props.data
// console.log("from BarChart")
// // console.log(mostDeaths);
// // const props.data = [
// //   { argument: 'Monday', value: 30 },
// //   { argument: 'Tuesday', value: 20 },
// //   { argument: 'Wednesday', value: 10 },
// //   { argument: 'Thursday', value: 50 },
// //   { argument: 'Friday', value: 60 },
// // ];
// let props.data = []
// function createData(country, deaths){
//   return{
//     country, 
//     deaths,
//   }
// }
// for (let i= 0; i< mostDeaths.length; i++)
// {
//   props.data.push(createData(mostDeaths[i]["Country"], mostDeaths[i]["Types"]["Deaths"]));
// }
// console.log("from BarChart")

// console.log(props.data)
// return (
//     <Paper>
    
//     <Chart
//       props.data={props.data}
//     >
//       <ArgumentAxis />
//       <ValueAxis />
//       <BarSeries valueField="deaths" argumentField="country" />
//       {/* <BarSeries valueField="value" argumentField="argument" /> */}
//       <Title text={`Top 5 Country ${type}`}/>
//     </Chart>
//   </Paper>
// );
// }


import * as React from "react";
import Paper from "@mui/material/Paper";
import {
	ArgumentAxis,
	ValueAxis,
	Chart,
	BarSeries,
  Title
} from "@devexpress/dx-react-chart-material-ui";
import { modalClasses } from "@mui/material";
import { CountryData } from "./data/CountryData";

function createData(country, deaths) {
	return {
		country: country,
		deaths: deaths,
	};
}

export default function BarChart(props) {
	const [newData, setNewData] = React.useState([]);
  const [type, setType] = React.useState(props.type);


	const UpdateChart = (data) => {
		let temp = [];
		for (let i = 0; i < data.length; i++) {
			temp.push(
				createData(data[i]["Country"], data[i]["Types"]["Deaths"])
			);
		}
		console.log(temp);
		setNewData(temp);
	};

	React.useEffect(() => {
		UpdateChart(props.data);
	}, [props.data]);

	console.log(props.data);
	return (
		<Paper>
			<Chart data={newData}>
				<ArgumentAxis />
				<ValueAxis />
				<BarSeries valueField="deaths" argumentField="country" />
        <Title text={`Top 5 Country ${type}`}/>
			</Chart>
		</Paper>
	);
}



