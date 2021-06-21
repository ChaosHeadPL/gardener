from datetime import datetime
from pydantic import BaseModel
from gardener import config
import random


class Item(BaseModel):
    id: int
    itme_name: str
    itme_type: str

    def __init__(self, itme_name, itme_type):
        self.id = random.randrange(0, 10000000000)
        self.itme_name = itme_name
        self.itme_type = itme_type
        self.created_at = datetime.now()

    def build_url(self):
        return f"{config.get('BASE_URL')}/{self.itme_type}/{self.id}"

    def generate_qr_code(self):
        #TODO: finish it
        return True

    def generate_label_to_print(self):
        #TODO: finish it
        return True


class  Flower(Item):
    genus: str


class Alcochol(Item):
    pass
