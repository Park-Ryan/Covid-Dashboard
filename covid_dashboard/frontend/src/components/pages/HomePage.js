import React, { useState, useEffect } from "react";
import { Grid, Button, Typography } from "@material-ui/core";
import TextField from "@material-ui/core/TextField";
import Autocomplete from "@material-ui/lab/Autocomplete";

import Logo from "../Logo";
import ControllableStates from "../ControllableStates";

import { CountryData } from "../data/CountryData";
import { StateData } from "../data/StateData";
import { TypeData } from "../data/TypeData";
import { DateData } from "../data/DateData";


import { hasNoLocationConflict } from "../tests/SearchValidation";

const countryOptions = CountryData;
const stateOptions = StateData;
const typeOptions = TypeData;
const dateOptions = DateData;

export default function HomePage(props) {
    const [inputText, setInputText] = useState("");
    const [payload, setPayload] = useState("");
    const [resultText, setResultText] = useState("");

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


    //Data modification variables
    //Country effect
    const [modCountryValue, modCountrySetValue] = React.useState("");
    const [modCountryInputValue, modCountrySetInputValue] = React.useState("");

    //State effect
    const [modStateValue, modStateSetValue] = React.useState("");
    const [modStateInputValue, modStateSetInputValue] = React.useState("");

    //Type effect
    const [modTypeValue, modTypeSetValue] = React.useState("");
    const [modTypeInputValue, modTypeSetInputValue] = React.useState("");

    //Date effect
    const [modDateValue, modDateSetValue] = React.useState("");
    const [modDateInputValue, modDateSetInputValue] = React.useState("");
    

    //Textfield updating logic
    function handleCountryInputChange(e){
        modCountrySetInputValue(e.target.value);
    }
    
    function handleStateInputChange(e){
        modStateSetInputValue(e.target.value);
    }

    function handleTypeInputChange(e){
        modTypeSetInputValue(e.target.value);
    }

    function handleDateInputChange(e){
        modDateSetInputValue(e.target.value);
    }



    useEffect(() => {
        setPayload(inputText);
    });

    function handleSubmit() {
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

        var payload = {
            countryVal: countryInputValue,
            stateVal: stateInputValue,
            typeVal: typeInputValue,
            dateVal: dateInputValue,
        };

        if (countryInputValue != "" && stateInputValue != "") {
            if (hasNoLocationConflict(countryInputValue, stateInputValue)) {
                console.log("Search Input Valid");
            } else {
                console.log("Conflict between Country and State inputs");
                alert(
                    "Location conflict between Country and State!\nPlease pick a Country and State that match."
                );
                return;
            }
        }

        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                payload,
            }),
        };

        console.log("Query Endpoint Fetched");
        fetch("/api/QueryEndpoint", requestOptions)
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                // for testing!
                setResultText(JSON.stringify(data));
            });
    }



    function handleAddButton(){
        console.log("Add Button Pressed")
        console.log("Country Begin")
        console.log(modCountryInputValue);
        console.log("Country End")
        console.log("State Begin")
        console.log(modStateInputValue);
        console.log("State End")
        console.log("Type Begin")
        console.log(modTypeInputValue);
        console.log("Type End")
        console.log("Date Begin")
        console.log(modDateInputValue);
        console.log("Date End")

        var payload = {
            countryVal: modCountryInputValue,
            stateVal: modStateInputValue,
            typeVal: modTypeInputValue,
            dateVal: modDateInputValue,
        };

        if (modCountryInputValue == "" || modStateInputValue == "" || modTypeInputValue == "" || modDateInputValue == "") {
            alert(
                "All fields text fields must be populated to perform data modifications (ADD, EDIT, DELETE)"
            );
            return;
        }

        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                payload,
            }),
        };

        console.log("Add Endpoint Fetched");
        fetch("/api/AddEndpoint", requestOptions)
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                // for testing!
                setResultText(JSON.stringify(data));
            });
    }

    function handleEditButton(){
        console.log("Edit Button Pressed")
        console.log("Country Begin")
        console.log(modCountryInputValue);
        console.log("Country End")
        console.log("State Begin")
        console.log(modStateInputValue);
        console.log("State End")
        console.log("Type Begin")
        console.log(modTypeInputValue);
        console.log("Type End")
        console.log("Date Begin")
        console.log(modDateInputValue);
        console.log("Date End")

        var payload = {
            countryVal: modCountryInputValue,
            stateVal: modStateInputValue,
            typeVal: modTypeInputValue,
            dateVal: modDateInputValue,
        };

        if (modCountryInputValue == "" || modStateInputValue == "" || modTypeInputValue == "" || modDateInputValue == "") {
            alert(
                "All fields text fields must be populated to perform data modifications (ADD, EDIT, DELETE)"
            );
            return;
        }

        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                payload,
            }),
        };

        console.log("Edit Endpoint Fetched");
        fetch("/api/EditEndpoint", requestOptions)
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                // for testing!
                setResultText(JSON.stringify(data));
            });
    }

    function handleDeleteButton(){
        console.log("Delete Button Pressed")
        console.log("Country Begin")
        console.log(modCountryInputValue);
        console.log("Country End")
        console.log("State Begin")
        console.log(modStateInputValue);
        console.log("State End")
        console.log("Type Begin")
        console.log(modTypeInputValue);
        console.log("Type End")
        console.log("Date Begin")
        console.log(modDateInputValue);
        console.log("Date End")

        var payload = {
            countryVal: modCountryInputValue,
            stateVal: modStateInputValue,
            typeVal: modTypeInputValue,
            dateVal: modDateInputValue,
        };

        if (modCountryInputValue == "" || modStateInputValue == "" || modTypeInputValue == "" || modDateInputValue == "") {
            alert(
                "All fields text fields must be populated to perform data modifications (ADD, EDIT, DELETE)"
            );
            return;
        }

        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                payload,
            }),
        };

        console.log("Delete Endpoint Fetched");
        fetch("/api/DeleteEndpoint", requestOptions)
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                // for testing!
                setResultText(JSON.stringify(data));
            });
    }

    function useForceUpdate() {
        const [value, setValue] = useState(0); // integer state
        return () => setValue((value) => value + 1); // update the state to force render
    }

    function displayResultText() {
        return <h4>{resultText}</h4>;
    }

    return (
        <div>
            <div className="center">
                <Grid container spacing={1}>
                    <Grid item xs={3}></Grid>
                    <Grid item algin="center" xs={6}>
                        <Logo />
                        <br></br>
                    </Grid>
                    <Grid item xs={3}></Grid>
                    <Grid item align="center" xs={12}>
                        <Typography component="h6" variant="h6" >
                            Enter fields for data extraction.
                        </Typography>
                    </Grid>
                    <Grid item xs={2}></Grid>
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
                            renderInput={(params) => (
                                <TextField {...params} label="Country" />
                            )}
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
                            renderInput={(params) => (
                                <TextField {...params} label="State" />
                            )}
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
                            renderInput={(params) => (
                                <TextField {...params} label="Type" />
                            )}
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
                            renderInput={(params) => (
                                <TextField {...params} label="Date" />
                            )}
                        />
                    </Grid>
                    <Grid item xs={2}></Grid>
                    <Grid item align="center" xs={12}>
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleSubmit}
                        >
                            Submit
                        </Button>
                    </Grid>
                    <Grid item align="center" xs={12}>
                        <br></br>
                        <Typography component="h6" variant="h6" >
                            Enter fields to add, edit, delete, and backup the dataset.
                        </Typography>
                    </Grid>
                    <Grid item align="center" xs={12}>
                        <Typography component="h6" variant="h6" >
                            (User must populate all fields to process)
                        </Typography>
                    </Grid>
                    <Grid item xs={2}></Grid>
                    <Grid item align="center" xs={2}>
                        <TextField
                            id="outlined-basic" 
                            label="Country"
                            // value={value}
                            onChange={handleCountryInputChange}
                            inputValue={modCountryInputValue}
                            onInputChange={(event, newInputValue) => {
                                modCountrySetInputValue(newInputValue);
                            }}
                            sx={{ width: 300 }}
                            renderInput={(params) => (
                                <TextField {...params} label="Country" />
                            )}
                        />
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <TextField
                            id="outlined-basic" 
                            label="State"
                            // value={value}
                            onChange={handleStateInputChange}
                            inputValue={modStateInputValue}
                            onInputChange={(event, newInputValue) => {
                                modStateSetInputValue(newInputValue);
                            }}
                            sx={{ width: 300 }}
                            renderInput={(params) => (
                                <TextField {...params} label="State" />
                            )}
                        />
                    </Grid>
                    <Grid item align="center" xs={2}>
                    <TextField
                            id="outlined-basic" 
                            label="Type"
                            // value={value}
                            onChange={handleTypeInputChange}
                            inputValue={modTypeInputValue}
                            onInputChange={(event, newInputValue) => {
                                modTypeSetInputValue(newInputValue);
                            }}
                            sx={{ width: 300 }}
                            renderInput={(params) => (
                                <TextField {...params} label="Type" />
                            )}
                        />
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <TextField
                            id="outlined-basic" 
                            label="Date"
                            // value={value}
                            onChange={handleDateInputChange}
                            inputValue={modDateInputValue}
                            onInputChange={(event, newInputValue) => {
                                modDateSetInputValue(newInputValue);
                            }}
                            sx={{ width: 300 }}
                            renderInput={(params) => (
                                <TextField {...params} label="Date" />
                            )}
                        />
                    </Grid>
                    <Grid item xs={2}></Grid>
                    <Grid item align="center" xs={2}>
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <Button
                            variant="contained"
                            color="secondary"
                            onClick={handleAddButton}
                        >
                            Add
                        </Button>
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <Button
                            variant="contained"
                            color="secondary"
                            onClick={handleEditButton}
                        >
                            Edit
                        </Button>
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <Button
                            variant="contained"
                            color="secondary"
                            onClick={handleDeleteButton}
                        >
                            Delete
                        </Button>
                    </Grid>
                    <Grid item align="center" xs={2}>
                        <Button
                            variant="contained"
                            color="secondary"
                            onClick={handleSubmit}
                        >
                            Backup
                        </Button>
                    </Grid>
                    <Grid item align="center" xs={2}>
                    </Grid>
                    <Grid item align="center" xs={12}>
                        {resultText != "" ? displayResultText() : ""}
                    </Grid>
                </Grid>
            </div>
        </div>
    );
}
