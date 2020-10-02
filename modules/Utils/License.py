class LicenseManager():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing

    def CheckExtension(self, license_name):
        return "Available" 

    def CheckOutExtension(self, license_name):
        return "CheckedOut"

    def CheckInExtension(self, license_name):
        return "CheckedIn"
