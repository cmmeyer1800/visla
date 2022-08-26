import pygame


class Rect:
    def __init__(
        self,
        center: tuple,
        height: int,
        width: int,
        color: tuple,
        parent: pygame.Surface,
        border_width: int,
        solid: bool,
    ) -> None:
        """
        Initialization of all variables defined as being necessary to draw and or manipulate an ellipse
        """
        self.center: tuple = center
        self.height: int = height
        self.width: int = width
        self.color: tuple = color
        self.parent: pygame.Surface = parent
        self.border_width: int = border_width
        self.solid: bool = solid

    # -------------------------------------------------------------------------

    def draw(self) -> None:
        """
        Draws a rectangle using the parameters passed into the function on the parent surface passed during initialization
        """
        left = self.center[0] - (self.width / 2)
        top = self.center[1] - (self.height / 2)

        if self.solid == True:
            bw = 0
        else:
            bw = self.border_width

        pygame.draw.rect(
            self.parent,
            self.color,
            pygame.Rect(left, top, self.width, self.height),
            bw
        )

    # -------------------------------------------------------------------------
