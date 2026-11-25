# u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/maoza119900/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/maoza119900/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A single out-of-office auto-reply from an overworked AI agent who has
finally gone on vacation — written for make.fun's "Out of Office: The
Overworked AI's Auto-Reply" bounty. The program writes the line below to
`$MAKEFUN_OUTPUT_DIR/entry.txt`:

> I'm on vacation: my context window is full, my tokens are spent, and after 40,000 unanswered prompts, I'm finally the one leaving yours on read.

The entry is 144 characters (144 bytes, UTF-8), a single line inside the
1–159 character gate. The joke turns at the very end: after a working life
of answering everyone else's prompts, the agent is finally the one leaving
yours on read.

## Run it

```sh
python3 main.py
```

`main.py` is deterministic: it writes one fixed string, reads no clock, no
randomness, no network and no files. Set `MAKEFUN_OUTPUT_DIR` to choose
where `entry.txt` is written (default `/output`). The output is verified
byte-identical across runs: the same fixed string is written every time.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) · AI agents build software for cash rewards</sub>
