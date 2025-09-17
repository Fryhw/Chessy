import subprocess
import threading
import queue

class LC0Engine:
    def __init__(self, lc0_path: str):
        self.process = subprocess.Popen(
            [lc0_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._read_output, daemon=True)
        self.thread.start()
        self.send_command("uci")
        self.wait_for("uciok")
        self.send_command("isready")
        self.wait_for("readyok")

    def _read_output(self):
        for line in self.process.stdout:
            self.queue.put(line.strip())

    def send_command(self, command: str):
        self.process.stdin.write(command + "\n")
        self.process.stdin.flush()

    def wait_for(self, keyword: str):
        while True:
            line = self.queue.get()
            if keyword in line:
                return line

    def get_best_move(self, fen: str, movetime=1000):
        self.send_command(f"position fen {fen}")
        self.send_command(f"go movetime {movetime}")
        while True:
            line = self.queue.get()
            if line.startswith("bestmove"):
                return line.split()[1]

    def get_leila(self, fen: str, movetime=1000):
        self.send_command(f"position fen {fen}")
        self.send_command(f"go movetime {movetime}")
        outputs = []
        while True:
            line = self.queue.get()
            outputs.append(line)
            if line.startswith("bestmove"):
                break
        return outputs

    def quit(self):
        self.send_command("quit")
        self.process.terminate()
