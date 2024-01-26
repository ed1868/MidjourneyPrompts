import os
import glob

def convert_webp_files(path):
    print(path)
    # Path Sanitizing
    if not path.endswith('/'):
        path += '/'
    
    # Find all Webp Files in the Folder Path
    webp_files = glob.glob(path + '*.webp')
    
    webp_files.sort()
    
    # print(webp_files)
    
    # Convert and Rename each file
    
    for i, path in enumerate(webp_files, start=1):
        print(i)
        new_file_name = f"nomad{i}.jpg"
        # os.path.join(path, new_file_name)
        os.rename(path, new_file_name)
        print(f"Renamed '{path}' to '{i}' ")
        

path = '../assets/images'

convert_webp_files(path)