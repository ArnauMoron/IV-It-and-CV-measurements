# iV and iT Measurement Program

This program allows for simultaneous measurements of leakage current (IV) and test current (It) using two Keithley 2410 multimeters. It is also designed to work with any multimeter compatible with the SCPI language, but has not been tested.

## Requirements

To run this program, you need to have the following Python libraries installed (there is also a requirements.txt file attached with the package)

- `numpy`
- `matplotlib`
- `pyqt5`
- `pyvisa`

Additionally, you need to install the appropriate backend for `pyvisa` compatible with the GPIB interface of your manufacturer, either National Instruments or Keysight.

1. **Clone the full package into one directory**:
    Full package is (IV_It.py and config.cfg)
    cd your_directory

2. **Install the dependences**:
    pip install numpy matplotlib pyqt5 pyvisa

    Other packages may be needed
    Also, ensure that you install the correct backend for `pyvisa` depending on your GPIB setup. For National Instruments, you can download the driver from [National Instruments](https://www.ni.com/es/support/downloads/drivers/download.ni-488-2.html#544048). If you are using Keysight hardware, download the IO Libraries Suite from [Keysight](https://www.keysight.com/us/en/lib/software-detail/computer-software/io-libraries-suite-downloads-2175637.html). This program is compatible to work with both at the same time, but I encourage to work with National Instruments VISA as primary and Keysight VISA as secondary.

3. **Configuration**:
    The program supports three different configurations:

    General Configuration: Sets common parameters for both functionalities.
    IV Configuration: Sets specific parameters for leakage current measurements.
    It Configuration: Sets specific parameters for test current measurements.
    To adjust these configurations, modify the parameters in the provided configuration boxes.

4. **Usage**:
    Run the programm using python IV_It.py
    Configure the necessary parameters in the respective sections.
    Configure the PATH where the data is going to be stored.
    Press the "Run" button to start automatic measurements.
    Use the "Abort" button to stop an ongoing measurement.
    The current limit functionality helps protect the equipment from potential damage.

5. **Data format**:
    In the resulting files where data is stored in this format: V1, I1, V2, I2, t. Time is stored in a timestamp format, which can be turned into a date using datetime model calling datetime.datetime.fromtimestamp(timestamp). It  is posible to change that structure editing the function savefile(). Comment: It changes the headers depending if the measurement is IV or It and the number of devices enabled (1 or 2)

6. **Comments on GPIB configuration**:
    The program is set up to detect devices on GPIB 25 as ring and on GPIB 24 as PAD. You can change this configuration:
    In the pykeithleyMonitor.py file, modify the getname function.
    Alternatively, change the addresses directly on the Keithley instruments.

7. **Debug configuration**:
    If the program does not detect a device, it substitutes it with a dummy that simulates a resistor. Depending on the model, the resistor will be larger or smaller. The dummy and device model can be changed in the configuration file.

8. **Compatibility**:
    The program is designed to work with Keithley 2410 models but also includes configurations for models lower than the 2400 series. It has not been tested with other Keithley models.

9. **Contact**:
    Developed by Arnau Morón based on a previous program developed by Ivan Lopez and Peter Svriha.

    Email: [contact email](arnau.moron@gmail.com)

    Thank you for using this program! If you have any questions or issues, feel free to get in touch.
