# Repository for Examination 2 by Group 42

Pig dice game, player vs computer, in Python.

----------------

### __To create and activate the Python virtual environment:__


On Windows with bash terminal:
1. ```
   python -m venv .venv
   ```
2. ```
    . .venv/Scripts/activate
   ```
3. ```
    python -m pip install -r requirements.txt
   ```

On Linux/Mac:
1. ```
   python -m venv .venv
   ```
2. ```
   . .venv/bin/activate
   ```
3. ```
   python -m pip install -r requirements.txt
   ```

### __To run the game:__
   ```
   python src/main.py
   ```
   or
   ```
   python3 src/main.py
   ```

## Game rules
- Goal: reach 100 points before your opponent(s).
- During your turn type `r` to roll, `h` to hold (bank points), `q` to abandon the round, or `+` to add 10 points for testing.
- Rolling a `1` ends your turn immediately and removes any unbanked turn score.

## Computer intelligence
- Computer strategies live in `pig_game/intelligence`.
- `BasicIntelligence` randomly chooses between rolling and holding; `MediumIntelligence` adjusts risk based on the score difference.
- Additional behaviours can be added by subclassing `Intelligence` and overriding `decide_action`.

### __ To generate uml diagram:__
   ```
   pyreverse src/pig_game/*
   ```

ReadTheDocs link:
https://examination-2.readthedocs.io/en/latest/
