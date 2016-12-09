import sys
import getopt
import Validation
import Prompts
import Constants
import AudioManager

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
    try:
        # getop breaks if you pass in program as a paramater
        opts, args = getopt.getopt(sys.argv[1:], "g:n:r:e:o:")

        # There should be 5 additional parameters passed in
        if len(opts) != 5:
            Terminate()

        # Assign values here
        for opt, arg in opts:
            if opt == "-g":
                genderChoice = int(arg)
            elif opt == "-o":
                outFileName = arg
            elif opt == "-n":
                phoneNumber = arg

        if (Validation.IsValidCommandArgs(opts, genderChoice, phoneNumber
        ,reasons, endings, outFileName)) == False:
            # invalid argument somewhere, terminate
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
    proceedToVMCreation = (validResponse == "y")

# If we get here, the user finalized their voicemail, so we can create it!
if len(sys.argv) == 1:
    outFileName = raw_input(Prompts.PROMPT_OUTPUT_NAME+"\n")

print("Creating voicemail.... Writing to " + outFileName)
audioSamples = AudioManager.DownloadAudio(genderChoice, phoneNumber, reasons, endings)
AudioManager.CombineAudioFiles(audioSamples, outFileName)

print(outFileName + " created.")




#################
#End main script#
#################
