import sys

INPUT_DIRECTORY = "input_data"
def main(args):
    try:
        file_path = f"{INPUT_DIRECTORY}/{args[1]}"
        try:
            with open(file_path, 'r') as file:
                str_data = file.read()
        except FileNotFoundError:
            print(f"Error: File not found. Please check the file path. (..{file_path})")
    except IndexError:
        print("Error: Provide file name as srgument when running script")


if __name__ == "__main__":
    main(sys.argv)