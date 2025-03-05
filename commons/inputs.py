class Input:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def as_list(self) -> list[str]:
        with open(self.file_path, "r") as file:
            return [line.rstrip() for line in file]

    def first_line(self) -> str:
        with open(self.file_path, "r") as file:
            return file.readline()

    def as_string(self) -> str:
        with open(self.file_path, "r") as file:
            return file.read()
