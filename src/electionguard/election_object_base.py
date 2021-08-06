"""Base objects to derive other election objects."""

from dataclasses import dataclass


@dataclass
class ElectionObjectBase:
    """A base object to derive other election objects identifiable by object_id."""

    object_id: str


@dataclass
class OrderedObjectBase(ElectionObjectBase):
    """A ordered base object to derive other election objects."""

    sequence_order: int
