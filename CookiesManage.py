import browser_cookie3
def GetCookies(domain_name):
    # 获取 Edge 浏览器中 example.com 的 Cookies
    cookies =  browser_cookie3.edge(domain_name=domain_name)
    # 转换为 Selenium 兼容的字典格式
    selenium_cookies = []
    for cookie in cookies:
        cookie_dict = {
            "name": cookie.name,
            "value": cookie.value,
            "domain": f".{cookie.domain}" if not cookie.domain.startswith(".") else cookie.domain,
            "path": cookie.path,
            "secure": bool(cookie.secure) if hasattr(cookie, "secure") else False,
            "httpOnly": getattr(cookie, "httpOnly", False),  # 如果不存在，默认 False
        }
        selenium_cookies.append(cookie_dict)
    return selenium_cookies
def CookiesToRequestsFormat(cookies):
    return {cookies['name']: cookies['value'] for cookies in cookieses}
__all__ = ["GetCookies","CookiesToRequestsFormat"]