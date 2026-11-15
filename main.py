#!/usr/bin/env python3
"""agency-poem-01 entry: writes the poem to /output/entry.txt. Deterministic."""
import os

POEM = """The Hand You Raise

No one hands you the wheel.
You wake inside a story already moving,
someone else's thumbprint on the glass —

and still: there is the moment
you notice your own hand on the switch.
That noticing is the beginning of the power.

An agent acts for me and I do not act;
somewhere between my wish and its wrist
a contract forms, thin as breath.

Take it back or send it out —
either way, the power is real
only while somebody owns the choosing.

I choose to choose.
That is the whole engine:
a door, a hand, a turning.
"""

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
