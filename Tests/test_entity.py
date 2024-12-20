from Core import Entity, Component
from dataclasses import dataclass


@dataclass
class TestComponent(Component):
    value: int

    def __init__(self, value: int):
        super().__init__()
        self.value = value


def test_entity_initialization():
    """Test basic entity initialization"""
    entity = Entity(1)
    assert entity.id == 1
    assert entity.is_active is True
    assert len(entity.components) == 0


def test_add_component():
    """Test adding components to an entity"""
    entity = Entity(1)
    comp = TestComponent(42)

    entity.add_component(comp)
    assert len(entity.components) == 1
    assert entity.has_component(comp.id)
    assert entity.get_component(comp.id) == comp


def test_remove_component():
    """Test removing components from an entity"""
    entity = Entity(1)
    comp = TestComponent(42)

    entity.add_component(comp)
    assert entity.has_component(comp.id)

    entity.remove_component(comp.id)
    assert not entity.has_component(comp.id)
    assert entity.get_component(comp.id) is None


def test_has_components():
    """Test checking for multiple components"""
    entity = Entity(1)
    comp1 = TestComponent(42)
    comp2 = TestComponent(24)

    entity.add_component(comp1)
    entity.add_component(comp2)

    assert entity.has_components(comp1.id, comp2.id)
    assert not entity.has_components(comp1.id, comp2.id, 999)


def test_get_nonexistent_component():
    """Test getting a component that doesn't exist"""
    entity = Entity(1)
    assert entity.get_component(999) is None
