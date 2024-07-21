hours = int(input("Enter hours taken to run the marathon: "))
minutes = int(input("Enter minutes taken to run the marathon: "))
seconds = int(input("Enter seconds taken to run the marathon: "))

TotalMarathonTimeSeconds = (hours * 3600) + (minutes * 60) + seconds

print("Marathon time in seconds:", TotalMarathonTimeSeconds)

PersonalBestSec = int(input("Enter your personal best time in seconds: "))

if TotalMarathonTimeSeconds < PersonalBestSec:
    
    PersonalBestSec = TotalMarathonTimeSeconds
    print("New personal best time:", PersonalBestSec)
else:
    print("Personal best time remains:", PersonalBestSec)