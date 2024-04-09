import argparse
import logging
import os

from floor_plan.floor_plan import FloorPlan, FloorPlanError


def setup_logging(log_level):
    """Configure the logging level and format."""
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def main():
    parser = argparse.ArgumentParser(description="Process a floor plan file.")

    # Define command-line arguments
    parser.add_argument(
        "file_path",
        type=str,
        nargs="?",
        default=None,
        help="The path to the floor plan file. If not provided, a default file path will be used.",
    )
    parser.add_argument(
        "--separators",
        type=lambda s: set(s.split(",")),
        default={"+", "-", "|", "/", "\\"},
        help="Characters used as separators. Provide as comma-separated. Default: '+,-,|,/,\\'.",
    )
    parser.add_argument(
        "--chair_chars",
        type=lambda s: set(s.split(",")),
        default={"C", "S", "P", "W"},
        help="Characters representing chairs. Provide as comma-separated. Default: 'C,S,P,W'.",
    )
    parser.add_argument(
        "--logging",
        type=str,
        default="info",
        choices=["debug", "info", "warning", "error", "critical"],
        help="Set the logging level. Default: 'info'.",
    )

    args = parser.parse_args()

    setup_logging(args.logging)

    # Set default file path if no file path is provided
    if args.file_path is None:
        current_directory = os.path.dirname(__file__)
        default_file_path = os.path.join(current_directory, "floor-plans", "rooms.txt")
        args.file_path = default_file_path

    while True:
        try:
            if args.file_path is None:
                args.file_path = input("Enter the path to the floor plan file: ")

            floor_plan = FloorPlan(args.file_path, args.separators, args.chair_chars)
            floor_plan.read_floor_plan_txt()
            floor_plan.parse_floor_plan()
            floor_plan.format_parsed_floor_plan()
            floor_plan.print_floor_plan()
        except FloorPlanError as e:
            logging.error(f"Failed to process floor plan: {e}")

        choice = input("Do you want to process another floor plan? (yes/no): ").lower()
        if choice != "yes":
            print("Exiting...")
            break

        # Reset file_path to None to prompt for a new file path
        args.file_path = None


if __name__ == "__main__":
    main()
