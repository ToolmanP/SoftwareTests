# 水源社区GUI Playwright 测试

## 使用方法

登录水源社区新建一个私信 并将私信话题的URL以及COOKIES 填入 `shuiyuan/const.py` 中 

用例可见`test_authenticate.py`以及`test_reply.py`

使用`setup.sh` 安装依赖文件

用例运行
`pytest test_authenticate.py`

* 测试iframe需要先发帖，内容为bilibili视频链接，比如
`https://www.bilibili.com/video/BV1GJ411x7h7`
* 测试link需要先发帖，内容为交大中文门户网站链接，具体为`https://www.sjtu.edu.cn/`
