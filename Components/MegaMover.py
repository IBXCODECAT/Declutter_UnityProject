import os
import shutil
from Components.Colors import Colors
from Components.Extensions import Extensions

class MegaMover:
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
                    MegaMover.move_asset_with_meta(absolute_path, audio_dir)