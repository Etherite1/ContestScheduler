import { useState } from 'react'
import './App.css'
import SiteCheckbox from './SiteCheckbox.jsx'
import GetContests from './GetContests.jsx'

function Contest({site, name, time, countdown}) // TODO: link
{
    return (
        <tr>
            <td>{site}</td>
            <td>{name}</td>
            <td>{time}</td>
            <td>{countdown}</td>
        </tr>
    );
}

function ContestTable({displayedSites}) 
{
    var contests = GetContests();

    const contestComponents = contests.map((contest) => {
        if(!displayedSites.get(contest[0])) return;
        return (
            <Contest key = {contest[0]} site = {contest[0]} name = {contest[1]} time = {contest[2]} countdown = {contest[3]}/>
        );
    });

    return (
        <table className = "table table-hover mb-0">
            <thead>
                <tr>
                    <th>Site</th>
                    <th style = {{width: "500px"}}>Name</th>
                    <th>Time</th>
                    <th>Countdown</th>
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