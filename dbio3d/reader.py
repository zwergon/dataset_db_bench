
class Reader:

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

    def __enter__(self):
        return self

    def load_cube(self, cube_id, idx):
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass