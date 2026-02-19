# Mini Language Interpreter

def execute_command(command):
    parts = command.strip().split()
    
    if not parts:
        return  # empty line
    
    cmd = parts[0].upper()

    if cmd == "PRINT":
        print(" ".join(parts[1:]))
    elif cmd == "ADD":
        try:
            result = float(parts[1]) + float(parts[2])
            print(result)
        except (IndexError, ValueError):
            print("Error: ADD requires two numbers")
    elif cmd == "SUB":
        try:
            result = float(parts[1]) - float(parts[2])
            print(result)
        except (IndexError, ValueError):
            print("Error: SUB requires two numbers")
    elif cmd == "MUL":
        try:
            result = float(parts[1]) * float(parts[2])
            print(result)
        except (IndexError, ValueError):
            print("Error: MUL requires two numbers")
    elif cmd == "DIV":
        try:
            if float(parts[2]) == 0:
                print("Error: Division by zero")
            else:
                result = float(parts[1]) / float(parts[2])
                print(result)
        except (IndexError, ValueError):
            print("Error: DIV requires two numbers")
    else:
        print(f"Unknown command: {cmd}")


def run_program(file_path):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Skip comments
                if line.strip().startswith("#") or not line.strip():
                    continue
                execute_command(line)
    except FileNotFoundError:
        print(f"File not found: {file_path}")


if __name__ == "__main__":
    file_name = input("Enter program filename (e.g., program.txt): ")
    run_program(file_name)
