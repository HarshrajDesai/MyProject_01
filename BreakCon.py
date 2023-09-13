#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Harshraj Desai
#
# Created:     31/08/2023
# Copyright:   (c) Harshraj Desai 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

std = ["Ram","Ramesh","Suresh","Shyam"]
for i in std:
    if i == "Suresh":
        break
    print(i)

for i in std:
    if i == "Suresh":
        continue
    print(i)