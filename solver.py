import os

output = open("flag.ppm", "w")
output.write("P3\n330 330\n255\n")
yellow = "255 225 0 "
green = "1 127 2 "
white = "255 255 255 "
black = "0 0 0 "
i = 0
count = 0
while (i<=329):
	j = 0
	while(j<=329):
		pixel_name_png = "gif_"+str(count)+".png"
		pixel_name_ppm = "gif_"+str(count)+".ppm"
		os.system("mogrify -format ppm "+pixel_name_png)
		os.system("convert "+pixel_name_ppm+" -compress none "+pixel_name_ppm)
		with open(pixel_name_ppm, 'r') as arquivo:
			run = 1
			printed = False
			for linha in arquivo:
				for numero in linha.split():
					if run <=5:
						run+=1
						continue
					else:
						if numero >=200:
							output.write(white)
						else:
							output.write(black)
						printed = True
						break

				if(printed):
					break
		count+=1
		j+=1
		os.system("rm "+pixel_name_ppm)
	output.write("\n")
	print(str(i+1)+"/330")
	i+=1
output.close()