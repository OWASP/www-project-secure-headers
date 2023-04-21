---
title: codesnippets
displaytext: Code Snippets
layout: null
tab: true
order: 7
tags: headers
---

# Code Snippets

🧾 The following code collection provides various code snippets to make working with HTTP security headers easier.

* [Convert a Permissions-Policy back to Feature-Policy](#convert-a-permissions-policy-back-to-feature-policy)
* [Test locally a Content-Security-Policy for weaknesses](#test-locally-a-content-security-policy-for-weaknesses)
* [Generate configuration code using the OSHP headers reference files](#generate-configuration-code-using-the-oshp-headers-reference-files)
* [Quickly check security HTTP headers for applications exposed on the Internet](#quickly-check-security-http-headers-for-applications-exposed-on-the-internet)
* [Quickly check security HTTP headers for applications exposed internally](#quickly-check-security-http-headers-for-applications-exposed-internally)

## Convert a Permissions-Policy back to Feature-Policy

As the [Permissions-Policy](https://github.com/w3c/webappsec-permissions-policy/blob/main/permissions-policy-explainer.md) header is still in development and is [not yet well supported](https://caniuse.com/permissions-policy), it can be interesting to use the two formats to increase the coverage of browsers according to their support level for **Permissions-Policy** and **[Feature-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy)** policy headers.

The following _python3_ code snippet can be useful to achieve such conversion.

📑 Source for the conversion rules was this [one](https://github.com/w3c/webappsec-permissions-policy/blob/main/permissions-policy-explainer.md#appendix-big-changes-since-this-was-called-feature-policy).

💻 Code snippet:

```python
permissions_policy = 'fullscreen=(), geolocation=(self "https://game.com" "https://map.example.com"), gyroscope=(self), usb=*'
feature_policy_directives = []
# Collect directives
permissions_policy_directives = permissions_policy.split(",")
# Process each directive
for permissions_policy_directive in permissions_policy_directives:
    # Remove leading and trailing spaces
    directive = permissions_policy_directive.strip(" ")
    # Remove all double quotes
    directive = directive.replace("\"", "")
    # Replace disabling expression () by the corresponding one in Feature-Policy
    directive = directive.replace("()", "'none'")
    # Quote keywords: self
    directive = directive.replace("self", "'self'")
    # Replace the equals affectation character by a space
    directive = directive.replace("=", " ")
    # Remove parenthesis
    directive = directive.replace("(", "").replace(")", "")
    # Add the current directive to the collection
    feature_policy_directives.append(directive)
# Convert the collection of directives to a string with ; as directives separator
feature_policy = "; ".join(feature_policy_directives)
print(feature_policy)
```

💻 Execution example:

```shell
$ python code.py
fullscreen 'none'; geolocation 'self' https://game.com https://map.example.com; gyroscope 'self'; usb *
```

## Test locally a Content-Security-Policy for weaknesses

It can be interesting to validate locally a **Content-Security-Policy** for presence of weaknesses prior to apply it on deployed web applications.

The following _JavaScript_ code snippet can be useful to achieve such validation by leveraging the [csp-evaluator](https://github.com/google/csp-evaluator) NPM module provided by Google.

💻 Code snippet:

```javascript
import {CspEvaluator} from "csp_evaluator/dist/evaluator.js";
import {CspParser} from "csp_evaluator/dist/parser.js";

const args = process.argv.slice(2)
if(args.length == 0){
    console.error("[!] Missing CSP!");
}else{
    const csp = args[0]
    console.info(`[+] CSP to evaluate:\n${csp}`);
    const parsed = new CspParser(csp).csp;
    console.info(`[+] Evaluation results:`);
    const results = new CspEvaluator(parsed).evaluate();
    results.forEach(elt => {
        let info = `[Directive '${elt.directive}' - Severity ${elt.severity}]: ${elt.description}`;
        console.info(info);
    });
}
```

💻 Execution example:

```shell
$ node code.js "default-src 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content"
[+] CSP to evaluate:
default-src 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content
[+] Evaluation results:
[Directive 'default-src' - Severity 50]: 'self' can be problematic if you host JSONP, Angular or user uploaded files.
```

## Generate configuration code using the OSHP headers reference files

The following _bash_ code snippet, leveraging [jq](https://stedolan.github.io/jq/), can be used to generate configuration code using the OSHP headers reference files.

💻 Code snippet and execution example:

```shell
# Generate the Nginx collection of instructions to add the recommanded HTTP response headers
$ curl -sk https://owasp.org/www-project-secure-headers/ci/headers_add.json | jq -r '.headers[] | "add_header \(.name) \(.value);"'
add_header Cache-Control no-store, max-age=0;
add_header Clear-Site-Data "cache","cookies","storage";
add_header Cross-Origin-Embedder-Policy require-corp;
...
```

## Quickly check security HTTP headers for applications exposed on the Internet

The online tool [securityheaders.com](https://securityheaders.com) can be used to achieve that objective.

Even if the API is not free, it is possible to leverage it in a free way. Indeed, the following **DIV** with the class **score**, contains the rating letter and its associated rating color:

```html
<div class="score"><div class="score_green"><span>A</span></div></div>
```

💻 Code snippet and execution example:

```shell
$ curl -s "https://securityheaders.com/?hide=on&followRedirects=on&q=https://mozilla.org" | grep -E '<div\s+class="score_[a-z]+">.*</div>'
<div class="score_green"><span>A</span></div>
# Parse the HTML of the DIV of the score to get the rating code directly
$ curl -s "https://securityheaders.com/?hide=on&followRedirects=on&q=https://mozilla.org" | grep -E '<div\s+class="score_[a-z]+">.*</div>' | sed -e 's/.*<span>\(.\+\)<\/span.*/\1/'
A
```

## Quickly check security HTTP headers for applications exposed internally

The portable cross-platform tool [Venom](https://github.com/ovh/venom) with the dedicated [OSHP Validator test suites aligned with the OWASP Secure Headers Project](https://github.com/oshp/oshp-validator).

💻 Use the following example set of commands:

```shell
$ venom run --var="target_site=https://mozilla.org" --var="logout_url=/logout" tests_suite.yml
• HTTP security response headers test suites
    • Strict-Transport-Security SUCCESS
    • X-Frame-Options SUCCESS
    • X-Content-Type-Options SUCCESS
    • Content-Security-Policy FAILURE
    • X-Permitted-Cross-Domain-Policies SUCCESS
    • Referrer-Policy SUCCESS
    • Clear-Site-Data SUCCESS
    • Cross-Origin-Embedder-Policy SUCCESS
    • Cross-Origin-Opener-Policy SUCCESS
    • Cross-Origin-Resource-Policy SUCCESS
    • Permissions-Policy SUCCESS    
    • Cache-Control SUCCESS    
    • Feature-Policy SUCCESS
        [info] This header was split into Permissions-Policy and Document-Policy and will be considered deprecated once all impacted features are moved off of feature policy.
    • Public-Key-Pins SUCCESS
        [info] This header has been deprecated by all major browsers and is no longer recommended. Avoid using it, and update existing code if possible!
    • Expect-CT SUCCESS
        [info] This header will likely become obsolete in June 2021. Since May 2018 new certificates are expected to support SCTs by default. Certificates before March 2018 were allowed to have a lifetime of 39 months, those will all be expired in June 2021.
    • X-Xss-Protection SUCCESS
        [info] The X-XSS-Protection header has been deprecated by modern browsers and its use can introduce additional security issues on the client side.
    • SecurityHeaders-Rating SKIPPED
```
