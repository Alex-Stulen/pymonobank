from dataclasses import dataclass, asdict


@dataclass
class BaseDataclass(object):
    def as_dict(self) -> dict:
        return asdict(self)
