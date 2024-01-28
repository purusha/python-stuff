import csv
from faker import Faker
import datetime
import time

def datagenerate(records, headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open("People_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name
            
            writer.writerow({
                    "EmailId" : userId,
                    "Prefix" : fake.prefix(),
                    "Name": fake.name(),
                    "BirthDate" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    "PhoneNumber" : fake1.phone_number(),
                    "AdditionalEmailId": fake.email(),
                    #"Address" : fake.address(),
                    "ZipCode" : fake.zipcode(),
                    "City" : fake.city(),
                    "State" : fake.state(),
                    "Country" : fake.country(),
                    "Year":fake.year(),
                    "Time": fake.time(),
                    "Link": fake.url(),
                    "Text": fake.word(),
             })
    
if __name__ == '__main__':
    records = 250000
    headers = ["EmailId", "Prefix", "Name", "BirthDate", "PhoneNumber", "AdditionalEmailId",
               #"Address", 
               "ZipCode", "City","State", "Country", "Year", "Time", "Link", "Text"]
               
    start_time = time.time()
    datagenerate(records, headers)
    print("CSV generation complete!")
    print("--- %s seconds ---" % (time.time() - start_time))
