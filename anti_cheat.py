# anti_cheat.py
import time

class AntiCheat:
    def __init__(self):
        self.data = {}

    def add_player(self, pid):
        self.data[pid] = {
            "start_time": None,
            "last_time": None,
            "streak": 0,
            "suspicion": 0
        }

    def start_question(self, pid):
        self.data[pid]["start_time"] = time.time()

    def register_answer(self, pid, correct):
        p = self.data[pid]
        now = time.time()

        # ⏱️ too fast answer
        if p["start_time"]:
            if now - p["start_time"] < 0.8:
                self._add(pid, 10, "too fast")

        # ⚡ spam check
        if p["last_time"]:
            if now - p["last_time"] < 0.25:
                self._add(pid, 5, "spamming")

        p["last_time"] = now

        # 🎯 streak check
        if correct:
            p["streak"] += 1
            if p["streak"] > 25:
                self._add(pid, 15, "perfect streak")
        else:
            p["streak"] = 0

    def _add(self, pid, amt, reason):
        self.data[pid]["suspicion"] += amt
        print(f"[ANTI-CHEAT] {reason} (+{amt}) → {self.data[pid]['suspicion']}")

    def is_cheating(self, pid):
        return self.data[pid]["suspicion"] > 50
