from pynput import keyboard
import time

start = time.time()
f = open('timestamps.txt', 'w')
f.close()


def write_timestamp(timestamp):
    hours, mins, secs = timestamp
    file = open('timestamps.txt', 'a')
    stamp = "H{} M{} S{}\n".format(hours, mins, secs)
    file.write(stamp)


def on_key_release(key):
    try:
        if key.char == "q":
            secs = int(time.time() - start)
            print('Q relesed at %d' % secs)
            hours = int(secs / 3600)
            secs = int(secs % 3600)
            mins = int(secs / 60)
            secs = int(secs % 60)
            write_timestamp((hours, mins, secs))
    except:
        pass


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
