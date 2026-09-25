# Over-Voltage and Under-Voltage Protection System

voltage = float(input("Enter voltage (V): "))

# Safe voltage range
MIN_VOLTAGE = 210
MAX_VOLTAGE = 250

if voltage < MIN_VOLTAGE:
    print("UNDER-VOLTAGE detected!")
    print("Protection: LOAD OFF")

elif voltage > MAX_VOLTAGE:
    print("OVER-VOLTAGE detected!")
    print("Protection: LOAD OFF")

else:
    print("Voltage is NORMAL")
    print("Protection: LOAD ON")
