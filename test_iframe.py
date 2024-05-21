import re
from playwright.sync_api import expect, Playwright
from shuiyuan.const import *


def test_iframe(playwright: Playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    _ = page.goto(TOPIC)
    expect(page).to_have_title(re.compile("水源社区"))

    iframe = page.query_selector("iframe.onebox-bilibili-iframe")
    iframe_content = iframe.content_frame()
    iframe_title_element = iframe_content.locator(".bpx-player-top-left-title-text")
    iframe_title = iframe_title_element.text_content()

    page.get_by_role("button", name="回复").first.click()
    page.get_by_placeholder(
        """在此处输入。使用 Markdown、BBCode 或 HTML 进行格式化。拖动或粘贴图片。

请对其他社区成员保持友善。
你的回复是否有益于交流？
欢迎有建设性的批评，但是请对事不对人。"""
    ).fill(f"检测到iframe内容标题为: {iframe_title}")
    page.get_by_role("button", name="发送消息").first.click()
    locator = page.get_by_text(f"检测到iframe内容标题为: 【官方 MV】Never Gonna Give You Up - Rick Astley")
    expect(locator.first).to_be_visible()

