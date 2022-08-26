from src.ast.node import ASTNode
from src.errors import throw_error
from src.drawer import Line, Rect, Ellipse
from src.helpers import str_to_tuple, str_to_bool
import pygame

# -----------------------------------------------------------------------------


class Interpreter:
    def __init__(self, ast: ASTNode) -> None:

        self.ast = ast
        self.lines = []
        self.rects = []
        self.ellipses = []

    # -------------------------------------------------------------------------

    def run(self) -> int:

        if len(self.ast.children) == 0:
            throw_error("No Functional Blocks found in source file")

        if self.ast.children[0].value != "canvas":
            throw_error(
                'Visla source file must begin with a "canvas" Functional Block to draw onto'
            )

        self.traverse_ast(self.ast)

        self.display()

    # -------------------------------------------------------------------------

    def traverse_ast(self, head: ASTNode):

        if head.value == "canvas":
            self.build_canvas(head)

        if head.value == "line":
            self.build_line(head)

        if head.value == "rect":
            self.build_rect(head)

        if head.value == "ellipse":
            self.build_ellipse(head)

        for child in head.children:
            self.traverse_ast(child)

    # -------------------------------------------------------------------------

    def build_canvas(self, node: ASTNode) -> None:

        width = None
        height = None

        for child in node.children:
            if "width" in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {width} needs to be an integer but cannot be interpretted as such"
                    )
                width = parsed

            if "height" in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {height} needs to be an integer but cannot be interpretted as such"
                    )
                height = parsed

        if height == None:
            throw_error("Canvas missing height parameter which is needed")
        if width == None:
            throw_error("Canvas missing width parameter which is needed")

        self.canvas = pygame.display.set_mode((width, height))

    # -------------------------------------------------------------------------

    def build_line(self, node: ASTNode) -> None:
        start: tuple = None
        end: tuple = None
        width: int = None
        color: tuple = None

        for child in node.children:
            if "start" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_tuple(str_rep, 2)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a tuple of 2 ints but cannot be interpretted as such"
                    )
                start = parsed

            if "end" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_tuple(str_rep, 2)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a tuple of 2 ints but cannot be interpretted as such"
                    )
                end = parsed

            if "width" in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {width} needs to be an integer but cannot be interpretted as such"
                    )
                width = parsed

            if "color" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_tuple(str_rep, 3)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a tuple of 3 ints but cannot be interpretted as such"
                    )
                color = parsed

        if start == None:
            throw_error("line missing start parameter which is needed")
        if end == None:
            throw_error("line missing end parameter which is needed")
        if color == None:
            throw_error("line missing color parameter which is needed")
        if width == None:
            width = 1

        self.lines.append(Line(start, end, width, color, self.canvas))

    # -------------------------------------------------------------------------

    def build_rect(self, node: ASTNode) -> None:
        center: tuple = None
        height: tuple = None
        width: int = None
        border_width: int = None
        color: tuple = None
        solid: bool = None

        for child in node.children:
            if "center" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_tuple(str_rep, 2)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a tuple of 2 ints but cannot be interpretted as such"
                    )
                center = parsed

            if "width" in child.value and "border_width" not in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {width} needs to be an integer but cannot be interpretted as such"
                    )
                width = parsed

            if "height" in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {width} needs to be an integer but cannot be interpretted as such"
                    )
                height = parsed

            if "border_width" in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {parsed} needs to be an integer but cannot be interpretted as such"
                    )
                border_width = parsed

            if "color" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_tuple(str_rep, 3)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a tuple of 3 ints but cannot be interpretted as such"
                    )
                color = parsed

            if "solid" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_bool(str_rep)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a boolean (true or false) but cannot be interpretted as such"
                    )
                solid = parsed

        if center == None:
            throw_error("line missing start parameter which is needed")
        if height == None:
            throw_error("line missing end parameter which is needed")
        if width == None:
            throw_error("line missing width parameter which is needed")
        if color == None:
            throw_error("line missing color parameter which is needed")
        if solid == None:
            solid = False
        if solid == True and border_width != None:
            throw_error("Solid cannot be true and a border_width specified")
        if border_width == None:
            border_width = 1

        self.rects.append(Rect(center, height, width, color, self.canvas, border_width, solid))

    # -------------------------------------------------------------------------

    def build_ellipse(self, node: ASTNode) -> None:
        center: tuple = None
        height: tuple = None
        width: int = None
        border_width: int = None
        color: tuple = None
        solid: bool = None

        for child in node.children:
            if "center" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_tuple(str_rep, 2)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a tuple of 2 ints but cannot be interpretted as such"
                    )
                center = parsed

            if "width" in child.value and "border_width" not in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {width} needs to be an integer but cannot be interpretted as such"
                    )
                width = parsed

            if "height" in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {width} needs to be an integer but cannot be interpretted as such"
                    )
                height = parsed

            if "border_width" in child.value:
                try:
                    parsed = int(child.value.split("=")[1])
                except:
                    throw_error(
                        f"Value {parsed} needs to be an integer but cannot be interpretted as such"
                    )
                border_width = parsed

            if "color" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_tuple(str_rep, 3)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a tuple of 3 ints but cannot be interpretted as such"
                    )
                color = parsed

            if "solid" in child.value:
                str_rep = child.value.split("=")[1]
                parsed = str_to_bool(str_rep)
                if parsed == None:
                    throw_error(
                        f"Value {str_rep} needs to be a boolean (true or false) but cannot be interpretted as such"
                    )
                solid = parsed

        if center == None:
            throw_error("line missing start parameter which is needed")
        if height == None:
            throw_error("line missing end parameter which is needed")
        if width == None:
            throw_error("line missing width parameter which is needed")
        if color == None:
            throw_error("line missing color parameter which is needed")
        if solid == None:
            solid = False
        if solid == True and border_width != None:
            throw_error("Solid cannot be true and a border_width specified")
        if border_width == None:
            border_width = 1

        self.ellipses.append(
            Ellipse(center, height, width, color, self.canvas, border_width, solid)
        )

    # -------------------------------------------------------------------------

    def display(self) -> None:

        pygame.init()
        pygame.display.set_caption("Visla")
        clock = pygame.time.Clock()

        running = True

        while running:

            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.canvas.fill((0, 0, 0))

            for line in self.lines:
                line.draw()

            for rect in self.rects:
                rect.draw()

            for ellipse in self.ellipses:
                ellipse.draw()

            pygame.display.flip()

        pygame.quit()

    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
