class HomeAppliances:
    def __init__(self, producer: str, name: str, price_in_uah: float):
        self.producer = producer
        self.name = name
        self.price = price_in_uah

        def __str__(self):
            return f"Producer : {self.producer}, Name : {self.name}, Price in uah : {self.price_in_uah}"
