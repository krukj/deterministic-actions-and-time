from dataclasses import dataclass


@dataclass
class Action:
    """A class representing an action.

    Example:
        hike = Action(preconditions={'in_kuznice': True, 'has_money': True},
            effects={'on_the_mountain': True},
            duration=1)
    """

    preconditions: dict[str, bool]
    effects: dict[str, bool]
    duration: int = 1

    def is_applicable(self, state: dict[str, bool]) -> bool:
        """Check if the action is applicable from the given state"""
        return all(state.get(f) == v for f, v in self.preconditions.items())

    def execute(self, state: dict[str, bool]) -> tuple[dict[str, bool], int]:
        """Execute an action if possible.

        Args:
            state (dict[str, bool]): A given state.

        Returns:
            tuple[dict[str, bool], int]: A tuple containing resulting state
                and action's duration.
        """
        new_state = state.copy()
        if self.is_applicable(state):
            new_state.update(self.effects)
            return new_state, self.duration
        return new_state, 0
