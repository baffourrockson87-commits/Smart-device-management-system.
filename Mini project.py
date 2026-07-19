
class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id   # private attribute
        self.__power_status = False    # private attribute

    # Encapsulation: getters and setters
    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, new_id):
        if new_id.strip() == "":
            print("Device ID cannot be empty!")
        else:
            self.__device_id = new_id

    @property
    def power_status(self):
        return self.__power_status

    def turn_on(self):
        self.__power_status = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.__power_status = False
        print(f"{self.name} is now OFF.")

    def display_info(self):
        print(f"Device: {self.name}, ID: {self.__device_id}, Power: {self.__power_status}")


class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature=25):
        super().__init__(name, device_id)
        self.temperature = temperature

    def read_temperature(self):
        print(f"{self.name} Temperature: {self.temperature}°C")



class SecurityCamera(SmartDevice):
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.recording_status = False

    def start_recording(self):
        self.recording_status = True
        print(f"{self.name} started recording.")

    def stop_recording(self):
        self.recording_status = False
        print(f"{self.name} stopped recording.")


class SmartLight(SmartDevice):
    def __init__(self, name, device_id, brightness=50):
        super().__init__(name, device_id)
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print("Brightness must be between 0 and 100.")

    def increase_brightness(self):
        if self.__brightness < 100:
            self.__brightness += 10
        print(f"{self.name} Brightness: {self.__brightness}")

    def decrease_brightness(self):
        if self.__brightness > 0:
            self.__brightness -= 10
        print(f"{self.name} Brightness: {self.__brightness}")



temp_sensor = TemperatureSensor("Living Room Sensor", "TS001", 28)
smart_light = SmartLight("Bedroom Light", "SL001", 70)
camera = SecurityCamera("Front Door Camera", "SC001")

devices = [temp_sensor, smart_light, camera]


def menu():
    while True:
        print("\nSmart Device Management Menu")
        print("1. Display Device Information")
        print("2. Turn Device On")
        print("3. Turn Device Off")
        print("4. Read Temperature")
        print("5. Adjust Brightness")
        print("6. Start Recording")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            for d in devices:
                d.display_info()

        elif choice == "2":
            device_id = input("Enter Device ID: ")
            for d in devices:
                if d.device_id == device_id:
                    d.turn_on()

        elif choice == "3":
            device_id = input("Enter Device ID: ")
            for d in devices:
                if d.device_id == device_id:
                    d.turn_off()

        elif choice == "4":
            temp_sensor.read_temperature()

        elif choice == "5":
            smart_light.increase_brightness()

        elif choice == "6":
            camera.start_recording()

        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid choice, try again.")


# Run the menu
if __name__ == "__main__":
    menu()
