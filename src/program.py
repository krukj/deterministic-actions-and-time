from dataclasses import dataclass, field

from src.action import Action


@dataclass
class Program:
    actions: list[Action] = field(default_factory=list)

    def execute_program(self, initial_state: dict[str, bool]) -> tuple[dict, int]:
        """Execute program.

        Args:
            initial_state (dict[str, bool]): Initial state.

        Returns:
            tuple[dict, int]: A tuple containing last state and total duration.
        """
        current_state = initial_state.copy()
        total_duration = 0
        for action in self.actions:
            current_state, duration = action.execute(state=current_state)
            total_duration += duration

        return current_state, total_duration
