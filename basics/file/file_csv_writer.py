import csv


with open('file.csv','w',newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["SN","movie","firstChar"])
  writer.writerow(["1","Red Line","natasha"])
  writer.writerow(["2","Van helsing","Pr.Anna"])
  writer.writerow(["3","Warrior","Tommy reardon"])

 