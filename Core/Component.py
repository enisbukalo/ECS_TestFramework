from typing import TypeVar, Generic
from .Types import ComponentId

T = TypeVar("T")


class Component(Generic[T]):
    """
    Base class for components in the ECS system.
    Components are pure data containers.
    """

    _next_id: ComponentId = 0

    def __init__(self):
        self.id = Component._next_id
        Component._next_id += 1
