"""Unit rules and a real request using the RPS-001 implementation."""

# pytest injects fixtures by their function names; descriptive test names act
# as the test documentation.
# pylint: disable=redefined-outer-name,missing-function-docstring

import pytest

import app as web
import game


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_determine_winner_returns_expected_result(player, computer, expected):
    assert game.determine_winner(player, computer) == expected


@pytest.mark.integration
def test_real_round_request_displays_choices_and_result(monkeypatch):
    web.app.config.update(TESTING=True)
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    response = web.app.test_client().post("/", data={"move": "rock"})

    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert 'aria-label="This round’s choices"' in page
    assert '<p class="choice-label">You chose</p><p class="choice-value">Rock' in page
    assert (
        '<p class="choice-label">Computer chose</p><p class="choice-value">Paper'
        in page
    )
    assert "Computer wins" in page
    assert 'data-outcome="lose"' in page
    assert "game rules not built yet" not in page
