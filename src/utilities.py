from tkinter import filedialog
from pathlib import Path


def file_picker(types=[], initial_dir=None, title="Select file(s)"):
    """
    Open a file picker window and return the selected file path(s).
    """

    # Allows selection of file type (default: all)
    file_types = []
    if "audio" in types:
        file_types.append(("Audio Files", '*.mp3 *.wav *.flac'))
    if "video" in types:
        file_types.append(("Video Files", '*.mkv *.mp4 *.avi'))
    if "subtitle" in types:
        file_types.append(("Subtitle Files", '*.srt'))
    if "text" in types:
        file_types.append(("Text Files", '*.txt'))
    if "all" in types or not file_types: 
        file_types.append(("All Files", '*.*'))

    filepaths = filedialog.askopenfilenames(
        title=title,
        filetypes=file_types,
        initialdir=initial_dir)
    
    return filepaths


