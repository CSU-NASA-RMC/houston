# houston
This is the base station program to control the rover.

Written and tested in Python 3.8 but will probably work in any 3.x version

## Setup
### Install Python
#### Mac/Windows
* Go to https://www.python.org/
* Download Python 3.x for your platform (make sure it's the 64 bit version if on Windows)
* When installing, check boxes to 'add pip to PATH', 'associate file types', 'precompile std lib', etc.

#### Linux
* Using your distro's package manager, install

        python3
        python3-pip

### Install modules
* Open Terminal (Mac/linux) or Powershell (Windows)
* Run the following command (on Linux, replace 'pip' with 'pip3')

        pip install inputs

## Running
* Boot up the rover and connect to the network via Wifi or ethernet

### Windows
* Go to folder containing houston.py
* Double click on houston.py

### Mac/Linux
* Open a Terminal application
* Run the command (on Linux, replace 'python' with 'python3')

      python path/to/houston.py
 
## Usage
The program will provide an interactive text menu. Type the desired option from the list and press enter to execute the command.

#### Autonomous mode:
* Launch houston.py
* Execute a runfile using the menu

#### Manual mode:
* Connect an Xbox compatible controller to you computer via USB **before** launching houston
* Launch houston.py
* Enter manual mode using the menu

| Xbox controller button | Rover action (Advanced mode) | Rover action (Easy mode) Coming soon<sup>tm</sup>|
| --------- | --------- | --------- |
| Start | Change to Easy mode | Change to Advanced mode |
| Select | Exit to menu | Exit to menu |
| A | Advance Auger | Unbound |
| B | Raise Depositor | Unbound |
| X | Lower Depositor | Unbound |
| Y | Retract Auger | Unbound |
| RT | Rotate auger forwards | Unbound |
| LT | Rotate auger backwards | Unbound |
| RB | Tilt auger down | Unbound |
| LB | Tilt auger up | Unbound |
| LS | Move rover | Unbound |
| RS | Unbound | Unbound |
| Dpad-N | Unbound | Unbound |
| Dpad-S | Unbound | Unbound |
| Dpad-E | Unbound | Unbound |
| Dpad-W | Unbound | Unbound |
