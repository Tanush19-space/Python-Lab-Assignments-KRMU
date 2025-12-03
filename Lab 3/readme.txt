LIBRARY INVENTORY MANAGER
=========================

A simple command-line Library Inventory Manager written in Python.
This program allows adding, viewing, searching, issuing, and returning books.
Data is persistently stored in a local JSON file (`books.json`).

Files
-----
- `Library Inventory Manager.py`  : Main program script (menu-driven CLI)
- `books.json`                   : Auto-generated data file (JSON)

Requirements
------------
- Python 3.x
- Uses only the Python standard library (`json`) — no external packages required

Quick Start
-----------
1. Open a terminal in the folder containing `Library Inventory Manager.py`.
2. Run the program:

   python "Library Inventory Manager.py"

3. Use the menu to add, view, search, issue, or return books.

Menu Options
------------
1. Add Book   - Prompt for title, author, ISBN; saves with status `available`.
2. View Books - Display all books and their status.
3. Search Book- Lookup by exact Title or ISBN.
4. Issue Book - Mark an `available` book as `issued` (by ISBN).
5. Return Book- Mark an `issued` book as `available` (by ISBN).
6. Exit       - Quit the program.

Data Format
-----------
Each book is saved as a JSON object in the `books.json` array with fields:
{
    "title": "Book Title",
    "author": "Author Name",
    "isbn": "ISBN Number",
    "status": "available" | "issued"
}

CSV / Other Notes
-----------------
- The script currently uses JSON for persistence and does not import/export CSV.
- Search matches must be exact for titles (case-sensitive). Searching by ISBN is recommended.

Limitations & Suggestions
-------------------------
- No duplicate-ISBN protection (consider adding checks).
- No user accounts, due dates, or copy counts — assumes one copy per ISBN.
- Consider adding fuzzy search, edit/delete functionality, and validation for ISBN formatting.

Troubleshooting
---------------
- If no books appear, ensure `books.json` exists in the same folder or add a book.
- If you get file permission errors, run the program from a folder with write access.
- To recover from corrupted JSON, rename or delete `books.json` and restart; the program will recreate it.

License
-------
Educational / personal use. No warranty.

Contact / Improvements
---------------------
You can edit the script directly to add features or convert it into a package/module.

Last updated: December 2025

