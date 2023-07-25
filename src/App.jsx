import { useState } from 'react'
import './App.css'
import SiteCheckbox from './SiteCheckbox.jsx'

function Contest({site, name, time}) // TODO: link
{
    return (
        <tr>
            <td>{site}</td>
            <td>{name}</td>
            <td>{time}</td>
        </tr>
    );
}

function ContestTable({displayedSites}) 
{
    var contest1 = ["CF", "Round 823239358235", "Tomorrow"];
    var contest2 = ["LC", "Biweekly", "Tuesday"];
    var contest3 = ["CC", "Lunchtime", "Friday"];

    var contests = [contest1, contest2, contest3];

    const contestComponents = contests.map((contest) => {
        if(!displayedSites.get(contest[0])) return;
        return (
            <Contest key = {contest[0]} site = {contest[0]} name = {contest[1]} time = {contest[2]}/>
        );
    });

    return (
        <table className = "table table-hover mb-0">
            <thead>
                <tr>
                    <th className = "text-center">Site</th>
                    <th className = "text-center">Name</th>
                    <th className = "text-center">Time</th>
                </tr>
            </thead>
            <tbody>
                {contestComponents}
            </tbody>
            
        </table>
    );
}

export default function ContestScheduler() 
{
    var siteNames = new Map();
    siteNames.set("CF", false);
    siteNames.set("LC", false);
    siteNames.set("CC", false);
    const [displayedSites, setDisplayedSites] = useState(siteNames);
    
    function onCheck(siteName)
    {
        const nextMap = new Map(displayedSites);
        nextMap.set(siteName, !displayedSites.get(siteName));
        setDisplayedSites(nextMap);
    }

    const FilterBoxes = [...Array.from(displayedSites.keys())].map((site) => {
        return (
            <SiteCheckbox key = {site} siteName = {site} onCheck = {onCheck} />
        );
    });

    return (
        <div className = "wrapper">
            <div className = "filterBoxes">
                {FilterBoxes}
            </div>
            <div className = "table-responsive">
                <ContestTable displayedSites = {displayedSites}/>
            </div>
        </div>
    );
}