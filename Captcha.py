from PIL import Image, ImageDraw, ImageFont
import random
import string

# Global variables
captcha_text = ""
attempts = 3

#CAPTCHA Generation Text
def generate_text():
    """Generate a simple 6-character alphanumeric CAPTCHA (uppercase + digits)."""
    global captcha_text
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return captcha_text

#Fuction for captcha stenography
def create_image(text):
    """Create CAPTCHA image with basic distortion and noise."""
    width, height = 250, 80
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Add random lines (noise)
    for _ in range(5):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill='gray', width=2)

    # Load font (fallback to default)
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()

    colors = ['blue', 'red', 'green', 'purple', 'orange']
    x_start = 20

    for i, char in enumerate(text):
        x = x_start + (i * 30)
        y = random.randint(15, 25)
        color = random.choice(colors)
        draw.text((x, y), char, fill=color, font=font)

    # Add dots (noise)
    for _ in range(100):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), fill='black')

    return image

#Validate the CAPTCHA Text
def validate(user_input):
    """Validate user input against the generated CAPTCHA."""
    global attempts
    if attempts <= 0:
        return False, "No attempts remaining!"

    user_answer = user_input.strip().upper()
    correct_answer = captcha_text.upper()

    if user_answer == correct_answer:
        return True, "✓ Correct! Verification successful."
    else:
        attempts -= 1
        return False, f"✗ Wrong! {attempts} attempts left."

def main():
    global attempts
    print("=" * 50)
    print("   SIMPLE CAPTCHA GENERATOR AND VALIDATOR")
    print("=" * 50)

    text = generate_text()
    image = create_image(text)
    image.save('captcha.png')
    try:
        image.show()
    except:
        pass

    print(f"\n[CAPTCHA Image Generated: captcha.png]")
    print(f"\nYou have {attempts} attempts.")

    while attempts > 0:
        user_input = input("\nEnter CAPTCHA: ")
        is_valid, message = validate(user_input)
        print(message)
        if is_valid:
            print("\nAccess Granted. Verification successful.")
            break
    else:
        print("\nMaximum attempts exceeded. Access Denied!")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()