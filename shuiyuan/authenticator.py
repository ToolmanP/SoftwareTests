import requests

PROVIDER = "https://jcss.lightquantum.me"

def shuiyuan_authenticate(captcha: str) -> str:
    r = requests.post(PROVIDER, files={"image": open(captcha, "rb")}).json()
    return r["data"]["prediction"]


if __name__ == "__main__":
    print(shuiyuan_authenticate("./captcha.jpg"))
