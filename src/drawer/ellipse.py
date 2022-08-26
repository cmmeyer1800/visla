import pygame


class Ellipse:
    def __init__(
        self,
        center: tuple,
        height: int,
        width: int,
        color: tuple,
        parent: pygame.Surface,
        border_width: int,
    ) -> None:
        """
        Initialization of all variables defined as being necessary to draw and or manipulate a line
        """
        self.center: tuple = center
        self.height: int = height
        self.width: int = width
        self.color: tuple = color
        self.parent: pygame.Surface = parent
        self.border_width = border_width

    # -------------------------------------------------------------------------

    def draw(self) -> None:
        """
        Draws a line using the parameters passed into the function on the parent surface passed during initialization
        """
        left = self.center[0] - (self.width / 2)
        top = self.center[1] - (self.height / 2)

        pygame.draw.ellipse(
            self.parent,
            self.color,
            pygame.Rect(left, top, self.width, self.height),
            self.border_width
        )

    # -------------------------------------------------------------------------
