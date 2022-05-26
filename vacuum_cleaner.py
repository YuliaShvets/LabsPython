from home_appliances import HomeAppliances


class VacuumCleaner(HomeAppliances):
    def __init__(self, producer: str, name: str, price_in_uah: float, power_in_watts: float):
        super().__init__(producer, name, price_in_uah)
        self.power_in_watts = power_in_watts

    def __str__(self):
        return super(HomeAppliances, self).__str__() \
               + f"Power in watts : {self.power_in_watts} "
