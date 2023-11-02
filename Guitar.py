class Guitar:
    def __init__(self, brand, strings):
        self.brand = brand  # Attribute specific to the Guitar class
        self.strings = strings  # Attribute specific to the Guitar class

    def play(self):
        print("Strumming the guitar...")

# Child class - ElectricGuitar
class ElectricGuitar(Guitar):
    def __init__(self, brand, strings, pickups, frets):
        super().__init__(brand, strings)  # Inheriting attributes from the Guitar class
        self.pickups = pickups  # Attribute specific to ElectricGuitar class
        self.frets = frets  # Attribute specific to ElectricGuitar class
    
    def solo(self):
        print("Playing an electrifying guitar solo!")

# Child class - AcousticGuitar
class AcousticGuitar(Guitar):
    def __init__(self, brand, strings, wood_type, body_shape):
        super().__init__(brand, strings)  # Inheriting attributes from the Guitar class
        self.wood_type = wood_type  # Attribute specific to AcousticGuitar class
        self.body_shape = body_shape

    def strum(self):
        print("Strumming the soothing tones of an acoustic guitar.")

        
fender = ElectricGuitar("Fender", 6, "Single-coil", 24)
print(f"Fender Electric Guitar with {fender.strings} strings, {fender.pickups} pickups, and {fender.frets} frets.")
fender.play()  # Inherited method from the Guitar class
fender.solo()  # Method specific to ElectricGuitar class

print("\n")

# Acoustic guitar instance
martin = AcousticGuitar("Martin", 6, "Mahogany", "Dreadnought")
print(f"Martin Acoustic Guitar with {martin.strings} strings, made of {martin.wood_type} wood, and has a {martin.body_shape} body.")
martin.play()  # Inherited method from the Guitar class
martin.strum()
