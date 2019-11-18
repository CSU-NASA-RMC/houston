# Launch and tend to autonomous run
import remote

port = 42071

# Checks if program is still running on CAM
def ask():
    return remote.send('HI', 42069) == 'BZ'

def init():
    print("Starting autonomous run")
    run_file = input("Enter name of remote script: ")
    print(remote.send(run_file, port)) # Possible race condition if you type really fast


if __name__ == "__main__":
    print(remote.send("AR", 42069))
    print(remote.send("test_runfile", port))
