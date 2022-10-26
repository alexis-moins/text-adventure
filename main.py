from core.engine import engine

from entity import Entity
from room import Room

room = Room(name='The castle entrance', description='The entrance of the castle is protected by a soldier')

fil = Entity(name='Fil', description='A young human soldier')

room.entities.append(fil)

engine.start_engine()
