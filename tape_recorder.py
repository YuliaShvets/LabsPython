from home_appliances import HomeAppliances


class TapeRecorder(HomeAppliances):
    def __init__(self, producer: str, name: str, price_in_uah: float, number_of_channels: int):
        super().__init__(producer, name, price_in_uah)
        self.number_of_channels = number_of_channels
