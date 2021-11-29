import * as React from "react";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import ListSubheader from "@mui/material/ListSubheader";
import DashboardIcon from "@mui/icons-material/Dashboard";
import BarChartIcon from "@mui/icons-material/BarChart";
import CancelIcon from '@mui/icons-material/Cancel';
import { Link } from "react-router-dom";

export const mainListItems = (
	<div>
		{/* passing link to mui component bc its the better */}
		<ListItem component={Link} to={'/'} button>
			<ListItemIcon>
				<DashboardIcon />
			</ListItemIcon>
			<ListItemText primary="Dashboard" />
		</ListItem>
		<ListItem component={Link} to={'/Analytics'} button>
			<ListItemIcon>
				<BarChartIcon />
			</ListItemIcon>
			<ListItemText primary="Analytics" />
		</ListItem>
		<ListItem component={Link} to={'/HomePage'} button>
			<ListItemIcon>
				<CancelIcon />
			</ListItemIcon>
			<ListItemText primary="Old Homepage" />
		</ListItem>
	</div>
);
