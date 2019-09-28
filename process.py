from random import randint, seed

seed(1)

class Process:
    def __init__(self, time, id):
        self.id = id
        self.used_time = 0
        self.state = 'unstarted'# unstarted, ready, running, blocked, terminated
        self.wait_time = 0
        self.finished = False
        if time:
            self.cpu_burst = time
        else:
            self.cpu_burst = randint(1, 5)

    def __str__(self):
        return f'Процесс № {self.id} требует {self.cpu_burst} процессорного времени, использовал {self.used_time} ' \
               f'состояние {self.state}\n'

    def tick(self):
        if self.state == 'terminated':
            return
        elif self.state == 'running':
            self.used_time += 1
            if self.used_time == self.cpu_burst:
                self.state = 'terminated'
        else:
            self.wait_time += 0

    def start(self):
        self.state = 'running'

    def block(self):
        self.state = 'blocked'

