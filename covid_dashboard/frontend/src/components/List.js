import * as React from 'react';
import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';

function filterData(type,data){
  var result = []
  for(let i = 0; i < data.length; ++i){
    if(data[i]["type"]==type){
      result.push(data[i]);
    }
  }
  return result;
}

export default function PinnedSubheaderList(props) {
  const [data, setData] = React.useState(JSON.parse(props.data));
  const [type, setType] = React.useState(props.type);
  const [stat, setStat] = React.useState(props.stat);
  const [shouldTruncate, setShouldTruncate] = React.useState(props.shouldTruncate);

  console.log("from List.js")
  console.log(data);

  
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
            <ListSubheader>{`${stat} ${type} by state `}</ListSubheader>
            {filterData(type,data).map((item) => (
              <ListItem alignItems="flex-start" key={`item-${sectionId}-${item}-${item}}`}>
                <ListItemText primary={`${item["state"]}`}/>
                {
                  shouldTruncate ? <ListItemText primary={`${Math.trunc(item[stat])}`}/> : <ListItemText primary={`${Math.trunc(item[stat]*100)/100}%`}/>
                }
                {/* // <ListItemText primary={`${Math.trunc(item[stat])}`}/> */}
              </ListItem>
            ))}
          </ul>
        </li>
      ))}
    </List>
  );
}