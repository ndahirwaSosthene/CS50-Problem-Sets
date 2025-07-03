# File Extensions

extensions.py is a simple script that maps file extensions to their corresponding media (MIME) types.

The program prompts the user for a file name and outputs its media type based on the file’s extension (e.g., .gif, .jpg, .pdf).
If the extension is not recognized or missing, it outputs application/octet-stream as a default.

Supported extensions and their media types include:

.gif → image/gif

.jpg or .jpeg → image/jpeg

.png → image/png

.pdf → application/pdf

.txt → text/plain

.zip → application/zip

Run with python extensions.py and enter a file name to see its media type.
Created for a CS50 exercise on string methods and conditional logic.