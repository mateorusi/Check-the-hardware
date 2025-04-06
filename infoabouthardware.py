import psutil

# Function to gather hardware information
def hardware_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_used = memory.percent
    disk = psutil.disk_usage('/')
    disk_used = disk.percent

    return f"CPU Usage: {cpu_percent}%\nRAM Usage: {memory_used}%\nDisk Usage: {disk_used}%\n"

# Function to get CPU temperature
def get_temperature():
    try:
        temperatures = psutil.sensors_temperatures()
        if 'coretemp' in temperatures:
            for name, entries in temperatures['coretemp']:
                return f"{name}: {entries.current}°C"
        else:
            return "Temperature data not available."
    except Exception as e:
        return f"Error retrieving temperature data: {e}"

# Save hardware info and temperature to a file
def save_to_file():
    # Gather hardware information and temperature
    hardware_data = hardware_info()
    temperature_data = get_temperature()

    # Set the title (name) of the file where we'll save the data
    file_name = "hardware_diagnostics_report.txt"

    # Open the file in write mode and save the data
    with open(file_name, 'w') as file:
        file.write("Hardware Diagnostics Report\n")
        file.write("="*30 + "\n")
        file.write(hardware_data)
        file.write("\nTemperature Information:\n")
        file.write(temperature_data)
    
    print(f"Report saved to {file_name}")

# Main function to run the program
if __name__ == "__main__":
    save_to_file()
