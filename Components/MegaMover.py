import os
import shutil
from Components.Colors import Colors
from Components.Constants import Directories, Extensions

class MegaMover:
    @staticmethod
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

    @staticmethod
    def move_audio_files(project_dir, asset_files):
        assets_dir = os.path.join(project_dir, "Assets")
        audio_dir = os.path.join(assets_dir, Directories.Audio)

        for file_path in asset_files:
            # Normalize paths for consistency
            normalized_path = os.path.normpath(file_path)
            absolute_path = os.path.abspath(os.path.join(project_dir, normalized_path))  # Ensure full path
            
            # Check if the file is an audio file
            if any(absolute_path.lower().endswith(f".{ext}") for ext in Extensions.Audio):
                
                print(Colors.CYAN + f"Found audio file: {file_path}" + Colors.RESET)
                # Check if it's already in an Audio directory at any level
                if Directories.Audio not in [dir for dir in normalized_path.split(os.sep)]:
                    MegaMover.move_asset_with_meta(absolute_path, audio_dir)

    @staticmethod
    def move_prefab_files(project_dir, asset_files):
        assets_dir = os.path.join(project_dir, "Assets")
        prefab_dir = os.path.join(assets_dir, Directories.Prefabs)

        for file_path in asset_files:
            # Normalize paths for consistency
            normalized_path = os.path.normpath(file_path)
            absolute_path = os.path.abspath(os.path.join(project_dir, normalized_path))

            # Check if the file is a prefab file
            if any(absolute_path.lower().endswith(f".{ext}") for ext in Extensions.prefab_file_extensions):
                print(Colors.CYAN + f"Found prefab file: {file_path}" + Colors.RESET)
                # Check if it's already in a Prefabs directory at any level
                if Directories.Prefabs not in [dir for dir in normalized_path.split(os.sep)]:
                    MegaMover.move_asset_with_meta(absolute_path, prefab_dir)

    @staticmethod
    def move_scene_files(project_dir, asset_files):
        assets_dir = os.path.join(project_dir, "Assets")
        scenes_dir = os.path.join(assets_dir, Directories.Scenes)

        for file_path in asset_files:
            # Normalize paths for consistency
            normalized_path = os.path.normpath(file_path)
            absolute_path = os.path.abspath(os.path.join(project_dir, normalized_path))

            # Check if the file is a scene file
            if any(absolute_path.lower().endswith(f".{ext}") for ext in Extensions.Scenes):
                print(Colors.CYAN + f"Found scene file: {file_path}" + Colors.RESET)
                # Check if it's already in a Scenes directory at any level
                if Directories.Scenes not in [dir for dir in normalized_path.split(os.sep)]:
                    MegaMover.move_asset_with_meta(absolute_path, scenes_dir)