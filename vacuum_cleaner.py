from home_appliances import HomeAppliances


class VacuumCleaner(HomeAppliances):
    def __init__(self, producer: str, name: str, price_in_uah: float, power_in_watts: float):
        super().__init__(producer, name, price_in_uah)
        self.power = power_in_watts
