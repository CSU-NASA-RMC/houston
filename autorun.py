# Launch and tend to autonomous run
import remote

port = 42070

def init():
    print("Starting autonomous run")
    run_file = input("Enter name of remote script: ")
    print(remote.send_until(run_file, port, 10))

if __name__ == "__main__":
    print(remote.send_until("test_runfile", port, 10))