---
title: bestpractices
displaytext: Best Practices
layout: null
tab: true
order: 5
tags: headers
---

# Best Practices

## Quickly check security HTTP headers for applications exposed on the Internet

The online tool [securityheaders.com](https://securityheaders.com) can be used to achieve that objective.

It returns the grade in the following HTTP response headers:

- **x-score**: Contains a Base64 encoded JSON object with the grade letter and its associated color name.
- **x-grade**: Contains the grade letter.

```shell
$ curl -v "https://securityheaders.com/?hide=on&followRedirects=on&q=https://mozilla.org"
> Trying 104.21.70.128:443...
> Connected to securityheaders.com (104.21.70.128) port 443
> ...
< HTTP/2 200
< date: Tue, 02 Mar 2021 17:29:23 GMT
< content-type: text/html; charset=UTF-8
< vary: Accept-Encoding
< x-score: eyJzY29yZSI6IkEiLCAiY29sb3VyIjoiZ3JlZW4ifQ==
< x-grade: A
< ...
```

Content of the **x-score** header value:

```shell
$ echo eyJzY29yZSI6IkEiLCAiY29sb3VyIjoiZ3JlZW4ifQ== | base64 -d
{"score":"A", "colour":"green"}
```

## Quickly check security HTTP headers for applications exposed internally

The portable cross-platform tool [Venom](https://github.com/ovh/venom) with the dedicated [test suites aligned with the OWASP Secure Headers Project](https://gist.github.com/righettod/f63548ebd96bed82269dcc3dfea27056) can be used to achieve that objective.

Use the following set of commands:

```shell
# Get Venom binary file from 
# https://github.com/ovh/venom/releases
# Get the YAML test suites from
# https://gist.github.com/righettod/f63548ebd96bed82269dcc3dfea27056
# Demonstration about usage available on
# https://gist.github.com/righettod/f63548ebd96bed82269dcc3dfea27056#gistcomment-3630811
$ venom run --var="target_site=https://mozilla.org" --var="logout_url=/logout" venom_security_headers_tests_suite.yml
• HTTP security response headers test suites (venom_security_headers_tests_suite.yml)
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
    • Feature-Policy SUCCESS
        [info] This header was split into Permissions-Policy and Document-Policy and will be considered deprecated once all impacted features are moved off of feature policy. (venom_security_headers_tests_suite.yml:152)
    • Public-Key-Pins SUCCESS
        [info] This header has been deprecated by all major browsers and is no longer recommended. Avoid using it, and update existing code if possible! (venom_security_headers_tests_suite.yml:164)
    • Expect-CT SUCCESS
        [info] This header will likely become obsolete in June 2021. Since May 2018 new certificates are expected to support SCTs by default. Certificates before March 2018 were allowed to have a lifetime of 39 months, those will all be expired in June 2021. (venom_security_headers_tests_suite.yml:175)
    • X-Xss-Protection SUCCESS
        [info] The X-XSS-Protection header has been deprecated by modern browsers and its use can introduce additional security issues on the client side. (venom_security_headers_tests_suite.yml:189)
    • SecurityHeaders-Rating SKIPPED
```
