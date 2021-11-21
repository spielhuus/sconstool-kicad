EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
NoConn ~ 3200 1700
$Comp
L Device:R R16
U 1 1 616B555C
P 3050 2100
F 0 "R16" H 3120 2146 50  0000 L CNN
F 1 "620" H 3120 2055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2980 2100 50  0001 C CNN
F 3 "~" H 3050 2100 50  0001 C CNN
	1    3050 2100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R14
U 1 1 616B5562
P 2750 2100
F 0 "R14" H 2820 2146 50  0000 L CNN
F 1 "620" H 2820 2055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2680 2100 50  0001 C CNN
F 3 "~" H 2750 2100 50  0001 C CNN
	1    2750 2100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R13
U 1 1 616B5568
P 2400 1600
F 0 "R13" V 2193 1600 50  0000 C CNN
F 1 "100k" V 2284 1600 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2330 1600 50  0001 C CNN
F 3 "~" H 2400 1600 50  0001 C CNN
	1    2400 1600
	0    1    1    0   
$EndComp
$Comp
L Device:C C17
U 1 1 616B556E
P 1950 1600
F 0 "C17" V 1698 1600 50  0000 C CNN
F 1 "470n" V 1789 1600 50  0000 C CNN
F 2 "Capacitor_SMD:C_2220_5650Metric" H 1988 1450 50  0001 C CNN
F 3 "~" H 1950 1600 50  0001 C CNN
	1    1950 1600
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR042
U 1 1 616B5574
P 2750 2250
F 0 "#PWR042" H 2750 2000 50  0001 C CNN
F 1 "GND" H 2755 2077 50  0000 C CNN
F 2 "" H 2750 2250 50  0001 C CNN
F 3 "" H 2750 2250 50  0001 C CNN
	1    2750 2250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR043
U 1 1 616B557A
P 3050 2250
F 0 "#PWR043" H 3050 2000 50  0001 C CNN
F 1 "GND" H 3055 2077 50  0000 C CNN
F 2 "" H 3050 2250 50  0001 C CNN
F 3 "" H 3050 2250 50  0001 C CNN
	1    3050 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1700 1600 1800 1600
Wire Wire Line
	2550 1600 2750 1600
Wire Wire Line
	2100 1600 2250 1600
Wire Wire Line
	2750 1950 2750 1600
Connection ~ 2750 1600
Wire Wire Line
	2750 1600 3200 1600
Wire Wire Line
	3050 1950 3050 1800
Wire Wire Line
	3050 1800 3200 1800
$Comp
L Amplifier_Operational:TL072 U4
U 1 1 616B558C
P 2900 4050
F 0 "U4" H 2900 3683 50  0000 C CNN
F 1 "TL072" H 2900 3774 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 2900 4050 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl071.pdf" H 2900 4050 50  0001 C CNN
F 4 "X" H 2900 4050 50  0001 C CNN "Spice_Primitive"
F 5 "TL072c" H 2900 4050 50  0001 C CNN "Spice_Model"
F 6 "Y" H 2900 4050 50  0001 C CNN "Spice_Netlist_Enabled"
	1    2900 4050
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL072 U4
U 2 1 616B5595
P 4650 1800
F 0 "U4" H 4650 1433 50  0000 C CNN
F 1 "TL072" H 4650 1524 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 4650 1800 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl071.pdf" H 4650 1800 50  0001 C CNN
F 4 "X" H 4650 1800 50  0001 C CNN "Spice_Primitive"
F 5 "TL072c" H 4650 1800 50  0001 C CNN "Spice_Model"
F 6 "Y" H 4650 1800 50  0001 C CNN "Spice_Netlist_Enabled"
	2    4650 1800
	1    0    0    1   
$EndComp
$Comp
L Device:R R19
U 1 1 616B559B
P 4700 1300
F 0 "R19" V 4493 1300 50  0000 C CNN
F 1 "18k" V 4584 1300 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 4630 1300 50  0001 C CNN
F 3 "~" H 4700 1300 50  0001 C CNN
	1    4700 1300
	0    1    1    0   
$EndComp
Wire Wire Line
	5050 1300 5050 1800
Wire Wire Line
	5050 1800 4950 1800
Wire Wire Line
	4350 1700 4300 1700
$Comp
L power:GND #PWR045
U 1 1 616B55A4
P 4300 1950
F 0 "#PWR045" H 4300 1700 50  0001 C CNN
F 1 "GND" H 4305 1777 50  0000 C CNN
F 2 "" H 4300 1950 50  0001 C CNN
F 3 "" H 4300 1950 50  0001 C CNN
	1    4300 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4350 1900 4300 1900
Wire Wire Line
	4300 1900 4300 1950
Wire Wire Line
	4300 1700 4300 1300
Connection ~ 4300 1700
Wire Wire Line
	4300 1700 3800 1700
Wire Wire Line
	4300 1300 4550 1300
Wire Wire Line
	4850 1300 5050 1300
Wire Wire Line
	5150 1800 5050 1800
Connection ~ 5050 1800
$Comp
L Device:R R12
U 1 1 616B55DD
P 2000 3950
F 0 "R12" V 1793 3950 50  0000 C CNN
F 1 "330k" V 1884 3950 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 1930 3950 50  0001 C CNN
F 3 "~" H 2000 3950 50  0001 C CNN
	1    2000 3950
	0    1    1    0   
$EndComp
$Comp
L Device:C C18
U 1 1 616B55E3
P 2900 3500
F 0 "C18" V 2648 3500 50  0000 C CNN
F 1 "1n" V 2739 3500 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 2938 3350 50  0001 C CNN
F 3 "~" H 2900 3500 50  0001 C CNN
	1    2900 3500
	0    1    1    0   
$EndComp
$Comp
L Device:R R15
U 1 1 616B55F3
P 2900 2700
F 0 "R15" V 2693 2700 50  0000 C CNN
F 1 "33k" V 2784 2700 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2830 2700 50  0001 C CNN
F 3 "~" H 2900 2700 50  0001 C CNN
	1    2900 2700
	0    1    1    0   
$EndComp
$Comp
L Device:R R18
U 1 1 616B55F9
P 4100 2700
F 0 "R18" V 3893 2700 50  0000 C CNN
F 1 "1k" V 3984 2700 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 4030 2700 50  0001 C CNN
F 3 "~" H 4100 2700 50  0001 C CNN
	1    4100 2700
	0    1    1    0   
$EndComp
Wire Wire Line
	2600 3950 2550 3950
Wire Wire Line
	1850 3950 1700 3950
$Comp
L power:GND #PWR041
U 1 1 616B5601
P 2550 4200
F 0 "#PWR041" H 2550 3950 50  0001 C CNN
F 1 "GND" H 2555 4027 50  0000 C CNN
F 2 "" H 2550 4200 50  0001 C CNN
F 3 "" H 2550 4200 50  0001 C CNN
	1    2550 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	2550 4200 2550 4150
Wire Wire Line
	2550 4150 2600 4150
Wire Wire Line
	2550 2700 2750 2700
Connection ~ 2550 3950
Wire Wire Line
	2550 3950 2150 3950
Wire Wire Line
	2750 3100 2550 3100
Connection ~ 2550 3100
Wire Wire Line
	2550 3100 2550 2700
Wire Wire Line
	2550 3950 2550 3500
Wire Wire Line
	2750 3500 2550 3500
Connection ~ 2550 3500
Wire Wire Line
	2550 3500 2550 3100
Wire Wire Line
	3250 4050 3250 3500
Wire Wire Line
	3050 3100 3250 3100
Wire Wire Line
	3050 3500 3250 3500
Connection ~ 3250 3500
Wire Wire Line
	3250 3500 3250 3100
$Comp
L power:GND #PWR046
U 1 1 616B5622
P 4350 2750
F 0 "#PWR046" H 4350 2500 50  0001 C CNN
F 1 "GND" H 4355 2577 50  0000 C CNN
F 2 "" H 4350 2750 50  0001 C CNN
F 3 "" H 4350 2750 50  0001 C CNN
	1    4350 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4350 2750 4350 2700
Wire Wire Line
	3050 2700 3500 2700
Wire Wire Line
	4250 2700 4350 2700
Wire Wire Line
	3500 3850 3500 2700
Connection ~ 3500 2700
$Comp
L Device:R R17
U 1 1 616B562D
P 3800 2050
F 0 "R17" H 3870 2096 50  0000 L CNN
F 1 "6.8k" H 3870 2005 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 3730 2050 50  0001 C CNN
F 3 "~" H 3800 2050 50  0001 C CNN
	1    3800 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 1800 3800 1900
Wire Wire Line
	3800 4250 3500 4250
Wire Wire Line
	3800 2200 3800 4250
Wire Wire Line
	3500 2700 3950 2700
$Comp
L Amplifier_Operational:LM13700 U1
U 3 1 61675BFD
P 3500 1700
F 0 "U1" H 3500 2067 50  0000 C CNN
F 1 "LM13700" H 3500 1976 50  0000 C CNN
F 2 "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm" H 3200 1725 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm13700.pdf" H 3200 1725 50  0001 C CNN
	3    3500 1700
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148W D2
U 1 1 616F8EAE
P 2900 3100
F 0 "D2" H 2900 3317 50  0000 C CNN
F 1 "1N4148W" H 2900 3226 50  0000 C CNN
F 2 "Diode_SMD:D_SOD-123" H 2900 2925 50  0001 C CNN
F 3 "https://www.vishay.com/docs/85748/1n4148w.pdf" H 2900 3100 50  0001 C CNN
	1    2900 3100
	1    0    0    -1  
$EndComp
$Comp
L Transistor_BJT:MMBT3906 Q2
U 1 1 61711EF4
P 3400 4050
F 0 "Q2" H 3591 4004 50  0000 L CNN
F 1 "MMBT3906" H 3591 4095 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 3600 3975 50  0001 L CIN
F 3 "https://www.onsemi.com/pub/Collateral/2N3906-D.PDF" H 3400 4050 50  0001 L CNN
	1    3400 4050
	1    0    0    1   
$EndComp
Text HLabel 5150 1800 2    50   Input ~ 0
OUT_2
Text HLabel 1700 1600 0    50   Input ~ 0
IN_2
Text HLabel 1700 3950 0    50   Input ~ 0
CV_2
$EndSCHEMATC
