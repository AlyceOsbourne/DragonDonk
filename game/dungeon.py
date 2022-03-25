"""Dungeon Generaton plan

first cycle, generate the main rooms deciding what should be connected to what, apply first cyle of features (this might be things like locked doors) and queue paired room types
second cycle place queued room types, also deciding what it should be connected too taking into account paired rooms
(no rooms containing keys for locked doors AFTER locked doors) and then begin corridor ganeration
based on connected faces I can state direction for generation, and for pathing I can get the rise and run of the connecting points, find the mid point and put the changin in x/y on that point to make the winding corridors (taking 
into account room positions and existing corridor positions, this may require some low level pathfinding, given the small foorprint of the actual data this wouldn't be a bad method of corridor creation and validity checking, there is an also where it knows the location of the connection point, so we can optimize to some degree)

"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
from random import randint

class Encounter(Protocol):
    pass

class Feature(Protocol):
    pass


@dataclass
class Room: 
    
    room_x: int
    room_y: int

    room_width: int
    room_height: int
    
    north: 'Room' or None = None
    east: 'Room' or None = None
    south: 'Room' or None = None
    west: 'Room' or None = None

    linked_rooms: list['Room'] or None = None

    feature: 'Feature' or None = None
    encounter: 'Encounter' or None = None

    def connect_room(self, room, direction):
        if direction == "north":
            self.north = room
            room.south = self
            
        if direction == "east":
            self.east = room
            room.west = self
            
        if direction == "south":
            self.south = room
            room.south == self
            
        if direction == "west":
            self.west = room
            room.east = self
    

class Dungeon:
    def __init__():
        """I want this dungeon to be infinitely generatable,
        represent as a k-ary heap
        https://www.geeksforgeeks.org/k-ary-heap/"""
        pass