import * as React from "react";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormHelperText from "@mui/material/FormHelperText";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import { display, flexbox } from "@mui/system";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import Stack from "@mui/material/Stack";
import Button from "@mui/material/Button";

// pass in props data to make custom input fields
// when user selects a country, the next input field will only show states from that country.
// use a dictonary for that
function SelectInputField(props) {
	const [InputLabel, setInputLabel] = React.useState(props.InputLabel);
	const [InputOptions, setInputOptions] = React.useState(props.InputOptions);

	const handleChange = (event) => {
		setInput(event.target.value);
	};

	const listInputs = InputOptions.map((input) => (
		<MenuItem value="">{input}</MenuItem>
	));

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
					{listInputs}
				</Select>
				{/* <FormHelperText>nah</FormHelperText> */}
			</FormControl>
		</div>
	);
}

// https://javascript.plainenglish.io/how-to-use-the-autocomplete-component-in-material-ui-11a7132d2b71?gi=eb1a40c3a4fe
function AutocompleteInputField(props) {
	const [InputLabel, setInputLabel] = React.useState(props.InputLabel);
	const [InputOptions, setInputOptions] = React.useState(props.InputOptions);
	// const [input, setInput] = React.useState(""); // '' is the initial state value

	const handleChange = (event, newInput, reason) => {
		if (reason === "clear") {
			props.setInput("");
		} else {
			props.setInput(newInput);
		}
	};

	return (
		<div>
			<Autocomplete
				disablePortal
				id={`${InputLabel}-combo-box`}
				onInputChange={handleChange}
				value={props.input}
				options={InputOptions}
				sx={{ width: 200 }}
				renderInput={(params) => (
					<TextField {...params} label={InputLabel} />
				)}
			/>
		</div>
	);
}

// pass these inputs values back up using callback? or lifting
// when submit is pressed pass up the values and make GET request for table?
// https://stackoverflow.com/questions/55726886/react-hook-send-data-from-child-to-parent-component
export function MainInputFields({ parentCallback }) {
	const [countryInput, setCountryInput] = React.useState("");
	const [stateInput, setStateInput] = React.useState("");
	const [typeInput, setTypeInput] = React.useState("");
	const [dateInput, setDateInput] = React.useState("");

	// test inputs
	const inputs = ["US", "China", "Japan", "Africa"];

	// pass back up the input values, then use those input values to make api call
	const handleSubmit = (event) => {
		// console.log(countryInput);
		// console.log(stateInput);
		// console.log(typeInput);
		// console.log(dateInput);

		const inputValues = {
			countryVal: countryInput,
			stateVal: stateInput,
			typeVal: typeInput,
			dateVal: dateInput,
		};

		// pass input values back to parent component
		parentCallback(inputValues);

		// console.log(inputValues)
		// then use those values to call the parent component's onSubmit method to call api
		// not sure if this will work since the inputs arent passed back up yet - I was right
		// onSubmit();
	};

	return (
		<div style={{ display: "flex", flexWrap: "wrap" }}>
			<AutocompleteInputField
				InputLabel="Country"
				InputOptions={inputs}
				input={countryInput}
				setInput={setCountryInput}
			/>
			<AutocompleteInputField
				InputLabel="State"
				InputOptions={inputs}
				input={stateInput}
				setInput={setStateInput}
			/>
			<AutocompleteInputField
				InputLabel="Type"
				InputOptions={inputs}
				input={typeInput}
				setInput={setTypeInput}
			/>
			<AutocompleteInputField
				InputLabel="Date"
				InputOptions={inputs}
				input={dateInput}
				setInput={setDateInput}
			/>
			<Button
				onClick={handleSubmit}
				variant="outlined"
				style={{
					marginLeft: "2rem",
					borderColor: "#FFFFFF",
					color: "#FFFFFF",
				}}
			>
				Submit
			</Button>
		</div>
	);
}
