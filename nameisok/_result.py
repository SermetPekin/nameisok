import requests
from dataclasses import dataclass


@dataclass
class Result:
    success: bool
    code: int
    value: str
