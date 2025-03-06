from Components.Colors import Colors
from Components.ProjectVerifier import input_directory
from Components.AssetScanner import list_assets_files, check_meta_files
from Components.MegaMover import MegaMover

def main():
    project_dir = input_directory()
    print(Colors.CYAN + f"\nValid Unity project found at: {project_dir}" + Colors.RESET)
    
    assets_files, meta_file_tuples = list_assets_files(project_dir)
    check_meta_files(project_dir, meta_file_tuples)
    
    MegaMover.move_audio_files(project_dir, meta_file_tuples)
    
if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
