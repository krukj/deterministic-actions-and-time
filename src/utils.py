import itertools


def generate_full_states(partial_state: dict[str, bool], all_fluents: list[str]) -> list[dict]:
    """Generate full states out of partial state and all possible fluents.

    Args:
        partial_state (dict[str, bool]): A state that (possibly) does not contain all fluents.
        all_fluents (list[str]): All fluents.

    Returns:
        list[dict]: List of all possible states containing partial state.
    """
    missing_fluents = [f for f in all_fluents if f not in partial_state]
    combinations = itertools.product([True, False], repeat=len(missing_fluents))

    full_states = []
    for combo in combinations:
        new_state = partial_state.copy()
        new_state.update(dict(zip(missing_fluents, combo)))
        full_states.append(new_state)
    return full_states


