# ⚙️ Task Automation

## 📌 Overview

The Task Automation project automatically organizes files into separate folders based on their file extensions. It helps keep directories clean and demonstrates practical automation using Python.

---

## ✨ Features

- Organizes files automatically
- Creates folders if they do not exist
- Supports Images, Documents, Audio, Videos, Programs, and Archives
- Moves unknown files into an "Others" folder
- Beginner-friendly implementation

---

## 🛠️ Technologies Used

- Python 3
- os Module
- shutil Module

---

## 📁 Project Structure

```
03_Task_Automation/
│
├── task_automation.py
├── README.md
├── requirements.txt
└── screenshot.png
```

---

## ▶️ How to Run

```bash
python task_automation.py
```

Enter the folder path you want to organize when prompted.

---

## 💻 Sample Output

```
Enter the folder path to organize:
C:\Users\Dakshinya\Downloads\Test

Moved: report.pdf → Documents
Moved: image.png → Images
Moved: song.mp3 → Audio
Moved: program.py → Programs

✅ File organization completed successfully!
```

---

## 📚 Concepts Used

- File Handling
- os Module
- shutil Module
- Loops
- Dictionaries
- Conditional Statements

---

## 🎯 Learning Outcome

This project improved my understanding of file automation, directory management, and organizing files using Python's built-in modules.