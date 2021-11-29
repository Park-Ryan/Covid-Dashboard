// import * as React from 'react';
// import Paper from '@mui/material/Paper';
// import {
//   Chart,
//   BarSeries,
//   Title,
//   ArgumentAxis,
//   ValueAxis,
// } from '@devexpress/dx-react-chart-material-ui';
// import { Animation } from '@devexpress/dx-react-chart';

// const data = [
//   { year: '1950', population: 2.525 },
//   { year: '1960', population: 3.018 },
//   { year: '1970', population: 3.682 },
//   { year: '1980', population: 4.440 },
//   { year: '1990', population: 5.310 },
//   { year: '2000', population: 6.127 },
//   { year: '2010', population: 6.930 },
// ];

// export default class Demo extends React.PureComponent {
//   constructor(props) {
//     super(props);

//     this.state = {
//       data,
//     };
//   }

//   render() {
//     const { data: chartData } = this.state;

//     return (
//       <Paper>
//         <Chart
//           data={chartData}
//         >
//           <ArgumentAxis />
//           <ValueAxis max={7} />

//           <BarSeries
//             valueField="population"
//             argumentField="year"
//           />
//           <Title text="World population" />
//           <Animation />
//         </Chart>
//       </Paper>
//     );
//   }
// }

import * as React from "react";
import Paper from "@mui/material/Paper";
import {
	ArgumentAxis,
	ValueAxis,
	Chart,
	BarSeries,
} from "@devexpress/dx-react-chart-material-ui";
import { modalClasses } from "@mui/material";
import { CountryData } from "./data/CountryData";

function createData(country, deaths) {
	return {
		country: country,
		deaths: deaths,
	};
}

export default function BarChart({data}) {
	const [newData, setNewData] = React.useState([]);

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
		UpdateChart(data);
	}, [data]);

	console.log(data);
	return (
		<Paper>
			<Chart data={newData}>
				<ArgumentAxis />
				<ValueAxis />
				<BarSeries valueField="deaths" argumentField="country" />
			</Chart>
		</Paper>
	);
}
