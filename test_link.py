import re
from playwright.sync_api import expect, Playwright
from shuiyuan.const import *


def test_link(playwright: Playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    _ = page.goto(TOPIC)
    expect(page).to_have_title(re.compile("水源社区"))

    link_element = page.query_selector('a.onebox[href="https://www.sjtu.edu.cn/"]')
    with page.expect_popup() as popup_info:
        link_element.click()
    new_page = popup_info.value

    new_page.wait_for_load_state()
    new_page_title = new_page.title()

    page.get_by_role("button", name="回复").first.click()
    page.get_by_placeholder(
        """在此处输入。使用 Markdown、BBCode 或 HTML 进行格式化。拖动或粘贴图片。

请对其他社区成员保持友善。
你的回复是否有益于交流？
欢迎有建设性的批评，但是请对事不对人。"""
    ).fill(f"检测到新页面标题为: {new_page_title}")
    page.get_by_role("button", name="发送消息").first.click()
    locator = page.get_by_text(f"检测到新页面标题为: {new_page_title}")
    expect(locator.first).to_be_visible()
