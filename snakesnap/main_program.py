""" Takes a thermal picture and emails it to the user. """

from datetime import datetime
from snake_functions import *

PARSED_CONFIG = parse_json()
PERSON_NAME = input(" Please enter your NAME: ") # ask for NAME
SEND_TO = input("Please enter your email: ").strip() # get and clean email
TIMESTAMP = datetime.now().strftime("%Y_%m_%d-%H:%M")
SPLIT_NAME = PERSON_NAME.replace(" ", "_")+'_'+TIMESTAMP
IMAGE_NAME = SPLIT_NAME + '.png' # create image name
PARSED_CONFIG[SPLIT_NAME] = [SEND_TO, IMAGE_NAME] # add name, email, and image name to json doc
# here, I will run the main picture function.

thermal_pic(IMAGE_NAME)
# then, run the email function.
MESSAGE = write_email(PARSED_CONFIG, PERSON_NAME, SPLIT_NAME)
update_json(PARSED_CONFIG)
try:
    send_email(MESSAGE, PARSED_CONFIG)
    print('thank you, your snake snap was sent!')
except:
    print('email failed. please double check your email. \n if correct email will be sent later')
    print(PARSED_CONFIG[SPLIT_NAME][0])
    #finally, update the json data file and exit.
    update_json(PARSED_CONFIG)
    print('Sorry, possible failure with email send.')
