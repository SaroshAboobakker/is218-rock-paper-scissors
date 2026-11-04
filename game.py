"""RPS-001: the rules students will build with AI. See SPEC.md."""


def determine_winner(player: str, computer: str) -> str:
    """Return the round result from the player's perspective."""
    if player == computer:
        return "tie"

    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    return "win" if winning_moves[player] == computer else "lose"
