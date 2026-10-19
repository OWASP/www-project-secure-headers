/*
Script to dynamically handle the redirection to the "/index" path depending on the initial domain requested:
- The GitHub page
- The custom sub domain
*/
const owaspSubDomain = "secure-headers-project.owasp.org";
const githubPageSubDomain = "owasp.github.io";
const sourceDomain = window.location.hostname;
const oshpFullUrl = `https://${owaspSubDomain}/index/`;

if (sourceDomain === owaspSubDomain) {
    console.info(`Visitor come from the custom sub domain so redirect it to '${oshpFullUrl}'.`);
    window.location.replace(oshpFullUrl);
} else if (sourceDomain === githubPageSubDomain) {
    console.info(`Visitor come from the GH page domain so redirect it to '${oshpFullUrl}'.`);
    window.location.replace(oshpFullUrl);
} else {
    console.error("The source domain is not an expected one so do nothing !");
}
