from src.ast.node import ASTNode
from src.errors import throw_error

SYMBOLS = [";", "{", "}"]

FUNCTIONAL_BLOCKS = ["canvas", "line", "rect", "ellipse"]

KEYWORDS = []


# -----------------------------------------------------------------------------


class Parsed:

    # -----------------------------------------------------------------------------

    def __init__(self, filepath: str) -> None:

        with open(filepath, "r") as FILE:
            self.lines = FILE.read()

        self.parse()

    # -----------------------------------------------------------------------------

    def format(self, input: str) -> list[str]:
        formatted = []
        build = ""

        for char in input:
            if char == " " or char == "\n":
                continue
            elif char not in SYMBOLS:
                build += char
            else:
                if build != "":
                    formatted.append(build)
                build = ""
                formatted.append(char)

        return formatted

    # -----------------------------------------------------------------------------

    def parse(self) -> None:
        self.ast = ASTNode("HEAD", head=True)

        formatted = self.format(self.lines)

        self.__parse(self.ast, formatted)

    # -----------------------------------------------------------------------------

    def __parse(self, head: ASTNode, blocks: list[str]) -> None:
        i = 0
        while i < len(blocks):
            block = blocks[i]
            if blocks[i].isalpha():
                if block not in FUNCTIONAL_BLOCKS:
                    throw_error(f"Block {block} not a valid Functional Block name")
                if i + 2 > len(blocks) or blocks[i + 1] != "{":
                    throw_error(
                        "Functional Block declaration must be followed by an opening bracket '{'"
                    )
                new_node = ASTNode(block)
                head.append_child(new_node)
                end_bracket_loc = self.__find_closing_bracket(i + 1, blocks)
                if end_bracket_loc == None:
                    throw_error("Unbalanced opening and closing brackets")

                self.__parse(new_node, blocks[i + 1 : end_bracket_loc])
                i = end_bracket_loc + 1

            elif "=" in block:
                if len(block.split("=")) != 2:
                    throw_error(
                        f"Statement {block} not valid, assignment must be like: name=value"
                    )
                new_node = ASTNode(block)
                head.append_child(new_node)
            elif block in SYMBOLS:
                pass
            else:
                throw_error(f"Statement {block} not valid")
            i += 1
        return

    # -----------------------------------------------------------------------------

    def __find_closing_bracket(self, curr_idx: int, blocks: list[str]) -> int:
        count = 0
        for idx in range(curr_idx + 1, len(blocks)):
            if blocks[idx] == "{":
                count += 1

            elif blocks[idx] == "}":
                if count == 0:
                    return idx
                else:
                    count -= 1

        return None

    # -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
