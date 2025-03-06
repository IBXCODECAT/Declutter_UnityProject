import os
from components.colors import Colors

def is_unity_project(directory):
    """Check if the given directory is a valid Unity project and log verification steps."""
    required_dirs = {
        "Assets": os.path.join(directory, "Assets"),
        "ProjectSettings": os.path.join(directory, "ProjectSettings"),
        "Packages": os.path.join(directory, "Packages")
    }
    
    project_settings_file = os.path.join(directory, "ProjectSettings", "ProjectVersion.txt")

    print(Colors.WHITE + "\nProject Path Verification:" + Colors.RESET)

    all_pass = True
    for name, path in required_dirs.items():
        if os.path.isdir(path):
            print(Colors.GREEN + f"-> {name}... PASS" + Colors.RESET)
        else:
            print(Colors.RED + f"-> {name}... FAIL (expected)" + Colors.RESET)
            all_pass = False

    if os.path.isfile(project_settings_file):
        print(Colors.GREEN + "-> ProjectVersion.txt found... PASS" + Colors.RESET)
    else:
        print(Colors.RED + "-> ProjectVersion.txt missing... FAIL (expected)" + Colors.RESET)
        all_pass = False

    return all_pass

def input_directory():
    """Prompt the user for a Unity project directory and verify it."""
    while True:
        input_directory = input(Colors.RESET + "Enter project root directory: " + Colors.YELLOW).strip()

        if os.path.isdir(input_directory) and is_unity_project(input_directory):
            return input_directory

        print(Colors.RED + "The specified directory does not exist on the system." + Colors.RESET)
