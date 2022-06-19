from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def create_ticket(train_name,train_start_time,train_end_time,people_place,ticket_number,from_city,to_city,sana):
    img = Image.open("media/ticket.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('media/fon_italic.ttf',50)
    font_junash=ImageFont.truetype('media/fon_italic.ttf',45)
    font_vil=ImageFont.truetype('media/fon_italic.ttf',40)
    draw.text((540, 15),f"{train_name} {sana}",(255,255,255),font=font)
    draw.text((265, 290),f"{train_start_time}",(255,255,255),font=font_junash)
    draw.text((260, 355),f"{train_end_time}",(255,255,255),font=font_junash)
    draw.text((309, 427),f"{people_place}",(255,255,255),font=font_junash)
    draw.text((348, 180),f"{ticket_number}",(255,255,255),font=font_junash)
    draw.text((185, 15),f"{from_city}",(255,255,255),font=font_vil)
    draw.text((185, 95),f"{to_city}",(255,255,255),font=font_vil)
    img.save(f'static/tickets/{ticket_number}.jpg')

create_ticket('ToshSam','12:43','19:43',32,76,'Toshkent','Samarqand',20)

