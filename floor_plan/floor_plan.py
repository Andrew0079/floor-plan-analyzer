import logging

from .file_reader import read_floor_plan
from .parser import FloorPlanParser


class FloorPlan:
    def __init__(
        self,
        filename,
        wall_separators: set[str] = {"|", "-", "+", "/"},
        chair_types: set[str] = {"P", "W", "S", "C"},
    ):
        self.filename = filename
        self.floor_plan = []
        self.visited = None
        self.wall_separators = wall_separators
        self.chair_types = chair_types
        self.room_mappings = {}
        self.rows = None
        self.cols = None
        self.parsed_floor_plan = {}

    def read_floor_plan_txt(self) -> list[list[str]]:
        """Reads a floor plan from a file."""
        try:
            self.floor_plan, self.rows, self.cols = read_floor_plan(self.filename)
        except Exception as e:
            raise FloorPlanError(
                f"Unable to read floor plan from '{self.filename}': {e}"
            ) from e

    def parse_floor_plan(self):
        """Parses the entire floor plan."""
        logging.debug("Starting to parse the floor plan.")
        parser = FloorPlanParser(self)
        parser.parse()
        logging.debug("Finished parsing the floor plan.")

    def format_parsed_floor_plan(self):
        """Sorts room mappings alphabetically and generates the total count of chairs."""
        total_chairs = {chair: 0 for chair in self.chair_types}
        sorted_room_mappings = {}

        # Define the order of chair types
        chair_order = ["W", "P", "S", "C"]

        for room_name in sorted(self.room_mappings.keys()):
            chairs = self.room_mappings[room_name]
            sorted_chairs = {chair: chairs.get(chair, 0) for chair in chair_order}
            sorted_room_mappings[room_name] = sorted_chairs
            for chair, count in chairs.items():
                total_chairs[chair] += count

        # Sort the total count of chairs based on chair_order
        sorted_total_chairs = {
            chair: total_chairs.get(chair, 0) for chair in chair_order
        }

        # Create a new dictionary with the sorted total count of chairs and room mappings
        parsed_floor_plan = {"total": sorted_total_chairs}
        parsed_floor_plan.update(sorted_room_mappings)

        self.parsed_floor_plan = parsed_floor_plan

    def print_floor_plan(self):
        # Print total section first
        print("total:")
        total = ", ".join(
            [
                f"{chair}: {count}"
                for chair, count in self.parsed_floor_plan["total"].items()
            ]
        )
        print(total)

        # Print individual room mappings
        for room_name, chairs in self.parsed_floor_plan.items():
            if room_name != "total":
                print(room_name + ":")
                room = ", ".join(
                    [f"{chair}: {count}" for chair, count in chairs.items()]
                )
                print(room)


class FloorPlanError(Exception):
    """Custom exception class for FloorPlan related errors."""
