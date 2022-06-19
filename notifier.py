from email import message
from socket import timeout
import time
from turtle import title
from plyer import notification

if __name__ == "__main__":  #this is to run the code always when file runs
    while True:
        notification.notify(
            title="Take a break 20-20-20 RULE!!",
            message="U have spent 20 mins on the screen now look away at something that is 20 feet away for 20 seconds.",
            app_icon=r"C:\Users\User\Desktop\MSRUAS\Projects\Python Projects\screenTimeNotifier\icon.icon.ico",
            timeout = 20
        )
        time.sleep(60*20)   #every 20 mins multiply with 60 since its default is in secs
