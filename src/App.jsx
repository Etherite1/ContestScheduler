import { useState, useEffect } from 'react'
import './App.css'
import SiteCheckbox from './SiteCheckbox.jsx'
import dayjs from 'dayjs'

function Contest({site, name, time}) // TODO: link
{
    function getLogo(site)
    {
        if(site == "CC") return "logos/cc.png";
        else if(site == "LC") return "logos/lc.png";
        else if(site == "CF") return "logos/cf.png";
        else if(site == "AC") return "logos/ac.png"
    }

    const [countdown, setCountdown] = useState(getRemainingTime(time));

    useEffect(() => {
        const intervalId = setInterval(() => {
            setCountdown(getRemainingTime(time));
        }, 1000);
        return () => clearInterval(intervalId);
    },[time])

    function getRemainingTime(iso8601) 
    {
        const timestampDjs = dayjs(iso8601); // dayjs obj created from isostring
        const nowDjs = dayjs();
        const seconds = timestampDjs.diff(nowDjs, 'seconds') % 60;
        const minutes = timestampDjs.diff(nowDjs, 'minutes') % 60;
        const hours = timestampDjs.diff(nowDjs, 'hours') % 24;
        const days = timestampDjs.diff(nowDjs, 'days');

        return {
            seconds: seconds,
            minutes: minutes,
            hours: hours,
            days: days
        };
    }
    return (
        <tr>
            <td><img src = {getLogo(site)} height = "50px" width = "auto" /></td>
            <td>{name}</td>
            <td>{time}</td>
            <td>
                <span>{countdown.days}d</span>
                <span>{countdown.hours}h</span>
                <span>{countdown.minutes}m</span>
                <span>{countdown.seconds}s</span>
            </td>
        </tr>
    );
}

function ContestTable({displayedSites}) 
{
    const [contests, setContests] = useState([]); // get from backend
    const serverURL = "http://167.71.159.133:8000/"
    const testServerURL = "http://127.0.0.1:5000/"
    const GetAPIData = () => {
        console.log("Queried :)")
        fetch(testServerURL)
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
                    next_contests.push(curr_contest);
                }
                setContests(next_contests);
            })
    };

    useEffect(() => {GetAPIData()}, []);

    useEffect(() => {
        const intervalId = setInterval(() => {
            GetAPIData();
        }, 300000);
        return () => clearInterval(intervalId);
    }, []);
    
    // useEffects -> update state and rerender child components

    var contestComponents = contests.map((contest) => { // contest is array containing event info, within array contests
        if(!displayedSites.get(contest[0])) return; // checking whether contest is toggled to false (checkbox unchecked)
        return (
            <Contest key = {contest[1]} 
            site = {contest[0]} 
            name = {contest[1]} 
            time = {contest[2]} />
        ); 
    });
    
    function applySorting(col) { // sorts specified col
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
                    <th onClick = {() => applySorting(2)} >Countdown</th>
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
    siteNames.set("AC", false);
    const [displayedSites, setDisplayedSites] = useState(siteNames);
    
    function onCheck(siteName)
    {
        const nextMap = new Map(displayedSites);
        nextMap.set(siteName, !displayedSites.get(siteName));
        setDisplayedSites(nextMap);
    }

    const FilterBoxes = [...Array.from(displayedSites.keys())].map((site) => { // checkboxes, call onCheck()
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
                <ContestTable displayedSites = {displayedSites}/> {/*displayedSites is a map*/}
            </div>
        </div>
    );
}