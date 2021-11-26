import React, { Component, useState, useEffect } from "react";
import "./TestPage.css";

export default function TestPage(props) {

	//Data extraction variables
    //Country effect
    const [countryValue, countrySetValue] = React.useState(countryOptions[0]);
    const [countryInputValue, countrySetInputValue] = React.useState("");

    //State effect
    const [stateValue, stateSetValue] = React.useState(stateOptions[0]);
    const [stateInputValue, stateSetInputValue] = React.useState("");

    //Type effects
    const [typeValue, typeSetValue] = React.useState(typeOptions[0]);
    const [typeInputValue, typeSetInputValue] = React.useState("");

    //Date effect
    const [dateValue, dateSetValue] = React.useState(dateOptions[0]);
    const [dateInputValue, dateSetInputValue] = React.useState("");
}
