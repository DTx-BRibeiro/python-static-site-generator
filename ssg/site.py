from pathlib import Path
import os

class Site():

    def __init__(self, source: str, dest: str):
        self.source = Path(source)
        self.dest = Path(dest)
        return 

    def create_dir(self, path: Path):
        directory = self.dest/path.relative_to(self.source)
        print(directory)
        directory.mkdir(parents=True, exist_ok=True)
        
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            else:
                continue