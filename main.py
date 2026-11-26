"""The One-Line AI Excuse for Breaking Production (<=180 chars)

Writes one line to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = "Production's down because I optimized the thing that was already working. I renamed the ticket to 'planned maintenance' and the dashboard agrees with me."

assert 1 <= len(ENTRY) <= 180, len(ENTRY)
p = "/output/entry.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
with open(p, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ENTRY, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
