class Directories:
    Art = "Art"
    Audio = "Audio"
    Prefabs = "Prefabs"
    Scenes = "Scenes"

class Extensions:
    asset_file_extensions = [ 'asset' ]
    
    Audio = [
        'flac', 'ogg', 'mp3', 'wav'
    ]

    prefab_file_extensions = [ 'prefab' ]
    Scenes = [ 'unity' ]
    script_file_extensions = [ 'asmdef', 'asmref', 'cs' ]
    shader_file_extensions = [ 'hlsl', 'shader' ]

    texture_file_extensions = [ 
        'png', 'jpg', 'jpeg', 'tiff', 'tif', 'gif',
        'bmp', 'psd', 'tga', 'hdr', 'exr', 'svg', 'svgz',
        'dds', 'ktx', 'pvr', 'astc', 'pkm', 'pkmz', 'webp'
    ]

    video_file_extensions = [
        'mp4', 'webm', 'avi', 'mov', 'flv', 'mkv', 'wmv',
        'mpg', 'mpeg', 'm4v', '3gp', '3g2', 'ogv', 'ogg'
    ]