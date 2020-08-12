from abc import ABC, abstractmethod
from typing import List

from app.models.rope import RopeModel


class HasRope(ABC):

    @abstractmethod
    def fetch_rope(self, id: int) -> RopeModel:
        pass

    @abstractmethod
    def fetch_ropes(self) -> List[RopeModel]:
        pass
