"""
MIT License

Copyright (c) 2024 Sermet Pekin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from dataclasses import dataclass
from ._globals import USER, PACKAGE_NAME


StrOrTuple = str | tuple[str, ...]


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
