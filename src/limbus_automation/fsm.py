"""Simple FSM base classes."""
from typing import Optional, Dict, Any

class State:
    name: str = "base"

    def on_enter(self, ctx: Dict[str, Any]):
        pass

    def execute(self, ctx: Dict[str, Any]) -> Optional['State']:
        """Returns the next state to transition to, or None if staying in current state."""
        return None

class FSM:
    def __init__(self, initial_state: State, context: Dict[str, Any]):
        self.current_state = initial_state
        self.context = context

    def update(self):
        if self.current_state:
            # On enter logic
            self.current_state.on_enter(self.context)
            # Execute state logic and get next state
            next_state = self.current_state.execute(self.context)
            if next_state:
                self.current_state = next_state


    def on_exit(self, ctx: dict):
        pass

    def run(self, ctx: dict) -> Optional[str]:
        """Perform state action. Return next state name or None to stay."""
        return None


class FSM:
    def __init__(self, states: dict, start: str, ctx: Optional[dict] = None):
        self.states = states
        self.current = states[start]
        self.ctx = ctx or {}
        self.current.on_enter(self.ctx)

    def step(self):
        next_name = self.current.run(self.ctx)
        if next_name and next_name in self.states:
            self.current.on_exit(self.ctx)
            self.current = self.states[next_name]
            self.current.on_enter(self.ctx)
