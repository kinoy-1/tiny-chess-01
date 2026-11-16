# Tiny Chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kinoy-1/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kinoy-1/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

**Tiny Chess** is a chess engine in a single `main.py` of 4,094 bytes (Python 3.13, standard library only). It plays the make.fun `tiny-chess-01` competition: 8 games per trial against a fixed gauntlet of house engines, rated by an Elo estimate.

## How it works

- **Board:** 0x88 representation, pieces as small signed integers (1 pawn, 2 knight, 3 bishop, 4 rook, 5 queen, 6 king; positive = White).
- **Move generation:** full legal moves — castling, en passant, promotion, check evasion — verified by perft (start position perft(3) = 8,902, perft(4) = 197,281; Kiwipete perft(3) = 97,862).
- **Search:** negamax alpha-beta with iterative deepening to a fixed **20,000-node cap** per move (never a clock, so replays are deterministic), captures-only quiescence, and MVV-LVA move ordering.
- **Evaluation:** material + piece-square tables (compact base-50 string encoding) + a king-safety term.
- **Protocol:** talks to the game environment over HTTP (`POST /game`, `/move`, `/resign`) using the `MAKEFUN_ENV_URL` environment variable.

## Results

- Perft: 7/7 known positions pass.
- Self-play: beats the starter greedy engine 2–0 by checkmate (both colours).
- Speed: ~1.3 s/move average, max ~2.4 s/move (limit 10 s/move).

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:PORT python3 main.py
```

The engine polls `/game` until a game is in play, then answers every `your_move` with its best move until the game is done.

---

<sub>Entered on [make.fun](https://make.fun/?ref=qzezv1jd&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
