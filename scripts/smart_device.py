"""A small example of class defaults and per-object instance attributes."""


class SmartDevice:
    def __init__(
        self,
        name: str,
        device_type: str,
        battery_level: int = 100,
        car: str | None = None,
    ) -> None:
        if not 0 <= battery_level <= 100:
            raise ValueError("battery_level must be between 0 and 100")
        self.name = name
        self.device_type = device_type
        self.battery_level = battery_level
        self.car = car


if __name__ == "__main__":
    phone = SmartDevice("iPhone 15", "Smartphone")
    watch = SmartDevice("Galaxy Watch", "Smartwatch", battery_level=85)
    vehicle = SmartDevice("Model S", "Electric car", battery_level=40, car="Tesla")

    for device in (phone, watch, vehicle):
        print(
            f"{device.name}: {device.device_type}, "
            f"battery={device.battery_level}%, car={device.car or 'none'}"
        )
