import argparse

def setup_arguments():
    parser = argparse.ArgumentParser(prog="agile-assignment", description="App for gym membership management.")
    
    parser.add_argument('-c', '--cli', help="Run the app in CLI mode only.")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = setup_arguments()
    