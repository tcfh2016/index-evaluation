## 403 Forbidden

When I tried to use the `requests` module to fetch the web page which contains the data set, I got the "403(Forbidden)":

```
r = requests.get('https://danjuanfunds.com/djmodule/value-center?channel=1300100141')
print(r.status_code ) # 403
```

After read [Python Requests.get访问网页403错误](https://zhuanlan.zhihu.com/p/35853860), seems the server can detect if the request is from a web scraper or not, so we need to build one header to simulate the real web browser.

The more content about the header building can be also found here [定制请求头](https://docs.python-requests.org/zh_CN/latest/user/quickstart.html#id6)。


Reference:

- [HTTP 状态码](https://www.runoob.com/http/http-status-codes.html)
