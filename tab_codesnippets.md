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
