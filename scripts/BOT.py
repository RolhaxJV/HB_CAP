from discord import Intents,Message,Client
from scripts import Vac_Sem
from covid_project.settings import DIS_TOKEN

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

def get_response(user_input):
    """
    Function to process user input and return a response.
    
    Parameters:
    - user_input: a string containing the user input
    
    Returns:
    - If user_input is empty, returns 'silencieux'
    - If 'cap_bot' is in user_input, returns "Donnes demander : + lien GitHub "
    - Otherwise, returns None
    """
    mess = user_input.lower()

    if mess == '':
        return 'silencieux'
    if 'jv_cap_bot' in mess:
        if '[' not in mess or ']' not in mess:
            return "Demande incorrecte"

        L = user_input.split("[")[1].split("]")[0].split(",")
        year = int(L[0])
        depart_id = L[1]

        if year == None or year == '' or depart_id == None or depart_id == '':
            return "Données incorrecte"

        nb_dose = Vac_Sem.find_data(year,depart_id)
        return f"Nombre de dose pour l'années {year} et le departement {depart_id} : {nb_dose} \n GitHub : https://github.com/RolhaxJV/HB_CAP"
    else:
        return 

async def send_message(message,user_message):
    """
    Asynchronous function to send a message in response to a user message.
    Args:
        message: The message object to send a response to.
        user_message: The message received from the user.
    Returns:
        None
    """
    if not user_message:
        print("Message empty")
        return
    try:
        response = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready():
    """
    This function is an event handler for the 'on_ready' event. It is called when the client has finished its initial data loading and is ready for action.
    """
    print(f'{client.user} fonctionnelle')

@client.event
async def on_message(message):
    """
    A function that is triggered when a message is received. 
    It checks if the message author is not the bot itself or "rolhax", then it retrieves the username, user message, and channel from the message object. 
    After that, it prints the message details to the console and sends a message using the send_message function.
    """
    if message.author == client.user:
        return

    username = str(message.author)
    usermess = message.content 
    channel = str(message.channel)

    if username != "rolhax":
        return

    print(f'[{channel}] {username}: "{usermess}"')
    await send_message(message,usermess)

def start():
    """
    Start the Discord Bot client.

    This function starts the Discord Bot client with the token
    specified in the settings.DIS_TOKEN variable.

    Parameters:
        None

    Returns:
        None
    """
    client.run(token=DIS_TOKEN)
start()