import qrcode
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/qr")
async def qr(link: str = Query(None)):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = img.get_bytes()

    return HTMLResponse(content=f'<img src="data:image/png;base64,{img_bytes.decode()}"/>', media_type='text/html')
