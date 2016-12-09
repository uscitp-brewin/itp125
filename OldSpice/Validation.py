##################################################
#Validation funtions for Voicemail via user input#
##################################################
import Constants
import Prompts

DEBUG = False

# Validate the command line arguments -- see Constants.USAGE_STATEMENT for
# acceptable formats. A succesful parse will fill the value of all additonal args
def IsValidCommandArgs(opts, genderVal, phoneNumberVal, reasonsVal, endingsVal ,outFileNameVal):
    genderChoice = -1
    # Parse the option argument pairs
    for opt, arg in opts:
        if opt == "-g":
            if IsValidGender(arg) == False:
                if DEBUG:
                    print("Not valid gender")
                return False
            genderChoice = int(arg)
            genderVal = int(arg)
        elif opt == "-n":
            if IsValidPhone(arg) == False:
                if DEBUG:
                    print("Not valid phone")
                return False
            phoneNumberVal = arg
        elif opt == "-r":
            if genderChoice == -1:
                print("Please provide the gender argument before reasons and endings")
                return False
            reasons = list(arg)
            rawReasons = ""
            for reason in reasons:
                rawReasons += reason + " "
                reasonsVal.append(int(reason))
            rawReasons.strip()
            if IsValidReasons(rawReasons, genderChoice) == False:
                if DEBUG:
                    print("Not valid reason")
                return False
        elif opt == "-e":
            if genderChoice == -1:
                print("Please provide the gender argument before reasons and endings")
                return False
            endings = list(arg)
            rawEndings = ""
            for ending in endings:
                rawEndings += ending + " "
                endingsVal.append(int(ending))
            rawEndings.strip()
            if IsValidEndings(rawEndings, genderChoice) == False:
                if DEBUG:
                    print("Not valid ending")
                return False
        elif opt == "-o":
            arg.strip()
            outFileNameVal = arg
            if DEBUG:
                 print(outFileNameVal)
        else:
            print("Unknown argument provided")
            return False

    return True


# Validate genderChoice according to GenderOptions
def IsValidGender(genderChoice):
    genderChoice.strip()

    idx = -1
    try:
        idx = int(genderChoice)
    except:
        return False
    return (idx == 0 or idx == 1)

# Validate phoneNumber
# Valid forms include:
# 012-345-6789
# (012) 345-6789
# 012.345.6789
# 0123456789
def IsValidPhone(phoneNumber):
    phoneNumber.strip()

    # Format 1
    splitString = phoneNumber.split("-") # xxx-xxx-xxxx
    if len(splitString) == 3:
        if DEBUG:
            print("its 3!")
        try:
            seg1 = int(splitString[0])
            seg2 = int(splitString[1])
            seg3 = int(splitString[2])
            return IsValidPhoneSegments(splitString[0], splitString[1], splitString[2])
        except:
            return False

    elif len(splitString) == 2:     # Format 2
        splitMore = splitString[0].split(" ") # Retrieve the first 6 nums (xxx) xxx

        if len(splitMore) != 2:
            return False

        openParIdx = splitMore[0].find("(")
        closeParIdx = splitMore[0].find(")")

        if(openParIdx == -1 or closeParIdx == -1):
            return False

        seg1 = splitMore[0].strip("()")
        try:
            seg = int(seg1)
            seg2 = int(splitMore[1])
            seg3 = int(splitString[1])
            return IsValidPhoneSegments(seg1,splitMore[1],splitString[1])
        except:
            return False

    # Format 3
    splitString = phoneNumber.split(".")
    if len(splitString) == 3:
        try:
            seg1 = int(splitString[0])
            seg2 = int(splitString[1])
            seg3 = int(splitString[2])
            return IsValidPhoneSegments(splitString[0], splitString[1], splitString[2])
        except:
            return False

    # Format 4
    try:
        asNum = int(phoneNumber)
        return len(phoneNumber) == 10
    except:
        return False

    # Default case
    return False

# Given the phone number as 3 separate segments, check that their lengths
# are valdid according to a typical US phone number
def IsValidPhoneSegments(seg1, seg2, seg3):
    return (len(seg1) == Constants.PHONE_SEG1_LEN
            and len(seg2) == Constants.PHONE_SEG2_LEN
            and len(seg3) == Constants.PHONE_SEG3_LEN)


# Validate the users selected reasons based on the gender they chose earlier.
# Also checks for duplicate reasons, in which it returns false
def IsValidReasons(reasonsRaw, genderChoice):

    splitReasons = reasonsRaw.split(" ")
    numOfReasons = -1

    # Dynamically set number of available reasons
    if genderChoice == Constants.MALE_OPTION:
        numOfReasons = len(Prompts.REASONS_MALE)
    elif genderChoice == Constants.FEMALE_OPTION:
        numOfReasons = len(Prompts.REASONS_FEMALE)

    if DEBUG:
        print splitReasons

    # Keep a bool map of the selected options to avoid duplicates
    selections = []
    for i in range(numOfReasons):
        selections.append(False)

    for userReason in splitReasons:
        try:
            asNum = int(userReason)
            if asNum < 0 or asNum >= numOfReasons:
                # Not a valid reason / out of range
                return False

            if selections[asNum] == True:
                # They have already chosen that options
                print("Please select a reason only once")
                return False

            selections[asNum] = True
        except:
            return False

    return True

# Validate the users selected endings based on the gender they chose earlier.
# Also checks for duplicate endings, in which it returns false
def IsValidEndings(endingsRaw, genderChoice):
    splitEndings = endingsRaw.split(" ")
    numOfEndings = -1

    # Dynamically set number of available reasons
    if genderChoice == Constants.MALE_OPTION:
        numOfEndings= len(Prompts.ENDINGS_MALE)
    elif genderChoice == Constants.FEMALE_OPTION:
        numOfEndings = len(Prompts.ENDINGS_FEMALE)

    # Keep a bool map of the selected options to avoid duplicates
    selections = []
    for i in range(numOfEndings):
        selections.append(False)

    for userEnding in splitEndings:
        try:
            asNum = int(userEnding)
            if asNum < 0 or asNum >= numOfEndings:
                # Not a valid reason / out of range
                return False

            if selections[asNum] == True:
                # They have already chosen that options
                print("Please select an ending only once")
                return False

            selections[asNum] = True
        except:
            return False

    return True

# Validate a user response to a confirmation prompt
def IsValidConfirmation(response):
    response.lower()
    response.strip()
    if response == "y" or response == "yes":
        return "y"
    elif response == "n" or response == "no":
        return "n"
    # If it gets here, it is invalid
    return "x"
