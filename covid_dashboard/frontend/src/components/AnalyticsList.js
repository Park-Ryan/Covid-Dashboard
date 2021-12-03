import * as React from "react";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListSubheader from "@mui/material/ListSubheader";

function createData(state, averages, percentages, std) {
  return {
    state: state,
    averages: averages,
    percentages: percentages,
    std: std,
  };
}
export default function AnalyticsList(props) {
  const { type, data } = props;
  
  
  React.useEffect(() => {
		console.log("from List.js");
		console.log(data);
	}, [data]);

  function filterData(type, data) {
    let result = [];
    for (let i = 0; i < data.length; i++) {
    //   let state = Object.keys(data[i])[0];
    //   let temp = Object.values(data[i])[0];
    //   console.log(state);
    //   console.log(temp);
      if (data[i].type == type) {
        result.push(
          createData(data[i].state, data[i].averages, data[i].percentages, data[i].std)
        );
      }
      console.log("hello");
    }
    console.log(result);
    return result;
  }

	function capitalizeFirstLetter(string) {
		return string.charAt(0).toUpperCase() + string.slice(1);
	}

	function numberWithCommas(x) {
		return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	}

  return (
    <>
      <List
        sx={{
          width: "100%",
          maxWidth: 530,
          bgcolor: "background.paper",
          position: "relative",
          overflow: "auto",
          maxHeight: 500,
          "& ul": { padding: 0 },
        }}
        subheader={<li />}
      >
        {filterData(type, data).map((item) => (
          <li>
            <ul>
              <ListSubheader sx={{color: "white", fontSize: "large"}}>{`${item.state} - ${type}`}</ListSubheader>
              {[item.averages, item.percentages, item.std].map((value, index) => (
                <ListItem sx={{textIndent: "30px"}} key={`item-${item.state}`}>
                  <ListItemText primary={`${capitalizeFirstLetter(Object.keys(item)[index+1])}: ${numberWithCommas(Math.round(value * 100) / 100)}`} />
                </ListItem>
              ))}
            </ul>
          </li>
        ))}
      </List>
    </>
  );
}

// import * as React from 'react';
// import List from '@mui/material/List';
// import ListItem from '@mui/material/ListItem';
// import ListItemText from '@mui/material/ListItemText';
// import ListSubheader from '@mui/material/ListSubheader';

// export default function PinnedSubheaderList() {
//   return (
//     <List
//       sx={{
//         width: '100%',
//         maxWidth: 360,
//         bgcolor: 'background.paper',
//         position: 'relative',
//         overflow: 'auto',
//         maxHeight: 300,
//         '& ul': { padding: 0 },
//       }}
//       subheader={<li />}
//     >
//       {[0, 1, 2, 3, 4].map((sectionId) => (
//         <li key={`section-${sectionId}`}>
//           <ul>
//             <ListSubheader>{`I'm sticky ${sectionId}`}</ListSubheader>
//             {[0, 1, 2].map((item) => (
//               <ListItem key={`item-${sectionId}-${item}`}>
//                 <ListItemText primary={`Item ${item}`} />
//               </ListItem>
//             ))}
//           </ul>
//         </li>
//       ))}
//     </List>
//   );
// }

//   return (
//     <List
//       sx={{
//         width: '100%',
//         maxWidth: 360,
//         bgcolor: 'background.paper',
//         position: 'relative',
//         overflow: 'auto',
//         maxHeight: 300,
//         '& ul': { padding: 0 },
//       }}
//       subheader={<li />}
//     >
//       {[
//           type,
//       ].map((sectionId) => (
//         <li key={`section-${sectionId}`}>
//           <ul>
//             <ListSubheader>{`${stat.toUpperCase()} ${type.toUpperCase()} BY STATE`}</ListSubheader>
//             {filterData(type,data).map((item) => (
//               <ListItem alignItems="flex-start" key={`item-${sectionId}-${item}-${item}}`}>
//                 <ListItemText primary={`${item["state"]}`}/>
//                 {
//                   shouldTruncate ? <ListItemText primary={`${Math.trunc(item[stat])}`}/> : <ListItemText primary={`${Math.trunc(item[stat]*100)/100}%`}/>
//                 }
//                 {/* // <ListItemText primary={`${Math.trunc(item[stat])}`}/> */}
// 				</ListItem>
// 				))}
// 			  </ul>
// 			</li>
// 		  ))}
// 		</List>
// 	  );
// 	}
