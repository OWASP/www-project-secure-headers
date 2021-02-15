import requests


#API for which Security Response Headers to Check. Please change to yours. Supports both Get and Post Mehod.
#Response headers are checked as mentioned here: https://owasp.org/www-project-secure-headers/
#Change the url,postUrl and postjson to your own API.

url = 'https://api.github.com/repos/owasp/www-project-secure-headers'
postUrl = 'http://api.forismatic.com/api/1.0/'
postJson = {'method': 'getQuote', 'format': 'json', 'key': '457653', 'language': 'en'}

#Security Response Headers Expected Value. Change as per your expected API value.
StrictTransportSecurity_ExpectedValue = 'max-age=31536000; includeSubdomains; preload'
XFrameOptions_ExpectedValue = 'deny'
XContentTypeOptions_ExpectedValue = 'nosniff'
ContentSecurityPolicy_ExpectedValue = 'default-src \'none\''
XssProtection_ExpectedValue = '1; mode=block'
XPermittedCrossDomainPolicies_ExpectedValue = 'none'
ReferrerPolicy_ExpectedValue = 'origin-when-cross-origin, strict-origin-when-cross-origin'
FeaturePolicy_ExpectedValue = 'vibrate \'none\'; geolocation \'none\''


#Function which checks for expected security response header exists or not.
def checkSecurityHeaders (securityHeader):
    
    if 'Strict-Transport-Security' in securityHeader:
        StrictTransportSecurityValue = securityHeader['Strict-Transport-Security']
        if StrictTransportSecurityValue == StrictTransportSecurity_ExpectedValue:
            print(f'Security Headers:Strict-Transport-Security is as excepted and equal to {StrictTransportSecurityValue}')
        else:
            print(f'Security Headers:Strict-Transport-Security is NOT Correct,{StrictTransportSecurityValue}')

    if 'X-Frame-Options' in securityHeader:
        XFrameOptionsValue = securityHeader['X-Frame-Options']
        if XFrameOptionsValue == XFrameOptions_ExpectedValue:
            print(f'Security Headers:X-Frame-Options is as excepted and equal to {XFrameOptionsValue}')
        else:
            print(f'Security Headers:X-Frame-Options is NOT Correct,{XFrameOptionsValue}')

    if 'X-Content-Type-Options' in securityHeader:
        XContentTypeOptionsValue = securityHeader['X-Content-Type-Options']
        if XContentTypeOptionsValue == XContentTypeOptions_ExpectedValue:
            print(f'Security Headers:X-Content-Type-Options is as excepted and equal to {XContentTypeOptionsValue}')
        else:
            print(f'Security Headers:X-Content-Type-Options is NOT Correct,{XContentTypeOptionsValue}')        

    if 'Content-Security-Policy' in securityHeader:
        ContentSecurityPolicyValue = securityHeader['Content-Security-Policy']
        if ContentSecurityPolicyValue == ContentSecurityPolicy_ExpectedValue:
            print(f'Security Headers:Content-Security-Policy is as excepted and equal to {ContentSecurityPolicyValue}')
        else:
            print(f'Security Headers:Content-Security-Policy is NOT Correct,{ContentSecurityPolicyValue}')        

    if 'X-XSS-Protection' in securityHeader:
        XssProtectionValue= securityHeader['X-XSS-Protection']
        if XssProtectionValue == XssProtection_ExpectedValue:
            print(f'Security Headers:X-XSS-Protection is as excepted and equal to {XssProtectionValue}')
        else:
            print(f'Security Headers:X-XSS-Protection is NOT Correct,{XssProtectionValue}')

    if 'X-Permitted-Cross-Domain-Policies' in securityHeader:
        XPermittedCrossDomainPolicies_Value= securityHeader['X-Permitted-Cross-Domain-Policies']
        if XPermittedCrossDomainPolicies_Value == XPermittedCrossDomainPolicies_ExpectedValue:
            print(f'Security Headers:X-Permitted-Cross-Domain-Policies is as excepted and equal to {XPermittedCrossDomainPolicies_Value}')
        else:
            print(f'Security Headers:X-Permitted-Cross-Domain-Policies is NOT Correct,{XPermittedCrossDomainPolicies_Value}')

    if 'Referrer-Policy' in securityHeader:
        ReferrerPolicy_Value= securityHeader['Referrer-Policy']
        if ReferrerPolicy_Value == ReferrerPolicy_ExpectedValue:
            print(f'Security Headers:Referrer-Policy is as excepted and equal to {ReferrerPolicy_Value}')
        else:
            print(f'Security Headers:Referrer-Policy is NOT Correct,{ReferrerPolicy_Value}')

    if 'Feature-Policy' in securityHeader:
        FeaturePolicy_Value= securityHeader['Feature-Policy']
        if FeaturePolicy_Value == FeaturePolicy_ExpectedValue:
            print(f'Security Headers:Feature-Policy is as excepted and equal to {FeaturePolicy_Value}')
        else:
            print(f'Security Headers:Feature-Policy is NOT Correct,{FeaturePolicy_Value}')


#Steps to execute API Security for Get Method.    
req = requests.get(url)
securityDict = req.headers
print(securityDict)
checkSecurityHeaders(securityDict)

#For Post Method, Send the request as below
#req = requests.post(postUrl,postJson)