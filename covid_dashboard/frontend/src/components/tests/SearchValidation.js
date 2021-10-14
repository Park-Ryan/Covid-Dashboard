import {CountryStateMap} from "../data/CountryStateMap"

export function hasNoLocationConflict(country, state){

    if(CountryStateMap[country].includes(state)){
        return true;
    }
    else{
        return false;
    }
}
