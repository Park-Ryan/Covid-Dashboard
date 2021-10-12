import React, {useState, useEffect} from "react";
import {Grid} from "@material-ui/core";
import Typography from "@material-ui/core/Typography";



export default function Logo(props){

    return(
        <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <Typography component="h2" variant="h2">
                    Covid Dashboard
                </Typography>
            </Grid>
        </Grid>
    )
}