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
            # Sonido o notificación cuando termina
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
        print(f"# Estado: {self.state.ljust(28)} #")
        print("#" + "-" * 38 + "#")
        print(f"# [p] Pausar     [r] Reanudar          #")
        print(f"# [s] Stop       [x] Reset             #")
        print(f"# [q] Quit                             #")
        print("#" * 40)


def run_with_commands(timer: PomodoroClock):
    timer.start()

    while True:
        try:
            command = input("\nComando [p/r/s/x/q]: ").lower().strip()
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Saliendo...")
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
            continue  # Ignorar entrada vacía
        else:
            print("Comando no válido. Usa: p, r, s, x, q")

        # Verificar si el temporizador terminó naturalmente
        if not timer.running and timer.state == "Completed":
            print(f"\n¡{timer.session_name} completado!")
            time.sleep(2)  # Pausa para mostrar el mensaje
            break


def pomodoro_cycle():
    pomodoros = 4
    completed_sessions = 0
    
    print("=== INICIANDO CICLO POMODORO ===")
    
    for i in range(1, pomodoros + 1):
        print(f"\n🎯 Pomodoro {i} de {pomodoros}")
        timer = PomodoroClock(25, "Trabajo")
        run_with_commands(timer)
        completed_sessions += 1

        # Verificar si el usuario quiere continuar
        if not timer.running and timer.state != "Completed":
            print("\nCiclo interrumpido por el usuario.")
            break

        if i < pomodoros:
            print(f"\n☕ Break corto ({completed_sessions}/{pomodoros} completados)")
            timer = PomodoroClock(5, "Descanso")
            run_with_commands(timer)
        else:
            print(f"\n🎉 ¡Todos los pomodoros completados! Break largo")
            timer = PomodoroClock(15, "Descanso Largo")
            run_with_commands(timer)

    print("\n=== CICLO POMODORO FINALIZADO ===")


def single_session():
    """Modo para una sola sesión personalizada"""
    try:
        minutes = int(input("Duración en minutos: "))
        name = input("Nombre de la sesión: ") or "Sesión"
        timer = PomodoroClock(minutes, name)
        run_with_commands(timer)
    except ValueError:
        print("Por favor ingresa un número válido.")


if __name__ == "__main__":
    print("Pomodoro Timer")
    print("1. Ciclo completo (4 pomodoros)")
    print("2. Sesión única")
    
    try:
        choice = input("Selecciona opción (1/2): ").strip()
        if choice == "2":
            single_session()
        else:
            pomodoro_cycle()
    except KeyboardInterrupt:
        print("\nHasta luego! 👋")