from collections import deque
from time import time
from random import randint
from time import sleep


class WindowSlot:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.times = 0


class RateLimiter:
    """
    :param window_time_range:int the time that permit the number of invocation
    :param window_max_request_limit:int the max number of invocation during the window_time_range
    :param slot_number:int

    current_slot_end_time:current slot end time
    current_slot_start_time:current slot end time
    current_request_time:int the time that permit the number of invocation
    slot_time:the time range of slot
    slot_dequeue:deque fix size deque filled with slots
    """

    def __init__(self, window_time_range, window_max_request_limit, slot_number):
        self.current_request_time = 0
        self.current_slot_end_time = None
        self.current_slot_start_time = None
        self.window_time_range = window_time_range
        self.window_max_request_limit = window_max_request_limit
        self.slot_number = slot_number
        self.slot_time = window_time_range / slot_number
        self.slot_dequeue = deque([], maxlen=slot_number)

    def request_permit(self):
        request_time = int(time() * 1000)  # current mill second
        if self.slot_dequeue.__len__() == 0:
            self.init(request_time)
        elif request_time >= self.slot_time + self.slot_dequeue[-1].end_time:
            self.init(request_time)

        current_times = self.current_request_time
        max_size = self.window_max_request_limit
        if current_times < max_size:
            self.current_request_time += 1
            self.slot_dequeue[-1].times += 1
            result = True
        else:
            result = False
        print("current invocation time: " + str(self.current_request_time))
        print("current slot start time: " + str(self.current_slot_start_time))
        print("current slot end time: " + str(self.current_slot_end_time))
        return result

    """
        generate window slot add to deque
    """

    def init(self, request_time):
        self.current_slot_start_time = request_time
        self.current_slot_end_time = request_time + self.slot_time
        window_slot = WindowSlot(self.current_slot_start_time, self.current_slot_end_time)
        slots = self.slot_dequeue
        # use list to freeze slot and check all the slot if out of window time. if so remove it and re-calculate the
        # current request time
        for slot in list(slots):
            if self.current_slot_end_time - slot.start_time > self.window_time_range:
                self.current_request_time = self.current_request_time - slot.times
                slots.remove(slot)
        slots.append(window_slot)


if __name__ == '__main__':
    a = RateLimiter(1000, 10, 10)
    pass_it = 0
    fail = 0
    for i in range(1000):
        sleep(randint(10, 200) / 1000)
        if a.request_permit():
            pass_it += 1
        else:
            fail += 1

    print("pass: ", pass_it)
    print("fail: ", fail)
