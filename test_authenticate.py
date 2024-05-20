from playwright.sync_api import Page, BrowserContext, expect
from shuiyuan.parser import parse_cookies
from shuiyuan.const import *
import pytest
import re

@pytest.mark.order(1)
def test_authenticate(context: BrowserContext, page: Page):

    context.add_cookies(parse_cookies(COOKIES))

    _ = page.goto("https://shuiyuan.sjtu.edu.cn")

    expect(page).to_have_title(re.compile("水源社区"))

    _ = context.storage_state(path="auth/state.json")
