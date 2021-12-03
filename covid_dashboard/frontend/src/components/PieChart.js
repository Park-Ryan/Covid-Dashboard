import * as React from "react";
import Paper from "@mui/material/Paper";
import {
	Chart,
	PieSeries,
	Title,
	Legend
} from "@devexpress/dx-react-chart-material-ui";
import { Animation } from "@devexpress/dx-react-chart";


function createData(country, area) {
	return {
		country: country,
		area: area,
	};
}

export default function PieChart({ data }) {
	const [newData, setNewData] = React.useState([]);

	const UpdateChart = (data) => {
		let temp = [];
		for (let i = 0; i < data.length; i++) {
			temp.push(createData(data[i]["Country"], data[i]["Types"]["Deaths"]));
		}
		console.log(temp);
		setNewData(temp);
	};

	React.useEffect(() => {
		UpdateChart(data);
		console.log("In PieChart");
		console.log(newData);
	}, [data]);


	return (
		<Paper> 
			{console.log(newData)}
			<Chart data={newData}>
				<PieSeries valueField="area" argumentField="country" />
				<Title text="Top 5 Country Deaths" />
				<Animation />
				<Legend />
			</Chart>
		</Paper>
	);
}

// class PieChart extends React.PureComponent {
// 	constructor(props) {
// 		super(props);
// 	}

// 	render(props) {
// 		console.log(props.data);
// 		const { data: chartData } = props.data;

// 		return (
// 			<Paper>
// 				<Chart data={chartData}>
// 					<PieSeries valueField="area" argumentField="country" />
// 					<Title text="Top 5 Country Deaths" />
// 					<Animation />
// 				</Chart>
// 			</Paper>
// 		);
// 	}
// }
