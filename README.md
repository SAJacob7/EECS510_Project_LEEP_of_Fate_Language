# EECS510 Project: LEEP of Fate Language
The code is a program that automates the below language. It is a Context-Free Grammar represented by a PDA.


**LEEP of Fate: Rock Chalk Chronicles**
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
