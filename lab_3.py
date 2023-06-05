class Phone:
    def __init__(self, model, date, memory):
        self.model = model
        self.date = date
        self.memory = memory

    @staticmethod
    def sortedMemory(phones):
        sorted_memory = sorted(phones, key=lambda phone: phone.memory)
        return sorted_memory

    @staticmethod
    def printIphones(phones):
        iphones = [phone for phone in phones if "iPhone" in phone.model]
        for iphone in iphones:
            print("Model:", iphone.model)
            print("Date:", iphone.date)
            print("Memory:", iphone.memory)
            print()


iphone1 = Phone("iPhone 12", "October 13, 2020", "256 GB")
samsung = Phone("Galaxy S23 Ultra", "February 17, 2023", "128 GB")
iphone2 = Phone("iPhone 14", "September 7, 2022", "512 GB")


phones = [iphone1, samsung, iphone2]
print("Only iPhones: ")
print()
Phone.printIphones(phones)
print("Sort by memory phone: ")
sorted_by_memory = Phone.sortedMemory(phones)
for phone in sorted_by_memory:
    print(phone.memory, phone.model)
    print("------------------------")
