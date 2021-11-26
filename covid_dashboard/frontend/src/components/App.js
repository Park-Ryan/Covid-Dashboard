import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import HomePage from "./pages/HomePage";
import TestPage from "./pages/TestPage";
import Dashboard from "./dashboard/Dashboard";

export default class App extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (
			// <div className="initLayout">
            <div>
				<Router>
					<Switch>
						<Route
							path="/"
							exact
							component={Dashboard}
						/>
						<Route path="/TestPage" exact component={TestPage} />
					</Switch>
				</Router>
			</div>
		);
	}
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
