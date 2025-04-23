from PIL import Image, ImageDraw
import requests
import hashlib
import time

def get_block_data(block_height):
    try:
        url = f"https://blockstream.info/api/block-height/{block_height}"
        response = requests.get(url)
        response.raise_for_status()
        block_hash = response.text.strip().rstrip('%')

        url = f"https://blockstream.info/api/block/{block_hash}"
        response = requests.get(url)
        response.raise_for_status()
        block = response.json()

        return {
            "height": block_height,
            "tx_count": block["tx_count"],
            "size": block["size"],
            "fees": block["tx_count"] / 10000,
            "timestamp": block["timestamp"],
            "hash": block_hash
        }
    except requests.RequestException as e:
        print(f"Error fetching block data for height {block_height}: {e}")
        return {
            "height": block_height,
            "tx_count": 2000,
            "size": 1000000,
            "fees": 0.2,
            "timestamp": 1696118400,
            "hash": str(block_height)
        }

def generate_bot_image(block_height):
    colors = {
        '0': 'darkgrey',
        '1': 'indigo',
        '2': 'lavender',
        '3': 'yellow',
        '4': 'cyan',
        '5': 'magenta',
        '6': 'lime',
        '7': 'green',
        '8': 'pink',
        '9': 'orange',
        '10': 'red',
        '11': 'purple',
        '12': 'teal',
        '13': 'gold',
        '14': 'violet'
    }
    
    block_data = get_block_data(block_height)
    
    hash_digits = hashlib.sha256(str(block_data["hash"]).encode()).hexdigest()
    head_idx = int(hash_digits[0], 16) % 15
    body_idx = int(hash_digits[1], 16) % 15
    left_ear_idx = int(hash_digits[2], 16) % 15
    right_ear_idx = int(hash_digits[3], 16) % 15
    paws_idx = int(hash_digits[4], 16) % 15
    tail_idx = int(hash_digits[5], 16) % 15
    eyes_idx = int(hash_digits[6], 16) % 15
    nose_idx = int(hash_digits[7], 16) % 15
    spot_idx = int(hash_digits[8], 16) % 15

    head_color = colors[str(head_idx)]
    body_color = colors[str(body_idx)]
    left_ear_color = colors[str(left_ear_idx)]
    right_ear_color = colors[str(right_ear_idx)]
    paws_color = colors[str(paws_idx)]
    tail_color = colors[str(tail_idx)]
    eyes_color = colors[str(eyes_idx)]
    pupils_color = 'black'
    nose_color = colors[str(nose_idx)]
    spot_color = colors[str(spot_idx)]
    
    head_size = min(150, max(50, block_data["size"] // 10000))
    head_x1, head_y1 = 150 - head_size // 2, 150 - head_size // 2
    head_x2, head_y2 = head_x1 + head_size, head_y1 + head_size
    
    body_width = head_size * 0.8
    body_height = head_size * 1.2
    body_x1, body_y1 = 150 - body_width // 2, head_y2
    body_x2, body_y2 = body_x1 + body_width, body_y1 + body_height
    
    spot_count = min(20, block_data["tx_count"] // 10)
    
    has_collar = block_data["fees"] > 0.2
    ear_shape_upright = block_data["timestamp"] % 2 == 0
    
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    
    ear_width, ear_height = 30, 40
    if ear_shape_upright:
        draw.rectangle((head_x1 - 10, head_y1 - ear_height, head_x1 + ear_width - 10, head_y1), fill=left_ear_color, outline='black', width=1)
        draw.rectangle((head_x2 - ear_width + 10, head_y1 - ear_height, head_x2 + 10, head_y1), fill=right_ear_color, outline='black', width=1)
    else:
        draw.rectangle((head_x1 - 10, head_y1 - ear_height // 2, head_x1 + ear_width - 10, head_y1 + ear_height // 2), fill=left_ear_color, outline='black', width=1)
        draw.rectangle((head_x2 - ear_width + 10, head_y1 - ear_height // 2, head_x2 + 10, head_y1 + ear_height // 2), fill=right_ear_color, outline='black', width=1)
    draw.rectangle((head_x1 - 5, head_y1 - ear_height + 5, head_x1 + ear_width - 15, head_y1 - 5), fill='pink')
    draw.rectangle((head_x2 - ear_width + 15, head_y1 - ear_height + 5, head_x2 + 5, head_y1 - 5), fill='pink')
    
    draw.rectangle((head_x1, head_y1, head_x2, head_y2), fill=head_color, outline='black', width=1)
    
    draw.rectangle((body_x1, body_y1, body_x2, body_y2), fill=body_color, outline='black', width=1)
    
    for i in range(spot_count):
        spot_x = body_x1 + (i % 5) * 15 + 5
        spot_y = body_y1 + (i // 5) * 15 + 5
        draw.rectangle((spot_x, spot_y, spot_x + 5, spot_y + 5), fill=spot_color)
    
    if has_collar:
        draw.rectangle((head_x1 + 10, head_y2 - 5, head_x2 - 10, head_y2), fill='red', outline='black', width=1)
    
    eye_size = head_size // 5
    draw.rectangle((head_x1 + head_size // 4, head_y1 + head_size // 4, head_x1 + head_size // 4 + eye_size, head_y1 + head_size // 4 + eye_size), fill=eyes_color, outline='black', width=1)
    draw.rectangle((head_x2 - head_size // 4 - eye_size, head_y1 + head_size // 4, head_x2 - head_size // 4, head_y1 + head_size // 4 + eye_size), fill=eyes_color, outline='black', width=1)
    pupil_size = int(eye_size // 1.5)
    draw.rectangle((head_x1 + head_size // 4 + eye_size // 4, head_y1 + head_size // 4 + eye_size // 4, head_x1 + head_size // 4 + eye_size // 4 + pupil_size, head_y1 + head_size // 4 + eye_size // 4 + pupil_size), fill=pupils_color, outline='black', width=1)
    draw.rectangle((head_x2 - head_size // 4 - eye_size // 4 - pupil_size, head_y1 + head_size // 4 + eye_size // 4, head_x2 - head_size // 4 - eye_size // 4, head_y1 + head_size // 4 + eye_size // 4 + pupil_size), fill=pupils_color, outline='black', width=1)
    
    nose_size = head_size // 10
    draw.rectangle((150 - nose_size // 2, head_y1 + head_size // 2 - nose_size // 2, 150 + nose_size // 2, head_y1 + head_size // 2 + nose_size // 2), fill=nose_color)
    
    draw.rectangle((150 - head_size // 4, head_y1 + head_size // 2 + 10, 150 + head_size // 4, head_y1 + head_size // 2 + 15), fill='black')
    
    paw_size = head_size // 5
    draw.rectangle((body_x1, body_y2 - 20, body_x1 + paw_size, body_y2), fill=paws_color, outline='black', width=1)
    draw.rectangle((body_x2 - paw_size, body_y2 - 20, body_x2, body_y2), fill=paws_color, outline='black', width=1)
    draw.rectangle((body_x1, body_y2 - 40, body_x1 + paw_size, body_y2 - 20), fill=paws_color, outline='black', width=1)
    draw.rectangle((body_x2 - paw_size, body_y2 - 40, body_x2, body_y2 - 20), fill=paws_color, outline='black', width=1)
    
    draw.rectangle((body_x2, body_y1 + body_height // 2 - 5, body_x2 + 40, body_y1 + body_height // 2 + 5), fill=tail_color, outline='black', width=1)
    
    img.save(f'bot_{block_height}.png')
    print(f"Bot image saved as bot_{block_height}.png")

for block_height in range(800000, 800010):
    generate_bot_image(block_height)
    time.sleep(1)