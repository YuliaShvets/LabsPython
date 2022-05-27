from home_appliances import HomeAppliances


class MusicCenter(HomeAppliances):
    def __init__(self, producer: str, name: str, price_in_uah: float, connect: str):
        super().__init__(producer, name, price_in_uah)
        self.connect = connect

    def __str__(self):
        return f"Music center - " + super(MusicCenter, self).__str__() \
               + f", Connect : {self.connect} "
