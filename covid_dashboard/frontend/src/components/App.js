import React, {Component} from "react";
import {render} from "react-dom";

import SamplePage from "./pages/SamplePage";

export default class App extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
            <div className="initLayout">
                <SamplePage/>
            </div>
        )
    }
}


const appDiv = document.getElementById("app");
render(<App/>, appDiv);