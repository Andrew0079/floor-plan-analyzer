import os
import unittest

from floor_plan.floor_plan import FloorPlan


def example_file_path():
    """Returns the path to the floor-plans directory."""
    current_directory = os.path.dirname(__file__)
    default_file_path = os.path.join(current_directory, "floor-plans", "rooms.txt")
    return default_file_path


class TestFloorPlan(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_floor_plan_reading(self):

        file_path = example_file_path()
        expected_output = """\
                            total:
                            W: 14, P: 7, S: 3, C: 1
                            balcony:
                            W: 0, P: 2, S: 0, C: 0
                            bathroom:
                            W: 0, P: 1, S: 0, C: 0
                            closet:
                            W: 0, P: 3, S: 0, C: 0
                            kitchen:
                            W: 4, P: 0, S: 0, C: 0
                            living room:
                            W: 7, P: 0, S: 2, C: 0
                            office:
                            W: 2, P: 1, S: 0, C: 0
                            sleeping room:
                            W: 1, P: 0, S: 1, C: 0
                            toilet:
                            W: 0, P: 0, S: 0, C: 1
                            """

        floor_plan = FloorPlan(file_path)
        floor_plan.read_floor_plan_txt()
        floor_plan.parse_floor_plan()
        floor_plan.format_parsed_floor_plan()
        result = floor_plan.print_floor_plan()

        self.assertEqual(result.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
