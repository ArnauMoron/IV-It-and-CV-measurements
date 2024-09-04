# HOW TO CREATE AN EXE FROM A .PY

1. **To make it lighter and faster, create a virtual environment in your computer using:**:
python -m venv name

2. **Activate it:**:
name\Scripts\actívate

3. **Install the requirements f the program (there are two requirements.txt files attached with the programs):**:
pip install -r path\requirements.txt (or pip install matplotlib pyvisa numpy pyqt5)

4. **Install auto-py-to-exe (graphical interface that uses pyinstaller)**:
pip install auto-py-to-exe

5. **Execute auto-py-to-exe to launch the graphical interface:**:
auto-py-to-exe

6. **Select all the files that are necessary and icons and chose the one directory option:**:
Path to file = CV.py or IV_It.py
Choose one directory
Choose icon (CV.ico or IV.ico), optional
Add the aditional files (config.cfg) with the changes that are necessary
In the settings options you can change the path where the exe file will be generated

7. **A .exe file now, should have been created that only works with a directory called _internal.**:

8. **Install in your computer Inno Setup Compiler.**:

9. **Run and compile one of the files that appear in this repository (CV_MEAS.iss or IV_and_IT_MEAS.iss)**:
Change the paths that appear in the script.
Now an installer has been created so an app to do the measuremnts can be installed.
Every time a modification is done, I recommend to change the name of the app or uninstall the previous app as I am unsure of how would work  both versions on the same computer.

10. **Any question, contact me: [contact email](arnau.moron@gmail.com)**:
