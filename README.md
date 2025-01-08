# File Organizer 🗂️  

## Overview  
The **File Organizer** is a Python-based automated solution designed to streamline file management tasks. This tool categorizes files based on their type, size, and creation/modification date, enabling efficient organization and retrieval. With its batch processing capability and robust error handling, this organizer significantly reduces file management time and ensures seamless operations across multiple directories.  

---

## Technologies Used  

- **Core Libraries:**  
  - `os`: For file and directory operations.  
  - `shutil`: For file movement and copying.  
  - `logging`: For error handling and operational logs.  
- **Batch Processing:** Handles up to 500 files per minute.  
- **Version Control:** Git  

---

## Features  

### 1. Automated File Categorization  
- Organizes files by:  
  - **Type:** Groups files into folders (e.g., Documents, Images, Videos).  
  - **Size:** Creates subfolders for small, medium, and large files.  
  - **Date:** Sorts files by year and month of creation/modification.  

### 2. Batch Processing  
- Processes 500+ files per minute.  
- Efficiently handles directories with 20,000+ files.  

### 3. File Operations  
- Supports renaming, moving, and copying files in bulk.  
- Maintains directory structure during file organization.  

### 4. Error Handling & Logging  
- Comprehensive error handling for file permission issues, missing files, etc.  
- Logs all operations and errors in a `log.txt` file.  

---

## Installation & Setup  

### Prerequisites  
- Python 3.7 or higher.  
- Install required libraries (if not part of the standard library):  
  ```bash  
  pip install -r requirements.txt  
