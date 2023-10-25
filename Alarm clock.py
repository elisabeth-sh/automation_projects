import datetime
import winsound

# winsound accepts "wav" files
# for other audiofiles try playsound
def alarm_clock(set_time):
    current_time = datetime.datetime.now().strftime("%H:%M")

    print(f"It is {current_time} now. You set the clock for {set_time}.")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if str(set_time) == str(current_time):
            # set the right path instead of "Audio File.wav"
            winsound.PlaySound("Audio File.wav", winsound.SND_LOOP)
            quit()

alarm_clock(set_time = input("When should the alarm clock go off?\n"))
