#temperatureconvertor.py

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(temp_celsius):
        """Convert Celsius to Fahrenheit"""
        return (temp_celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(temp_fahrenheit):
        """Convert Fahrenheit to Celsius"""
        return (temp_fahrenheit - 32) * 5/9

    @classmethod
    def info(cls):
        """Display class information"""
        print("This class provides temperature conversion utilities.")

# Convert 100°C to Fahrenheit
print(f"100°C to Fahrenheit: {TemperatureConverter.celsius_to_fahrenheit(100)}°F")  

# Convert 212°F to Celsius
print(f"212°F to Celsius: {TemperatureConverter.fahrenheit_to_celsius(212)}°C")  

# Display class info
TemperatureConverter.info()
