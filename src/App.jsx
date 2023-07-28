import { useState, useEffect } from 'react'
import './App.css'
import SiteCheckbox from './SiteCheckbox.jsx'
import GetContests from './GetContests.jsx'

function Contest({site, name, time, countdown}) // TODO: link
{
    function getLogo(site)
    {
        if(site == "CC") return "logos/cc.png";
        else if(site == "LC") return "logos/lc.png";
        else if(site == "CF") return "logos/cf.png";
    }
    return (
        <tr>
            <td><img src = {getLogo(site)} height = "50px" width = "auto" /></td>
            <td>{name}</td>
            <td>{time}</td>
            <td>{countdown}</td>
        </tr>
    );
}

function ContestTable({displayedSites}) 
{
    const [contests, setContests] = useState([]);

    const GetAPIData = () => {
        fetch('http://127.0.0.1:5000')
            .then(res => {
                return res.json();
            })
            .then(data => {
                var next_contests = [];
                for(let curr_data of data)
                {
                    var curr_contest = [];
                    curr_contest[0] = curr_data['site'];
                    curr_contest[1] = curr_data['name'];
                    curr_contest[2] = curr_data['time'];
                    curr_contest[3] = curr_data['countdown'];
                    next_contests.push(curr_contest);
                }
                setContests(next_contests);
            })
    };

    useEffect(() => {
        GetAPIData();
    }, [])

    var contestComponents = contests.map((contest) => {
        if(!displayedSites.get(contest[0])) return;
        return (
            <Contest key = {contest[1]} site = {contest[0]} name = {contest[1]} time = {contest[2]} countdown = {contest[3]}/>
        );
    });
    
    function applySorting(col) {
        var nextContests = contests.slice();
        nextContests.sort(function(x, y) {
            if(x[col] < y[col]) return -1;
            else if(x[col] === y[col]) return 0;
            else return 1;
        });
        setContests(nextContests);
    }

    return (
        <table className = "table table-hover mb-0">
            <thead>
                <tr>
                    <th onClick = {() => applySorting(0)}>Site</th>
                    <th onClick = {() => applySorting(1)} style = {{width: "500px"}}>Name</th>
                    <th onClick = {() => applySorting(2)} >Time (UTC)</th>
                    <th onClick = {() => applySorting(3)} >Countdown</th>
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