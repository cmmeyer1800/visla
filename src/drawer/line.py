import pygame


class Line:
    def __init__(
        self, start: tuple, end: tuple, width: int, color: tuple, parent: pygame.Surface
    ) -> None:
        """
        Initialization of all variables defined as being necessary to draw and or manipulate a line
        """
        self.start: tuple = start
        self.end: tuple = end
        self.width: int = width
        self.color: tuple = color
        self.parent: pygame.Surface = parent

        # Should be only left in for debugging purposes, slows down execution unnecessarily
        # self.asserts()

    # -------------------------------------------------------------------------

    def draw(self) -> None:
        """
        Draws a line using the parameters passed into the function on the parent surface passed during initialization
        """
        pygame.draw.line(self.parent, self.color, self.start, self.end, self.width)

    # -------------------------------------------------------------------------

    def asserts(self) -> None:
        """
        A list of assert statements to ensure that the line parameters that are passed are
        within the design specification set for lines to be drawn
        """
        assert type(self.start) == tuple
        assert type(self.end) == tuple
        assert type(self.width) == int
        assert type(self.color) == tuple
        assert type(self.parent) == pygame.Surface

        assert self.start[0] > 0 and self.start[0] < self.parent.get_width()
        assert self.start[1] > 0 and self.start[1] < self.parent.get_height()

        assert self.width < self.parent.get_width()

        assert len(self.color) == 3
        for i in range(3):
            assert self.color[i] > 0 and self.color[i] < 256
            assert type(self.color[i]) == float or type(self.color[i]) == int

    # -------------------------------------------------------------------------
