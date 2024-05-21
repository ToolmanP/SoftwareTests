import re
from playwright.sync_api import expect, Playwright
from shuiyuan.const import *


def test_dropdown(playwright: Playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    _ = page.goto(TOPIC)
    expect(page).to_have_title(re.compile("水源社区"))

    dropdown_header = page.query_selector('summary.select-kit-header')

    # get current value
    current_value = dropdown_header.get_attribute('data-value')
    next_value = str((int(current_value) + 1) % 4)

    # open dropdown
    dropdown_header.click()
    dropdown_list = page.query_selector('ul.select-kit-collection')
    current_option_name = dropdown_list.query_selector(f'li[data-value="{current_value}"]').query_selector('.name').text_content()
    next_option = dropdown_list.query_selector(f'li[data-value="{next_value}"]')
    next_option_name = next_option.query_selector('.name').text_content()
    next_option.click()

    # output
    output_text = f"之前选中项为: {current_option_name}\n当前选中项为: {next_option_name}"
    reply(page, output_text)
    locator = page.get_by_text(output_text)
    expect(locator.first).to_be_visible()


def reply(page, content):
    page.get_by_role("button", name="回复").first.click()
    page.get_by_placeholder(
        """在此处输入。使用 Markdown、BBCode 或 HTML 进行格式化。拖动或粘贴图片。

请对其他社区成员保持友善。
你的回复是否有益于交流？
欢迎有建设性的批评，但是请对事不对人。"""
    ).fill(content)
    page.get_by_role("button", name="发送消息").first.click()
