import * as React from "react";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormHelperText from "@mui/material/FormHelperText";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import { display, flexbox } from "@mui/system";
import Autocomplete from "@material-ui/lab/Autocomplete";

// pass in props data to make custom input fields
// when user selects a country, the next input field will only show states from that country.
// use a dictonary for that
function SelectInputField(props) {
	const [InputLabel, setInputLabel] = React.useState(props.InputLabel);
	const [InputOptions, setInputOptions] = React.useState(props.InputOptions);

	const handleChange = (event) => {
		setInputLabel(event.target.value);
	};

	const listInputs = InputOptions.map((input) => (
		<MenuItem value="">{input}</MenuItem>
	));
	console.log("Input Label" + InputLabel);
	console.log("List Inputs" + InputOptions);

	return (
		<div>
			<FormControl required sx={{ m: 1, minWidth: 120 }}>
				<InputLabel id="demo-simple-select-required-label">
					{InputLabel}
				</InputLabel>
				<Select
					labelId="demo-simple-select-required-label"
					id="demo-simple-select-required"
					value={InputLabel}
					label={`${InputLabel}"*"`}
					onChange={handleChange}
				>
					<MenuItem value="">
						<em>None</em>
					</MenuItem>
					{listInputs}
				</Select>
				{/* <FormHelperText>nah</FormHelperText> */}
			</FormControl>
		</div>
	);
}

function AutocompleteInputField(props) {
	const [InputLabel, setInputLabel] = React.useState(props.InputLabel);
	const [InputOptions, setInputOptions] = React.useState(props.InputOptions);

	const handleChange = (event) => {
		setInputLabel(event.target.value);
	};

	return(
		<Autocomplete
			// value={value}
			onChange={handleChange}
			inputValue={InputLabel}
			onInputChange={(event, newInputValue) => {
				countrySetInputValue(newInputValue);
			}}
			// id="controllable-states-demo"
			// options={}
			sx={{ width: 300 }}
			renderInput={(params) => <TextField {...params} label="Country" />}
		/>
	);
}

export function MainInputFields() {
	const inputs = [1, 2, 3, 4];
	return (
		<div style={{ display: "flex", flexWrap: "wrap" }}>
			<SelectInputField InputLabel="Country" InputOptions={inputs} />
			{/* Based off the country selection, we update the inputs list of state */}
			<SelectInputField InputLabel={"State"} InputOptions={inputs} />
			<SelectInputField InputLabel={"Type"} InputOptions={inputs} />
			<SelectInputField InputLabel={"Date"} InputOptions={inputs} />
		</div>
	);
}
