import os
import shutil
from components.colors import Colors
from components.project_verifier import input_directory
from components.asset_scanner import list_assets_files, check_meta_files
from components.extensions import Extensions

def move_asset_with_meta(asset_path, destination_dir):
    """Moves an asset and its corresponding meta file to the destination directory."""
    os.makedirs(destination_dir, exist_ok=True)
    
    # Ensure absolute paths
    asset_path = os.path.abspath(asset_path)  # Resolve to absolute path
    destination_dir = os.path.abspath(destination_dir)
    
    new_asset_path = os.path.join(destination_dir, os.path.basename(asset_path))
    
    # Generate expected meta file path
    meta_path = asset_path + ".meta"
    new_meta_path = os.path.join(destination_dir, os.path.basename(meta_path))
    
    # Verify asset file exists before moving
    if os.path.exists(asset_path):
        shutil.move(asset_path, new_asset_path)
        print(Colors.GREEN + f"Moved: {asset_path} -> {new_asset_path}" + Colors.RESET)
    else:
        print(Colors.RED + f"Error: Asset file not found {asset_path}" + Colors.RESET)
        return
    
    # Move the meta file if it exists
    if os.path.exists(meta_path):
        shutil.move(meta_path, new_meta_path)
        print(Colors.GREEN + f"Moved: {meta_path} -> {new_meta_path}" + Colors.RESET)
    else:
        print(Colors.RED + f"Warning: Missing meta file for {asset_path}" + Colors.RESET)

def move_audio_files(project_dir, meta_file_tuples):
    assets_dir = os.path.join(project_dir, "Assets")
    audio_dir = os.path.join(assets_dir, "Audio")
    
    audio_extensions = Extensions.audio_file_extensions
    
    for _, file_path in meta_file_tuples:
        # Normalize paths for consistency
        normalized_path = os.path.normpath(file_path)
        absolute_path = os.path.abspath(os.path.join(project_dir, normalized_path))  # Ensure full path
        
        # Check if the file is an audio file
        if any(absolute_path.lower().endswith(f".{ext}") for ext in audio_extensions):
            print(Colors.YELLOW + f"Found audio file: {absolute_path}" + Colors.RESET)
            
            # Check if it's already in an Audio directory at any level
            if "audio" not in [folder.lower() for folder in normalized_path.split(os.sep)]:
                move_asset_with_meta(absolute_path, audio_dir)

def main():
    project_dir = input_directory()
    print(Colors.CYAN + f"\nValid Unity project found at: {project_dir}" + Colors.RESET)
    
    assets_files, meta_file_tuples = list_assets_files(project_dir)
    check_meta_files(project_dir, meta_file_tuples)
    move_audio_files(project_dir, meta_file_tuples)
    
if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
