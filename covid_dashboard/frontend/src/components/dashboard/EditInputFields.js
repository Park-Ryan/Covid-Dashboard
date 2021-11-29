import * as React from "react";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import Button from "@mui/material/Button";
import { CountryData } from "../data/CountryData";
import { CountryStateMap } from "../data/CountryStateMap";
import { TypeData } from "../data/TypeData";
import { DateData } from "../data/DateData";
import { AutocompleteInputField } from "./SearchInputFields";

// pass these inputs values back up using callback? or lifting
// when submit is pressed pass up the values and make GET request for table?
// https://stackoverflow.com/questions/55726886/react-hook-send-data-from-child-to-parent-component
export function EditInputFields({ parentCallback }) {
	const [countryInput, setCountryInput] = React.useState("");
	const [stateInput, setStateInput] = React.useState("");
	const [typeInput, setTypeInput] = React.useState("");
	const [dateInput, setDateInput] = React.useState("");
	const [amountInput, setAmountInput] = React.useState("");
	const [endPoint, setEndpoint] = React.useState("");

	const countryOptions = CountryData;
	const countryStateMapOptions = CountryStateMap;
	const typeOptions = TypeData;
	const dateOptions = DateData;

	function getInputValues() {
		return {
			countryVal: countryInput,
			stateVal: stateInput,
			typeVal: typeInput,
			dateVal: dateInput,
			amountVal: Number(amountInput),
		};
	}

	// pass back up the input values, then use those input values to make api call

	const handleAdd = (event) => {
		parentCallback(getInputValues(), "AddEndpoint");
	};

	const handleEdit = (event) => {
		parentCallback(getInputValues(), "EditEndpoint");
	};

	const handleDelete = (event) => {
		parentCallback(getInputValues(), "DeleteEndpoint");
	};

	const handleBackup = (event) => {
		parentCallback(getInputValues(), "BackupEndpoint");
	};

	return (
		<>
			<div
				style={{ display: "flex", flexWrap: "wrap", marginTop: "30px" }}
			>
				<AutocompleteInputField
					InputLabel="Country"
					InputOptions={countryOptions}
					input={countryInput}
					setInput={setCountryInput}
				/>
				<AutocompleteInputField
					InputLabel="State"
					InputOptions={countryStateMapOptions[countryInput]}
					input={stateInput}
					setInput={setStateInput}
				/>
				<AutocompleteInputField
					InputLabel="Type"
					InputOptions={typeOptions}
					input={typeInput}
					setInput={setTypeInput}
				/>
				<AutocompleteInputField
					InputLabel="Date"
					InputOptions={dateOptions}
					input={dateInput}
					setInput={setDateInput}
				/>
				<TextField
					id="amount-text-field"
					label="Amount"
					type="number"
					onInput={(e) => {
						e.target.value = Math.max(0, parseInt(e.target.value))
							.toString()
							.slice(0, 12);
					}}
					variant="outlined"
					value={amountInput}
					onChange={(e) => {
						setAmountInput(e.target.value);
					}}
				/>
			</div>
			{/* 0 auto margin apparently centers a div lol */}
			<div
				style={{ display: "flex", flexWrap: "wrap", margin: "0 auto" }}
			>
				<Button
					id="Add"
					onClick={handleAdd}
					variant="outlined"
					style={{
						borderColor: "#FFFFFF",
						color: "#FFFFFF",
					}}
				>
					Add
				</Button>
				<Button
					id="Edit"
					onClick={handleEdit}
					variant="outlined"
					style={{
						borderColor: "#FFFFFF",
						color: "#FFFFFF",
					}}
				>
					Edit
				</Button>
				<Button
					id="Delete"
					onClick={handleDelete}
					variant="outlined"
					style={{
						borderColor: "#FFFFFF",
						color: "#FFFFFF",
					}}
				>
					Delete
				</Button>
				<Button
					id="Backup"
					onClick={handleBackup}
					variant="outlined"
					style={{
						borderColor: "#FFFFFF",
						color: "#FFFFFF",
					}}
				>
					Backup
				</Button>
			</div>
		</>
	);
}
