import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import Analytics from "./pages/Analytics";
import TextAnalytics from "./pages/TextAnalytics";
import Dashboard from "./dashboard/Dashboard";
import { SearchInputsContext } from "./dashboard/SearchInputsContext";
// callbacks, pass child data back to parent component
export default function App() {
	// constructor(props) {
	// 	super(props);

	// 	this.state = {
	// 		mainData: null,
	// 	};
	// 	this.setMainData = this.setMainData.bind(this);
	// }

	const [mainData, setMainData] = React.useState({})
	const [searchInputsValues, setSearchInputsValues] = React.useState({			
		countryVal: "",
		stateVal: "",
		typeVal: "",
		dateVal: "",
	})

	// setMainData(data) {
	// 	this.setState({
	// 		mainData: data,
	// 	});
	// 	console.log("Hello from setMainData in App.js, data stored : ");
	// 	console.log(data);
	// }

	// render() {
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
						<SearchInputsContext.Provider value = {{ searchInputsValues, setSearchInputsValues }}>
							<Route exact path="/">
								<Dashboard grandparentCallback={setMainData} />
							</Route>
							<Route path="/Analytics"> <Analytics inputValues = {mainData}/> </Route>
							<Route path="/TextAnalytics"> <TextAnalytics/> </Route>
							<Route path="/HomePage" exact component={HomePage} />
						</SearchInputsContext.Provider>
					</Switch>
				</Router>
			</div>
		);
	// }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
