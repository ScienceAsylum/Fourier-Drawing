# Drawing with Fourier Series
A <a href="https://en.wikipedia.org/wiki/Fourier_series">Fourier series</a> is a type of mathematical series made of complex exponential functions. Because of that we use the complex plane to draw shapes. In fact, any shape can drawn as long as you keep enough terms. These programs are designed to put that idea into action.

## Necessary Software
They're coded in Python 3.8 using the Visual Python 7 (vpython) package. If you haven't already, install Python then type the following into your command line to add the vpython package:

```
pip install vpython --upgrade
```

## How to Use
Each term in the Fourier series (for each shape) is represented as an arrow rotating in the complex plane. The arrows are attached to each other, tail to head, in the order of their length. The shorter the arrow, the finer the adjustment. When you first run the program, the simulation will be frozen at t=0. Just click anywhere in the display canvas to start the Drawing process. A thick blue curve will then draw over the faint outline.

<img src="https://github.com/ScienceAsylum/Fourier-Drawing/blob/main/N-Screenshot1.png">

<img src="https://github.com/ScienceAsylum/Fourier-Drawing/blob/main/N-Screenshot2.png">

## How to draw your own shape
If you don't have a mathematical function that describes the shape, then you need the location of the points on the shape in 2D space. Include those points as a list in a text document <a href="https://github.com/ScienceAsylum/Fourier-Drawing/blob/main/LetterN.txt">like this</a> and have the program call that text document. I found this <a href="https://spotify.github.io/coordinator/">website</a> helpful when converting shape images into point lists. Then just look for the following line in the code:

```ruby
PointFile = open("PointListFileName.txt", "r")
```

## Issues
The code works fine if you only keep 100-200 terms. If you get up near 1000, the program really drags. You have to let your computer render the frames using a capture command in the animation loop:

```ruby
scene.capture("FileName.png")
```

Then you can import all those frames into a compositor (like Adobe After Effects) to see the animation play out in real time. Unfortunately, as far as I can tell, having 1000 or more terms is necessary for more complicated shapes. Otherwise, they won't draw properly. It might work faster if it wasn't using a 3D environment.

## Inspiration for the Project
The first time I saw this process, it was in the following <a href="https://github.com/3b1b">3blue1brown</a> video:

<a href="https://youtu.be/r6sGWTCMz2k">
    <b>But what is a Fourier series? From heat flow to drawing with circles | DE4</b></br>
    <img src="https://img.youtube.com/vi/r6sGWTCMz2k/mqdefault.jpg">
</a>

## License
This code is under the <a href="https://github.com/ScienceAsylum/Fourier-Drawing/blob/main/LICENSE">GNU General Public License v3.0</a>.
