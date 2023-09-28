from win10toast import ToastNotifier

toaster = ToastNotifier()

# Specify the path to your sound file (replace 'path_to_sound_file.wav' with the actual file path)
sound_path = 'path_to_sound_file.wav'

# Show the toast notification with sound
toaster.show_toast(
    "Reminder",
    "Waktunya pengamatan dan pengiriman sandi!",
    icon_path=None,
    duration=20,
    sound=sound_path  # Specify the sound file path
)

# Wait for threaded notification to finish
import time
while toaster.notification_active():
    time.sleep(0.1)
