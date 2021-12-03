import * as React from "react";
import { styled, createTheme, ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import MuiDrawer from "@mui/material/Drawer";
import Box from "@mui/material/Box";
import MuiAppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import List from "@mui/material/List";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import MenuIcon from "@mui/icons-material/Menu";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import { mainListItems } from "../dashboard/listItems";
import PieChart from "../PieChart";
import BarChart from "../BarChart";
import SplineChart from "../SplineChart";
import RotatedBarChart from "../RotatedBarChart";
import StreamGraph from "../StreamGraph";
import LineChart from "../LineChart";
import AnalyticsList from "../AnalyticsList";
import Statistic from "../Statistics";
import { SearchInputsContext } from "../dashboard/SearchInputsContext";

const drawerWidth = 220;

const AppBar = styled(MuiAppBar, {
	shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
	zIndex: theme.zIndex.drawer + 1,
	transition: theme.transitions.create(["width", "margin"], {
		easing: theme.transitions.easing.sharp,
		duration: theme.transitions.duration.leavingScreen,
	}),
	...(open && {
		marginLeft: drawerWidth,
		width: `calc(100% - ${drawerWidth}px)`,
		transition: theme.transitions.create(["width", "margin"], {
			easing: theme.transitions.easing.sharp,
			duration: theme.transitions.duration.enteringScreen,
		}),
	}),
}));

const Drawer = styled(MuiDrawer, {
	shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
	"& .MuiDrawer-paper": {
		position: "relative",
		whiteSpace: "nowrap",
		width: drawerWidth,
		transition: theme.transitions.create("width", {
			easing: theme.transitions.easing.sharp,
			duration: theme.transitions.duration.enteringScreen,
		}),
		boxSizing: "border-box",
		...(!open && {
			overflowX: "hidden",
			transition: theme.transitions.create("width", {
				easing: theme.transitions.easing.sharp,
				duration: theme.transitions.duration.leavingScreen,
			}),
			width: theme.spacing(7),
			[theme.breakpoints.up("sm")]: {
				width: theme.spacing(9),
			},
		}),
	},
}));

const mdTheme = createTheme({ palette: { mode: "dark" } });

export default function AnalyticsContent(props) {
	const [open, setOpen] = React.useState(true);
	const [payload, setPayload] = React.useState("");
	const [confirmedPayload, setConfirmedPayload] = React.useState("");
    const [stateAnalyticsPayload, setstateAnalyticsPaylod] = React.useState("");
	const [inputsValues, setInputValues] = React.useState({});
	const {searchInputsValues, setSearchInputsValues} = React.useContext(SearchInputsContext)

	const inputs = {};
	const confirmedInput = {};

	// const msg = React.useContext(userInputContext)
	// timer for the rerender of chart
	// setInterval(function(){
	// 	CallAPI(inputs, "CountryTopDeaths");
	// }, 10000);
	// if (payload === "") {
	// 	CallAPI(inputs, "CountryTopDeaths");
	// }

	// CallAPI(inputs, "CountryTopDeaths");
	// whenever state updates, this will be called
	// that means if ANY of the hooks are changed, it will trigger
	// maybe use this to rerender components?
	React.useEffect(() => {
		console.log("Calling useEffect");
		// rerender when new data in payload
		// const inputs = {}
		CallAPI(inputs, "CountryTopDeaths", setPayload);
		CallAPI(confirmedInput, "CountryTopConfirmed",setConfirmedPayload);
		
		CallAPI(searchInputsValues, "AnalyticsEndpoint",setstateAnalyticsPaylod);
		
		console.log("Printing analytics");
		console.log(stateAnalyticsPayload);
		// console.log(payload);
	}, [searchInputsValues]);
	// },[]);

	const toggleDrawer = () => {
		setOpen(!open);
	};
	console.log("From analytics");
	console.log(props.inputValues);

	const dummy = [   
	{
        "Washington": {
            "type": "Confirmed",
            "start-date": "01/22/2020",
            "end-date": "05/29/2021",
            "std": 144822.76730905243,
            "averages": 162055.16483516485,
            "percentages": 1.310744548217932
        }
    },
    {
        "Washington": {
            "type": "Confirmed",
            "start-date": "01/22/2020",
            "end-date": "05/29/2021",
            "std": 1757.440701538113,
            "averages": 2674.0505494505496,
            "percentages": 0.9700390034763238
        }
    },
    {
        "Washington": {
            "type": "Confirmed",
            "start-date": "01/22/2020",
            "end-date": "05/29/2021",
            "std": 0.13142783637561364,
            "averages": 0.017582417582417582,
            "percentages": 0.0
        }
    }
	];

	return (
		<ThemeProvider theme={mdTheme}>
			<Box sx={{ display: "flex" }}>
				<CssBaseline />
				<AppBar position="absolute" open={open}>
					<Toolbar
						sx={{
							pr: "24px", // keep right padding when drawer closed
						}}
					>
						<IconButton
							edge="start"
							color="inherit"
							aria-label="open drawer"
							onClick={toggleDrawer}
							sx={{
								marginRight: "36px",
								...(open && { display: "none" }),
							}}
						>
							<MenuIcon />
						</IconButton>
						<Typography
							component="h1"
							variant="h6"
							color="inherit"
							noWrap
							sx={{ flexGrow: 1 }}
						>
							Covid Dashboard
						</Typography>
					</Toolbar>
				</AppBar>
				<Drawer variant="permanent" open={open}>
					<Toolbar
						sx={{
							display: "flex",
							alignItems: "center",
							justifyContent: "flex-end",
							px: [1],
						}}
					>
						<IconButton onClick={toggleDrawer}>
							<ChevronLeftIcon />
						</IconButton>
					</Toolbar>
					<Divider />
					<List>{mainListItems}</List>
					<Divider />
				</Drawer>
				<Box
					component="main"
					sx={{
						backgroundColor: (theme) =>
							theme.palette.mode === "light"
								? theme.palette.grey[100]
								: theme.palette.grey[900],
						flexGrow: 1,
						height: "100vh",
						overflow: "auto",
					}}
				>
					<Toolbar />
					<Container maxWidth="100" sx={{ mt: 4, mb: 4 }}>
						<Grid container spacing={3}>
							<Grid item xs={12} md={4} lg={4}>
								{/* Call which endpoint? Top 5 country deaths*/}
								<PieChart data={payload} /> 
							</Grid>  
							<Grid item xs={12} md={4} lg={4}>
								<BarChart data={payload} type = {"Deaths"}/>
							</Grid> 
							<Grid item xs={12} md={4} lg={4}>
								<BarChart data={confirmedPayload} type = {"Confirmed"}/>
							</Grid>  
							<Grid  item xs={12} md={4} lg={4}>
									<AnalyticsList 
										data={stateAnalyticsPayload}
										type="Confirmed"
									/>
							</Grid>
							<Grid  item xs={12} md={4} lg={4}>
									<AnalyticsList 
										data={stateAnalyticsPayload}
										type="Deaths"
									/>
							</Grid>
							<Grid  item xs={12} md={4} lg={4}>
									<AnalyticsList 
										data={stateAnalyticsPayload}
										type="Recovered"
									/>
							</Grid>
							{/* <Grid item xs={12} md={4} lg={4}>
								<SplineChart />
							</Grid>
							<Grid item xs={12} md={4} lg={4}>
								<RotatedBarChart />
							</Grid>
							<Grid item xs={12} md={4} lg={4}>
								<StreamGraph />
							</Grid>
							<Grid item xs={12} md={4} lg={4}>
								<BarChart />
							</Grid> */}
						</Grid>
					</Container>
				</Box>
			</Box>
		</ThemeProvider>
	);

	function CallAPI(inputs, endPoint, setterHook) {
		console.log("CallAPI called");
		// if (isEmpty(inputs)) {
		// 	return;
		// }
		// Checks if empty
		// Object.values(inputs).forEach((val) => {
		// 	console.log(val);
		// 	if (val === "") return;
		// });
		const requestOptions = {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				inputs,
			}),
		};

		console.log(`${endPoint} Fetched`);
		fetch(`/api/${endPoint}`, requestOptions)
			.then((response) => response.json())
			.then((data) => {
				// for testing
				// console.log(data);
				// if the data is empty we do not setPayload bc we can only do it once per render!
				if (!isEmpty(data)) {
					console.log(!isEmpty(data));
					setterHook(data);
				}
			});
		
	}
}


function isEmpty(obj) {
	return Object.keys(obj).length === 0;
}
