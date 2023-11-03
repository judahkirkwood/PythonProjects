# Parent class
class Guitars:
    manufacturer = 'unknown'
    instrument_type = 'stringed'
    picking_style = 'Hybrid'
    effects = None
    origin = 'USA'
    material = 'hardwood'

    def information(self):
        msg = "\nManufacturer: {}\nInstrument Type: {}\nPicking Style: {}\nEffects: {}\nOrigin: {}\nMaterial: {}".format(self.manufacturer, self.instrument_type, self.picking_style, self.effects, self.origin, self.material)
        return msg


# Child class instance - Electric Guitar
class Electric(Guitars):
    strings_type = 'Steel'
    string_number = 6
    pickups = 'Humbucker'
    amplified = True
    body_type = 'Solid'
    fretboard = 'Maple'

    def solo(self):
        msg = "\nThe breakdown starts and the guitar begins to play an anthematic melody above the other instruments!"
        return msg

    def information(self):  # Overriding the method from the parent class
        msg = "\nElectric Guitar Information - Manufacturer: {}\nStrings Type: {}\nString Number: {}\nPickups: {}\nAmplified: {}\nBody Type: {}\nFretboard: {}".format(self.manufacturer, self.strings_type, self.string_number, self.pickups, self.amplified, self.body_type, self.fretboard)
        return msg


# Another child class instance - Acoustic Guitar
class Acoustic(Guitars):
    strings_type = 'Wound Nickel'
    string_number = 6
    tuning = 'Open D'
    amplified = False
    body_type = 'Chambered'
    fretboard = 'Rosewood'

    def strum(self):
        msg = "\nRhythmically brushing the strings with a guitar pick, creating a percussive chord structure."
        return msg

    def information(self):  # Overriding the method from the parent class
        msg = "\nAcoustic Guitar Information - Manufacturer: {}\nStrings Type: {}\nString Number: {}\nTuning: {}\nAmplified: {}\nBody Type: {}\nFretboard: {}".format(self.manufacturer, self.strings_type, self.string_number, self.tuning, self.amplified, self.body_type, self.fretboard)
        return msg


if __name__ == "__main__":
    electric = Electric()
    print(electric.information())  # Calls the overridden method in Electric class

    acoustic = Acoustic()
    print(acoustic.information())  # Calls the overridden method in Acoustic class

    # Calling other methods specific to each class
    print(electric.solo())
    print(acoustic.strum())




