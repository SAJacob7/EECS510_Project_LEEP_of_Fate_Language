# EECS 510 Project: LEEP of Fate Language
The code is a program that automates the below language. It is a Context-Free Grammar represented by a PDA.
## Instructions to Run the Code
First, download our GitHub project folder (in Visual Studio Code):
```
git clone https://github.com/SAJacob7/EECS510_Project_LEEP_of_Fate_Language.git <target-directory>
```
Alternatively, you can go to our GitHub website and click the Green Code button and Download the zip file.

**If you do not already have the ascii_magic library, run this command:**
```
pip install ascii_magic
```
Since this is a Python file, you can run it with the Run button in Visual Studio code or do this command in terminal:
```
python3 leep_of_fate_program.py
```
_Note that our driver file is the leep_of_fate_program.py. Please run this file. The .txt file is also in this folder._

When you run the leep_of_fate_program.py file, it will ask you for user input. Please input the string that you would like to test to see if our language accepts or rejects it. There are also other starter instructions given when you run the .py file.

From there, our code will give you the transitions the PDA took to accept the string if it is part of the language, or gives you a reject message.

**Bonus!** We also included some fun ASCII art surprises when you run the code of a Jayhawk vs. a Wildcat, in the spirit of our language.

## LEEP of Fate: Rock Chalk Chronicles Language Overview

**Purpose**: To defeat the wildcats using the correct series of spells that will lead to the ultimate demise of the cat.

**Alphabet** = { f, w, a, e,*}

**Rules:**
* f and w combined have to be odd in length.
  * This means that there must be at least one f or w.

* The length of a and e combined is even in length.
  * If there are a’s and e’s in the string, then a single run of a’s and e’s must be even in length, meaning they must be consecutively next to each other. For example, aafeaaewf* is valid, but afefeef* is not valid.

* Having a * at the very end of the string to denote that this is the end of the spell.

**Definitions:**
* f = Fire
* w = Water
* a = Air
* e = Earth
* The * means Rock Chalk Jayhawk!

**Example Strings:**


**Valid Strings**
* fwaaeef*
* faawaaeewww*
* aefwfaeff*
* weefeafaaaa*
* aeaefwf*
* f*

**Invalid Strings:**
* fwaaee
* fawe*
* afeff*
* efe*
* afefewa*
