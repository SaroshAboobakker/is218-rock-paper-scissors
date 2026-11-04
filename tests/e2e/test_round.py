"""Real-browser round and replay using the actual rules and HTTP server."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_player_can_play_a_round_and_replay(page: Page, live_server, monkeypatch):
    """Two separate submissions show their actual outcomes in the browser."""
    computer_moves = iter(("paper", "paper"))
    monkeypatch.setattr(web.random, "choice", lambda _moves: next(computer_moves))
    page.goto(live_server)

    page.get_by_role("button", name="Rock", exact=True).click()
    expect(page.get_by_label("This round’s choices")).to_contain_text("Rock")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Paper")
    expect(page.locator('[data-outcome="lose"]')).to_be_visible()
    expect(page.get_by_role("heading", name="Computer wins")).to_be_visible()

    page.get_by_role("button", name="Scissors", exact=True).click()
    expect(page.get_by_label("This round’s choices")).to_contain_text("Scissors")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Paper")
    expect(page.locator('[data-outcome="win"]')).to_be_visible()
    expect(page.get_by_role("heading", name="You win!")).to_be_visible()
