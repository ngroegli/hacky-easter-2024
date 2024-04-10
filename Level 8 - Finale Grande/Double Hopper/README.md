# Challenge "Double Hopper"
![Banner Image](banner.jpg)

Double hopper will not show you a double whopper.

[Double Hopper web site](http://ch.hackyeaster.com:2406/)

Note: The service is restarted every hour at x:00.

[config.txt](config.txt)

# Solution
The [config.txt](config.txt) file suggests a HAProxy web server configuration. Searching for path configuration vulnerabilities for that kind of server suggests the following possible exploit: https://jfrog.com/blog/critical-vulnerability-in-haproxy-cve-2021-40346-integer-overflow-enables-http-smuggling/

WORK:

    <img src="/static/flag-55a8408e060a25096eb95be8b86f3a2c66f91193.png"/>

## The flag
    he2024{}
