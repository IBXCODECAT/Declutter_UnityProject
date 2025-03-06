import os
from components.colors import Colors
from components.project_verifier import is_unity_project, input_directory
from components.asset_scanner import list_assets_files, check_meta_files

def main():
    # Get the Unity project directory
    project_dir = input_directory()
    print(Colors.CYAN + f"\nValid Unity project found at: {project_dir}" + Colors.RESET)

    # List all files in the Assets folder (excluding .meta files) and generate meta file paths
    assets_files, meta_file_tuples = list_assets_files(project_dir)

    # Check if meta files exist and warn if they don't
    check_meta_files(project_dir, meta_file_tuples)

if __name__ == "__main__":
    main()

input("Press Enter to exit...")