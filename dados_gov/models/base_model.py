from abc import ABC, abstractmethod
from datetime import date, datetime


class BaseModel(ABC):

    @abstractmethod
    def attribute_mapping(self):
        pass

    @staticmethod
    def fix_attribute(value):
        if isinstance(value, date):
            return value.strftime('%Y-%m-%d')

        if isinstance(value, datetime):
            return value.isoformat(sep='T', timespec='auto')

        return value

    def to_dict(self):
        return {self.attribute_mapping().get(k, k): self.fix_attribute(v) for k, v in self.__dict__.items()}
