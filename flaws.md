## FLAW 1: Cross-Site Request Forgery (CSRF)
# Exact source links pinpointing flaw 1:
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myapp/views.py#L36
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myapp/views.py#L53
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myapp/templates/add_entry.html#L7

# Description of flaw 1:
The Cross-Site Request Forgery security risk, or CSRF for short, occurs when an attcker tricks a victim into submitting a malicious request. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application[1]
In the example django-application, the built in is_valid() function would normally check for a valid CSRF token. However, because the function is not used to validate the form -parameter and because the the html tag {% csrf_token %} is missing, the entry adding -functionality could be compromised by an attacker. It should be also noted that because the django framework expects the csrf token to be included in POST requests, one has to add the decorator @csrf_exempt to the function to allow posting without the tag, meaning that by default, applications that utilize the framework are relatively safe from this security risk.

# How to fix it:
The CSRF security risk can be mitigated in the context of the django application by using the html tag {% csrf_token %} with POST requests, and by checking the posted content with the is_valid() function, as well as making sure not to include the @csrf_exempt -decorator in functions that handle POST requests.


## FLAW 2: Server side request forgery (SSRF)
# Exact source links pinpointing flaw 2:
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myapp/views.py#L51-L52
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myapp/views.py#L21-L34

# Description of flaw 2:
Server side request forgery risk, or SSRF for short, can occur when a web application is fetching a remote resource without validating the user-supplied URL. It allows an attacker to force the application to send a request with a malicious intent to an unexpected destination, even when protected by a firewall, VPN, or another type of network access control list (ACL).[2]. In the example application, the user has the ability add an image to their entry by providing the image url. The flaw is that there is a lack of a validating mechanism that makes sure that the url is given in an appropriate format or whether the url is identified as a malicious url.

# How to fix it:
The SSRF flaw can be fixed in this case by including a function is_valid_url() that takes the given url as its parameter. The function then checks whether the url starts with 'http://' or 'https://', and whether the given url is on a list of identified malicious url’s. It should be noted that in the application the currently listed malicious url’s are manually added and found at https://openphish.com/ that list url’s used for phishing, but in a larger scale application a separate API could be used to check url’s against a variety of security databases. If the function does not return False, the image url is handled accordingly. If the function returns False, the user is given an error response stating that the url they have provided is invalid.


## FLAW 3: Vulnerable and outdated components
# Exact source links pinpointing flaw 3:
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/requirements.txt#L1

# Description of flaw 3:
The flaw of Vulnerable and outdated components can occur, for example, if the versions of all used components are not known, the software is vulnerable, unsupported, or out of date, or if potential vulnerabilities are not scanned for regularly and the security bulletins related to the components in use are not followed.[3] In the example application, such vulnerability is made possible by the fact that the reqired version of the Django is 4.0.0 which included an SQL injection vulnerability that was fixed in a later patch [4]. This means that if the user installs the application according to the instructions, their become vulnerable to SQL injection risk that have been identified and fixed in later release versions.

# How to fix it:
In this case, the flaw can be fixed by making sure that the requirements.txt document includes the latest version of django as one of the dependencies instead af a specific version, especially if that specific version has identified security flaws. In the case of the example application, the first row of the requirements.txt file should be ignored as it is the insecure Django version, and should be replaced by the second row that is hashed out, that makes sure a relatively new version is used.

## FLAW 4: Security misconfiguration
# Exact source link pinpointing flaw 4:
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myproject/settings.py#L27

# Description of flaw 4:
Security misconfiguration can occur when lacking appropriate security hardening across any part of the application stack or improperly configured permissions on cloud services, when having unnecessary features enabled or installed, or when default accounts and their passwords are still enabled and unchanged, just to name a few examples.[5] In the example application, there is a security misconfiguration in the settings, where DEBUG is set to True. Having the DEBUG setting enabled in a production environment can expose sensitive information, such as stack traces and internal configuration details, to potential attackers. This information is useful for understanding the inner workings of the application and can be exploited to identify and target vulnerabilities.

# How to fix it:
The fix to the security issue cuased by the DEBUG setting is to replace the “DEBUG = True” with “DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'” This makes sure that if the DEBUG variable is not set, it defaults to 'False', which in turn allows control of the DEBUG setting using an environment variable.

## FLAW 5: Cryptographic failure
# Exact source link pinpointing flaw 5:
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myapp/views.py#L54-L57
https://github.com/hakkajoe/cyber-security-course-app/blob/main/myproject/myapp/login.py
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myproject/settings.py#L86-L88

# Description of flaw 5:
Cryptographic failures are security flaws where sensitive data is exposed due to failures related to cryptography or lack of cryptography. This can happen, for example, by storing sensitive data unnecessarily, by not encrypting sensitive data or by not using up-to-date and strong standard algorithms, protocols or keys.[6] In the example application, a cryptographic failure occurs due to the fact that when creating a new user, the given password is not hashed, but rather saved as it is given with “user.password = (form.cleaned_data['password1'])”. Additionally, because Django expects passwords to be hashed when logging in with them, a custom authentication backend has to be created that can authenticate users with unhashed passwords. Finally, this custom backend must also be listed in settings.

# How to fix it:
The flaw can be fixed by using django’s built in save() function, that takes care of password hashing. Therefore, by creating the user paramter with “user = form.save()”, the password creation is handled securely and the parameter can be used securely in the following rows. Alternatively, hashing can be done by using the user.set_password() function.

## FLAW 6: Injection
# Exact source link pinpointing flaw 6:
https://github.com/hakkajoe/cyber-security-course-app/blob/441c62c0edf6aac2f5b9982b830d8990475fe4e5/myproject/myapp/views.py#L16

# Description of flaw 6:
Injections are security flaws where user-given data is not validated, filtered, or sanitized appropriately, and where hostile data is used within object-relational mapping (ORM) search parameters to extract sensitive records[7]. In the example application, injection can occur when retrieving user added entries since the search query is not given in a sanitized format.

# How to fix it:
The security flaw can be fixed by using the .filter() function, which is a standard Django ORM query which is safe from SQL injection, as Django's query builder properly escapes and sanitizes inputs. Using it ensures that the given sql query does not lead to sql injection attacks.


## References:
[1] Cross Site Request Forgery (CSRF). DOI: https://owasp.org/www-community/attacks/csrf
[2] Server-Side Request Forgery (SSRF). DOI: https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/
[3] Vulnerable and Outdated Components. DOI: https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/
[4] Django fixes SQL Injection vulnerability in new releases. DOI: https://www.bleepingcomputer.com/news/security/django-fixes-sql-injection-vulnerability-in-new-releases/
[5] Security Misconfiguration, DOI: https://owasp.org/Top10/A05_2021-Security_Misconfiguration/
[6] Cryptographic Failures, DOI: https://owasp.org/Top10/A02_2021-Cryptographic_Failures/
[7] Injection, DOI: https://owasp.org/Top10/A03_2021-Injection/
