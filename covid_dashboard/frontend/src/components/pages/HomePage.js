import React, {useState, useEffect} from "react";
import {Grid, Button} from "@material-ui/core";
import TextField from '@material-ui/core/TextField';
import Autocomplete from "@material-ui/lab/Autocomplete"

import Logo from "../Logo";
import ControllableStates  from "../ControllableStates"

import { CountryData } from "../data/CountryData";
import { StateData } from "../data/StateData";
import { TypeData } from '../data/TypeData';
import { DateData} from "../data/DateData";

import { hasNoLocationConflict } from "../tests/SearchValidation";

const countryOptions = CountryData;
const stateOptions = StateData;
const typeOptions = TypeData;
const dateOptions = DateData;


export default function HomePage(props){

    const [inputText, setInputText] = useState("");
    const [payload, setPayload] = useState("");
    const [resultText, setResultText] = useState("");

    //Country effect
    const [countryValue, countrySetValue] = React.useState(countryOptions[0]);
    const [countryInputValue, countrySetInputValue] = React.useState('');

    //State effect
    const [stateValue, stateSetValue] = React.useState(stateOptions[0]);
    const [stateInputValue, stateSetInputValue] = React.useState('');


    //Type effects
    const [typeValue, typeSetValue] = React.useState(typeOptions[0]);
    const [typeInputValue, typeSetInputValue] = React.useState('');

    //Date effect
    const [dateValue, dateSetValue] = React.useState(dateOptions[0]);
    const [dateInputValue, dateSetInputValue] = React.useState('');
 
    
    useEffect(() => {
        setPayload(inputText)
    });

    function handleSubmit(){

        console.log("Country Begin :");
        console.log(countryInputValue);
        console.log("Country End");

        console.log("State Begin :");
        console.log(stateInputValue);
        console.log("State End");

        console.log("Type Begin :");
        console.log(typeInputValue);
        console.log("Type End");

        console.log("Date Begin :");
        console.log(dateInputValue);
        console.log("Date End");


        if(countryInputValue!="" && stateInputValue != ""){
            if(hasNoLocationConflict(countryInputValue,stateInputValue)){
                console.log("Search Input Valid");
            }
            else{
                console.log("Conflict between Country and State inputs");
                alert("Location conflict between Country and State!\nPlease pick a Country and State that match.");
                return
            }
        }


        //REPLACE ME WITH A DIFFERENT API
        // const requestOptions = {
        //     method: "POST",
        //     headers: { "Content-Type": "application/json"},
        //     body: JSON.stringify({
        //         payload_bus : payload
        //     }),
        // };

        // console.log('Sample Endpoint Fetched');
        // fetch('/api/SampleEndpoint',requestOptions)
        // .then(response => response.json())
        // .then(data => {
        //     setResultText(data);
        //     console.log(data);
        // });
    }

    function useForceUpdate(){
        const [value, setValue] = useState(0); // integer state
        return () => setValue(value => value + 1); // update the state to force render
    }

    function displayResultText(){
        return(
            <h4>{resultText}</h4>
        )
    }

    return(
        <div>
            <div className="center">
                <Grid container spacing={1}>
                    <Grid item xs={3}>
                    </Grid>
                    <Grid item algin="center" xs={6}>
                        <Logo/>
                    </Grid>
                    <Grid item xs={3}>
                    </Grid>
                    <Grid item xs={2}>
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <Autocomplete
                            // value={value}
                            onChange={(event, newValue) => {
                            countrySetValue(newValue);
                            }}
                            inputValue={countryInputValue}
                            onInputChange={(event, newInputValue) => {
                            countrySetInputValue(newInputValue);
                            }}
                            id="controllable-states-demo"
                            options={countryOptions}
                            sx={{ width: 300 }}
                            renderInput={(params) => <TextField {...params} label="Country" />}
                        />
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <Autocomplete
                            // value={value}
                            onChange={(event, newValue) => {
                            stateSetValue(newValue);
                            }}
                            inputValue={stateInputValue}
                            onInputChange={(event, newInputValue) => {
                            stateSetInputValue(newInputValue);
                            }}
                            id="controllable-states-demo"
                            options={stateOptions}
                            sx={{ width: 300 }}
                            renderInput={(params) => <TextField {...params} label="State" />}
                        />
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <Autocomplete
                            // value={value}
                            onChange={(event, newValue) => {
                            typeSetValue(newValue);
                            }}
                            inputValue={typeInputValue}
                            onInputChange={(event, newInputValue) => {
                            typeSetInputValue(newInputValue);
                            }}
                            id="controllable-states-demo"
                            options={typeOptions}
                            sx={{ width: 300 }}
                            renderInput={(params) => <TextField {...params} label="Type" />}
                        />
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <Autocomplete
                            // value={value}
                            onChange={(event, newValue) => {
                            dateSetValue(newValue);
                            }}
                            inputValue={dateInputValue}
                            onInputChange={(event, newInputValue) => {
                            dateSetInputValue(newInputValue);
                            }}
                            id="controllable-states-demo"
                            options={dateOptions}
                            sx={{ width: 300 }}
                            renderInput={(params) => <TextField {...params} label="Date" />}
                        />
                    </Grid>
                    <Grid item xs={2}>
                    </Grid>
                    <Grid item align="center" xs={12}>
                        <Button variant="contained" color="primary" onClick={handleSubmit}>
                            Submit
                        </Button>
                    </Grid>
                    <Grid item align="center" xs={12}>
                        {resultText != "" ? displayResultText() : ""}
                    </Grid>
                </Grid>           
            </div>
        </div>
    )
}

