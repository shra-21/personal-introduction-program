import sys
from PIL import Image, ImageDraw, ImageFont

def generate_terminal_screenshot(output_path):
    # Terminal text simulation
    lines = [
        ("PS C:\\Users\\DELL\\Desktop\\Shravani(Projects)\\DevelopersArenaInternship\\personal-introduction-program> ", "#7cd37c"),
        ("python personal_intro.py", "#ffffff"),
        ("", "#ffffff"),
        ("============================================================", "#4ec9b0"),
        ("      🌟 WELCOME TO THE PERSONAL INTRODUCTION PROGRAM 🌟      ", "#f1fa8c"),
        ("============================================================", "#4ec9b0"),
        ("Let's get to know you! Please answer a few quick questions.", "#cccccc"),
        ("", "#ffffff"),
        ("👉 What is your name? ", "#ffb86c"),
        ("Alex", "#8be9fd"),
        ("👉 How old are you? ", "#ffb86c"),
        ("21", "#8be9fd"),
        ("👉 What is your favorite hobby? ", "#ffb86c"),
        ("Coding", "#8be9fd"),
        ("👉 Which city are you currently in? ", "#ffb86c"),
        ("Seattle", "#8be9fd"),
        ("👉 What are your top 2 favorite foods (separated by comma)? ", "#ffb86c"),
        ("Pizza, Sushi", "#8be9fd"),
        ("", "#ffffff"),
        ("============================================================", "#4ec9b0"),
        ("🎉 Welcome, Alex! 🎉", "#50fa7b"),
        ("============================================================", "#4ec9b0"),
        ("📍 Location      : Seattle", "#f8f8f2"),
        ("🎂 Age           : 21 years old (Estimated birth year: ~2005)", "#f8f8f2"),
        ("⏳ Milestone     : You will hit 100 in 79 years!", "#f8f8f2"),
        ("🎨 Favorite Hobby: Coding", "#f8f8f2"),
        ("", "#ffffff"),
        ("🍽️  Favorite Foods:", "#ff79c6"),
        ("   1. Pizza", "#f8f8f2"),
        ("   2. Sushi", "#f8f8f2"),
        ("", "#ffffff"),
        ("------------------------------------------------------------", "#6272a4"),
        ("💬 \"It's fantastic to have you here, Alex!", "#f1fa8c"),
        ("    Keep practicing Python and enjoying Coding in Seattle!\"", "#f1fa8c"),
        ("============================================================", "#4ec9b0"),
        ("", "#ffffff"),
        ("✨ Thank you for using the Personal Introduction Program! Have a great day! ✨", "#50fa7b"),
    ]

    width = 950
    height = 920
    bg_color = "#1e1e2e"
    header_color = "#282a36"

    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Window header bar
    draw.rectangle([0, 0, width, 40], fill=header_color)
    # Window controls (mac/linux/modern terminal style dots)
    draw.ellipse([15, 13, 27, 25], fill="#ff5555")
    draw.ellipse([35, 13, 47, 25], fill="#ffb86c")
    draw.ellipse([55, 13, 67, 25], fill="#50fa7b")

    # Try to load a nice monospace font, fall back to default
    try:
        font = ImageFont.truetype("consola.ttf", 16)
        title_font = ImageFont.truetype("consola.ttf", 13)
    except Exception:
        try:
            font = ImageFont.truetype("arial.ttf", 16)
            title_font = font
        except Exception:
            font = ImageFont.load_default()
            title_font = font

    draw.text((width // 2 - 120, 12), "Developers Arena - Terminal Output", fill="#8be9fd", font=title_font)

    y = 60
    margin_left = 30
    line_height = 22

    # Group prompt and user response where needed
    idx = 0
    while idx < len(lines):
        line_text, color = lines[idx]
        
        # Check if next line is user input inline
        if line_text.startswith("👉") or line_text.startswith("PS "):
            draw.text((margin_left, y), line_text, fill=color, font=font)
            if idx + 1 < len(lines) and not lines[idx+1][0].startswith("👉") and not lines[idx+1][0].startswith("=") and lines[idx+1][0] != "":
                # Calculate width of prompt
                bbox = draw.textbbox((margin_left, y), line_text, font=font)
                text_w = bbox[2] - bbox[0]
                draw.text((margin_left + text_w, y), lines[idx+1][0], fill=lines[idx+1][1], font=font)
                idx += 2
                y += line_height
                continue
        else:
            draw.text((margin_left, y), line_text, fill=color, font=font)
        
        idx += 1
        y += line_height

    img.save(output_path, "PNG")
    print(f"Screenshot successfully saved to: {output_path}")

if __name__ == "__main__":
    generate_terminal_screenshot(sys.argv[1])
