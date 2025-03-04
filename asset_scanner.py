import os
from colors import Colors

def list_assets_files(directory):
    """Search for all files in the Assets folder (excluding .meta files) and list them along with their .meta counterparts."""
    assets_path = os.path.join(directory, "Assets")
    file_list = []
    meta_file_tuples = []

    print(Colors.WHITE + "\nSearching for files in Assets folder..." + Colors.RESET)

    if not os.path.isdir(assets_path):
        print(Colors.RED + "Assets folder not found!" + Colors.RESET)
        return file_list, meta_file_tuples

    for root, _, files in os.walk(assets_path):
        for file in files:
            if not file.endswith(".meta"):  
                file_path = os.path.relpath(os.path.join(root, file), directory) 
                meta_file_path = file_path + ".meta" 

                file_list.append(file_path)
                meta_file_tuples.append((meta_file_path, file_path))

    if file_list:
        print(Colors.GREEN + f"Found {len(file_list)} files in Assets folder (excluding .meta files):\n" + Colors.RESET)
    else:
        print(Colors.RED + "No valid files found in Assets folder." + Colors.RESET)

    return file_list, meta_file_tuples

def check_meta_files(directory, meta_file_tuples):
    """Check if meta files exist and warn if they do not."""
    print(Colors.WHITE + "\nMeta File Verification:" + Colors.RESET)

    for meta, asset in meta_file_tuples:
        meta_full_path = os.path.join(directory, meta)
        
        if os.path.isfile(meta_full_path):
            print(Colors.GREEN + f"Meta: {meta} (exists)" + Colors.RESET)
        else:
            print(Colors.RED + f"Meta: {meta} (not found)" + Colors.RESET)
