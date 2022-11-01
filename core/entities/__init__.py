"""
Module providing classes for all base entities. Currenlty offers the
possibility to create NPC and Player instances.

Also provide Describable, Entity and Character abstract classes.
"""
from .entity import Entity
from .character import Character
from .describable import Describable

from .npc import NPC
from .player import Player
