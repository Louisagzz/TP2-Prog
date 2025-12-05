import enum

from typing import Optional


class Move(enum.Enum):
    """
    The type representing the possible moves of the read/write head.
    """

    LEFT = "left"
    NONE = "none"
    RIGHT = "right"


# the set of possible states
STATES: set[str] = {"done", "propagate-carry", "rightmost-digit"}

# the initial state
START_STATE = "rightmost-digit"

# the set of final states
ACCEPTING_STATES: set[str] = {"done"}

# the (partial) transition function, as a map from state/character pairs
# to state/character/move triples
TRANSITIONS: dict[tuple[str, Optional[str]], tuple[str, Optional[str], Move]] = {
    ("rightmost-digit", "0"): ("rightmost-digit", "0", Move.RIGHT),
    ("rightmost-digit", "1"): ("rightmost-digit", "1", Move.RIGHT),
    ("rightmost-digit", None): ("propagate-carry", None, Move.LEFT),
    ("propagate-carry", "0"): ("done", "1", Move.NONE),
    ("propagate-carry", "1"): ("propagate-carry", "0", Move.LEFT),
    ("propagate-carry", None): ("done", "1", Move.NONE),
}

# the type of a machine: tape, position, and state
Machine = tuple[list[Optional[str]], int, str]


def init_machine(word: str) -> Machine:
    """
    Returns a machine with the passed word on the tape (one character per
    cell), the read/write head on the leftmost character, in the initial
    state.
    """
    pass


def print_machine(machine: Machine) -> None:
    """
    Prints the passed machine onto the screen, with one cell per character, the
    state, and a `^` character to shows where the read/write head is.

    For instance, a machine with "101" on the tape, and the read/write head on the
    leftmost character would be displayed as:

    ```
    +---+---+---+
    | 1 | 0 | 1 | state-name
    +---+---+---+
      ^
    ```
    """
    pass


def step_machine(machine: Machine) -> Optional[Machine]:
    """
    Computes one step of the machine, returning the new configuration of the
    machine or `None` if there are no transitions from the passed configuration.
    """
    pass


def run_machine(machine: Machine) -> Optional[str]:
    """
    Performs computation steps until the execution stops, returning either the
    word on tape at the end (if the execution is successful), or `None` (if the
    execution fails).
    """
    pass
