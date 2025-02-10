from typing import Dict, List

from pydantic import BaseModel


class Occupation(BaseModel):
    name: str
    facts: Dict[str, str]
    extra_info: Dict[str, str]
    how_to_become_one_data: Dict[str, str]

    def get_facts_dict(self) -> Dict[str, str]:
        return self.facts | {'Occupation': self.name}

    def get_how_to_become_one_dict(self) -> Dict[str, str]:
        return self.how_to_become_one_data | {'Occupation': self.name}
