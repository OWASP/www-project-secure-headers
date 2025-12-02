/* Script to allow to direct link a section (header) into a tab (div). */
function handleDirectLink() {
    if (window.location.hash) {
        //Format expected is [TAB-ID]_[HEADER-ID-INSIDE-TAB]
        let directLocationRef = window.location.hash;
        const validationRegex = new RegExp("^#[a-z0-9\-]{1,100}_[a-z0-9\-]{1,100}$");
        //Ensure that the directLink respect the syntax
        if (validationRegex.test(directLocationRef)) {
            directLocationRef = directLocationRef.substring(1);//Remove the starting dash character
            let parts = directLocationRef.split("_");
            let tabLocation = parts[0].substring(4) + "-link";//remove the "-div" prefix and add the "-link" suffix
            let headerLocation = parts[1];
            console.debug(`[DirectLinkHandler] Move to tab '${tabLocation}' on header '${headerLocation}'.`);
            //Retrieve the target TAB that is a link to a DIV and trigger a click
            let tabLink = document.getElementById(tabLocation)
            if (typeof tabLink !== "undefined") {
                tabLink.click();
                //Now move to the target header that have a link with a href to it
                let links = document.querySelectorAll("a");
                let headerLink = null;
                links.forEach(function (lnk) {
                    if (lnk.href.endsWith(`#${headerLocation}`) && headerLink === null) {
                        headerLink = lnk;
                    }
                });
                if (headerLink !== null) {
                    setTimeout(() => { headerLink.click(); console.debug(`[DirectLinkHandler] Move performed.`); }, "2000");
                    console.debug(`[DirectLinkHandler] Move scheduled.`)
                } else {
                    console.warn(`[DirectLinkHandler] Header tag not found.`);
                }
            } else {
                console.warn(`[DirectLinkHandler] Tab link not found.`);
            }
        } else {
            console.warn("[DirectLinkHandler] Direct link does not match the validation regex.")
        }
    }
}

window.addEventListener("load", function () {
    const isFirefox = (navigator.userAgent.indexOf("Firefox") !== -1);
    if (isFirefox) {
        //Fix for issue "github.com/OWASP/www-project-secure-headers/issues/251"
        console.debug(`[DirectLinkHandler] Firefox so delayed call to let the page load.`);
        setTimeout(() => { handleDirectLink(); }, "3000");
    } else {
        console.debug(`[DirectLinkHandler] Not Firefox so direct call.`);
        handleDirectLink();
    }
});
