from __future__ import annotations


class ASTNode:
    def __init__(self, value, head=False) -> None:
        self.children = []
        self.value = value
        self.head = head

    def append_child(self, node: ASTNode) -> None:
        self.children.append(node)

    def print_rec(self) -> None:
        self.__print_rec(self, 0)

    def __print_rec(self, node: ASTNode, indent: int) -> None:
        print("\t" * indent + f"Value='{node.value}'")
        for child in node.children:
            self.__print_rec(child, indent + 1)
