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
import Badge from "@mui/material/Badge";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Link from "@mui/material/Link";
import MenuIcon from "@mui/icons-material/Menu";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import NotificationsIcon from "@mui/icons-material/Notifications";
import { mainListItems, secondaryListItems } from "./listItems";
import BarChart from "../BarChart";
import TopList from "../list"
import Chart from "./Chart";
import Deposits from "./Deposits";
import Orders from "./Orders";
import Table from "./Table";
import { MainInputFields } from "./InputFields";

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

const mdTheme = createTheme({ palette: { mode: "light" } });

function DashboardContent() {
	const [open, setOpen] = React.useState(true);
	const [payload, setPayload] = React.useState({});
	const [mainInputs, setMainInputs] = React.useState({});

	// whenever state updates, this will be called
	// that means if ANY of the hooks are changed, it will trigger
	// maybe use this to rerender components?
	React.useEffect(() => {
		console.log(mainInputs);
	});

	const toggleDrawer = () => {
		setOpen(!open);
	};

	const callback = (inputs) => {
		// do something with value in parent component, like save to state
		setMainInputs(inputs);

		// If you find that useState / setState are not updating immediately, the answer is simple: they're just queues. React useState and setState don't make changes directly to the state object; 
		// they create queues to optimize performance, which is why the changes don't update immediately.
		// console.log(inputs)

		const requestOptions = {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				inputs,
			}),
		};

		console.log("Query Endpoint Fetched");
		fetch("/api/QueryEndpoint", requestOptions)
			.then((response) => response.json())
			.then((data) => {
				// for testing
				// console.log(data);
				setPayload(data);
			});
	};


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
							Analytics
						</Typography>
						{/* <IconButton color="inherit">
							<Badge badgeContent={4} color="secondary">
								<NotificationsIcon />
							</Badge>
						</IconButton> */}
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
					{/* <List>{secondaryListItems}</List> */}
				</Drawer>
				<Box
					component="main"
					sx={{
						backgroundColor: (theme) =>
							theme.palette.mode === "light"
								? theme.palette.grey[100]
								: theme.palette.grey[100],
						flexGrow: 1,
						height: "100vh",
						overflow: "auto",
					}}
				>
					<Toolbar />
					<Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
						<Grid container spacing={3}>
							{/* Chart */}
							<Grid item xs={12} md={8} lg={12}>
								{/* <Paper
									sx={{
										p: 2,
										display: "flex",
										flexDirection: "column",
										height: 240,
									}}
								> */}
									{/* <Chart /> */}
									{/* <MainInputFields
										parentCallback={callback}
									/> */}
                            		<BarChart mostDeaths={[{'Country':"USA", 'Types':{'Deaths':1000}}]}>
                            		</BarChart>  
								{/* </Paper> */}
							</Grid>
							{/* Recent Deposits
							<Grid item xs={12} md={4} lg={3}>
								<Paper
									sx={{
										p: 2,
										display: "flex",
										flexDirection: "column",
										height: 240,
									}}
								>
									<Deposits />
								</Paper>
							</Grid> */}
							{/* Covid Table */}
							<Grid item xs={6}>
								{/* <Paper
									sx={{
										p: 2,
										display: "flex",
										flexDirection: "column",
									}}
								> */}
									{/* <Orders /> */}
									<Table data={payload}/>
								{/* </Paper> */}
							</Grid>
							<Grid item xs={6}>
								{/* <Paper
									sx={{
										p: 2,
										display: "flex",
										flexDirection: "column",
									}}
								> */}
									{/* <Orders /> */}
									{/* <Table data={payload}/>
									 */}
									<BarChart mostDeaths={[{'Country':"USA", 'Types':{'Deaths':1000}}]}>
                            		</BarChart>  
								{/* </Paper> */}
							</Grid>
							<Grid item xs ={6}>
								{/* <TopList
                                data = {[{'Country':'USA', 'Types':{'Recovered':1000}, 'State']}
                                type = {"Recovered"}
                                stat = {"percentages"}
                                shouldTruncate={0}
                            ></TopList> */}
							</Grid>
						</Grid>
						{/* <Copyright sx={{ pt: 4 }} /> */}
					</Container>
				</Box>
			</Box>
		</ThemeProvider>
	);
}

export default function Dashboard() {
	return <DashboardContent />;
}
