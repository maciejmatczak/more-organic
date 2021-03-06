EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L keebio-components:ProMicro U1
U 1 1 5F33BD8C
P 1800 6650
F 0 "U1" H 1800 7500 60  0000 C CNN
F 1 "ProMicro" H 1800 7400 60  0000 C CNN
F 2 "keebio-footprints:ArduinoProMicro" V 2850 4150 60  0001 C CNN
F 3 "" V 2850 4150 60  0001 C CNN
	1    1800 6650
	1    0    0    -1  
$EndComp
$Comp
L keebio-components:TRRS U2
U 1 1 5F33BD92
P 5800 7300
F 0 "U2" H 6050 7650 60  0000 L CNN
F 1 "TRRS" H 6050 7500 60  0000 L CNN
F 2 "keebio-footprints:TRRS-PJ-320A-dual" H 5950 7300 60  0001 C CNN
F 3 "" H 5950 7300 60  0001 C CNN
	1    5800 7300
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_RESET1
U 1 1 5F33BD98
P 3850 6200
F 0 "SW_RESET1" H 3850 6400 50  0000 C CNN
F 1 "MX" H 3850 5900 60  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm_H7.3mm" H 3850 6200 60  0001 C CNN
F 3 "" H 3850 6200 60  0001 C CNN
	1    3850 6200
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR01
U 1 1 5F33BD9E
P 900 1000
F 0 "#PWR01" H 900 850 50  0001 C CNN
F 1 "VCC" H 950 1200 50  0000 C CNN
F 2 "" H 900 1000 50  0001 C CNN
F 3 "" H 900 1000 50  0001 C CNN
	1    900  1000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR02
U 1 1 5F33BDA4
P 900 2000
F 0 "#PWR02" H 900 1750 50  0001 C CNN
F 1 "GND" H 950 1800 50  0000 C CNN
F 2 "" H 900 2000 50  0001 C CNN
F 3 "" H 900 2000 50  0001 C CNN
	1    900  2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	900  2000 900  1900
Wire Wire Line
	900  1000 900  1100
Text Label 900  1100 0    50   ~ 0
VCC
Text Label 900  1900 0    50   ~ 0
GND
$Comp
L power:PWR_FLAG #FLG01
U 1 1 5F33BDAE
P 900 1100
F 0 "#FLG01" H 900 1175 50  0001 C CNN
F 1 "PWR_FLAG" H 900 1300 50  0000 C CNN
F 2 "" H 900 1100 50  0001 C CNN
F 3 "~" H 900 1100 50  0001 C CNN
	1    900  1100
	-1   0    0    1   
$EndComp
$Comp
L power:PWR_FLAG #FLG02
U 1 1 5F33BDB4
P 900 1900
F 0 "#FLG02" H 900 1975 50  0001 C CNN
F 1 "PWR_FLAG" H 900 2100 50  0000 C CNN
F 2 "" H 900 1900 50  0001 C CNN
F 3 "~" H 900 1900 50  0001 C CNN
	1    900  1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 6200 2800 6200
Wire Wire Line
	2500 6300 2800 6300
Wire Wire Line
	2500 6400 2800 6400
Wire Wire Line
	2500 6700 2800 6700
Wire Wire Line
	2500 6800 2800 6800
Wire Wire Line
	2500 6900 2800 6900
Wire Wire Line
	2500 7000 2800 7000
Wire Wire Line
	2500 7100 2800 7100
Wire Wire Line
	2500 7200 2800 7200
Text Label 2800 7200 2    50   ~ 0
col0
Wire Wire Line
	1100 6400 1050 6400
Wire Wire Line
	1050 6400 1050 6300
Wire Wire Line
	1050 6300 1100 6300
Wire Wire Line
	1050 6300 800  6300
Connection ~ 1050 6300
Text Label 800  6300 0    50   ~ 0
GND
Wire Wire Line
	1100 6500 800  6500
Text Label 800  6500 0    50   ~ 0
sda
Wire Wire Line
	1100 6600 800  6600
Text Label 800  6600 0    50   ~ 0
scl_uart
NoConn ~ 1100 6100
NoConn ~ 1100 6200
NoConn ~ 1100 6700
NoConn ~ 2500 6500
NoConn ~ 2500 6100
Text Label 2800 6200 2    50   ~ 0
GND
Text Label 2800 6400 2    50   ~ 0
VCC
Text Label 2800 6300 2    50   ~ 0
rst
Text Label 2800 7100 2    50   ~ 0
col1
Text Label 2800 7000 2    50   ~ 0
col2
Text Label 2800 6900 2    50   ~ 0
col3
Text Label 2800 6800 2    50   ~ 0
col4
Text Label 2800 6700 2    50   ~ 0
col5
NoConn ~ 2500 6600
Wire Wire Line
	1100 6800 800  6800
Wire Wire Line
	1100 6900 800  6900
Wire Wire Line
	1100 7000 800  7000
Wire Wire Line
	1100 7100 800  7100
Text Label 800  6800 0    50   ~ 0
row0
Text Label 800  6900 0    50   ~ 0
row1
Text Label 800  7000 0    50   ~ 0
row2
Text Label 800  7100 0    50   ~ 0
row3
Wire Wire Line
	3650 6200 3500 6200
Text Label 3500 6200 0    50   ~ 0
rst
Wire Wire Line
	4050 6200 4250 6200
Text Label 4250 6200 2    50   ~ 0
GND
Wire Wire Line
	5100 6900 5450 6900
Text Label 5100 6900 0    50   ~ 0
GND
$Comp
L Jumper:SolderJumper_2_Open JP1
U 1 1 5F33BDEA
P 4150 6850
F 0 "JP1" H 4150 7100 50  0000 C CNN
F 1 "SolderJumper_2_Open" H 4150 7000 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 4150 6850 50  0001 C CNN
F 3 "~" H 4150 6850 50  0001 C CNN
	1    4150 6850
	1    0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_2_Open JP2
U 1 1 5F33BDF0
P 4150 7450
F 0 "JP2" H 4150 7700 50  0000 C CNN
F 1 "SolderJumper_2_Open" H 4150 7600 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 4150 7450 50  0001 C CNN
F 3 "~" H 4150 7450 50  0001 C CNN
	1    4150 7450
	1    0    0    -1  
$EndComp
Text Label 5100 7200 0    50   ~ 0
VCC
Wire Wire Line
	5450 7200 5100 7200
Wire Wire Line
	5450 7100 5100 7100
Wire Wire Line
	5450 7000 5100 7000
Text Label 5100 7000 0    50   ~ 0
scl_uart
Text Label 5100 7100 0    50   ~ 0
xtradata
$Comp
L Device:R R1
U 1 1 5F33BDFC
P 3550 6850
F 0 "R1" V 3300 6850 50  0000 C CNN
F 1 "R" V 3400 6850 50  0000 C CNN
F 2 "keebio-footprints:Resistor-Hybrid" V 3480 6850 50  0001 C CNN
F 3 "~" H 3550 6850 50  0001 C CNN
	1    3550 6850
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 5F33BE02
P 3550 7450
F 0 "R2" V 3300 7450 50  0000 C CNN
F 1 "R" V 3400 7450 50  0000 C CNN
F 2 "keebio-footprints:Resistor-Hybrid" V 3480 7450 50  0001 C CNN
F 3 "~" H 3550 7450 50  0001 C CNN
	1    3550 7450
	0    1    1    0   
$EndComp
Wire Wire Line
	3700 6850 4000 6850
Wire Wire Line
	4000 7450 3850 7450
Wire Wire Line
	4300 6850 4650 6850
Text Label 4650 6850 2    50   ~ 0
scl_uart
Text Label 4650 7450 2    50   ~ 0
xtradata
Wire Wire Line
	4300 7450 4650 7450
Wire Wire Line
	3400 6850 3150 6850
Text Label 3150 6850 0    50   ~ 0
VCC
Wire Wire Line
	3400 7450 3150 7450
Text Label 3150 7450 0    50   ~ 0
VCC
Wire Wire Line
	3850 7450 3850 7600
Wire Wire Line
	3850 7600 3150 7600
Connection ~ 3850 7450
Wire Wire Line
	3850 7450 3700 7450
Text Label 3150 7600 0    50   ~ 0
sda
$Comp
L Switch:SW_Push SW1
U 1 1 5F33BE17
P 5700 1000
F 0 "SW1" H 5700 1300 50  0000 C CNN
F 1 "SW_Push" H 5700 1200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 5700 1200 50  0001 C CNN
F 3 "~" H 5700 1200 50  0001 C CNN
	1    5700 1000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D1
U 1 1 5F33BE1D
P 5900 1150
F 0 "D1" V 5950 1250 50  0000 L CNN
F 1 "D" V 5900 1250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 5900 1150 50  0001 C CNN
F 3 "~" H 5900 1150 50  0001 C CNN
	1    5900 1150
	0    1    -1   0   
$EndComp
Wire Wire Line
	5500 1000 5400 1000
Wire Wire Line
	5900 1300 5900 1500
$Comp
L Switch:SW_Push SW2
U 1 1 5F33BE25
P 6700 1000
F 0 "SW2" H 6700 1300 50  0000 C CNN
F 1 "SW_Push" H 6700 1200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 6700 1200 50  0001 C CNN
F 3 "~" H 6700 1200 50  0001 C CNN
	1    6700 1000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D2
U 1 1 5F33BE2B
P 6900 1150
F 0 "D2" V 6950 1250 50  0000 L CNN
F 1 "D" V 6900 1250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 6900 1150 50  0001 C CNN
F 3 "~" H 6900 1150 50  0001 C CNN
	1    6900 1150
	0    1    -1   0   
$EndComp
Wire Wire Line
	6500 1000 6400 1000
Wire Wire Line
	6900 1300 6900 1500
$Comp
L Switch:SW_Push SW3
U 1 1 5F33BE33
P 7700 1000
F 0 "SW3" H 7700 1300 50  0000 C CNN
F 1 "SW_Push" H 7700 1200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 7700 1200 50  0001 C CNN
F 3 "~" H 7700 1200 50  0001 C CNN
	1    7700 1000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D3
U 1 1 5F33BE39
P 7900 1150
F 0 "D3" V 7950 1250 50  0000 L CNN
F 1 "D" V 7900 1250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 7900 1150 50  0001 C CNN
F 3 "~" H 7900 1150 50  0001 C CNN
	1    7900 1150
	0    1    -1   0   
$EndComp
Wire Wire Line
	7500 1000 7400 1000
Wire Wire Line
	7900 1300 7900 1500
$Comp
L Switch:SW_Push SW4
U 1 1 5F33BE41
P 8700 1000
F 0 "SW4" H 8700 1300 50  0000 C CNN
F 1 "SW_Push" H 8700 1200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 8700 1200 50  0001 C CNN
F 3 "~" H 8700 1200 50  0001 C CNN
	1    8700 1000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D4
U 1 1 5F33BE47
P 8900 1150
F 0 "D4" V 8950 1250 50  0000 L CNN
F 1 "D" V 8900 1250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 8900 1150 50  0001 C CNN
F 3 "~" H 8900 1150 50  0001 C CNN
	1    8900 1150
	0    1    -1   0   
$EndComp
Wire Wire Line
	8500 1000 8400 1000
Wire Wire Line
	8900 1300 8900 1500
$Comp
L Switch:SW_Push SW5
U 1 1 5F33BE4F
P 9700 1000
F 0 "SW5" H 9700 1300 50  0000 C CNN
F 1 "SW_Push" H 9700 1200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 9700 1200 50  0001 C CNN
F 3 "~" H 9700 1200 50  0001 C CNN
	1    9700 1000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D5
U 1 1 5F33BE55
P 9900 1150
F 0 "D5" V 9950 1250 50  0000 L CNN
F 1 "D" V 9900 1250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 9900 1150 50  0001 C CNN
F 3 "~" H 9900 1150 50  0001 C CNN
	1    9900 1150
	0    1    -1   0   
$EndComp
Wire Wire Line
	9500 1000 9400 1000
Wire Wire Line
	9900 1300 9900 1500
$Comp
L Switch:SW_Push SW6
U 1 1 5F33BE5D
P 10700 1000
F 0 "SW6" H 10700 1300 50  0000 C CNN
F 1 "SW_Push" H 10700 1200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 10700 1200 50  0001 C CNN
F 3 "~" H 10700 1200 50  0001 C CNN
	1    10700 1000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D6
U 1 1 5F33BE63
P 10900 1150
F 0 "D6" V 10950 1250 50  0000 L CNN
F 1 "D" V 10900 1250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 10900 1150 50  0001 C CNN
F 3 "~" H 10900 1150 50  0001 C CNN
	1    10900 1150
	0    1    -1   0   
$EndComp
Wire Wire Line
	10500 1000 10400 1000
Wire Wire Line
	10900 1300 10900 1500
$Comp
L Switch:SW_Push SW7
U 1 1 5F33BE6B
P 5700 2000
F 0 "SW7" H 5700 2300 50  0000 C CNN
F 1 "SW_Push" H 5700 2200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 5700 2200 50  0001 C CNN
F 3 "~" H 5700 2200 50  0001 C CNN
	1    5700 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D7
U 1 1 5F33BE71
P 5900 2150
F 0 "D7" V 5950 2250 50  0000 L CNN
F 1 "D" V 5900 2250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 5900 2150 50  0001 C CNN
F 3 "~" H 5900 2150 50  0001 C CNN
	1    5900 2150
	0    1    -1   0   
$EndComp
Wire Wire Line
	5500 2000 5400 2000
Wire Wire Line
	5900 2300 5900 2500
$Comp
L Switch:SW_Push SW8
U 1 1 5F33BE79
P 6700 2000
F 0 "SW8" H 6700 2300 50  0000 C CNN
F 1 "SW_Push" H 6700 2200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 6700 2200 50  0001 C CNN
F 3 "~" H 6700 2200 50  0001 C CNN
	1    6700 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D8
U 1 1 5F33BE7F
P 6900 2150
F 0 "D8" V 6950 2250 50  0000 L CNN
F 1 "D" V 6900 2250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 6900 2150 50  0001 C CNN
F 3 "~" H 6900 2150 50  0001 C CNN
	1    6900 2150
	0    1    -1   0   
$EndComp
Wire Wire Line
	6500 2000 6400 2000
Wire Wire Line
	6900 2300 6900 2500
$Comp
L Switch:SW_Push SW9
U 1 1 5F33BE87
P 7700 2000
F 0 "SW9" H 7700 2300 50  0000 C CNN
F 1 "SW_Push" H 7700 2200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 7700 2200 50  0001 C CNN
F 3 "~" H 7700 2200 50  0001 C CNN
	1    7700 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D9
U 1 1 5F33BE8D
P 7900 2150
F 0 "D9" V 7950 2250 50  0000 L CNN
F 1 "D" V 7900 2250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 7900 2150 50  0001 C CNN
F 3 "~" H 7900 2150 50  0001 C CNN
	1    7900 2150
	0    1    -1   0   
$EndComp
Wire Wire Line
	7500 2000 7400 2000
Wire Wire Line
	7900 2300 7900 2500
$Comp
L Switch:SW_Push SW10
U 1 1 5F33BE95
P 8700 2000
F 0 "SW10" H 8700 2300 50  0000 C CNN
F 1 "SW_Push" H 8700 2200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 8700 2200 50  0001 C CNN
F 3 "~" H 8700 2200 50  0001 C CNN
	1    8700 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D10
U 1 1 5F33BE9B
P 8900 2150
F 0 "D10" V 8950 2250 50  0000 L CNN
F 1 "D" V 8900 2250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 8900 2150 50  0001 C CNN
F 3 "~" H 8900 2150 50  0001 C CNN
	1    8900 2150
	0    1    -1   0   
$EndComp
Wire Wire Line
	8500 2000 8400 2000
Wire Wire Line
	8900 2300 8900 2500
$Comp
L Switch:SW_Push SW11
U 1 1 5F33BEA3
P 9700 2000
F 0 "SW11" H 9700 2300 50  0000 C CNN
F 1 "SW_Push" H 9700 2200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 9700 2200 50  0001 C CNN
F 3 "~" H 9700 2200 50  0001 C CNN
	1    9700 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D11
U 1 1 5F33BEA9
P 9900 2150
F 0 "D11" V 9950 2250 50  0000 L CNN
F 1 "D" V 9900 2250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 9900 2150 50  0001 C CNN
F 3 "~" H 9900 2150 50  0001 C CNN
	1    9900 2150
	0    1    -1   0   
$EndComp
Wire Wire Line
	9500 2000 9400 2000
Wire Wire Line
	9900 2300 9900 2500
$Comp
L Switch:SW_Push SW12
U 1 1 5F33BEB1
P 10700 2000
F 0 "SW12" H 10700 2300 50  0000 C CNN
F 1 "SW_Push" H 10700 2200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 10700 2200 50  0001 C CNN
F 3 "~" H 10700 2200 50  0001 C CNN
	1    10700 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D12
U 1 1 5F33BEB7
P 10900 2150
F 0 "D12" V 10950 2250 50  0000 L CNN
F 1 "D" V 10900 2250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 10900 2150 50  0001 C CNN
F 3 "~" H 10900 2150 50  0001 C CNN
	1    10900 2150
	0    1    -1   0   
$EndComp
Wire Wire Line
	10500 2000 10400 2000
Wire Wire Line
	10900 2300 10900 2500
Wire Wire Line
	10900 1500 9900 1500
Connection ~ 6900 1500
Wire Wire Line
	6900 1500 5900 1500
Connection ~ 7900 1500
Wire Wire Line
	7900 1500 6900 1500
Connection ~ 8900 1500
Wire Wire Line
	8900 1500 7900 1500
Connection ~ 9900 1500
Wire Wire Line
	9900 1500 8900 1500
Wire Wire Line
	5900 1500 5700 1500
Connection ~ 5900 1500
$Comp
L Switch:SW_Push SW13
U 1 1 5F33BECA
P 5700 3000
F 0 "SW13" H 5700 3300 50  0000 C CNN
F 1 "SW_Push" H 5700 3200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 5700 3200 50  0001 C CNN
F 3 "~" H 5700 3200 50  0001 C CNN
	1    5700 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D13
U 1 1 5F33BED0
P 5900 3150
F 0 "D13" V 5950 3250 50  0000 L CNN
F 1 "D" V 5900 3250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 5900 3150 50  0001 C CNN
F 3 "~" H 5900 3150 50  0001 C CNN
	1    5900 3150
	0    1    -1   0   
$EndComp
Wire Wire Line
	5500 3000 5400 3000
Wire Wire Line
	5900 3300 5900 3500
$Comp
L Switch:SW_Push SW14
U 1 1 5F33BED8
P 6700 3000
F 0 "SW14" H 6700 3300 50  0000 C CNN
F 1 "SW_Push" H 6700 3200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 6700 3200 50  0001 C CNN
F 3 "~" H 6700 3200 50  0001 C CNN
	1    6700 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D14
U 1 1 5F33BEDE
P 6900 3150
F 0 "D14" V 6950 3250 50  0000 L CNN
F 1 "D" V 6900 3250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 6900 3150 50  0001 C CNN
F 3 "~" H 6900 3150 50  0001 C CNN
	1    6900 3150
	0    1    -1   0   
$EndComp
Wire Wire Line
	6500 3000 6400 3000
Wire Wire Line
	6900 3300 6900 3500
$Comp
L Switch:SW_Push SW15
U 1 1 5F33BEE6
P 7700 3000
F 0 "SW15" H 7700 3300 50  0000 C CNN
F 1 "SW_Push" H 7700 3200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 7700 3200 50  0001 C CNN
F 3 "~" H 7700 3200 50  0001 C CNN
	1    7700 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D15
U 1 1 5F33BEEC
P 7900 3150
F 0 "D15" V 7950 3250 50  0000 L CNN
F 1 "D" V 7900 3250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 7900 3150 50  0001 C CNN
F 3 "~" H 7900 3150 50  0001 C CNN
	1    7900 3150
	0    1    -1   0   
$EndComp
Wire Wire Line
	7500 3000 7400 3000
Wire Wire Line
	7900 3300 7900 3500
$Comp
L Switch:SW_Push SW16
U 1 1 5F33BEF4
P 8700 3000
F 0 "SW16" H 8700 3300 50  0000 C CNN
F 1 "SW_Push" H 8700 3200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 8700 3200 50  0001 C CNN
F 3 "~" H 8700 3200 50  0001 C CNN
	1    8700 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D16
U 1 1 5F33BEFA
P 8900 3150
F 0 "D16" V 8950 3250 50  0000 L CNN
F 1 "D" V 8900 3250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 8900 3150 50  0001 C CNN
F 3 "~" H 8900 3150 50  0001 C CNN
	1    8900 3150
	0    1    -1   0   
$EndComp
Wire Wire Line
	8500 3000 8400 3000
Wire Wire Line
	8900 3300 8900 3500
$Comp
L Switch:SW_Push SW17
U 1 1 5F33BF02
P 9700 3000
F 0 "SW17" H 9700 3300 50  0000 C CNN
F 1 "SW_Push" H 9700 3200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 9700 3200 50  0001 C CNN
F 3 "~" H 9700 3200 50  0001 C CNN
	1    9700 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D17
U 1 1 5F33BF08
P 9900 3150
F 0 "D17" V 9950 3250 50  0000 L CNN
F 1 "D" V 9900 3250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 9900 3150 50  0001 C CNN
F 3 "~" H 9900 3150 50  0001 C CNN
	1    9900 3150
	0    1    -1   0   
$EndComp
Wire Wire Line
	9500 3000 9400 3000
Wire Wire Line
	9900 3300 9900 3500
$Comp
L Switch:SW_Push SW18
U 1 1 5F33BF10
P 10700 3000
F 0 "SW18" H 10700 3300 50  0000 C CNN
F 1 "SW_Push" H 10700 3200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 10700 3200 50  0001 C CNN
F 3 "~" H 10700 3200 50  0001 C CNN
	1    10700 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D18
U 1 1 5F33BF16
P 10900 3150
F 0 "D18" V 10950 3250 50  0000 L CNN
F 1 "D" V 10900 3250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 10900 3150 50  0001 C CNN
F 3 "~" H 10900 3150 50  0001 C CNN
	1    10900 3150
	0    1    -1   0   
$EndComp
Wire Wire Line
	10500 3000 10400 3000
Wire Wire Line
	10900 3300 10900 3500
$Comp
L Switch:SW_Push SW19
U 1 1 5F33BF1E
P 5700 4000
F 0 "SW19" H 5700 4300 50  0000 C CNN
F 1 "SW_Push" H 5700 4200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 5700 4200 50  0001 C CNN
F 3 "~" H 5700 4200 50  0001 C CNN
	1    5700 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D19
U 1 1 5F33BF24
P 5900 4150
F 0 "D19" V 5950 4250 50  0000 L CNN
F 1 "D" V 5900 4250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 5900 4150 50  0001 C CNN
F 3 "~" H 5900 4150 50  0001 C CNN
	1    5900 4150
	0    1    -1   0   
$EndComp
Wire Wire Line
	5500 4000 5400 4000
Wire Wire Line
	5900 4300 5900 4500
$Comp
L Switch:SW_Push SW20
U 1 1 5F33BF2C
P 6700 4000
F 0 "SW20" H 6700 4300 50  0000 C CNN
F 1 "SW_Push" H 6700 4200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 6700 4200 50  0001 C CNN
F 3 "~" H 6700 4200 50  0001 C CNN
	1    6700 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D20
U 1 1 5F33BF32
P 6900 4150
F 0 "D20" V 6950 4250 50  0000 L CNN
F 1 "D" V 6900 4250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 6900 4150 50  0001 C CNN
F 3 "~" H 6900 4150 50  0001 C CNN
	1    6900 4150
	0    1    -1   0   
$EndComp
Wire Wire Line
	6500 4000 6400 4000
Wire Wire Line
	6900 4300 6900 4500
$Comp
L Switch:SW_Push SW21
U 1 1 5F33BF3A
P 7700 4000
F 0 "SW21" H 7700 4300 50  0000 C CNN
F 1 "SW_Push" H 7700 4200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 7700 4200 50  0001 C CNN
F 3 "~" H 7700 4200 50  0001 C CNN
	1    7700 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D21
U 1 1 5F33BF40
P 7900 4150
F 0 "D21" V 7950 4250 50  0000 L CNN
F 1 "D" V 7900 4250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 7900 4150 50  0001 C CNN
F 3 "~" H 7900 4150 50  0001 C CNN
	1    7900 4150
	0    1    -1   0   
$EndComp
Wire Wire Line
	7500 4000 7400 4000
Wire Wire Line
	7900 4300 7900 4500
$Comp
L Switch:SW_Push SW22
U 1 1 5F33BF48
P 8700 4000
F 0 "SW22" H 8700 4300 50  0000 C CNN
F 1 "SW_Push" H 8700 4200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 8700 4200 50  0001 C CNN
F 3 "~" H 8700 4200 50  0001 C CNN
	1    8700 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D22
U 1 1 5F33BF4E
P 8900 4150
F 0 "D22" V 8950 4250 50  0000 L CNN
F 1 "D" V 8900 4250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 8900 4150 50  0001 C CNN
F 3 "~" H 8900 4150 50  0001 C CNN
	1    8900 4150
	0    1    -1   0   
$EndComp
Wire Wire Line
	8500 4000 8400 4000
Wire Wire Line
	8900 4300 8900 4500
$Comp
L Switch:SW_Push SW23
U 1 1 5F33BF56
P 9700 4000
F 0 "SW23" H 9700 4300 50  0000 C CNN
F 1 "SW_Push" H 9700 4200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 9700 4200 50  0001 C CNN
F 3 "~" H 9700 4200 50  0001 C CNN
	1    9700 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D23
U 1 1 5F33BF5C
P 9900 4150
F 0 "D23" V 9950 4250 50  0000 L CNN
F 1 "D" V 9900 4250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 9900 4150 50  0001 C CNN
F 3 "~" H 9900 4150 50  0001 C CNN
	1    9900 4150
	0    1    -1   0   
$EndComp
Wire Wire Line
	9500 4000 9400 4000
Wire Wire Line
	9900 4300 9900 4500
$Comp
L Switch:SW_Push SW24
U 1 1 5F33BF64
P 10700 4000
F 0 "SW24" H 10700 4300 50  0000 C CNN
F 1 "SW_Push" H 10700 4200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 10700 4200 50  0001 C CNN
F 3 "~" H 10700 4200 50  0001 C CNN
	1    10700 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D24
U 1 1 5F33BF6A
P 10900 4150
F 0 "D24" V 10950 4250 50  0000 L CNN
F 1 "D" V 10900 4250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 10900 4150 50  0001 C CNN
F 3 "~" H 10900 4150 50  0001 C CNN
	1    10900 4150
	0    1    -1   0   
$EndComp
Wire Wire Line
	10500 4000 10400 4000
Wire Wire Line
	10900 4300 10900 4500
$Comp
L Switch:SW_Push SW25
U 1 1 5F33BF72
P 5700 5000
F 0 "SW25" H 5700 5300 50  0000 C CNN
F 1 "SW_Push" H 5700 5200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 5700 5200 50  0001 C CNN
F 3 "~" H 5700 5200 50  0001 C CNN
	1    5700 5000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D25
U 1 1 5F33BF78
P 5900 5150
F 0 "D25" V 5950 5250 50  0000 L CNN
F 1 "D" V 5900 5250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 5900 5150 50  0001 C CNN
F 3 "~" H 5900 5150 50  0001 C CNN
	1    5900 5150
	0    1    -1   0   
$EndComp
Wire Wire Line
	5500 5000 5400 5000
Wire Wire Line
	5900 5300 5900 5500
$Comp
L Switch:SW_Push SW26
U 1 1 5F33BF80
P 6700 5000
F 0 "SW26" H 6700 5300 50  0000 C CNN
F 1 "SW_Push" H 6700 5200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 6700 5200 50  0001 C CNN
F 3 "~" H 6700 5200 50  0001 C CNN
	1    6700 5000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D26
U 1 1 5F33BF86
P 6900 5150
F 0 "D26" V 6950 5250 50  0000 L CNN
F 1 "D" V 6900 5250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 6900 5150 50  0001 C CNN
F 3 "~" H 6900 5150 50  0001 C CNN
	1    6900 5150
	0    1    -1   0   
$EndComp
Wire Wire Line
	6500 5000 6400 5000
Wire Wire Line
	6900 5300 6900 5500
$Comp
L Switch:SW_Push SW27
U 1 1 5F33BF8E
P 7700 5000
F 0 "SW27" H 7700 5300 50  0000 C CNN
F 1 "SW_Push" H 7700 5200 50  0000 C CNN
F 2 "keyswitches:Kailh_socket_MX_optional_reversible_alt" H 7700 5200 50  0001 C CNN
F 3 "~" H 7700 5200 50  0001 C CNN
	1    7700 5000
	1    0    0    -1  
$EndComp
$Comp
L Device:D D27
U 1 1 5F33BF94
P 7900 5150
F 0 "D27" V 7950 5250 50  0000 L CNN
F 1 "D" V 7900 5250 50  0000 L CNN
F 2 "keebio-footprints:Diode-dual" H 7900 5150 50  0001 C CNN
F 3 "~" H 7900 5150 50  0001 C CNN
	1    7900 5150
	0    1    -1   0   
$EndComp
Wire Wire Line
	7500 5000 7400 5000
Wire Wire Line
	7900 5300 7900 5500
Wire Wire Line
	10900 2500 9900 2500
Connection ~ 6900 2500
Wire Wire Line
	6900 2500 5900 2500
Connection ~ 7900 2500
Wire Wire Line
	7900 2500 6900 2500
Connection ~ 8900 2500
Wire Wire Line
	8900 2500 7900 2500
Connection ~ 9900 2500
Wire Wire Line
	9900 2500 8900 2500
Wire Wire Line
	5900 2500 5700 2500
Connection ~ 5900 2500
Wire Wire Line
	10900 3500 9900 3500
Connection ~ 5900 3500
Wire Wire Line
	5900 3500 5700 3500
Connection ~ 6900 3500
Wire Wire Line
	6900 3500 5900 3500
Connection ~ 7900 3500
Wire Wire Line
	7900 3500 6900 3500
Connection ~ 8900 3500
Wire Wire Line
	8900 3500 7900 3500
Connection ~ 9900 3500
Wire Wire Line
	9900 3500 8900 3500
Wire Wire Line
	10900 4500 9900 4500
Connection ~ 5900 4500
Wire Wire Line
	5900 4500 5700 4500
Connection ~ 6900 4500
Wire Wire Line
	6900 4500 5900 4500
Connection ~ 7900 4500
Wire Wire Line
	7900 4500 6900 4500
Connection ~ 8900 4500
Wire Wire Line
	8900 4500 7900 4500
Connection ~ 9900 4500
Wire Wire Line
	9900 4500 8900 4500
Connection ~ 5900 5500
Wire Wire Line
	5900 5500 5700 5500
Connection ~ 6900 5500
Wire Wire Line
	6900 5500 5900 5500
Wire Wire Line
	7900 5500 6900 5500
Wire Wire Line
	5400 5000 5400 4000
Connection ~ 5400 2000
Wire Wire Line
	5400 2000 5400 1000
Connection ~ 5400 3000
Wire Wire Line
	5400 3000 5400 2000
Connection ~ 5400 4000
Wire Wire Line
	5400 4000 5400 3000
Wire Wire Line
	5200 1000 5400 1000
Connection ~ 5400 1000
Wire Wire Line
	6400 1000 6400 2000
Connection ~ 6400 2000
Wire Wire Line
	6400 2000 6400 3000
Connection ~ 6400 3000
Wire Wire Line
	6400 3000 6400 4000
Connection ~ 6400 4000
Wire Wire Line
	6400 4000 6400 5000
Wire Wire Line
	7400 5000 7400 4000
Connection ~ 7400 2000
Wire Wire Line
	7400 2000 7400 1000
Connection ~ 7400 3000
Wire Wire Line
	7400 3000 7400 2000
Connection ~ 7400 4000
Wire Wire Line
	7400 4000 7400 3000
Wire Wire Line
	8400 1000 8400 2000
Connection ~ 8400 2000
Wire Wire Line
	8400 2000 8400 3000
Connection ~ 8400 3000
Wire Wire Line
	8400 3000 8400 4000
Connection ~ 9400 2000
Wire Wire Line
	9400 2000 9400 1000
Connection ~ 9400 3000
Wire Wire Line
	9400 3000 9400 2000
Wire Wire Line
	9400 4000 9400 3000
Wire Wire Line
	10400 1000 10400 2000
Connection ~ 10400 2000
Wire Wire Line
	10400 2000 10400 3000
Connection ~ 10400 3000
Wire Wire Line
	10400 3000 10400 4000
Wire Wire Line
	10400 1000 10200 1000
Connection ~ 10400 1000
Wire Wire Line
	9400 1000 9200 1000
Connection ~ 9400 1000
Wire Wire Line
	8400 1000 8200 1000
Connection ~ 8400 1000
Wire Wire Line
	7400 1000 7200 1000
Connection ~ 7400 1000
Wire Wire Line
	6400 1000 6200 1000
Connection ~ 6400 1000
Text Label 5200 1000 0    50   ~ 0
col0
Text Label 6200 1000 0    50   ~ 0
col1
Text Label 7200 1000 0    50   ~ 0
col2
Text Label 8200 1000 0    50   ~ 0
col3
Text Label 9200 1000 0    50   ~ 0
col4
Text Label 10200 1000 0    50   ~ 0
col5
Text Label 5700 1500 0    50   ~ 0
row0
Text Label 5700 2500 0    50   ~ 0
row1
Text Label 5700 3500 0    50   ~ 0
row2
Text Label 5700 4500 0    50   ~ 0
row3
Text Label 5700 5500 0    50   ~ 0
row4
Text Label 800  7200 0    50   ~ 0
row4
Wire Wire Line
	800  7200 1100 7200
$EndSCHEMATC
