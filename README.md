# EECS 510 Project: LEEP of Fate Language
The code is a program that automates the language below. It is a Context-Free Grammar represented by a PDA.
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

**Bonus!** We also included some fun ASCII art surprises when you run a valid string vs. an invalid string.

## LEEP of Fate: Rock Chalk Chronicles Language Overview

**Purpose**: To defeat the wildcats using the correct series of spells that will lead to the ultimate demise of the cat.

**Alphabet** = { f, w, a, e,*}

**Rules:**
* The string must have only one * in the string that appears as the last character.
  * The smallest valid string is *.

* If there are f's and w's in the string, then the combined length has to be odd.
  
* If there are, a's and e's in the string, then the combined length has to be even.
 * Additionally, each run of a’s and e’s must be even in length, meaning they must be consecutively next to each other. For example, aafeaaewf* is valid, but afefeef* is not valid.

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
* \*

**Invalid Strings:**
* fwaaee
* fawe*
* afeff*
* efe*
* afefewa*
