import time
import threading
import os

class PomodoroClock:
    def __init__(self, minutes, session_name="Work"):
        self.minutes = minutes
        self.seconds = minutes * 60
        self.session_name = session_name
        self.running = False
        self.paused = False
        self.thread = None
        self.state = "Idle"
        self.start_time = None
        self.elapsed_paused_time = 0

    def start(self):
        if not self.running:
            self.running = True
            self.state = "Running"
            self.start_time = time.time()
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
    
    def run(self):
        while self.seconds > 0 and self.running:
            if not self.paused:
                mins, secs = divmod(self.seconds, 60)
                self.print_table(f"{self.session_name} {mins:02d}:{secs:02d}")
                time.sleep(1)
                self.seconds -= 1
            else:
                time.sleep(0.1)  # Reduce CPU usage when paused
                
        if self.running and self.seconds == 0:
            self.state = "Completed"
            self.print_table(f"{self.session_name} 00:00")
            self.running = False
            # Sound notification when finished
            print("\a")  # Beep sound

    def pause(self):
        if self.running and not self.paused:
            self.paused = True
            self.state = "Paused"
    
    def resume(self):
        if self.running and self.paused:
            self.paused = False
            self.state = "Running"
    
    def stop(self):
        if self.running:
            self.running = False
            self.state = "Stopped"

    def reset(self):
        was_running = self.running
        if was_running:
            self.stop()
        self.paused = False
        self.seconds = self.minutes * 60
        self.state = "Reset"
        return was_running

    def get_remaining_time(self):
        return self.seconds

    def print_table(self, timer_display):
        os.system('cls' if os.name == 'nt' else 'clear')  # Cross-platform clear
        print("#" * 40)
        print(f"# {timer_display.center(36)} #")
        print(f"# Status: {self.state.ljust(28)} #")
        print("#" + "-" * 38 + "#")
        print(f"# [p] Pause      [r] Resume            #")
        print(f"# [s] Stop       [x] Reset             #")
        print(f"# [q] Quit                             #")
        print("#" * 40)


def run_with_commands(timer: PomodoroClock):
    timer.start()

    while True:
        try:
            command = input("\nCommand [p/r/s/x/q]: ").lower().strip()
        except KeyboardInterrupt:
            print("\nInterruption detected. Exiting...")
            timer.stop()
            break

        if command == "p":
            timer.pause()
        elif command == "r":
            timer.resume()
        elif command == "s":
            timer.stop()
        elif command == "x":
            was_running = timer.reset()
            if was_running:
                timer.start()
        elif command == "q":
            timer.stop()
            break
        elif command == "":
            continue  # Ignore empty input
        else:
            print("Invalid command. Use: p, r, s, x, q")

        # Check if timer ended naturally
        if not timer.running and timer.state == "Completed":
            print(f"\n{timer.session_name} completed!")
            time.sleep(2)  # Pause to show message
            break


def pomodoro_cycle():
    pomodoros = 4
    completed_sessions = 0
    
    print("=== STARTING POMODORO CYCLE ===")
    
    for i in range(1, pomodoros + 1):
        print(f"\nPomodoro {i} of {pomodoros}")
        timer = PomodoroClock(25, "Work")
        run_with_commands(timer)
        completed_sessions += 1

        # Check if user wants to continue
        if not timer.running and timer.state != "Completed":
            print("\nCycle interrupted by user.")
            break

        if i < pomodoros:
            print(f"\nShort break ({completed_sessions}/{pomodoros} completed)")
            timer = PomodoroClock(5, "Break")
            run_with_commands(timer)
        else:
            print(f"\nAll pomodoros completed! Long break")
            timer = PomodoroClock(15, "Long Break")
            run_with_commands(timer)

    print("\n=== POMODORO CYCLE FINISHED ===")


def single_session():
    """Mode for a single custom session"""
    try:
        minutes = int(input("Duration in minutes: "))
        name = input("Session name: ") or "Session"
        timer = PomodoroClock(minutes, name)
        run_with_commands(timer)
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    print("Pomodoro Timer")
    print("1. Full cycle (4 pomodoros)")
    print("2. Single session")
    
    try:
        choice = input("Select option (1/2): ").strip()
        if choice == "2":
            single_session()
        else:
            pomodoro_cycle()
    except KeyboardInterrupt:
        print("\nGoodbye!")