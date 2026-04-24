from src.program import Program
from src.utils import generate_full_states


def _check_condition(state: dict[str, bool], condition: dict[str, bool]) -> bool:
    """Checks whether the condition is fullfilled (condition is in state).

    Args:
        state (dict[str, bool]): State to be checked.
        condition (dict[str, bool]): Condition.

    Returns:
        bool: True if condition is in state, False otherwise.
    """
    return all(state.get(k) == v for k, v in condition.items())


def query_Q1(
    partial_state: dict[str, bool],
    program: Program,
    goal_condition: dict[str, bool],
    all_fluents: list[str],
) -> bool:
    """Checks whether the given goal condition holds after perforing a given program."""
    all_states = generate_full_states(partial_state, all_fluents)

    for state in all_states:
        final_state, _ = program.execute_program(state)
        if not _check_condition(final_state, goal_condition):
            # if final state does not contain goal state retrun False
            return False
    return True


def query_Q2(
    partial_state: dict[str, bool],
    program: Program,
    max_time: int,
    all_fluents: list[str],
) -> bool:
    """Checks whether the given program is executable withing time max_time."""
    all_states = generate_full_states(partial_state, all_fluents)
    for state in all_states:
        _, duration = program.execute_program(state)
        if duration > max_time:
            # retun false if program was not exected within max_time
            return False
    return True
