# Library/CLI app to display some solarmax-smt data

Display some stats about the solarmax SMT. The
unit needs to be connected to the network.

Example output:
```
$ ./solarmax-smt
Current power: 3.37 kW
Max power today: 5.31 kW
Total power today: 12.00 kW
Total power: 143.00 kW
Internal converter temperature: 53.00 °C
Voltage 1: 392.60 V
Current 1: 0.83 A
Power 1: 0.33 kW
Voltage 2: 594.50 V
Current 2: 5.39 A
Power 2: 3.21 kW
```

## How to install

On Ubuntu/Debian just run:

```
$ sudo apt install -y python3-pymodbus
```

With that all dependencies are installed.

