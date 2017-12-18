# 3DSCTF-Microscope-MISC-
Microscope - 488 Points (17 solvers)
http://microscope01.3dsctf.org:8011/
Author: @atcasanova

>The site site contain a one gif(http://microscope01.3dsctf.org:8011/gif.gif).
>So lets to down it with:
```
wget http://microscope01.3dsctf.org:8011/gif.gif
```
>Convert all the frames to png with:
```
convert gif.gif gif.png
```
>There are 108900 images, each one has a unique color, if Title Chall name is Microscope and the frames are only one color, i presuppose that the images are pixels of a 330x330, because sqrt(108900) = 330.

>Verifing the frames, they are only 2 colors: green and yellow

>I'll to use ppm format to manipulate all the frames for a single image.

>Obs: before begin, lets rename and enum the files that start with zeros to better the implementation:
```
mkdir zeros
mv gif_0* zeros/
cd zeros
ls | cat -n | while read n f; do mv "$f" "$n.png"; done
mv * ../
```
### Here is the code:

>Ppm files have as header: Format(P3), Resolution(330x330), Color max value(255), next comes values RGB for each pixel
```python
output = open("flag.ppm", "w")
output.write("P3\n330 330\n255\n")
```
>Use 'mogrify' to transform the png frame to ppm, after convert P6 to P3 with 'convert'
```python
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
```

>After open the frame, compare the Green value to check if the pixel is green or yellow, more than 200 is yellow, bellow is green, if the frame is yellow, print white("255 255 255 ") on output, else, black("0 0 0 ")

```python 
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
```

>After the code execution, we have a QRCODE image, scan it and get the flag!

![Screen shot](https://github.com/lucasnathaniel/3DSCTF-Microscope-MISC/blob/master/qrcode.png "Flag")


By: Lucas ~K4L1~ Nathaniel | FireShell
