from __future__ import annotations
from Node import Node


class Edge:
    def __init__(self, weight: float, src: Node = None, dst: Node = None) -> None:
        if src == dst:
            raise ValueError("src and dst must be different")
        self.weight: float = weight
        self.dst: Node = dst
        self.src: Node = src

    def __eq__(self, other: Edge) -> bool:
        return self.dst == other.dst and self.src == other.src or self.dst == other.src and self.src == other.dst

    def __str__(self) -> str:
        return f"{self.src} -> {self.dst} ({self.weight})"

    @staticmethod
    def fromString(s: str) -> Edge:
        s = s.strip()
        s = s.replace("(", "")
        s = s.replace(")", "")
        s = s.replace("-", "")
        s = s.replace(">", "")
        s = s.replace("N", "")
        src, dst, value = s.split()
        return Edge(float(value), Node(int(src)), Node(int(dst)))
