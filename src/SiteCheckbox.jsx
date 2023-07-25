export default function SiteCheckbox({siteName, onCheck})
{
    return (
        <div className = "site-filter">
            <input type = "checkbox" onChange = {() => onCheck(siteName)} />{siteName}
        </div>
    );
}