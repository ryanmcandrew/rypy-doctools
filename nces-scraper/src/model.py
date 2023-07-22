class NcesSearchPage():
    def __init__(self):
        self.district_name = None
        self.nces_district_id = None
        self.street_address = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.distance = None
        self.county = None
        self.phone_area_code = None
        self.phone_no_area_code = None

class NcesDistrictPage():
    def __init__(self):

        self.data_to_scrape = [
            "District Name:",
            "NCES District ID:",
            "State District ID:",
            "Mailing Address:",
            "Physical Address:",
            "Phone:",
            "Type:", 
            "Status:", 
            "Total Schools:", 
            "Supervisory Union #:", 
            "NCES District ID:", 
            "Grade Span:", 
            "Website:", 
            "District Demographics:", 
            "County:", 
            "County ID:", 
            "Locale:", 
            "Total Students:", 
            "CSA/CBSA:", 
            "Classroom Teachers (FTE):", 
            "Student/Teacher Ratio:"
        ]

        self.data = [None for i in self.data_to_scrape]

    def load(self, dataString):
        for index, data in enumerate(self.data_to_scrape):
            if dataString is not None:
                if not (str(dataString).count(':') > 1):
                    if str(dataString).find(data) != -1:
                        self.data[index] = str(dataString).replace(data, '').strip().strip(',')
        return self.data

class NcesSchoolPage():
    def __init__(self, *data):

        self.data_to_scrape = [
            "School Name:",
            "NCES School ID:",
            "State School ID:",
            "District Name:",
            "NCES District ID:",
            "State District ID:",
            "Mailing Address:",
            "Physical Address:",
            "Phone:",
            "Type:",
            "Status:",
            "Charter:",
            "Supervisory Union #:",
            "Grade Span:",
            "Website:",
            "County:",
            "Locale:",
            "Total Students:",
            "Magnet:",
            "Classroom Teachers (FTE):"
            "Title I Eligible:",
            "Student/Teacher Ratio:",
            "Schoolwide Title I Eligible:"
        ]

        self.data = [None for i in self.data_to_scrape]

    def load(self, dataString):
        for index, data in enumerate(self.data_to_scrape):
            if dataString is not None:
                if not (str(dataString).count(':') > 1):
                    if str(dataString).find(data) != -1:
                        self.data[index] = str(dataString).replace(data, '').strip().strip(',')
        return self.data
