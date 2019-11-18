# Launch and tend to autonomous run
import remote

port = 42071

def init():
    print("Starting autonomous run")
    run_file = input("Enter name of remote script: ")
    load_status = remote.send(run_file, port) # Possible race condition if you type really fast
    if load_status != "OK":
        print("Error loading file: {}".format(load_status))
        return
    print("File loaded")
    # Get user input
    while True:
        opt = input("Autonomy Options:\n"
                    "\tQ - Kill script and return to menu\n"
                    "\tS - Start script\n"
                    "\t0 - Get status update\n"
                    "Enter choice: ")
        if opt.capitalize() == 'Q':
            remote.send('KP', port)
            return
        elif opt.capitalize() == 'S':
            remote.send('GO', port)
        elif opt != '':
            response = remote.send(opt, port)
            print(response)
            if response == "FIN":
                print("Program finished")
                return

if __name__ == "__main__":
    print(remote.send("AR", 42069))
    print(remote.send("test_runfile", port))
