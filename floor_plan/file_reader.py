def read_floor_plan(filename: str) -> tuple[list[list[str]], int, int]:
    """
    Reads a floor plan from a file, ensuring uniform row lengths.
    Args: filename (str): The path to the file containing the floor plan.
    Returns:
        tuple: A tuple containing:
            - A list of lists representing the floor plan with equal row lengths.
            - The number of rows in the floor plan.
            - The number of columns in the floor plan.
    """
    floor_plan = []
    rows, cols = 0, 0
    try:
        with open(filename, encoding="utf-8-sig") as f:
            floor_plan = [list(line.rstrip()) for line in f]
            rows = len(floor_plan)
            cols = max(len(row) for row in floor_plan)
            floor_plan = [row + [" "] * (cols - len(row)) for row in floor_plan]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Unable to find file '{filename}'.") from e
    return floor_plan, rows, cols
