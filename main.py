from music_center import MusicCenter
from radio import Radio
from tape_recorder import TapeRecorder
from television import Television
from vacuum_cleaner import VacuumCleaner


def main():
    vacuum_cleaner = VacuumCleaner("BOSCH", "BGS05", 2600, 700)
    television = Television("Samsung", "UE50AU", 20000, 50)
    radio = Radio("CROSLEY", "Corsair", 7710, "USB")
    tape_recorder = TapeRecorder("Pioneer", "MVH-09UB", 2000, 2)
    music_center = MusicCenter("Phillips", "TAM3205", 3000, "AUX")

    print(tape_recorder)
    print(radio)


if __name__ == '__main__':
    main()
