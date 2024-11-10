from dataclasses import dataclass

@dataclass
class Result:
    exists: bool
    code: int
    value: str
