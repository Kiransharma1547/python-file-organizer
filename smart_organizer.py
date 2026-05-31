files = [
    "photo.jpg",
    "movie.mp4",
    "notes.txt",
    "resume.pdf",
    "python.py"
]

for file in files:

    if file.endswith(".jpg"):
        print(file, "→ Image File")

    elif file.endswith(".mp4"):
        print(file, "→ Video File")

    elif file.endswith(".pdf"):
        print(file, "→ PDF File")

    elif file.endswith(".txt"):
        print(file, "→ Text File")

    else:
        print(file, "→ Other File")