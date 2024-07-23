#!/bin/bash

resolve_symlinks() {
    local directory="$1"
    for file in $(find "$directory" -type l); do
        echo "$file"
        resolved_path=$(readlink "$file")
        echo "Resolving symlink: $file -> $resolved_path"
        try_copy "$resolved_path" "${file%_link}"
    done
}

try_copy() {
    local src="$1"
    local dst="$2"
    if cp "$src" "$dst"; then
        echo "Copied $src to $dst"
    else
        echo "Error resolving symlink: $?"
    fi
}

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

resolve_symlinks "$1"