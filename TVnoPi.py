import vlc      # Python-VLC library
import time
import os
import random
import keyboard  # Import the keyboard library
import sys

# start execution
print("start")

random.seed()

def exit_program():
    print("Exiting the program...")
    # Stop all active player instances
    for player_instance in active_players:
        player_instance.stop()
    global should_run
    should_run = False

# Register the exit and break loop functions to be triggered by the respective keys
keyboard.add_hotkey('x', exit_program)

# list all files in a directory and subdirectories
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

# movies path
path = "c:\\Users\\Tim (Intertech)\\Downloads\\FakeTV"

file = random.choice(list_files(path))
print(file)

time.sleep(1)

Instance = vlc.Instance()
player = Instance.media_player_new()
player.toggle_fullscreen()
media = Instance.media_new(file)
player.set_media(media)
player.play()

time.sleep(2)
while not player.is_playing():
    time.sleep(0.001)

# loop
    # Next video if video is finished

active_players = []  # List to store active player instances
should_run = True  # Flag to control the loop

skip_counter = 0  # Initialize skip counter
stop_counter = 0  # Initialize stop counter

while should_run:
    if keyboard.is_pressed('esc'):  # Check if 's' key is pressed
        stop_counter += 1
        if stop_counter >= 2:
            print("Stop video")
            player.stop()  # Stop the player
            stop_counter = 0  # Reset the counter
            time.sleep(0.5)  # Wait for key release to avoid multiple skips
    else:
        stop_counter = 0  # Reset counter if 's' is not held

    if not player.is_playing():
        print('next')
        player.stop()
        time.sleep(0.1)
        file = random.choice(list_files(path))
        media = Instance.media_new(file)
        player.set_media(media)
        player.play()
        time.sleep(2)

# end of execution
    print("stop")