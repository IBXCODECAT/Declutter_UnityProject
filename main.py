from Components.Colors import Colors
from Components.ProjectVerifier import input_directory
from Components.AssetScanner import list_assets_files, check_meta_files
from Components.MegaMover import MegaMover

def main():
    project_dir = input_directory()
    print(Colors.CYAN + f"\nValid Unity project found at: {project_dir}" + Colors.RESET)
    
    in_place = input(Colors.YELLOW + "Do you want to move the files in place? (y/n): " + Colors.RESET).strip().lower()
    
    assets_files = list_assets_files(project_dir)  # Only returns file list, no meta file tuples
    check_meta_files(project_dir, assets_files)  # Now using only the asset files list
    
    MegaMover.move_audio_files(project_dir, assets_files)  # Pass only the asset file list here
    MegaMover.move_prefab_files(project_dir, assets_files)  # Pass only the asset file list here
    MegaMover.move_scene_files(project_dir, assets_files)  # Pass only the asset file list here
    MegaMover.move_art_files(project_dir, assets_files)  # Pass only the asset file list here


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
