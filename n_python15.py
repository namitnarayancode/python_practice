from PIL import Image
imgs = Image.open("n_python15.png")
img = imgs.crop((12,12,360-12,360-12))
height, width = img.height, img.width
framheight,framwidth = height//3, width//6
frames = []
for row in range(3):
    for col in range(6):
        left = col*framwidth
        upper = row*framheight
        right = left + framwidth
        lower = upper + framheight
        frame = img.crop((left, upper, right, lower))
        frames.append(frame)

frames[0].save(
    "n_python15.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0
)
