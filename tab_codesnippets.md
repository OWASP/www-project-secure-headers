---
title: codesnippets
displaytext: Code Snippets
layout: null
tab: true
order: 5
tags: headers
---

# Code Snippets

🧾 The following code collection provides various code snippets to make working with HTTP security headers easier.

* [Convert a Permissions-Policy back to Feature-Policy](#convert-a-permissions-policy-back-to-feature-policy)
* [Test locally a Content-Security-Policy for weaknesses](#test-locally-a-content-security-policy-for-weaknesses)
* [Generate configuration code using the OSHP headers reference files](#generate-configuration-code-using-the-oshp-headers-reference-files)
* [Quickly check security HTTP headers](#quickly-check-security-http-headers)
* [Syntax for adding HTTP response headers on different web or application servers](#syntax-for-adding-http-response-headers-on-different-web-or-application-servers)

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
$ node code.js "default-src 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests"
[+] CSP to evaluate:
default-src 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests
[+] Evaluation results:
[Directive 'default-src' - Severity 50]: 'self' can be problematic if you host JSONP, Angular or user uploaded files.
```

## Generate configuration code using the OSHP headers reference files

The following _bash_ code snippet, leveraging [jq](https://stedolan.github.io/jq/), can be used to generate configuration code using the OSHP headers reference files.

💻 Code snippet and execution example:

```shell
# Generate the Nginx collection of instructions to add the recommended HTTP response headers
$ curl -sk https://owasp.org/www-project-secure-headers/ci/headers_add.json | jq -r '.headers[] | "add_header \(.name) \(.value);"'
add_header Cache-Control no-store, max-age=0;
add_header Clear-Site-Data "cache","cookies","storage";
add_header Cross-Origin-Embedder-Policy require-corp;
...
```

## Quickly check security HTTP headers

The portable cross-platform tool [Venom](https://github.com/ovh/venom) with the dedicated [OSHP Validator test suites aligned with the OWASP Secure Headers Project](https://github.com/oshp/oshp-validator) can be used.

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
```

## Syntax for adding HTTP response headers on different web or application servers

Use the following **user prompt** to leverage an "LLM as a Service" (LLMaaS) to generate corresponding configuration code snippet for the wanted web or application server:

```text
Generate the configuration code for the "[TARGET_APPLICATION_OR_WEB_SERVER_NAME]" server to set HTTP response security headers recommended by the OWASP Secure Headers Project (project website is "https://owasp.org/www-project-secure-headers/").

The list of HTTP response security headers recommended is available in a JSON file located here "https://raw.githubusercontent.com/OWASP/www-project-secure-headers/refs/heads/master/ci/headers_add.json".

Requirements:
- Parse the JSON file and extract all headers and their recommended values.
- Preserve header values exactly as defined in the JSON.
- Ensure the configuration overwrites any existing header values.
- Add comments indicating the purpose of each header.
- Do not include explanatory text outside the configuration block.
```

🔬 The user prompt proposed was tested against the following model:

* Google Gemini 3 Flash.
* OpenAI ChatGPT GPT-5.3.
* Anthropic Claude Sonnet 4.6.
* Mistral AI Large.

💡 The following value for the `[TARGET_APPLICATION_OR_WEB_SERVER_NAME]` placeholder can be used:

* `apache web`.
* `nginx`.
* `iis`.
