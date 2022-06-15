# Regex101

One of the flags in this file is the real flag.
The hint given is that the real flag consists of 5 uppercase letters, followed by 5 digits and another 6 uppercase letters.
Also the name of the challenge is a commonly used online Regex tool.

![Given](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Regex101/Images/flags.JPG)

Solvable by regular expression, I used an [online Regex tool](https://regex101.com/)

![Regex 101](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Regex101/Images/regex101.JPG)

There was only 1 match for `[A-Z]{5}[0-9]{5}[A-Z]{6}`

## Flag

> SEE{RGSXG13841KLWIUO}
