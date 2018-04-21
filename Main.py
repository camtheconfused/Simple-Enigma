# Simple Enigma
# Author: Cameron Stewart
# This is a simple simulation of the enigma machine. No plug board functionality at this stage.
# Licence: MIT

# TODO Plugboard function, prior to enciphering the selected letter is swapped for its pair and this repeats afterwards
# This plugboard is what gave the ENIGMA most of its key space

# This section contains the wiring of the rotors and the fixed reflector.
# Currently, the rotors are fixed from left to right as rotors I,II,III
alphaint = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'ESC']
rotor_I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9, 17]
rotor_II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4, 4]
rotor_III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14, 22]
rotor_IV = []
rotor_V = []
reflector_b = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
# TODO add in Rotors IV, V

# this  sets the rotors to their starting positions
def start_pos(left, middle, right):
    for i in range(left):
        rotor_L.append(rotor_L[0])
        del rotor_L[0]
    for i in range(middle):
        rotor_M.append(rotor_M[0])
        del rotor_M[0]
    for i in range(right):
        rotor_R.append(rotor_R[0])
        del rotor_R[0]


def input_check(input_value):
    if input_value.islower():
        input_value = input_value.upper()
    while input_value not in alphaint:
        input_value = input('Please check your input and renter')
        if input_value.islower():
            input_value = input_value.upper()
    return input_value

# As enigma increments the rotor before enciphering, the rotor is incremented. This is done by shifting each list left.
def stepping(left_pos, middle_pos, right_pos,):
    if middle_pos == middle_kick:
        rotor_L.append(rotor_L[0])
        del rotor_L[0]
        left_pos = left_pos + 1
        rotor_M.append(rotor_M[0])
        del rotor_M[0]
        middle_pos = middle_pos + 1
        print('kicking left rotor')
    rotor_R.append(rotor_R[0])
    del rotor_R[0]
    right_pos = right_pos + 1
    if right_pos == 26:
        right_pos = 0
    if right_pos == right_kick:
        rotor_M.append(rotor_M[0])
        del rotor_M[0]
        print('kicking middle rotor')
        middle_pos = middle_pos + 1
    if left_pos == 26:
        left_pos = left_pos - 26

    print('Rotor Positions:', alphaint[left_pos] + alphaint[middle_pos] + alphaint[right_pos])
    return left_pos, middle_pos, right_pos,


# This is where the enciphering happens.
# The path through the machine is right to left then through the reflector and back through the machine.
# The code takes the key input, looks up the key input (a) and outputs the corresponding int (14) and feeds it into the
# next rotor and so on. Note, this changes (using the element to find the index) because the direction through
# the machine has reversed.
def encipher(key_input):
    right_output = rotor_R[key_input]
    # print('the output of the right rotor is', alphaint[right_output])
    middle_output = rotor_M[(right_output - right_pos)]
    # print('the output of the middle rotor is', alphaint[middle_output])
    left_output = rotor_L[middle_output - middle_pos]
    # print('the output of the left rotor is', alphaint[left_output])
    reflector_output = reflector_b[left_output - left_pos]
    # print('the output of the reflector is', alphaint[reflector_output])
    left_input = (reflector_output + left_pos)
    if left_input >= 26:
        left_input = left_input - 26
    left_output = rotor_L.index(left_input)
    # print('the output of the left rotor is', alphaint[left_output])
    middle_input = (left_output + middle_pos)
    if middle_input >= 26:
        middle_input = middle_input - 26
    middle_output = rotor_M.index(middle_input)
    # print('the output of the middle rotor is', alphaint[middle_output])
    right_input = (middle_output + right_pos)
    if right_input >= 26:
        right_input = right_input - 26
    right_output = rotor_R.index(right_input)
    # print('the output of the right rotor is', alphaint[right_output])
    print(alphaint[key_input], ' enciphers to ', alphaint[right_output])
    return alphaint[right_output]


# this section sets the rotors up according to the user input
rotor_selection = [str(x) for x in input('What is the rotor order (left to right)?'
                                         ' Separate each rotor with a comma').split(",")]
rotors = {'I': rotor_I, 'II': rotor_II, 'III': rotor_III}
rotor_L = rotors[rotor_selection[0]]
rotor_M = rotors[rotor_selection[1]]
rotor_R = rotors[rotor_selection[2]]


# This ensures that the kick positions are at the right point based on the selected rotor. These are stored in the
# last index of the rotor list but have to be deleted before stepping.
# Note, because the left rotor doesn't kick anything it can just be deleted.
right_kick = rotor_R[26]
del rotor_R[26]
middle_kick = rotor_M[26]
del rotor_M[26]
del rotor_L[26]


left_pos = alphaint.index((input_check(input('What is the starting position of the left rotor?'))))
middle_pos = alphaint.index(input_check(input('What is the starting position of the middle rotor?')))
right_pos = alphaint.index(input_check(input('What is the starting position of the right rotor?')))
start_pos(left_pos, middle_pos, right_pos)
message = ''

key_input = alphaint.index(input_check(input('What letter to encipher?')))

while key_input != 26:
    left_pos, middle_pos, right_pos = stepping(left_pos, middle_pos, right_pos,)
    letter = encipher(key_input)
    message = message + letter
    key_input = alphaint.index(input_check(input('What letter to encipher next? ESC to quit')))
print('Thanks for using Simple Enigama! Your Super Secret Message is', message)
