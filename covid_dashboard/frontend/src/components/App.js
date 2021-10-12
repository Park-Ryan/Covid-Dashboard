import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from "./pages/HomePage";

import SamplePage from "./pages/SamplePage";

export default class App extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
            <div className="initLayout">
                <HomePage/>
            </div>
        )
    }
}


const appDiv = document.getElementById("app");
render(<App/>, appDiv);