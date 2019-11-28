# houston
This is the base station program to control the rover.

Written and tested in Python 3.8 but will probably work in any 3.x version

## How to use

### Setup
#### Install Python
##### Mac/Windows
* Go to https://www.python.org/
* Download Python 3.x for your platform (make sure it's the 64 bit version if on Windows)
* When installing, check boxes to 'add pip to PATH', 'associate file types', 'precompile std lib', etc.

##### Linux
* Using your distro's package manager, install

        python3
        pip3

#### Install modules
* Open Terminal (Mac/linux) or Powershell (Windows)
* Run the following command (on Linux, replace 'pip' with 'pip3')

        pip install inputs

### Running
* Boot up the rover and connect to the network via Wifi or ethernet

#### Windows
* Go to folder containing houston.py
* Double click on houston.py

#### Mac/Linux
* Open a Terminal application
* Run the command (on Linux, replace 'python' with 'python3')

      python path/to/houston.py
 
### Usage
The program will provide an interactive text menu. Type the desired option from the list and press enter to execute the command.

##### Autonomous mode:
* Launch houston.py
* Use built in utility to upload a runfile to CAM
* Execute the runfile using the menu

##### Manual mode:
* Connect an Xbox compatible controller to you computer via USB and insure it is detected by the OS (usually automatic)
* Launch houston.py
* Enter manual mode using the menu

###### Easy control
<img src="https://raw.githubusercontent.com/CSU-NASA-RMC/houston/master/images/Xbox%20Layout%20-%20Easy%20Mode.png" height="400px">

###### Advanced control
<img src="https://raw.githubusercontent.com/CSU-NASA-RMC/houston/master/images/Xbox%20Layout%20-%20Advanced%20Mode.png" height="400px">
