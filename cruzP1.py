"""
Program: CS 115 Project 1
Author: Adrian Cruz
Course: CS 115
Description: This program will make a calculator that determines the Air Quality Index (AQI) while also producing
average polutant concentrations and minimum and maximum (AQI) in different locations.
It also determines how healthy the location is.
"""
import sys

def main():

    print("===Air Quality Index (AQI) Calculator===")
    #At the end of each concentration there is an equation that is used to calculate
    # the average quality index of each polutant.
    num_location = int(input("How many locations would you like: "))

    if (num_location < 1):
        print("Error: ", num_location, 'is not a valid input.')
        sys.exit(-1)

    BigAQI = 0
    SmallAQI = float('inf')
    all_locmax = ''
    all_locmin = ''
    avg_pm2 = 0
    avg_pm2_loc = 0
    for i in range(num_location):
        C_low = 0
        C_high = 0
        I_high = 0
        I_low = 0
        Max_AQI = 0
        O31 = 0
        location_name = input("\nEnter name of ** Location " + (str(i + 1)) + " **: ")

        pm2 = float(input("\t-> PM-2.5 [ug/m3, 24-hr avg] Monitor: "))

        pm2 = round(pm2,1 )
        if(0.0 <= pm2 <= 12.0):
            I_high, I_low, C_high, C_low = 50, 0, 12.0, 0

        elif(12.1<= pm2 <= 35.4):
            I_high, I_low, C_high, C_low = 100, 51, 35.4, 12.1

        elif (35.5<= pm2 <= 55.4):
            I_high, I_low, C_high, C_low = 150, 101, 55.4, 35.5

        elif (55.5<= pm2 <= 150.4):
            I_high, I_low, C_high, C_low = 200, 151, 150.4, 55.5

        elif (150.5<= pm2 <= 250.4):
            I_high, I_low, C_high, C_low = 300, 201, 250.4, 150.5

        elif (250.5<= pm2 <= 500.4):

            I_high, I_low, C_high, C_low = 500, 301, 500.4, 250.5

        elif (pm2 != -1 and pm2 < 0) or pm2 > 500.4:

            print("         Your value is out of range, the program will now be terminated.")

            sys.exit(-1)
        if pm2 != -1:

        # The elif exit statement that written after each concentration is supposed exit if a negative number is inputed
            IPM_2_5 = (I_high - I_low) / (C_high - C_low) * (pm2 - C_low) + I_low


            print("\t   PM-2.5 concentration", (pm2), "yield", round(IPM_2_5), "index")

            avg_pm2 += pm2
            avg_pm2_loc += 1
            if IPM_2_5 > Max_AQI:
                Max_AQI = round(IPM_2_5)
                all_locmax = location_name


        pm10 = round(float(input('\t-> PM-10 [ug/m3, 24-hr avg] Monitor: ')))

        if (0 <= pm10 <= 54):
            I_high, I_low, C_high, C_low = 50, 0, 54, 0

        elif (55 <= pm10 <= 154):
            I_high, I_low, C_high, C_low = 100, 51, 154, 55

        elif (155 <= pm10 <= 254):
            I_high, I_low, C_high, C_low = 150, 101, 254, 155

        elif (255 <= pm10 <= 354):
            I_high, I_low, C_high, C_low = 200, 151, 354, 255

        elif (355 <= pm10 <= 424):
            I_high, I_low, C_high, C_low = 300, 201, 424, 355

        elif (425 <= pm10 <= 604):

            I_high, I_low, C_high, C_low = 604, 301, 604, 425


        elif (pm10 != -1 and pm10 < 0) or pm10 > 604:
            print("         Your value is out of range, the program will now be terminated.")
            sys.exit(-1)

        if pm10 != -1:

                IPM_10 = (I_high - I_low) / (C_high - C_low) * (pm10 - C_low) + I_low



                print("\t   PM-10 concentration", round(pm10), "yield", round(IPM_10), "index")



        if IPM_10 > Max_AQI:
             Max_AQI = round(IPM_10)
        NO_2 = round(float(input('\t-> NO2 [ppb, 1-hr avg] Monitor: ')))

        if (0 <= NO_2 <= 53):
            I_high, I_low, C_high, C_low = 50, 0, 53, 0

        elif (54 <= NO_2 <= 100):
            I_high, I_low, C_high, C_low = 100, 51, 100, 54

        elif (101 <= NO_2 <= 360):
            I_high, I_low, C_high, C_low = 150, 101, 360, 101

        elif (361 <= NO_2 <= 649):
            I_high, I_low, C_high, C_low = 200, 151, 649, 361

        elif (650 <= NO_2 <= 1249):
            I_high, I_low, C_high, C_low = 300, 201, 1249, 650

        elif (1250 <= NO_2 <= 2049):

            I_high, I_low, C_high, C_low = 500, 301, 2049, 1250


        elif (NO_2 != -1 and NO_2 < 0) or NO_2 > 2049:

            print("         Your value is out of range, the program will now be terminated.")

            sys.exit(-1)
        if NO_2 != -1:

            INO_2 = (I_high - I_low) / (C_high - C_low) * (NO_2 - C_low) + I_low

            print("\t   NO2 concentration", round(NO_2), "yield", round(INO_2), "index")


            if INO_2 > Max_AQI:
                Max_AQI = round(INO_2)
                all_locmax = location_name

        SO2 = round(float(input("\t-> SO2 [ppb, 1-hr avg] Monitor: ")))
        if (0.0 <= SO2 <= 35):
            I_high, I_low, C_high, C_low = 50, 0, 35, 0

        elif (36 <= SO2 <= 75):
            I_high, I_low, C_high, C_low = 100, 51, 75, 36

        elif (76 <= SO2 <= 185):
            I_high, I_low, C_high, C_low = 150, 101, 185, 76

        elif (186 <= SO2 <= 304):
            I_high, I_low, C_high, C_low = 200, 151, 304, 186

        elif (305 <= SO2 <= 604):
            I_high, I_low, C_high, C_low = 300, 201, 604, 305

        elif (605 <= SO2 <= 1004):

            I_high, I_low, C_high, C_low = 500, 301, 1004, 605


        elif (SO2 != -1 and SO2 < 0) or SO2 > 1004:

            print("         Your value is out of range, the program will now be terminated.")

            sys.exit(-1)
        if SO2 != -1:

            SO2x = (I_high - I_low) / (C_high - C_low) * (SO2 - C_low) + I_low



            print("\t   SO2 concentration", (SO2), "yield", round(SO2x), "index")


            if SO2x > Max_AQI:
                Max_AQI = round(SO2x)

        CO = round(float(input("\t-> CO [ppm, 8-hr avg] Monitor: ")), 1)
        if (0 <= CO <= 4.4):
            I_high, I_low, C_high, C_low = 50, 0, 4.4, 0

        elif (4.5 <= CO <= 9.4):
            I_high, I_low, C_high, C_low = 100, 51, 9.4, 4.5

        elif (9.5 <= CO <= 12.4):
            I_high, I_low, C_high, C_low = 150, 101, 12.4, 9.5

        elif (12.5 <= CO <= 15.4):
            I_high, I_low, C_high, C_low = 200, 151, 15.4, 12.5

        elif (15.5 <= CO <= 30.4):
            I_high, I_low, C_high, C_low = 300, 201, 30.4, 15.5


        elif (CO != -1 and CO < 0) or CO > 30.4:

            print("         Your value is out of range, the program will now be terminated.")

            sys.exit(-1)
        if CO != -1:

            COy = (I_high - I_low) / (C_high - C_low) * (CO - C_low) + I_low


            print("\t   CO concentration", (CO), "yield", round(COy), "index")


            if COy > Max_AQI:
                Max_AQI = round(COy)

        O3x = 0
        O3xindex = 0
        O38 = round(float(input("\t-> O3 [ppb, 8-hr avg] Monitor: ")))
        if (0 <= O38 <= 54):
            I_high, I_low, C_high, C_low = 50, 0, 54, 0

        elif (55 <= O38 <= 70):
            I_high, I_low, C_high, C_low = 100, 51, 70, 55

        elif (71 <= O38 <= 85):
            I_high, I_low, C_high, C_low = 150, 101, 71, 85

        elif (86 <= O38 <= 105):
            I_high, I_low, C_high, C_low = 200, 151, 105, 86

        elif (106 <= O38 <= 200):
            I_high, I_low, C_high, C_low = 300, 201, 200, 106
        else:
            O3xindex = -1

        if O3xindex >= 0:
            O3x = (I_high - I_low) / (C_high - C_low) * (O38 - C_low) + I_low

        if O3x > Max_AQI:
            Max_AQI = round(O3x)

        O31xindex = 0
        O3 = round(float(input("\t-> O3 [ppb, 1-hr avg] Monitor: ")))
        if (125 <= O3 <= 164):
            I_high, I_low, C_high, C_low = 150, 101, 164, 125

        elif (165 <= O3 <= 204):
            I_high, I_low, C_high, C_low = 204, 165, 204, 165

        elif (205 <= O3 <= 404):
            I_high, I_low, C_high, C_low = 300, 201, 404, 205

        elif (405 <= O3 <= 604):
            I_high, I_low, C_high, C_low = 500, 301, 604, 405

        else:
            O31xindex = -1

        if O3xindex >= 0:
            O31 = (I_high - I_low) / (C_high - C_low) * (O3 - C_low) + I_low

        if O3xindex != -1 or O31xindex != -1:
            if O3x > O31:

                print("\t   O3 concentration", round(float(O38), 0), "yield", round(O3x), "index")
            else:
                print("\t   O3 concentration", round(float(O3), 0), "yield", round(O31), "index")

        if O31 > Max_AQI:
            Max_AQI = round(O31)
        print('\tAQI for', location_name, 'is', Max_AQI)

        if(0 <= Max_AQI <=50):
            print('\tCondition: Good')
        elif (51 <= Max_AQI <= 100):
            print('\tCondition: Moderate')
        elif (101 <= Max_AQI <= 150):
            print('\tCondition: Unhealthy for Sensitive Groups')
        elif (151 <= Max_AQI <= 200):
            print('\tCondition: Unhealthy')
        elif (201 <= Max_AQI <= 300):
            print('\tCondition: Very Unhealthy')
        else:
            print('\tCondition: Hazardous')

        # in this part of the code it will calculate the ending maximum and minimum index when we input certain values 
        if Max_AQI > BigAQI: #maxindex after if
            BigAQI = round(Max_AQI)
            all_locmax = location_name #name_loc
        if Max_AQI < SmallAQI: #maxindex after if
            SmallAQI = round(Max_AQI) #maxindex
            all_locmin = location_name #name_loc
        if pm2 > avg_pm2 :
            avg_pm2 = pm2



    print('\n Summary Report')

    print('\t Location with max AQI is ', all_locmax, ' (', BigAQI, ')', sep = '')
    print('\t Location with min AQI is ', all_locmin, ' (', SmallAQI, ')', sep = '')
    print('\t Avg PM-2.5 concentration reading:', round(avg_pm2/avg_pm2_loc, 1))





main()