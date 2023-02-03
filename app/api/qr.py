import qrcode
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/qr")
async def qr(link: str = Query(None)):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = img.get_bytes()

    # serve the image as a base64 encoded string in an HTML page
    return HTMLResponse(content=f'<img src="data:image/png;base64,{img_bytes.decode()}"/>', media_type='text/html')