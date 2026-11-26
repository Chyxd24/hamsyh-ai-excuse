"""The One-Line AI Excuse for Breaking Production (<=180 chars)

Writes one line to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = "I broke prod testing a fix for a bug nobody reported. It's back up - I just need you to approve the rollback, the forward-fix, and the retro doc. By standup."

assert 1 <= len(ENTRY) <= 180, len(ENTRY)
p = "/output/entry.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
with open(p, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ENTRY, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
