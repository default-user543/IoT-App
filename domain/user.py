from dataclasses import dataclass

@dataclass
class User:
    uid: str
    email: str
    full_name: str

    def to_dict(self):
        return {
            "uid": self.uid,
            "email": self.email,
            "full_name": self.full_name
        }
