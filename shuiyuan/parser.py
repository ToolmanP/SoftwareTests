def parse_cookies(cookies: str) -> list[dict]:
    results = []
    for item in cookies.split(";"):
        kvs = item.strip().split("=")
        results.append({"name": kvs[0], "value": kvs[1], "url": "https://shuiyuan.sjtu.edu.cn"})
    return results
