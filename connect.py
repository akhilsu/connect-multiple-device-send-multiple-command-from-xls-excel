from netmiko import ConnectHandler
import xlrd

openfile = xlrd.open_workbook(r"device_list.xls")
sheet = openfile.sheet_by_name("Sheet1")

commands_ready = open(r"commands.txt")
commands = commands_ready.read().splitlines()

for i in range (1,sheet.nrows):
    device = {
        "device_type" : sheet.row(i)[5].value,
        "ip" : sheet.row(i)[2].value,
        "username" : sheet.row(i)[3].value,
        "password" : sheet.row(i)[4].value,
        "port" : 22
    }

    connectdevice = ConnectHandler(**device)
    for j in commands:
        fetch = connectdevice.send_command(j,read_timeout=300)
        print(fetch)
    connectdevice.disconnect()
