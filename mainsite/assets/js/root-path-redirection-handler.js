/*
Script to dynamically handle the redirection to the "/index" path depending on the initial domain requested:
- The GitHub page
- The custom sub domain
*/
const owaspSubDomain = "secure-headers-project.owasp.org";
const githubPageSubDomain = "owasp.github.io";
const sourceDomain = window.location.hostname;

if (sourceDomain === owaspSubDomain) {
    const targetLocation = `https://${owaspSubDomain}/index/`;
    console.info(`Visitor come from the custom sub domain so redirect it to '${targetLocation}'.`);
    window.location.replace(targetLocation);
} else if (sourceDomain === githubPageSubDomain) {
    const targetLocation = `https://${githubPageSubDomain}/secure-headers-project/index/`;
    console.info(`Visitor come from the GH page domain so redirect it to '${targetLocation}'.`);
    window.location.replace(targetLocation);
} else {
    console.error("The source domain is not an expected one so do nothing !");
}
