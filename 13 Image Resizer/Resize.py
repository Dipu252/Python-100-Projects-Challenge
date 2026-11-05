from PIL import Image

img=Image.open("earth.png")
width=100
height=100
resize=img.resize((width,height), Image.Resampling.LANCZOS)
resize.save("resize earth.png")
resize.show()