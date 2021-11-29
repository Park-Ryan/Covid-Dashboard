import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import Analytics from "./pages/Analytics";
import TextAnalytics from "./pages/TextAnalytics";
import Dashboard from "./dashboard/Dashboard";

// callbacks, pass child data back to parent component
export default class App extends Component {
	constructor(props) {
		super(props);

		this.state = {
			mainData: null,
		};
		this.setMainData = this.setMainData.bind(this);
	}

	setMainData(data) {
		this.setState({
			mainData: data,
		});
		console.log("Hello from setMainData in App.js, data stored : ");
		console.log(data);
	}

	render() {
		return (
			// <div className="initLayout">
			<div>
				<Router>
					<Switch>
						{/* <Route
							path="/"
							exact
							component={Dashboard}
							grandparentCallback={this.setMainData}
						/> */}
						<Route exact path="/">
							<Dashboard grandparentCallback={this.setMainData} />
						</Route>
						<Route path="/Analytics"> <Analytics/> </Route>
						<Route path="/TextAnalytics"> <TextAnalytics/> </Route>
						<Route path="/HomePage" exact component={HomePage} />
					</Switch>
				</Router>
			</div>
		);
	}
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
