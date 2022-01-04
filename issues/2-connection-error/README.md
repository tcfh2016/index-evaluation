## ConnectionError

It worked yesterday, but failed now when run the script on my working laptop with below prompt:

```
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='danjuanfunds.com', port=443): Max retries exceeded with url: /djmodule/value-center?channel=1300100141 (Cause
d by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001973B47D0D0>: Failed to establish a new connection: [WinError 10060] A connection attempt fail
ed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond'))
```

Seems like one connection error, but I can access the link by web browser. I got the same result when tested with `baidu.com`, so it can confirmed that the proxy seems to be needed.
