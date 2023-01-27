""" A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
Letters in some SOS messages are altered by cosmic radiation during transmission.
Given the signal received by Earth as a string,s,
determine how many letters of the SOS message have been changed by radiation."""


def marsExploration(s):
    if s.islower():
        return

    if 1 < len(s) < 100:
        length = len(s) // 3
        orig_msg, count = "SOS" * length, 0

        if s == orig_msg:
            return 0
        else:
            for x in s:
                if x not in orig_msg:
                    count += 1
            return count


print(marsExploration("POSSESSOR"))
