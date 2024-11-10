from dataclasses import dataclass

StrOrTuple = str | tuple[str, ...]
from ._globals import USER, PACKAGE_NAME


@dataclass
class Url:
    domain: str
    user: str
    package_name: str
    h: str

    def __call__(self):
        self.url = f'{self.domain}/{self.user}/{self.package_name}/{self.h}'
        return self


def get_url_instance():
    u = Url(DOMAIN, USER, PACKAGE_NAME, HASH)
    return u()
def get_url_instance2():
    u = Url(DOMAIN, USER, PACKAGE_NAME, HASH2)
    return u()

"""
from dataclasses import dataclass



StrOrTuple = str | tuple[str, ...]
from ._globals import USER , PACKAGE_NAME 


@dataclass
class Url:
    domain: str
    user: str
    package_name: str
    h: str

    def __call__(self):
        self.url = f'{self.domain}/{self.user}/{self.package_name}/{self.h}'
        return self


def get_url_instance():
    u = Url( DOMAIN , USER , PACKAGE_NAME , HASH)
    return u()



"""

HASH = '680f11c457858a058ad81bda819008cb341d3bd2'
HASH2 = 'd6048743d42fed02254a01a53c1ef563141deea9'
DOMAIN = 'https://raw.githubusercontent.com'
