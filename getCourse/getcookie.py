import requests

# 根据上一次请求的响应中的返回的cookie来进行本次请求同时返回这次请求的响应的set-cookie，有点递归那味了
def get_next_cookie(current_url,last_cookie):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "user-agent": "Mozilla/5.0 (Windows NT10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "cookie": last_cookie
    }
    response = requests.get(current_url, headers=headers)
    cookie_str = ""  # 存cookie
    for cookie in response.cookies:
        cookie_str += cookie.name + '=' + cookie.value + ';'
    response.close()
    return cookie_str





