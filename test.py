from macheronte.whatsapp.client import WhatsappClient
from macheronte.whatsapp.enums.browsers import Browsers

import time

client = WhatsappClient(Browsers.CHROME, "")
client.connect()

while True:
    try:

        if client.is_logged():
            status = client.get_user_status("Daniil")

            print(status.value)

    except Exception as e:
        print(e)

    time.sleep(2)