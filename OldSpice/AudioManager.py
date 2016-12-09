import urllib
import sys
from subprocess import call
import Constants

DEBUG = False

URL =  "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/"

##############
# MALE AUDIO #
##############
MALE_GREETING = "m-b1-hello.mp3"
HAVE_DIALED = "m-b2-have_dialed.mp3"
CANNOT_COME_TO_PHONE = "m-r0-cannot_come_to_phone.mp3"
REASONS_MALE_AUDIO = (
    "m-r4-ripping_weights.mp3",
    "m-r3-polishing_monocole.mp3",
    "m-r2-cracking_walnuts.mp3",
    "m-r1-building.mp3"
)
LEAVE_MESSAGE = "m-leave_a_message.mp3"
ENDINGS_MALE_AUDIO = (
    "m-e1-horse.mp3",
    "m-e3-on_phone.mp3",
    "m-e4-swan_dive.mp3",
    "m-e5-voicemail.mp3",
    "m-e2-jingle.mp3"
)

################
# FEMALE AUDIO #
################
FEMALE_GREETING = "f-b1-hello_caller.mp3"
LADY_AT = "f-b2-lady_at.mp3"
UNABLE = "f-r0.1-unable_to_take_call.mp3"
BUSY = "f-r0.2-she_is_busy.mp3"
REASONS_FEMALE_AUDIO = (
    "f-r5-riding_a_horse.mp3",
    "f-r2-listening_to_reading.mp3",
    "f-r1-ingesting_old_spice.mp3",
    "f-r4-moon_kiss.mp3",
    "f-r3-lobster_dinner.mp3"
)
ENDINGS_FEMALE_AUDIO = (
    "f-e1-she_will_get_back_to_you.mp3",
    "f-e2-thanks_for_calling.mp3"
)


# Download all relevant audio samples from URL. Files are stored in a list
# which is return from the function
def DownloadAudio(gender, phoneNumber, reasons, endings):
    audioSamples = []
    numbers = list(phoneNumber)

    if DEBUG:
        print(gender, phoneNumber, reasons, endings)

    if gender == Constants.MALE_OPTION:
        audioSamples.append(urllib.urlretrieve(URL + MALE_GREETING)[0])
        audioSamples.append(urllib.urlretrieve(URL + HAVE_DIALED)[0])
        for number in numbers:
            audioSamples.append(urllib.urlretrieve(URL + number + ".mp3")[0])
        audioSamples.append(urllib.urlretrieve(URL + CANNOT_COME_TO_PHONE)[0])
        for reason in reasons:
            audioSamples.append(urllib.urlretrieve(URL
                + REASONS_MALE_AUDIO[reason])[0])
        audioSamples.append(urllib.urlretrieve(URL + LEAVE_MESSAGE)[0])
        for ending in endings:
            audioSamples.append(urllib.urlretrieve(URL
                + ENDINGS_MALE_AUDIO[ending])[0])
    elif gender == Constants.FEMALE_OPTION:
        audioSamples.append(urllib.urlretrieve(URL + FEMALE_GREETING)[0])
        audioSamples.append(urllib.urlretrieve(URL + LADY_AT)[0])
        for number in numbers:
            audioSamples.append(urllib.urlretrieve(URL + number + ".mp3")[0])
        audioSamples.append(urllib.urlretrieve(URL + UNABLE)[0])
        audioSamples.append(urllib.urlretrieve(URL + BUSY)[0])
        for reason in reasons:
            audioSamples.append(urllib.urlretrieve(URL
                + REASONS_FEMALE_AUDIO[reason])[0])
        #audioSamples.append(urllib.urlretrieve(URL + LEAVE_MESSAGE)[0])
        for ending in endings:
            audioSamples.append(urllib.urlretrieve(URL
                + ENDINGS_FEMALE_AUDIO[ending])[0])

    return audioSamples

# Given a list of audio samples, combines them all into one file and returns
# the combined file to the outputFile. The method is OS independent
def CombineAudioFiles(audioSamples, outputFile):
    # Get each sample and combine into one string
    cmdString = ""
    for sample in audioSamples:
        if DEBUG:
            print(str(sample))
        cmdString += str(sample) + " "

    # Determine OS / platform
    if (sys.platform == "linux" or sys.platform == "linux2"
    or sys.platform == "darwin"):
        cmdString = "cat " + cmdString + "> " + "./" + outputFile
        call(cmdString, shell=True)
    elif sys.platform == "win32":
        #print("win")
    else:
        print("Unsupported OS. Terminating process.")
        sys.exit(2)
