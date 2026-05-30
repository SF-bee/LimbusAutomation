"""Simple FSM base classes."""
from typing import Optional


class State:
    name: str = "base"

    def on_enter(self, ctx: dict):
        pass

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
