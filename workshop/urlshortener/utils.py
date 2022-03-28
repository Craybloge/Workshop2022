'''
Utilities for Shortener
'''
from django.conf import settings

from random import choice

from string import ascii_letters, digits


# Try to get the value from the settings module
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAIABLE_CHARS):
    """
    Creates a random string with the predetermined size
    """
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )
    
def create_shortened_url(model_instance, url="" ):
    model_class = model_instance.__class__
    if url != "":
        if model_class.objects.filter(short_url=url).exists():
            # gérer le cas où on essaye de créer une url existant déja
            return create_shortened_url(model_instance)
        else:
            return url
    else:
            
        random_code = create_random_code()
        # Gets the model class


        if model_class.objects.filter(short_url=random_code).exists():
            # Run the function again
            return create_shortened_url(model_instance)

        return random_code
    


def qr_Code_generator(Data):
    import qrcode
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    path = "./workshop/image/qr_codes/" + Data +".png"
    qr.add_data(Data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#9E7552", back_color="white")
    img.save(path)
    return(path)

