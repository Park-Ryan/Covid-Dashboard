import React, {useState, useEffect} from "react";
import {Grid, Button} from "@material-ui/core";
import TextField from '@material-ui/core/TextField';


export default function SamplePage(props){

    const [inputText, setInputText] = useState("");
    const [payload, setPayload] = useState("");
    const [resultText, setResultText] = useState("");

    function handleInputTextChange(e){
        setInputText(e.target.value);
    }

    useEffect(() => {
        setPayload(inputText)
    });

    function handleSubmit(){
        console.log("Payload Begin :");
        console.log(payload);
        console.log("Payload End");

        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({
                payload_bus : payload
            }),
        };
        
        console.log('Sample Endpoint Fetched');
        fetch('/api/SampleEndpoint',requestOptions)
        .then(response => response.json())
        .then(data => {
            setResultText(data);
            console.log(data);
        });
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
                        <h1>Welcome to Sample Page</h1>
                    </Grid>
                    <Grid item xs={3}>
                    </Grid>
                    <Grid item xs={3}>
                    </Grid>
                    <Grid item align="center" xs={6}>
                        <TextField onChange={handleInputTextChange}
                            label="Input sample text" 
                            variant="outlined" 
                            margin="normal" 
                            multiline rows={5} 
                            fullWidth
                            >
                        </TextField>
                    </Grid>
                    <Grid item xs={3}>
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