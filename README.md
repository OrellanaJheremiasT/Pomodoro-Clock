# Pomodoro Timer ⏱️  

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Issues](https://img.shields.io/github/issues/OrellanaJheremiasT/pomodoro-timer)](https://github.com/OrellanaJheremiasT/pomodoro-timer/issues)  
[![Stars](https://img.shields.io/github/stars/OrellanaJheremiasT/pomodoro-timer?style=social)](https://github.com/OrellanaJheremiasT/pomodoro-timer/stargazers)  

An interactive **Python Pomodoro Timer** based on Francesco Cirillo's **Pomodoro Technique**.  
Manage your work and break sessions directly from the terminal, with commands to **pause, resume, stop, and reset** the timer.  

---

## 🚀 Features  

- **Full cycle mode** (4 pomodoros of 25 minutes with short and long breaks).  
- **Single session mode** (custom duration and session name).  
- **Terminal table interface**, clear and minimalistic.  
- Real-time interactive commands:  
  - `p` → Pause  
  - `r` → Resume  
  - `s` → Stop  
  - `x` → Reset  
  - `q` → Quit  
- End notification with **system beep**.  
- Cross-platform support: **Windows, Linux, macOS**.  

---

## 📖 Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/OrellanaJheremiasT/pomodoro-timer.git
   cd pomodoro-timer
   ```

2. Make sure you have **Python 3.8+** installed.  

3. Run the program:  
   ```bash
   python pomodoro.py
   ```

---

## 🖥️ Usage  

When you start, you will see two options:  

```
Pomodoro Timer
1. Full cycle (4 pomodoros)
2. Single session
Select option (1/2):
```

- **Option 1:** Runs a full cycle with 4 pomodoros (25 min each) and breaks (5 min short, 15 min long).  
- **Option 2:** Set up your own session (example: 50 min "Study").  

During execution, use these commands:  

```
[p] Pause       [r] Resume
[s] Stop        [x] Reset
[q] Quit
```

---

## 📷 Preview (terminal example)  

```
########################################
#            Work 24:59                #
# State: Running                       #
#--------------------------------------#
# [p] Pause       [r] Resume           #
# [s] Stop        [x] Reset            #
# [q] Quit                             #
########################################
```

---

## 📝 TODO / Future Improvements  

- Add desktop notifications.  
- Save statistics of completed sessions.  
- GUI mode (Tkinter or PyQt).  

---

## 📜 License  

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it.  
