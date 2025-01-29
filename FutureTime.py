#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  
  #Ask user for minutes
  minutes = input("Enter minutes: ")
  minutes = int(minutes)
  futureMinutes = currentMinute + minutes
  futureMinutes = futureMinutes % 60
  extraMinutes = minutes // 60 
  
  #Ask user for hours
  hours = input("Enter hours: ") 
  hours =int(hours)  % 24 #changes text to numbers
  futureHours = currentHour + hours + extraMinutes
  futureHours = int(futureHours) % 24

  #Output the future time in standard format "HH:MM"
  print (str(futureHours) + ":" + str(futureMinutes))

if __name__ == '__main__':
  main()
