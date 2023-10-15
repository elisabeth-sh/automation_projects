#The Pomodoro technique
from plyer import notification
import time

def timer_start():
    # Determining the local time
    start = time.strftime("%H:%M", time.localtime())
    notification.notify(
        title="Start",
        message=f"You started working at {start}",
        timeout=60
    )

def break_time():
    notification.notify(
        title="Break",
        message="Take a break, eat something, relax a little.",
        timeout=60
    )

# You determine how long the programme will work
hour_loc = time.strftime("%H", time.localtime())
while "22" <= hour_loc < "23":
    # This notification shows when you started studying
    timer_start()
    time.sleep(60 * 25)
    # The programme will give you another notification in 25 minutes
    break_time()
    time.sleep(60 * 5)
