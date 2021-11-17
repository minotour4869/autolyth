import json
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key, Controller, Events, HotKey, Listener

note = ["q", "w", "e", "r", "t", "y", "u", "a", "s", "d", "f", "g", "h", "j", "z", "x", "c", "v", "b", "n", "m"]

ctrler = Controller()

file = input("File direction (.gichart): ")

with open(file, "r") as f:
    chart = json.load(f)

interval = 60.0/chart["bpm"]

def song():
    print("Playing chart...")
    for keys in chart["chart"]:
        rate = 1.0
        for key in keys:
            if (key == '+'): rate *= 2
            if (key == '-'): rate /= 2
            if (key in note):
                ctrler.press(key)
                ctrler.release(key)
        sleep(interval*rate)
    print("Done playing chart")

def end():
    exit(0)

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hk = HotKey(HotKey.parse("p"), song)
hk2 = HotKey(HotKey.parse("<ctrl>+l"), end)

with Listener(on_press=for_canonical(hk.press), on_release=for_canonical(hk.release)) as l: l.join()
