# testing zapier by acting like the sawyer input data

def main():
    input_data = {
        "StudentName": "John Doe",
        "Dates": "2024-06-18",
        "Times": "3:30pm - 4:30pm EDT",
        "Street1": "70 Washington St",
        "Street2": "TEST", 
        "City": "Brooklyn",
        "State": "NY",
        "Zip": "11201",
        "CustomerName": "Jane Doe",
        "TeachName": "TEST",
        "Class": "Roblox Online FREE TRIAL",
        "Location": "TEST",
        "Zoom": "TEST", 
        "TeachOutput": 1214905
    }

    StudentName = input_data["StudentName"] 
    InputID = input_data["TeachOutput"]
    CustomerName = input_data["CustomerName"]
    Dates = input_data["Dates"]
    Class = input_data["Class"]
    Times = input_data["Times"]

main()