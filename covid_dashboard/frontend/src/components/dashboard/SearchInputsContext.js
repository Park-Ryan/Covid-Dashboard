import { createContext } from "react";

export const SearchInputsContext = createContext({			
	countryVal: "",
	stateVal: "",
	typeVal: "",
	dateVal: "",
});