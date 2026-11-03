
# 💽 Disk Scheduling Algorithm Simulator

A Python-based Graphical User Interface (GUI) application that simulates different disk scheduling algorithms used in Operating Systems.

## 📌 Project Overview

The Disk Scheduling Algorithm Simulator allows users to enter disk configuration details, provide a disk request queue, select a scheduling algorithm, and calculate disk head movement.

It provides an easy way to understand how different disk scheduling algorithms process requests.

## ⚙️ Supported Algorithms

| No. | Algorithm | Description |
|---|---|---|
| 1 | FIFO | First In, First Out |
| 2 | SSTF | Shortest Seek Time First |
| 3 | LOOK | LOOK Disk Scheduling |
| 4 | ELEVATOR | SCAN Disk Scheduling |
| 5 | C-SCAN | Circular SCAN Disk Scheduling |

## ✨ Features

- Customizable number of disk cylinders
- User-defined initial head position
- Custom disk request queue
- Algorithm selection
- Upward and downward head direction
- Total head movement calculation
- Average head movement calculation
- Graphical User Interface using Tkinter

## 🖥️ Technologies Used

- Python 3
- Tkinter
- GitHub

## 📂 Project Structure

```text
Disk-Scheduling-Visualizer/
│
├── app.py
├── disk_algorithms.py
├── README.md
└── .gitignore
```

## 🚀 How to Run

### Requirements

- Python 3 installed
- Tkinter installed

### Steps

1. Clone or download this repository.
2. Open the project folder.
3. Run the following command:

```bash
python app.py
```

## 📊 Output

The simulator displays:

- Selected scheduling algorithm
- Head movement sequence
- Individual head movements
- Total head movement
- Average head movement

## 🎯 Project Purpose

This project was developed to demonstrate and understand disk scheduling techniques in Operating Systems through an interactive graphical application.
