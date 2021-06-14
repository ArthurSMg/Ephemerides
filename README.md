# Ephemerides


Hello there!

This is a program made by me for an astronomy class in college. Each student was given an asteroid to do some research on, and get all the physical properties as we can without looking it up online. I was given the asteroid 4Vesta

So, the idea behind this simple code, is to calculate the orbital period of the asteroid arround the Eath, its apogee and perigee. The key of the program, is the website [In the Sky org](https://in-the-sky.org/data/asteroids.php#), where one is able to select an asteroid anda a defined period of time, to get  all the information about its position in that time spam.

So basically the program reads the data, that its avaliable here as "vesta_data.csv", then produces a plot of position x time of the asteroids orbit arround the Earth, what is also called the Ephemerides. You expect it to have a periodic behavior since it goes arround and comes back. The period of the orbit can be calculated as the period how many days it takes to the graph to repeats itself, and the apogee and peregee are easily calculated by using the max() and min() list function of Python;

* Here an example of how the graph will look like:

![alt text](https://github.com/ArthurSMg/Ephemerides/blob/main/Graph_vesta.png?raw=true)
