# Problem: Slime Box

Slimes are basic creatures in any fantasy world. They tend to have liquid-like
properties which allow them to change their shapes. There are many
interpretations and media adaptations based on this concept, including elemental
slimes, various methods of reproduction, as well as a man who was reincarnated
into a slime and a female individual known to be a rancher who breeds slimes for
profit.

That aside, in this world, we have learned that slimes have a few key properties
that are common to all of them, including:

* Color. Slime coloration is well-documented by Dr. F.D.C. Willard. Slimes have
  three basic values that define the color, simply known as "R", "G", and "B".
  These values are integers that range from 0 to 255.
* Mass. Slimes are mostly measured in mass as it is generally easier. When
  slimes combine, the mass is simply added up together. When a slime eats, its
  mass increases by 90% of the mass of the food. Mass must be an integer 
  GREATER THAN zero. (A slime cannot be massless.)
* Volume. Each slime has its volume, and when combined, the volumes also add up
  together. Slimes are liquid in nature and cannot be compressed. The volume
  must be an integer GREATER THAN zero. (You know, physics.)
  
These are what they can do:

* Eat. Slimes can be fed food. If you feed LIQUID food, the slime's mass
  increases by 90% of the food mass, and the volume increases by the same
  amount. However, SOLID food increases slime's mass by only 40% and does not
  increase volume. Generally, liquid food is better for growth and more
  economical, but solid food is great if you want to do some last-minute slime
  fattening without risking not fitting them into boxes.
* Combination. When slimes of different colors mix, each of their color values
  combine based on their masses. Therefore, for a particular color value, if a
  slime with mass *m1* combines with a slime of mass *m2*, the color value R
  combines as follows: `R' = ((R1 * m1) + (R2 * m2))/(m1+m2)`. This is called
  the weighted arithmetic mean. The same logic applies to cases of G and B color
  values, as well as cases of multiple simultaneous combinations. Color values
  are rounded down. The new slime will have mass and volume equal the sum of
  the original slimes' masses and volumes, respectively.
* Splitting. A slime can split into many smaller copies. Splitting divides both
  the mass and the volume evenly, but rounded down.

Slimes are regularly shipped in enclosed spaces like boxes and glass jars.
In some worlds, slimes hide in ceramic or clay pots, waiting to be broken free
by a hero.

Also, two slimes are considered equal when their mass and volume are exactly the
same values. Just like for humans, body color does not matter.

## The Quantum Nature of the Slime World

TLDR: Always round everything down *just before returning*.

In the Slime World, we know that everything operates on a quantum basis which
means there is no such thing as a real number. Although computation may
temporarily have floating-point values, the result at the end of each
calculation operation will always be an integer. This makes things a little ...
discrete, but simple nonetheless.

Although there is a little loss here and there, we know that loss happens all
the time, everywhere.

Are we living in a simulation? *Is this loss?*

## Your Story

The story is, a delivery man from "JTF Express" came to your doorstep and left
you with three boxes, each containing a slime. The man left in a hurry as he has
to pick up his daughter from the school.

As a white feather falls onto your head (which really hurts because it's from an
Ancient Eagle), you decided to become a Slime Master and open your own farm.

## Your Task:

1. Implement the slimebox module (file).
2. Implement the sim module (file) that interprets the order and uses the
   slimebox module to work the orders as given.

### INPUT and Order Processing

At the beginning of each order round you will be given a list of slimes.

This is an example input:

```
5 12
100 10 0 0 999
200 20 -50 0 0
150 300 124 255 50
200 100 4 6 200
5000 810 90 20 0
EAT 0 100 L
EAT 1 100 L
EAT 4 200 L
EAT 2 1000 S
SPLIT 2 3
COMBINE 1 3
SPLIT 1 4
EAT 4 1000 L
SPLIT 4 2
COMBINE 5 6
COMBINE 11 12
COMBINE 0 13
```

The first line of the input will say `s n` where:

* `s` is the number of slimes
* `n` is the number of orders

`s` lines follow, each indicating the properties of a slime as follows:

``` m v r g b
```

Where:

* `m` is the mass.
* `v` is the volume.
* `r`, `g`, `b` are color values (0-255).

The following `n` lines will list individual orders as follows:

* A combining order, `COMBINE i j`, to combine two slimes together. When slimes
  are combined, the location [j] becomes blank and won't be reused.
* A splitting order, `SPLIT i`, to split the `i`th slime into two parts. The
  location [i] becomes blank and won't be reused. The new slimes take up next
  indices (indexes).
* An eating order, `EAT i m S|L`, which instructs the `i`th slime to eat food of
  mass `m`. Food type is indicated by an uppercase `S` or `L`.

The index i always starts from 0.

### Conditions of Order Processing

You must ensure that the behaviors are correct in some cases, such as
out-of-range color values that must be converted, or exceptions that must be
properly raised.

For the operation to be successful, it must meet all conditions of the operation
listed in their respective sections.

If the order references a nonexistent slime (the position is blank or never been
occupied), you must properly catch the exception but do not report it in the
result. Do not remove existing or required exceptions, as the script will
actively look for them. You will not receive full marks if you remove or ignore
implementing required exceptions.

When a new slime is created, it will have the index next to the very last slime.
For example, if you have 1000 slimes (last one indexed 999), and breed one more,
the new slime will have index 1000. If you have 20 slimes (last one indexed 19)
and split the 14th one, the new slimes will be indexed 20-23, but index 14 will
become empty.

Index starts at 0. Your first slime is indexed 0.

### OUTPUT: Reporting

Your report contains n lines, where n is the number of slimes you still have.

For each line, report:

* the index of the slime
* the mass of the slime
* the volume of the slime
* the R G B components of the slime color, just the numbers

Below is an example output of the test case given above.

```
0 3230 1045 84 18 15
3 200 100 4 6 200
5 366 200 124 255 50
6 183 100 124 255 50
7 183 100 124 255 50
8 122 52 1 2 81
9 122 52 1 2 81
10 122 52 1 2 81
11 3162 997 86 19 3
12 3040 945 90 20 0
13 3040 945 90 20 0
```

## Program Template

There is a damaged program that models farm management. You must restore the
supplied code, by hand, to account for slime farm management.

You will use the following Python knowledge in this problem:

* Nesting objects and duplicating them safely.
* Implementing object properties instead of using simple getters and setters.
* Implementing object privacy (information hiding).
* Manage interactions between objects.

You will also learn by example how to handle errors using try-except.

## Grading

This problem is graded using a test script.

You can run the test script to see the available checkpoints.

Note that for the programming challenge part (the simulation), only the first
test case has an associated output file. The other two test cases' output files
are not given.

The provided doctest will be quite credible as an at-home test. If you pass all
of them, you will mostly pass the script.

## Rules

* ***ALL ATTRIBUTES IN Slime AND Color MUST BE PRIVATE!***
* Even if some attributes are not actually used in the simulation, if they are
  included or abstracted in the slimebox file, you must implement it.
* You may use `copy` or `itertools` if required. You may not import anything
  else, especially `os` or `sys`. (NG) Everything already included in the
  prepared starter code is permitted (and should not be removed).
* Your code may not create external network connections. (NG)
* Your code may not open a file. (NG) The only exception is to open a test case,
  when administered automatically by the testing script.
* Your code may not create additional threads. (NG)
* Late submissions are penalized. (-20 points penalty per day)
* Items marked NG means work will "Not be Graded" if you violate them.
* Extraneous means not meaningfully used.

All grading rules are enforced by an automatic script. However, deliberate
attempts to spoil the intentions of the problem by exploiting the capabilities
(or lack thereof) of the automatic grading system ("cheesing") will be given
zero points. Disciplinary actions may be taken if such behavior is also
considered intentional and/or disruptive.
