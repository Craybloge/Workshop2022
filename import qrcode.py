import qrcode
import sys
def generator(Data, FileName):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(Data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#9E7552", back_color="white")
    img.save(FileName)

if __name__ == "__main__":
    Data = sys.argv[1]
    FileName = sys.argv[2]
    generator(Data, FileName)