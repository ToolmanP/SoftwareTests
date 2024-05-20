import re
from playwright.sync_api import expect, Playwright
from shuiyuan.const import *


def test_reply(playwright: Playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    _ = page.goto(TOPIC)
    expect(page).to_have_title(re.compile("水源社区"))
    page.get_by_role("button", name="回复").first.click()
    page.get_by_placeholder(
        """在此处输入。使用 Markdown、BBCode 或 HTML 进行格式化。拖动或粘贴图片。

请对其他社区成员保持友善。
你的回复是否有益于交流？
欢迎有建设性的批评，但是请对事不对人。"""
    ).fill("This is a playwright comment. 不要点赞。")
    page.get_by_role("button", name="发送消息").first.click()
    locator = page.get_by_text("This is a playwright comment. 不要点赞。")
    expect(locator.first).to_be_visible()

def test_reply_close(playwright: Playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    _ = page.goto(TOPIC)
    expect(page).to_have_title(re.compile("水源社区"))
    page.get_by_role("button", name="回复").first.click()
    page.get_by_placeholder(
        """在此处输入。使用 Markdown、BBCode 或 HTML 进行格式化。拖动或粘贴图片。

请对其他社区成员保持友善。
你的回复是否有益于交流？
欢迎有建设性的批评，但是请对事不对人。"""
    ).fill("This is a playwright comment. 不要点赞。")
    page.get_by_role("button", name="关闭").first.click()
    locator = page.get_by_text("您想对您的帖子做什么？").first
    expect(locator).to_be_visible()
    page.get_by_role("button", name="舍弃").first.click()
    locator = page.get_by_text("您想对您的帖子做什么？").first
    expect(locator).not_to_be_visible()
