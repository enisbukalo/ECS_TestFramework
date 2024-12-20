from Core import System, Entity, Component
from dataclasses import dataclass


@dataclass
class TestComponent(Component):
    value: int

    def __init__(self, value: int):
        super().__init__()
        self.value = value


class TestSystem(System):
    def __init__(self):
        super().__init__()
        self.update_called = False
        self.last_dt = 0.0

    def update(self, dt: float) -> None:
        self.update_called = True
        self.last_dt = dt


def test_system_initialization():
    """Test basic system initialization"""
    system = TestSystem()
    assert system.enabled is True
    assert system.priority == 0
    assert len(system.entities) == 0


def test_add_remove_entities():
    """Test adding and removing entities from system"""
    system = TestSystem()

    # Add entities
    system.add_entity(1)
    system.add_entity(2)
    assert len(system.entities) == 2

    # Remove entity
    system.remove_entity(1)
    assert len(system.entities) == 1
    assert 2 in system.entities

    # Clear all entities
    system.clear_entities()
    assert len(system.entities) == 0


def test_system_update():
    """Test system update method"""
    system = TestSystem()

    assert not system.update_called
    system.update(0.16)
    assert system.update_called
    assert system.last_dt == 0.16


def test_system_enable_disable():
    """Test enabling and disabling system"""
    system = TestSystem()
    assert system.enabled is True

    system.enabled = False
    assert system.enabled is False


def test_system_priority():
    """Test system priority setting"""
    system = TestSystem()
    assert system.priority == 0

    system.priority = 10
    assert system.priority == 10
