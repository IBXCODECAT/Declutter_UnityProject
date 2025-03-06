import os
from Components.Colors import Colors

def list_assets_files(directory):
    """Search for all files in the Assets folder (excluding .meta files) and return only asset paths."""
    assets_path = os.path.join(directory, "Assets")
    file_list = []

    print(Colors.WHITE + "\nSearching for files in Assets folder..." + Colors.RESET)

    if not os.path.isdir(assets_path):
        print(Colors.RED + "Assets folder not found!" + Colors.RESET)
        return file_list

    for root, _, files in os.walk(assets_path):
        for file in files:
            if not file.endswith(".meta"):  
                file_path = os.path.relpath(os.path.join(root, file), directory) 
                file_list.append(file_path)

    if file_list:
        print(Colors.GREEN + f"Found {len(file_list)} files in Assets folder (excluding .meta files):\n" + Colors.RESET)
    else:
        print(Colors.RED + "No valid files found in Assets folder." + Colors.RESET)

    return file_list

def check_meta_files(directory, asset_files):
    """Check if meta files exist for the given asset files and provide a summary of missing vs. found."""
    linked_meta_count = 0  # Counter for found meta files
    missing_meta_count = 0  # Counter for missing meta files

    for asset in asset_files:
        meta_file = asset + ".meta"
        meta_full_path = os.path.join(directory, meta_file)
        
        if os.path.isfile(meta_full_path):
            linked_meta_count += 1
        else:
            missing_meta_count += 1

    # Print the summary of linked and missing meta files
    print(Colors.GREEN + f"Found {linked_meta_count} linked meta files, {missing_meta_count} missing." + Colors.RESET)
