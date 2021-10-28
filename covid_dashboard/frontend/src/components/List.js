import * as React from 'react';
import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';

export default function PinnedSubheaderList(props) {
  const [MostConfirmed, setMostConfirmed] = React.useState(props.mostConfirmed);
  const [mostDeaths, setMostDeaths] = React.useState(props.mostDeaths);
  const [MostRecovered, setMostRecovered] = React.useState(props.mostRecovered);
  const [location,setLocation] = React.useState(props.location);

  const [type,setType] = React.useState(props.category);

  console.log("from List.js")
  console.log(JSON.parse(mostDeaths));

  
  return (
    <List
      sx={{
        width: '100%',
        maxWidth: 360,
        bgcolor: 'background.paper',
        position: 'relative',
        overflow: 'auto',
        maxHeight: 300,
        '& ul': { padding: 0 },
      }}
      subheader={<li />}
    >
      {[
          type,
      ].map((sectionId) => (
        <li key={`section-${sectionId}`}>
          <ul>
            <ListSubheader>{`${location} Most ${sectionId}`}</ListSubheader>
            {JSON.parse(mostDeaths).map((item) => (
              <ListItem alignItems="flex-start" key={`item-${sectionId}-${item}-${item}}`}>
                <ListItemText primary={`${item[location]}`}/>
                <ListItemText primary={`${item["Types"][type]}`}/>
              </ListItem>
            ))}
          </ul>
        </li>
      ))}
    </List>
  );
}