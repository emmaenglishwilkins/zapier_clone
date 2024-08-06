# Address dictionary for all locations, to be used for emails
LocationAddresses = {
    "Newton" : "1223 Centre St. Newton Centre, MA",
    "Lexington" : "Suite 101 (Bottom Floor) of 5 Militia Drive, Lexington MA 02421" , 
    "Acton" : "411 Massachusetts Ave. Suite 101 Acton, MA 01720", 
    "Park Slope" : "424 7th Ave, Brooklyn, NY, 11215 (Corner of 14th street and 7th Ave)",
    "Cobble Hill" : "156 Smith Street, Brooklyn, NY 11201",
    "Online" : "N/A",
    "No Location" : ""
}
#Phone number dictionary for the locations, to be used for the emails
phoneNumbers = {
    "Newton" : "(617) 608-4757",
    "Lexington" : "(781) 277-2755" , 
    "Acton" : "(781) 277-2956", 
    "Park Slope" : "(347) 620-9235",
    "Cobble Hill" : "(917) 813-1007",
    "Online" : "(917) 813-1007",
    "No Location" : "MA Phone: (781) 277-2755\t\tNY Phone: (347) 620-9235"
}
# Camp message about Early drop off. Specific to location. For Camp Emails
campMessage = {
    "Newton" : "If you registered for early drop off, camp starts at 8:30am. If you registered for extended care, the pick up time is 5pm.",
    "Lexington" : "If you registered for early drop off, camp starts at 8:30am. If you registered for extended care, the pick up time is 5pm." , 
    "Acton" : "If you registered for early drop off, camp starts at 8:30am. If you registered for extended care, the pick up time is 5pm.", 
    "Park Slope" : "If you registered for extended care, the pick up time is 5pm.",
    "Cobble Hill" : "If you registered for extended care, the pick up time is 5pm.",
}

try:
    #Save input data in variables and test to see if any are empty.
    StudentName = input_data["StudentName"] 
    InputID = input_data["TeachOutput"]
    CustomerName = input_data["CustomerName"]
    Dates = input_data["Dates"]
    Class = input_data["Class"]
    Times = input_data["Times"]
    #Zip = input_data["Zip"]
    #City = input_data["City"]
    #State = input_data["State"]
    #Address = input_data["Street1"] + " "
    

    #Location Address and Phone number and other information
    TeacherName = ""
    location = ""
    try:
        location = input_data["Location"]        
    except:
        location = "No Location"
    zoomLink = ""
    
    #Check if a Teacher Has been assigned
    if InputID != "No ID" and location != "Double": 
        TeacherName = input_data["TeachName"]
        location = input_data["Location"]
        zoomLink = input_data["Zoom"]
        LocationAddresses = LocationAddresses[location]
    #No Teacher Assigned Yet, i.e. no location data 
    else:
        location = "No Location"
    LocationPhone = phoneNumbers[location]


    #Some addresses have a Street 2 address. If they don't it will cause errors if we try to accesss if. This just makes sure that correct address is saved with no errors.
    #**This is only for if you need an address but not really used much here
    #try: 
        #Address += input_data["Street2"] + " " + City + " " + State + ", " + Zip
    #except:
        #Address += City + " " + State + ", " + Zip

    #Free Trial Links based on location and type of class
    trialLink= "https://penguincodingschool.com/"
    type = "kids"
    if "Minecraft" in Class:
        type = "minecraft"
    elif "Scratch" in Class:
        type = "scratch"
    elif "Javascript" in Class:        
        type = "javascript"
    elif "Java" in Class:
        type  = "java"
    elif "Roblox" in Class:
        type = "Roblox"
    elif "Robotics" in Class:
        type = "robotics"
    if location != "No Location" and "trial" in Class.lower() :
        trialLink += type + "-class-" + location.lower().replace(" ", "")
        if location == "Park Slope" or location == "Cobble Hill":
            trialLink += "-brooklyn"
        
    print(trialLink)
    
    # Split the input data so we can clean it up later. Get individual instances 
    splitdates = Dates.split(",") 
    splittimes = Times.split(" ") 
    splitClasses = Class.split(",") # split names of input classes
    splitName = CustomerName.split(" ") # split first and last name of parent
    
    # Figure out Student name based on if there is 1 or >1 student listed:
    splitnames = StudentName.split(",")
    if len(splitnames) > 1 and splitnames[1] == "": #no real second student (ex: "John Doe, ")
        StudentName = splitnames[0]
    elif len(splitnames) > 1: #>1 student:
        StudentName = ""
        for x in range(0, len(splitnames)-1):
            StudentName += splitnames[x] + ", " 
        #Clean up multiple student names for Email formatting (ex: Jane Doe and John Doe)
        StudentName += "and" + splitnames[len(splitnames)-1]

    
    #All the dates sometimes come in unsorts. This just sorts them and cleans them up
    sortedDates = []
    for date in splitdates:
        splitDate = date.split("-")
        sortedDates.append(splitDate[1] + "/" + splitDate[2] + "/" + splitDate[0])
   
    sortedDates.sort()
    startdate = sortedDates[0]
    enddate = startdate

    if len(sortedDates) > 1:
        enddate = sortedDates[len(sortedDates)-1]
       
    # Missing student name field, error
    if len(splitClasses) > 1 and "Summer" not in Class: 
        output = {"output": ">1 Class"}

    # No Teacher Assignment when registered 
    elif InputID == "No ID" or location == "No Location":
        output = {"output": "No Teacher",
                "enddate" : enddate, 
                "startdate" : startdate,
                "starttime" : splittimes[0],
                "endtime" : splittimes[2], 
                "fname" : splitName[0], 
                "lname" : splitName[1], 
                "LocationNumber" : LocationPhone, 
                "Student(s)Name(s)" : StudentName  }

    # Check class is no summer camp & only one class was registered
    elif "Summer" not in Class: 
        # Regular Semester Class, >= 1 student
        if ("trial" not in Class.lower()):
            output = {"output": "Single Class", 
                    "enddate" : enddate, 
                    "startdate" : startdate, 
                    "starttime" : splittimes[0], 
                    "endtime" : splittimes[2], 
                    "location" : location, 
                    "fname" : splitName[0], 
                    "lname" : splitName[1], 
                    "teacher" : TeacherName, 
                    "zoom" : zoomLink, 
                    "ClassAddress" : LocationAddresses, 
                    "LocationNumber" : LocationPhone, 
                    "Student(s)Name(s)" : StudentName }
            
        # free trial,  >=1 student
        elif ("trial" in Class.lower()): 
            output = {"output": "Free Trial", 
                    "TrialDate" : startdate, 
                    "starttime" : splittimes[0], 
                    "endtime" : splittimes[2], 
                    "location" : location, 
                    "fname" : splitName[0], 
                    "lname" : splitName[1], 
                    "teacher" : TeacherName, 
                    "zoom" : zoomLink,  
                    "ClassAddress" : LocationAddresses , 
                    "LocationNumber" : LocationPhone, 
                    "Student(s)Name(s)" : StudentName  }
    
    # single summer camps
    elif "Summer" in Class and Class.count("Summer") == 1: # single summer camps
        #All the dates from summer camps come in unsorts. This just sorts them
        output = {"output": "Summer", 
                "timeframe" : splittimes[0] + " - " + splittimes[2], 
                "fname" : splitName[0], 
                "lname" : splitName[1], 
                "teacher" : TeacherName, 
                "location" : location,  
                "ClassAddress" : LocationAddresses , 
                "LocationNumber" : LocationPhone, 
                "StartDate" : startdate, 
                "EndDate" : enddate, 
                "StudentName" : StudentName, 
                "CampMessage" : campMessage[location] }
    else:
        output = {"output": "Multiple Classes"}
        
except:
    output = {"output": "Missing Information"}
