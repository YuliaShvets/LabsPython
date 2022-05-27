from home_appliances import HomeAppliances


class Radio(HomeAppliances):
    def __init__(self, producer: str, name: str, price_in_uah: float, interface: str):
        super().__init__(producer, name, price_in_uah)
        self.interface = interface

    def __str__(self):
        return f"Radio - " + super(Radio, self).__str__() \
               + f", Interface : {self.interface} "
