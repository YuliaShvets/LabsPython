from home_appliances import HomeAppliances


class Television(HomeAppliances):
    def __init__(self, producer: str, name: str, price_in_uah: float, size_in_inches: int):
        super().__init__(producer, name, price_in_uah)
        self.size_in_inches = size_in_inches

