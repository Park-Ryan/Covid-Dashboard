import * as React from 'react';
import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';

export default function PinnedSubheaderList(props) {
  const [MostConfirmed, setMostConfirmed] = React.useState(props.mostConfirmed);
  const [MostDeaths, setMostDeaths] = React.useState(props.mostDeaths);
  const [MostRecovered, setMostRecovered] = React.useState(props.mostRecovered);

  console.log(MostConfirmed);
  console.log(MostDeaths);
  console.log(MostRecovered);
  
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
          "Deaths",
      ].map((sectionId) => (
        <li key={`section-${sectionId}`}>
          <ul>
            <ListSubheader>{`Most ${sectionId}`}</ListSubheader>
            {MostConfirmed.map((item) => (
              <ListItem key={`item-${sectionId}-${item}`}>
                <ListItemText primary={`${item["US"]}`} />
                <ListItemText primary={`${item["China"]}`}/>
              </ListItem>
            ))}
          </ul>
        </li>
      ))}
    </List>
  );
}