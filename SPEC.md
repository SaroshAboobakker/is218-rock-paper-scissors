# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

Implement the specified one-round behavior in `game.py`. Keep the supplied page and server, reject unsupported or missing moves through the existing request validation, and add the nine unit outcomes, one real request/result check, and a real-browser round with replay. Use deterministic computer choices in request and browser tests, while exercising the actual rule function.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: add your own issue URL.
- Pull request / CI: add actual URLs when they exist.
- Implementation: [game.py](game.py), [tests/test_game.py](tests/test_game.py), and [tests/e2e/test_round.py](tests/e2e/test_round.py).
- Checks: `.venv/bin/python check.py` passed — Black (11 files unchanged), Pylint, 23 non-browser tests, and 6 Chromium tests. The student confirmed the starter page loaded and showed its unfinished notice before implementation; no manual post-implementation round has been reported yet. Automated browser evidence is in [tests/e2e/test_round.py](tests/e2e/test_round.py).
