from datetime import datetime

import pytest


class Std:
    def __int__(self, name, dob, branch):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.cred = 0

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def add_cred(self, value):
        self.cred += value

    def get_cred(self):
        return self.cred


