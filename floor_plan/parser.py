import logging
import re
from collections import deque
from typing import Optional, Union


class FloorPlanParser:
    def __init__(self, floor_plan_obj):
        (
            self.floor_plan,
            self.rows,
            self.cols,
            self.wall_separators,
            self.chair_types,
            self.room_mappings,
        ) = (
            floor_plan_obj.floor_plan,
            floor_plan_obj.rows,
            floor_plan_obj.cols,
            floor_plan_obj.wall_separators,
            floor_plan_obj.chair_types,
            floor_plan_obj.room_mappings,
        )

    def parse(self):
        """Parses the floor plan."""
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        for x in range(self.rows):
            for y in range(self.cols):
                if self.is_coordinate_visitable((x, y)):
                    self.explore_coordinate(x, y)

    def explore_coordinate(self, x: int, y: int) -> None:
        """Explore a single cell in the floor plan, updating room_mappings if a
        room is found.
        Args: x (int): The x-coordinate of the cell. y (int): The y-coordinate of the cell.
        """
        # Skip over the cells that have been visited or are marked as wall separators.
        if not self.visited[x][y] and self.floor_plan[x][y] not in self.wall_separators:
            logging.debug(f"Exploring from cell ({x}, {y}).")

            # Perform BFS from each unvisited cell that is not a wall to discover rooms
            area_name, chairs = self.breadth_first_search((x, y))

            if area_name:
                if area_name in self.room_mappings:
                    logging.debug(f"Updating room: {area_name} with chairs: {chairs}")

                    # Merge chair counts if the room was already discovered
                    for chair, count in chairs.items():
                        self.room_mappings[area_name][chair] = (
                            self.room_mappings[area_name].get(chair, 0) + count
                        )
                else:
                    logging.debug(
                        f"New room is found: {area_name} with chairs: {chairs}"
                    )
                    self.room_mappings[area_name] = chairs
            else:
                logging.debug(
                    f"Encountered an unmarked area starting at cell ({x}, {y}); skipping."
                )

        logging.debug(f"Last explored cell ({x}, {y}).")

    def is_coordinate_visitable(self, coordinate: tuple[int, int]) -> bool:
        """
        Checks if a cell is within bounds, not visited, and not a wall.
        Args: cell (tuple[int, int]): The cell coordinates (x, y) as a tuple.
        Returns: bool: True if the cell is visitable or False otherwise.
        """
        x, y = coordinate
        return (
            0 <= x < self.rows
            and 0 <= y < self.cols
            and not self.visited[x][y]
            and self.floor_plan[x][y] not in self.wall_separators
        )

    def get_room_name(self, row_str: str, y: int) -> Union[str, None]:
        """Extracts a room name from a row string."""
        pattern = re.compile(r"\(([^)]+)\)")
        matches = pattern.finditer(row_str)
        for match in matches:
            if match.start() <= y < match.end():
                return match.group(1)
        return None

    def breadth_first_search(
        self, start_cell: tuple[int, int]
    ) -> tuple[Optional[str], dict[str, int]]:

        if not self.floor_plan or not self.floor_plan[0]:
            return None, []

        queue = deque([start_cell])
        chairs = {chair: 0 for chair in self.chair_types}
        area_name = None

        self.visited[start_cell[0]][start_cell[1]] = True

        while queue:
            x, y = queue.popleft()
            cell_value = self.floor_plan[x][y]

            if cell_value in self.chair_types:
                chairs[cell_value] += 1

            elif not area_name and cell_value == "(":
                area_name = self.get_room_name("".join(self.floor_plan[x]), y)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if self.is_coordinate_visitable((nx, ny)):
                    self.visited[nx][ny] = True
                    queue.append((nx, ny))

        return area_name, chairs
