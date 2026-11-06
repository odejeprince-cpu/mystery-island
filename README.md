# Mystery Island: The Lost Lighthouse

A text adventure in Python. You wake up on an island after a storm. Light the beacon to be rescued.

## Prerequisites
Python 3.8 or newer. No external packages.

## How to run
    python3 main.py

## How to run tests
    python3 -m unittest discover -s tests -v

## Game rules
- Map: Beach - Jungle - Cave - Old Bridge - Lighthouse (you can move back and forth).
- You start with 5 energy. Every legal move costs 1. Rejected input costs nothing.
- The rope is in the Jungle and the lantern is in the Cave. Each can be picked up once.
- Crossing from the Old Bridge to the Lighthouse needs the rope.
- Lighting the beacon needs you to be at the Lighthouse with the lantern.
- Decisions: eat the jungle fruit (once, +1 energy), swim from the Beach (you lose), or spend moves wandering (you run out of energy).
- You lose if energy reaches 0 before the beacon is lit.

## Example winning run
Go to Jungle, pick up rope, go to Cave, pick up lantern, go to Old Bridge, go to Lighthouse, light the beacon.

## Known limits
- One fixed map, no randomness.
- Menu choices are numbered, so typing action names does nothing.