# Launch and tend to autonomous run
import remote

port = 42071 # Port for network

def init():
    # Try to load file
    print("Starting autonomous run")
    run_file = input("Enter name of remote script: ") # Get user input
    load_status = remote.send(run_file, port) # Probably impossible race condition if you type really fast
    if load_status != "OK": # Load failed
        print("Error loading file: {}".format(load_status))
        return # Exit to main menu

    # Autorun menu
    print("File loaded")
    # Get user input
    while True:
        opt = input("Autonomy Options:\n"
                    "\tQ - Kill script and return to menu\n"
                    "\tS - Start script\n"
                    "\t0 - Get status update\n"
                    "Enter choice: ")
        # Kill and return
        if opt.capitalize() == 'Q':
            remote.send('KP', port)
            return

        # Start run
        elif opt.capitalize() == 'S':
            if remote.send('GO', port) == "OK":
                print("Run started")
            else:
                print("Error starting run")

        # Send command, print response
        elif opt != '':
            response = remote.send(opt, port)
            print(response)
            if response == "FIN":
                print("Program finished")
                return

# Testing
if __name__ == "__main__":
    print(remote.send("AR", 42069))
    print(remote.send("test_runfile", port))
