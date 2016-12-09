import sys
import getopt
import Validation
import Prompts
import Constants

DEBUG = False

#######################
#Main method functions#
#######################
def Terminate():
    print(Constants.USAGE_STATEMENT)
    sys.exit(2)

#####################
#Program entry point#
#####################
print(Prompts.WELCOME_MESSAGE)

# Initialize voicemail options
proceedToVMCreation = True
genderChoice = -1
phoneNumber = ""
reasons = []
endings = []
outFileName = ""

# Determine if they ran the program with paramaters or not
if len(sys.argv) != 1:
    if len(sys.argv) != 11:
        Terminate()
    try:
        opts, args = getopt.getopt(sys.argv, "g:n:r:e:o:")
        if Validation.IsValidCommandArgs(opts) == False:
            Terminate()
    except getopt.GetoptError:
        Terminate()
else:
    proceedToVMCreation = False


while proceedToVMCreation == False:
    # Gender selection
    validGender = False
    while validGender == False:
        genderChoice = raw_input(Prompts.GENDER_PROMPT + "\n"
            + Prompts.DisplayGenderOptions())
        validGender = Validation.IsValidGender(genderChoice)
    genderChoice = int(genderChoice)

    # Phone number entry
    validPhone = False
    while validPhone == False:
        phoneNumber = raw_input("\n" + Prompts.PHONE_PROMPT + "\n"
            + Prompts.PHONE_ACCEPTABLE_FORMATS + "\n")
        validPhone = Validation.IsValidPhone(phoneNumber)

    # Select reasons
    validReasons = False
    while validReasons == False:
        reasonsRaw = raw_input("\n" + Prompts.PROMPT_REASONS + "\n"
            + Prompts.DisplayReasonOptions(genderChoice))
        validReasons = Validation.IsValidReasons(reasonsRaw, genderChoice)
    reasons = reasonsRaw.split(" ")
    # Store as ints
    for i in range(len(reasons)):
        reasons[i] = int(reasons[i])

    # Select endings
    validEndings = False
    while validEndings == False:
        endingsRaw = raw_input("\n" + Prompts.PROMPT_ENDINGS + "\n"
            + Prompts.DisplayEndingOptions(genderChoice))
        validEndings = Validation.IsValidEndings(endingsRaw, genderChoice)
    endings = endingsRaw.split(" ")
    # Store as IsValidPhoneSegments
    for i in range(len(endings)):
        endings[i] = int(endings[i])

    # Summarize voicemail message, user confirmation
    validResponse = "x"
    userResponse= ""
    while validResponse == "x":
        userResponse = raw_input(Prompts.DisplayVoicemailSummary(genderChoice,
        phoneNumber, reasons, endings) + Prompts.PROMPT_CONFIRM + "\n")
        validResponse = Validation.IsValidConfirmation(userResponse)
def Terminate():
    print(Constants.USAGE_STATEMENT)
    sys.exit(2)

# If we get here, the user finalized their voicemail, so we can create it!
print("Creating voicemail....")




#################
#End main script#
#################
