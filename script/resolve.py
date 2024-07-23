import os
import sys
import shutil

def resolve_symlinks(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.islink(file_path):
                print(file_path)
                resolved_path = os.readlink(file_path)
                print(f"Resolving symlink: {file_path} -> {resolved_path}")
                try:
                    os.unlink(file_path)
                    shutil.copy(resolved_path, file_path)
                except Exception as e:
                    print(f"Error resolving symlink: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python resolve_symlinks.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    resolve_symlinks(directory)