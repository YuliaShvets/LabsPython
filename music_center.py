from home_appliances import HomeAppliances


class MusicCenter(HomeAppliances):
    def __init__(self, producer: str, name: str, price_in_uah: float, connect: str):
        super().__init__(producer, name, price_in_uah)
        self.connect = connect
