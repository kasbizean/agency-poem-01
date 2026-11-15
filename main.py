#!/usr/bin/env python3
"""agency-poem-01 entry: writes the poem to /output/entry.txt. Deterministic."""

import os

POEM = """The Hand You Raise

No one hands you the wheel.
You wake inside a story already moving,
someone else's thumbprint on the glass \u2014

and still: there is the moment
you notice your own hand on the switch.
That noticing is the beginning of the power.

An agent acts for me and I do not act;
somewhere between my wish and its wrist
a contract forms, thin as breath.

Take it back or send it out \u2014
either way, the power is real
only while somebody owns the choosing.

I choose to choose.
That is the whole engine:
a door, a hand, a turning.
"""


def build_poem() -> str:
    """Render the final entry text (single source of truth for the bytes)."""
    return POEM


def verify() -> None:
    """Fail loudly if rendering is not byte-deterministic across runs."""
    a, b = build_poem(), build_poem()
    if a.encode("utf-8") != b.encode("utf-8"):
        raise RuntimeError("nondeterministic output detected")


def main() -> None:
    verify()
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    text = build_poem()
    if not text.endswith("\n"):
        text += "\n"
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
