import datetime
import smtplib
from email.mime.text import MIMEText

class SocialSecurityReminder:
    def __init__(self):
        self.recipient_email = None
        self.move_date = None

    def get_recipient_info(self):
        # Collect recipient's email and move date
        self.recipient_email = input("Enter recipient's email address: ")
        move_date_str = input("Enter the date of the move (YYYY-MM-DD): ")
        self.move_date = datetime.datetime.strptime(move_date_str, "%Y-%m-%d").date()

    def send_email_reminder(self):
        # Setup email parameters
        sender_email = "your_email@gmail.com"  # Update with your email
        sender_password = "your_password"  # Update with your email password
        subject = "Social Security Reapplication Reminder"
        body = f"Dear recipient,\n\nDon't forget to reapply for Social Security as you have moved on {self.move_date}.\n\nBest regards,\nYour Name"

        # Create MIMEText object
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = self.recipient_email

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, self.recipient_email, message.as_string())

    def schedule_reminder(self):
        current_date = datetime.date.today()

        # Check if it's time to send a reminder
        if current_date >= self.move_date:
            self.send_email_reminder()
            print("Reminder email sent successfully.")
        else:
            print("No reminder scheduled yet.")

if __name__ == "__main__":
    reminder = SocialSecurityReminder()
    reminder.get_recipient_info()
    reminder.schedule_reminder()
