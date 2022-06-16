from __future__ import annotations


class Node:
    def __init__(self, id=None) -> None:
        self.id = id

    def __eq__(self, other: Node) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(str(self))

    def __str__(self) -> str:
        return "N"+str(self.id)
