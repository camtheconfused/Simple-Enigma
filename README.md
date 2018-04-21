This is a super basic implementation of the german ENIGMA cryptography machine.
It is currently essentially a civilian variant as there are only three rotor options, rotors IV, and V will be added soon
The simulation is equiped with a reflector of type b as it was the most common.
Currently, plugboard and ring setting are not supported.

A brief description of ENIGMA
The ENIGMA machine looks like a large typewriter with a alphabetical keyboard. There are 26 indicator lamps, one for each letter of the alphabet.
In addition, the non-naval Enigma is equipped with slots for 3 encryption rotors.
When the key was depressed a circuit was created between a battery and the lightbulbs with the three rotors in between.
There were a number of different 'types' (the germans eventually had 8) of rotors that were used to expand the keyspace.
Each rotor type had 26 inputs on the lef hand side of the rotor and 26 outputs on the right hand side. Between was 26 wires that meant that the output differed from the input.
In addition to the three rotors there was also a static reflect that returned the signal back through the rotors and thence onto the indicator lamps.
The reflector had a static wiring that essentially swapped each letter with its pair. For example, 'A'always returned 'Y'
The reflector design meant that the output was a symmetrical cipher that could be decrypted by running the ciphertext back through the machine using the same key settings, thus reducing the weight of the device.
However, it also gave ENIGMA a major flaw, that no letter could encipher to itself. This flaw would be exploited by Bletchley Park in breaking the supposable unbreakable code.
Thus, the electrical signal created by they key went through the rotors and was scrambled three times and swapped with its reflector pair and then back through the rotors and scrambled again.
The ENIGMA rotors were equipped with a gearing system that moved them on each keypress. The leftmost rotor, known as the 'fast rotor' incremented one letter every key press.
Each rotor had a kickpoint (or two) that would move the rotor to its right.
Thus, the middle rotor moved every 13/26 turns of the fast rotor and the leftmost rotor, the 'slow rotor', incremented every 13/26th turns  of the middle rotor.
The differing kickpoints on each rotor was actually flawed as it helped codebreakers guess which rotor was in which position, too slow for real-time codebreaking but still a flaw.
In addition, there was also a plugboard which allowed the operator to wire up pairs of letters. These letters pairs would be swapped electrically before and after being enciphered.
For example, if 'A' and 'T' were 'steckered' then an 'A' would be swapped into a 'T' and then enciphered with the output also being swapped with its pair.
This feature gave the ENIGMA a truly staggering keyspace, however german protocal to only use exactly 10 pairs limited the keyspace.
Because of the moving rotor system, two identical cleartext  would be enciphered to different letters. For example 'A','A' might become 'S','M'.

#Todo add in description of double stepping and ring setting.


Using ENIGMA
To encipher, the operators (one to type the message, the other to record the ciphertext) would have to know a number of settings, hopefully only known to the recipient:
1. The rotor selection and order (Eg. 'I','II','III')
2. The key setting: the starting positions of each of the rotors (E.G D K M)
3. The plugboard settings

With these setting the opperator would begin typing the cleartext and writing down the resulting lamps illuminating (giving the cipher text).
Luckily Simple Enigma remembers the output for you, meaning you don't need a second operator.

P.S don't use the ENIGMA for anything where security is required. The keyspace is large, but it has serious flaws and is easily broken today.