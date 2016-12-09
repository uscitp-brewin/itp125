import Constants

DEBUG = False

###########
#Constants#
###########

## PROMPTS / MESSAGES ##
WELCOME_MESSAGE = "Welcome to the Old Spice voicemail service!"
CONTROL_INSTRUCTIONS = "You can type 'restart' at anytime to restart the program.\nType 'exit' at anytime to exit the program"
GENDER_PROMPT = "Would you like to create a voicemail for a male or female? (Select '0' or '1')"
PHONE_PROMPT = "Please enter your 10-digit phone number."
PHONE_ACCEPTABLE_FORMATS = "Acceptable formats include:\n 012-345-6789\n (012) 345-6789\n 012.345.6789\n 0123456789"
PROMPT_REASONS = """Please select the reason(s) you cannot answer the phone.
If you wish to have multple reasons, separate all numeric entries with spaces:"""
PROMPT_ENDINGS = """Please select your voicemail ending(s). If you wish to have
multiple endings, separate all numeric entries with spaces:"""
PROMPT_CONFIRM = "Create the above voicemail? [y/n]"
SUMMARY_PREFACE = "You selected the following options:"
PROMPT_OUTPUT_NAME = " Please enter the name of the output file."

## GENDERS ##
GENDERS = (
    "[0] Male",
    "[1] Female"
)

## REASONS ##
REASONS_MALE = (
    "[0] Ripping out mass loads of weights.",

    "[1] Polishing their monocle smile.",

    "[2] Cracking walnuts with their man mind.",

    """[3] Building an orphanage for children with their bare hands while playing
    'sweet sweet lullaby' for those children with two mallets against
    their ab xylophone."""
)
REASONS_FEMALE = (
    "[0] Riding a horse backwards with me.",

    """[1] Listening to me read romatic poetry while I make a boquet of paper
    flowers from each read page.""",

    "[2] Ingesting my delicious Old Spice man smell.",

    """[3] Being serenaded on the moon with a view of the Earth, while surviving
    off the oxygen in my lungs via a passionate kiss.""",

    """[4] Enjoying a delicious lobster dinner I prepared just for her, while
    carrying her on my back safely through piranha infested waters."""
)

## ENDINGS ##
ENDINGS_MALE = (
    "[0] I'm on a horse.",

    "[1] I'm on a phone.",

    "[2] Swan dive!",

    "[3] This voicemail is now dynamite.",

    "[4] Dodo do do do dodo do!"
)

ENDINGS_FEMALE = (
    "[0] But she'll get back to you as soon as she can.",
    "[1] Thanks for calling.",
)

###########################
#Dynamic display functions#
###########################
# Display the available gender options
def DisplayGenderOptions():
    return "[0] Male\n[1] Female\n"


# Display the reason options based on the provided gender
def DisplayReasonOptions(gender):
    output = ""
    if(gender == Constants.MALE_OPTION):
        for reason in REASONS_MALE:
            output += (reason + "\n")

    elif(gender == Constants.FEMALE_OPTION):
        for reason in REASONS_FEMALE:
            output += (reason + "\n")

    return output

# Display the ending options based on the provided gender
def DisplayEndingOptions(gender):
    output = ""
    if(gender == Constants.MALE_OPTION):
        for ending in ENDINGS_MALE:
            output += (ending + "\n")

    elif(gender == Constants.FEMALE_OPTION):
        for ending in ENDINGS_FEMALE:
            output += (ending + "\n")

    return output

def DisplayVoicemailSummary(gender, phoneNumber, reasons, endings):
    output = "\n" + SUMMARY_PREFACE + "\n"
    output += "Gender: " + GENDERS[gender] + "\n"
    output += "Phone number: " + phoneNumber + "\n"
    output += "Reasons:\n"
    for reason in reasons:
        if gender == Constants.MALE_OPTION:
            if DEBUG:
                print(reason)
            output += " " + REASONS_MALE[reason] + "\n"
        elif gender == Constants.FEMALE_OPTION:
            output += " " + REASONS_FEMALE[reason] + "\n"
    output += "Endings:\n"
    for ending in endings:
        if gender == Constants.MALE_OPTION:
            output += " " + ENDINGS_MALE[ending] + "\n"
        elif gender == Constants.FEMALE_OPTION:
            output += " " + ENDINGS_FEMALE[ending] + "\n"

    return output
