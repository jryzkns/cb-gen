from PIL import Image, ImageFont, ImageDraw, ImageFilter

msg = "I KNOW EVERYTHING HAPPENS\nFOR A REASON\n\nBUT WHAT THE FUCK"

s        = (700, 400)    # stretch to 800x600 later on (lyfhax oh yeah!)
out_fn   = "result.png"
p_x, p_y = 60, 40
font     = ImageFont.truetype(
            "ITC Cheltenham LT Bold Condensed Italic.ttf", 36)

render_kwg = {
    "spacing" : -4,
    "font"    : font,
}

text_kwg = {
    **render_kwg,
    "fill"    : (255,) * 4,
    "align"   : "right",
}

base_layer = Image.new('RGBA', s, (0, 0, 0, 255))
text_layer = Image.new('RGBA', s, (0, 0, 0,   0))

base_layer_draw = ImageDraw.Draw(base_layer)
text_layer_draw = ImageDraw.Draw(text_layer)

m_w, m_h = base_layer_draw.textsize(msg, **render_kwg)

textbox_pos = (s[0] - m_w - p_x, s[1] - m_h - p_y)

base_layer_draw.text(textbox_pos, msg, **text_kwg)

base_layer = base_layer.filter(
    ImageFilter.GaussianBlur(2))

text_layer_draw.text(textbox_pos, msg, **text_kwg)

base_layer.paste(text_layer, (0, 0), text_layer)

base_layer = base_layer.resize((800, 600))

base_layer.save(out_fn, "PNG")
