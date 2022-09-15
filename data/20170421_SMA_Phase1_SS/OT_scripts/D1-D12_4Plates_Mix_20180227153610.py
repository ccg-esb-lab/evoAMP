

###################################################################################
#
# SCRIPT GENERATED ON 27/02/2018 FROM THE FOLLOWING LAYOUT FILES:
#  fileDictName=layouts/EvoAMP_key_dict.txt
#  fileTroughName=layouts/EvoAmp_trough.txt
#  fileLayoutName=layouts/EvoAmp_layout_4plates_Mix.txt
#
###################################################################################
from opentrons import Robot
from opentrons import containers, instruments
from itertools import chain

robot = Robot()

p200rack = containers.load('tiprack-200ul', 'A2', 'tiprack')
trough = containers.load('tube-rack-15_50ml','A1','trough')
for tube in trough:
	tube.properties['height']+=50
plate1 = containers.load('96-PCR-flat','B1','plate-1')
plate2 = containers.load('96-PCR-flat','B2','plate-2')
plate3 = containers.load('96-PCR-flat','C1','plate-3')
plate4 = containers.load('96-PCR-flat','C2','plate-4')
trash = containers.load('point','D2','trash')
p200 = instruments.Pipette(name='p200',trash_container=trash,tip_racks=[p200rack],min_volume=18,axis='b',channels=1)

p200.set_max_volume(180)

p200.pick_up_tip(p200rack['0'])
p200.move_to(plate1[0].bottom(), 'arc')
p200.move_to(plate1[95].bottom(), 'arc')
p200.move_to(plate2[0].bottom(), 'arc')
p200.move_to(plate2[95].bottom(), 'arc')
p200.move_to(plate3[0].bottom(), 'arc')
p200.move_to(plate3[95].bottom(), 'arc')
p200.move_to(plate4[0].bottom(), 'arc')
p200.move_to(plate4[95].bottom(), 'arc')

# *********** Dispense M

p200.aspirate(174, trough['A3'].bottom(90))
p200.dispense(29, plate1[64].top(-2)).touch_tip() #1 <Slot B1><Well A9>
p200.dispense(29, plate1[65].top(-2)).touch_tip() #2: <Slot B1><Well B9>
p200.dispense(29, plate1[66].top(-2)).touch_tip() #3: <Slot B1><Well C9>
p200.dispense(29, plate1[67].top(-2)).touch_tip() #4: <Slot B1><Well D9>
p200.dispense(29, plate1[68].top(-2)).touch_tip() #5: <Slot B1><Well E9>
p200.dispense(29, plate1[69].top(-2)).touch_tip() #6: <Slot B1><Well F9>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(29, plate1[70].top(-2)).touch_tip() #7: <Slot B1><Well G9>
p200.dispense(29, plate1[71].top(-2)).touch_tip() #8: <Slot B1><Well H9>
p200.dispense(58, plate1[56].top(-2)).touch_tip() #9: <Slot B1><Well A8>
p200.dispense(58, plate1[57].top(-2)).touch_tip() #10: <Slot B1><Well B8>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(58, plate1[58].top(-2)).touch_tip() #11: <Slot B1><Well C8>
p200.dispense(58, plate1[59].top(-2)).touch_tip() #12: <Slot B1><Well D8>
p200.dispense(58, plate1[60].top(-2)).touch_tip() #13: <Slot B1><Well E8>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(58, plate1[61].top(-2)).touch_tip() #14: <Slot B1><Well F8>
p200.dispense(58, plate1[62].top(-2)).touch_tip() #15: <Slot B1><Well G8>
p200.dispense(58, plate1[63].top(-2)).touch_tip() #16: <Slot B1><Well H8>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[48].top(-2)).touch_tip() #17: <Slot B1><Well A7>
p200.dispense(86, plate1[49].top(-2)).touch_tip() #18: <Slot B1><Well B7>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[50].top(-2)).touch_tip() #19: <Slot B1><Well C7>
p200.dispense(86, plate1[51].top(-2)).touch_tip() #20: <Slot B1><Well D7>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[52].top(-2)).touch_tip() #21: <Slot B1><Well E7>
p200.dispense(86, plate1[53].top(-2)).touch_tip() #22: <Slot B1><Well F7>

p200.aspirate(172, trough['A3'].bottom(87))
p200.dispense(86, plate1[54].top(-2)).touch_tip() #23: <Slot B1><Well G7>
p200.dispense(86, plate1[55].top(-2)).touch_tip() #24: <Slot B1><Well H7>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[40].top(-2)).touch_tip() #25: <Slot B1><Well A6>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[41].top(-2)).touch_tip() #26: <Slot B1><Well B6>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[42].top(-2)).touch_tip() #27: <Slot B1><Well C6>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[43].top(-2)).touch_tip() #28: <Slot B1><Well D6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[44].top(-2)).touch_tip() #29: <Slot B1><Well E6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[45].top(-2)).touch_tip() #30: <Slot B1><Well F6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[46].top(-2)).touch_tip() #31: <Slot B1><Well G6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[47].top(-2)).touch_tip() #32: <Slot B1><Well H6>

p200.aspirate(144, trough['A3'].bottom(85))
p200.dispense(144, plate1[32].top(-2)).touch_tip() #33: <Slot B1><Well A5>

p200.aspirate(144, trough['A3'].bottom(85))
p200.dispense(144, plate1[33].top(-2)).touch_tip() #34: <Slot B1><Well B5>

p200.aspirate(144, trough['A3'].bottom(85))
p200.dispense(144, plate1[34].top(-2)).touch_tip() #35: <Slot B1><Well C5>

p200.aspirate(144, trough['A3'].bottom(85))
p200.dispense(144, plate1[35].top(-2)).touch_tip() #36: <Slot B1><Well D5>

p200.aspirate(144, trough['A3'].bottom(84))
p200.dispense(144, plate1[36].top(-2)).touch_tip() #37: <Slot B1><Well E5>

p200.aspirate(144, trough['A3'].bottom(84))
p200.dispense(144, plate1[37].top(-2)).touch_tip() #38: <Slot B1><Well F5>

p200.aspirate(144, trough['A3'].bottom(84))
p200.dispense(144, plate1[38].top(-2)).touch_tip() #39: <Slot B1><Well G5>

p200.aspirate(144, trough['A3'].bottom(84))
p200.dispense(144, plate1[39].top(-2)).touch_tip() #40: <Slot B1><Well H5>

p200.aspirate(147, trough['A3'].bottom(83))
p200.dispense(147, plate1[88].top(-2)).touch_tip() #41: <Slot B1><Well A12>

p200.aspirate(147, trough['A3'].bottom(83))
p200.dispense(147, plate1[89].top(-2)).touch_tip() #42: <Slot B1><Well B12>

p200.aspirate(147, trough['A3'].bottom(83))
p200.dispense(147, plate1[90].top(-2)).touch_tip() #43: <Slot B1><Well C12>

p200.aspirate(147, trough['A3'].bottom(83))
p200.dispense(147, plate1[91].top(-2)).touch_tip() #44: <Slot B1><Well D12>

p200.aspirate(147, trough['A3'].bottom(82))
p200.dispense(147, plate1[92].top(-2)).touch_tip() #45: <Slot B1><Well E12>

p200.aspirate(147, trough['A3'].bottom(82))
p200.dispense(147, plate1[93].top(-2)).touch_tip() #46: <Slot B1><Well F12>

p200.aspirate(147, trough['A3'].bottom(82))
p200.dispense(147, plate1[94].top(-2)).touch_tip() #47: <Slot B1><Well G12>

p200.aspirate(147, trough['A3'].bottom(81))
p200.dispense(147, plate1[95].top(-2)).touch_tip() #48: <Slot B1><Well H12>

p200.aspirate(154, trough['A3'].bottom(81))
p200.dispense(154, plate1[80].top(-2)).touch_tip() #49: <Slot B1><Well A11>

p200.aspirate(154, trough['A3'].bottom(81))
p200.dispense(154, plate1[81].top(-2)).touch_tip() #50: <Slot B1><Well B11>

p200.aspirate(154, trough['A3'].bottom(81))
p200.dispense(154, plate1[82].top(-2)).touch_tip() #51: <Slot B1><Well C11>

p200.aspirate(154, trough['A3'].bottom(80))
p200.dispense(154, plate1[83].top(-2)).touch_tip() #52: <Slot B1><Well D11>

p200.aspirate(154, trough['A3'].bottom(80))
p200.dispense(154, plate1[84].top(-2)).touch_tip() #53: <Slot B1><Well E11>

p200.aspirate(154, trough['A3'].bottom(80))
p200.dispense(154, plate1[85].top(-2)).touch_tip() #54: <Slot B1><Well F11>

p200.aspirate(154, trough['A3'].bottom(80))
p200.dispense(154, plate1[86].top(-2)).touch_tip() #55: <Slot B1><Well G11>

p200.aspirate(154, trough['A3'].bottom(79))
p200.dispense(154, plate1[87].top(-2)).touch_tip() #56: <Slot B1><Well H11>

p200.aspirate(160, trough['A3'].bottom(79))
p200.dispense(160, plate1[72].top(-2)).touch_tip() #57: <Slot B1><Well A10>

p200.aspirate(160, trough['A3'].bottom(79))
p200.dispense(160, plate1[73].top(-2)).touch_tip() #58: <Slot B1><Well B10>

p200.aspirate(160, trough['A3'].bottom(78))
p200.dispense(160, plate1[74].top(-2)).touch_tip() #59: <Slot B1><Well C10>

p200.aspirate(160, trough['A3'].bottom(78))
p200.dispense(160, plate1[75].top(-2)).touch_tip() #60: <Slot B1><Well D10>

p200.aspirate(160, trough['A3'].bottom(78))
p200.dispense(160, plate1[76].top(-2)).touch_tip() #61: <Slot B1><Well E10>

p200.aspirate(160, trough['A3'].bottom(78))
p200.dispense(160, plate1[77].top(-2)).touch_tip() #62: <Slot B1><Well F10>

p200.aspirate(160, trough['A3'].bottom(77))
p200.dispense(160, plate1[78].top(-2)).touch_tip() #63: <Slot B1><Well G10>

p200.aspirate(160, trough['A3'].bottom(77))
p200.dispense(160, plate1[79].top(-2)).touch_tip() #64: <Slot B1><Well H10>

p200.aspirate(162, trough['A3'].bottom(77))
p200.dispense(162, plate1[24].top(-2)).touch_tip() #65: <Slot B1><Well A4>

p200.aspirate(162, trough['A3'].bottom(76))
p200.dispense(162, plate1[25].top(-2)).touch_tip() #66: <Slot B1><Well B4>

p200.aspirate(162, trough['A3'].bottom(76))
p200.dispense(162, plate1[26].top(-2)).touch_tip() #67: <Slot B1><Well C4>

p200.aspirate(162, trough['A3'].bottom(76))
p200.dispense(162, plate1[27].top(-2)).touch_tip() #68: <Slot B1><Well D4>

p200.aspirate(162, trough['A3'].bottom(75))
p200.dispense(162, plate1[28].top(-2)).touch_tip() #69: <Slot B1><Well E4>

p200.aspirate(162, trough['A3'].bottom(75))
p200.dispense(162, plate1[29].top(-2)).touch_tip() #70: <Slot B1><Well F4>

p200.aspirate(162, trough['A3'].bottom(75))
p200.dispense(162, plate1[30].top(-2)).touch_tip() #71: <Slot B1><Well G4>

p200.aspirate(162, trough['A3'].bottom(75))
p200.dispense(162, plate1[31].top(-2)).touch_tip() #72: <Slot B1><Well H4>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[0].top(-2)).touch_tip() #73: <Slot B1><Well A1>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[8].top(-2)).touch_tip() #74: <Slot B1><Well A2>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[16].top(-2)).touch_tip() #75: <Slot B1><Well A3>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[1].top(-2)).touch_tip() #76: <Slot B1><Well B1>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[9].top(-2)).touch_tip() #77: <Slot B1><Well B2>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[17].top(-2)).touch_tip() #78: <Slot B1><Well B3>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[2].top(-2)).touch_tip() #79: <Slot B1><Well C1>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[10].top(-2)).touch_tip() #80: <Slot B1><Well C2>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[18].top(-2)).touch_tip() #81: <Slot B1><Well C3>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[3].top(-2)).touch_tip() #82: <Slot B1><Well D1>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[11].top(-2)).touch_tip() #83: <Slot B1><Well D2>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[19].top(-2)).touch_tip() #84: <Slot B1><Well D3>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[4].top(-2)).touch_tip() #85: <Slot B1><Well E1>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[12].top(-2)).touch_tip() #86: <Slot B1><Well E2>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[20].top(-2)).touch_tip() #87: <Slot B1><Well E3>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[5].top(-2)).touch_tip() #88: <Slot B1><Well F1>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[13].top(-2)).touch_tip() #89: <Slot B1><Well F2>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[21].top(-2)).touch_tip() #90: <Slot B1><Well F3>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[6].top(-2)).touch_tip() #91: <Slot B1><Well G1>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[14].top(-2)).touch_tip() #92: <Slot B1><Well G2>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[22].top(-2)).touch_tip() #93: <Slot B1><Well G3>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[7].top(-2)).touch_tip() #94: <Slot B1><Well H1>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[15].top(-2)).touch_tip() #95: <Slot B1><Well H2>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[23].top(-2)).touch_tip() #96: <Slot B1><Well H3>

p200.aspirate(174, trough['A3'].bottom(67))
p200.dispense(29, plate2[64].top(-2)).touch_tip() #97: <Slot B2><Well A9>
p200.dispense(29, plate2[65].top(-2)).touch_tip() #98: <Slot B2><Well B9>
p200.dispense(29, plate2[66].top(-2)).touch_tip() #99: <Slot B2><Well C9>
p200.dispense(29, plate2[67].top(-2)).touch_tip() #100: <Slot B2><Well D9>
p200.dispense(29, plate2[68].top(-2)).touch_tip() #101: <Slot B2><Well E9>
p200.dispense(29, plate2[69].top(-2)).touch_tip() #102: <Slot B2><Well F9>

p200.aspirate(174, trough['A3'].bottom(66))
p200.dispense(29, plate2[70].top(-2)).touch_tip() #103: <Slot B2><Well G9>
p200.dispense(29, plate2[71].top(-2)).touch_tip() #104: <Slot B2><Well H9>
p200.dispense(58, plate2[56].top(-2)).touch_tip() #105: <Slot B2><Well A8>
p200.dispense(58, plate2[57].top(-2)).touch_tip() #106: <Slot B2><Well B8>

p200.aspirate(174, trough['A3'].bottom(66))
p200.dispense(58, plate2[58].top(-2)).touch_tip() #107: <Slot B2><Well C8>
p200.dispense(58, plate2[59].top(-2)).touch_tip() #108: <Slot B2><Well D8>
p200.dispense(58, plate2[60].top(-2)).touch_tip() #109: <Slot B2><Well E8>

p200.aspirate(174, trough['A3'].bottom(66))
p200.dispense(58, plate2[61].top(-2)).touch_tip() #110: <Slot B2><Well F8>
p200.dispense(58, plate2[62].top(-2)).touch_tip() #111: <Slot B2><Well G8>
p200.dispense(58, plate2[63].top(-2)).touch_tip() #112: <Slot B2><Well H8>

p200.aspirate(172, trough['A3'].bottom(65))
p200.dispense(86, plate2[48].top(-2)).touch_tip() #113: <Slot B2><Well A7>
p200.dispense(86, plate2[49].top(-2)).touch_tip() #114: <Slot B2><Well B7>

p200.aspirate(172, trough['A3'].bottom(65))
p200.dispense(86, plate2[50].top(-2)).touch_tip() #115: <Slot B2><Well C7>
p200.dispense(86, plate2[51].top(-2)).touch_tip() #116: <Slot B2><Well D7>

p200.aspirate(172, trough['A3'].bottom(65))
p200.dispense(86, plate2[52].top(-2)).touch_tip() #117: <Slot B2><Well E7>
p200.dispense(86, plate2[53].top(-2)).touch_tip() #118: <Slot B2><Well F7>

p200.aspirate(172, trough['A3'].bottom(64))
p200.dispense(86, plate2[54].top(-2)).touch_tip() #119: <Slot B2><Well G7>
p200.dispense(86, plate2[55].top(-2)).touch_tip() #120: <Slot B2><Well H7>

p200.aspirate(108, trough['A3'].bottom(64))
p200.dispense(108, plate2[40].top(-2)).touch_tip() #121: <Slot B2><Well A6>

p200.aspirate(108, trough['A3'].bottom(64))
p200.dispense(108, plate2[41].top(-2)).touch_tip() #122: <Slot B2><Well B6>

p200.aspirate(108, trough['A3'].bottom(64))
p200.dispense(108, plate2[42].top(-2)).touch_tip() #123: <Slot B2><Well C6>

p200.aspirate(108, trough['A3'].bottom(64))
p200.dispense(108, plate2[43].top(-2)).touch_tip() #124: <Slot B2><Well D6>

p200.aspirate(108, trough['A3'].bottom(63))
p200.dispense(108, plate2[44].top(-2)).touch_tip() #125: <Slot B2><Well E6>

p200.aspirate(108, trough['A3'].bottom(63))
p200.dispense(108, plate2[45].top(-2)).touch_tip() #126: <Slot B2><Well F6>

p200.aspirate(108, trough['A3'].bottom(63))
p200.dispense(108, plate2[46].top(-2)).touch_tip() #127: <Slot B2><Well G6>

p200.aspirate(108, trough['A3'].bottom(63))
p200.dispense(108, plate2[47].top(-2)).touch_tip() #128: <Slot B2><Well H6>

p200.aspirate(144, trough['A3'].bottom(63))
p200.dispense(144, plate2[32].top(-2)).touch_tip() #129: <Slot B2><Well A5>

p200.aspirate(144, trough['A3'].bottom(62))
p200.dispense(144, plate2[33].top(-2)).touch_tip() #130: <Slot B2><Well B5>

p200.aspirate(144, trough['A3'].bottom(62))
p200.dispense(144, plate2[34].top(-2)).touch_tip() #131: <Slot B2><Well C5>

p200.aspirate(144, trough['A3'].bottom(62))
p200.dispense(144, plate2[35].top(-2)).touch_tip() #132: <Slot B2><Well D5>

p200.aspirate(144, trough['A3'].bottom(62))
p200.dispense(144, plate2[36].top(-2)).touch_tip() #133: <Slot B2><Well E5>

p200.aspirate(144, trough['A3'].bottom(61))
p200.dispense(144, plate2[37].top(-2)).touch_tip() #134: <Slot B2><Well F5>

p200.aspirate(144, trough['A3'].bottom(61))
p200.dispense(144, plate2[38].top(-2)).touch_tip() #135: <Slot B2><Well G5>

p200.aspirate(144, trough['A3'].bottom(61))
p200.dispense(144, plate2[39].top(-2)).touch_tip() #136: <Slot B2><Well H5>

p200.aspirate(147, trough['A3'].bottom(60))
p200.dispense(147, plate2[88].top(-2)).touch_tip() #137: <Slot B2><Well A12>

p200.aspirate(147, trough['A3'].bottom(60))
p200.dispense(147, plate2[89].top(-2)).touch_tip() #138: <Slot B2><Well B12>

p200.aspirate(147, trough['A3'].bottom(60))
p200.dispense(147, plate2[90].top(-2)).touch_tip() #139: <Slot B2><Well C12>

p200.aspirate(147, trough['A3'].bottom(60))
p200.dispense(147, plate2[91].top(-2)).touch_tip() #140: <Slot B2><Well D12>

p200.aspirate(147, trough['A3'].bottom(59))
p200.dispense(147, plate2[92].top(-2)).touch_tip() #141: <Slot B2><Well E12>

p200.aspirate(147, trough['A3'].bottom(59))
p200.dispense(147, plate2[93].top(-2)).touch_tip() #142: <Slot B2><Well F12>

p200.aspirate(147, trough['A3'].bottom(59))
p200.dispense(147, plate2[94].top(-2)).touch_tip() #143: <Slot B2><Well G12>

p200.aspirate(147, trough['A3'].bottom(59))
p200.dispense(147, plate2[95].top(-2)).touch_tip() #144: <Slot B2><Well H12>

p200.aspirate(154, trough['A3'].bottom(58))
p200.dispense(154, plate2[80].top(-2)).touch_tip() #145: <Slot B2><Well A11>

p200.aspirate(154, trough['A3'].bottom(58))
p200.dispense(154, plate2[81].top(-2)).touch_tip() #146: <Slot B2><Well B11>

p200.aspirate(154, trough['A3'].bottom(58))
p200.dispense(154, plate2[82].top(-2)).touch_tip() #147: <Slot B2><Well C11>

p200.aspirate(154, trough['A3'].bottom(58))
p200.dispense(154, plate2[83].top(-2)).touch_tip() #148: <Slot B2><Well D11>

p200.aspirate(154, trough['A3'].bottom(57))
p200.dispense(154, plate2[84].top(-2)).touch_tip() #149: <Slot B2><Well E11>

p200.aspirate(154, trough['A3'].bottom(57))
p200.dispense(154, plate2[85].top(-2)).touch_tip() #150: <Slot B2><Well F11>

p200.aspirate(154, trough['A3'].bottom(57))
p200.dispense(154, plate2[86].top(-2)).touch_tip() #151: <Slot B2><Well G11>

p200.aspirate(154, trough['A3'].bottom(56))
p200.dispense(154, plate2[87].top(-2)).touch_tip() #152: <Slot B2><Well H11>

p200.aspirate(160, trough['A3'].bottom(56))
p200.dispense(160, plate2[72].top(-2)).touch_tip() #153: <Slot B2><Well A10>

p200.aspirate(160, trough['A3'].bottom(56))
p200.dispense(160, plate2[73].top(-2)).touch_tip() #154: <Slot B2><Well B10>

p200.aspirate(160, trough['A3'].bottom(56))
p200.dispense(160, plate2[74].top(-2)).touch_tip() #155: <Slot B2><Well C10>

p200.aspirate(160, trough['A3'].bottom(55))
p200.dispense(160, plate2[75].top(-2)).touch_tip() #156: <Slot B2><Well D10>

p200.aspirate(160, trough['A3'].bottom(55))
p200.dispense(160, plate2[76].top(-2)).touch_tip() #157: <Slot B2><Well E10>

p200.aspirate(160, trough['A3'].bottom(55))
p200.dispense(160, plate2[77].top(-2)).touch_tip() #158: <Slot B2><Well F10>

p200.aspirate(160, trough['A3'].bottom(54))
p200.dispense(160, plate2[78].top(-2)).touch_tip() #159: <Slot B2><Well G10>

p200.aspirate(160, trough['A3'].bottom(54))
p200.dispense(160, plate2[79].top(-2)).touch_tip() #160: <Slot B2><Well H10>

p200.aspirate(162, trough['A3'].bottom(54))
p200.dispense(162, plate2[24].top(-2)).touch_tip() #161: <Slot B2><Well A4>

p200.aspirate(162, trough['A3'].bottom(53))
p200.dispense(162, plate2[25].top(-2)).touch_tip() #162: <Slot B2><Well B4>

p200.aspirate(162, trough['A3'].bottom(53))
p200.dispense(162, plate2[26].top(-2)).touch_tip() #163: <Slot B2><Well C4>

p200.aspirate(162, trough['A3'].bottom(53))
p200.dispense(162, plate2[27].top(-2)).touch_tip() #164: <Slot B2><Well D4>

p200.aspirate(162, trough['A3'].bottom(53))
p200.dispense(162, plate2[28].top(-2)).touch_tip() #165: <Slot B2><Well E4>

p200.aspirate(162, trough['A3'].bottom(52))
p200.dispense(162, plate2[29].top(-2)).touch_tip() #166: <Slot B2><Well F4>

p200.aspirate(162, trough['A3'].bottom(52))
p200.dispense(162, plate2[30].top(-2)).touch_tip() #167: <Slot B2><Well G4>

p200.aspirate(162, trough['A3'].bottom(52))
p200.dispense(162, plate2[31].top(-2)).touch_tip() #168: <Slot B2><Well H4>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[0].top(-2)).touch_tip() #169: <Slot B2><Well A1>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[8].top(-2)).touch_tip() #170: <Slot B2><Well A2>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[16].top(-2)).touch_tip() #171: <Slot B2><Well A3>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[1].top(-2)).touch_tip() #172: <Slot B2><Well B1>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[9].top(-2)).touch_tip() #173: <Slot B2><Well B2>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[17].top(-2)).touch_tip() #174: <Slot B2><Well B3>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[2].top(-2)).touch_tip() #175: <Slot B2><Well C1>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[10].top(-2)).touch_tip() #176: <Slot B2><Well C2>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[18].top(-2)).touch_tip() #177: <Slot B2><Well C3>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[3].top(-2)).touch_tip() #178: <Slot B2><Well D1>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[11].top(-2)).touch_tip() #179: <Slot B2><Well D2>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[19].top(-2)).touch_tip() #180: <Slot B2><Well D3>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[4].top(-2)).touch_tip() #181: <Slot B2><Well E1>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[12].top(-2)).touch_tip() #182: <Slot B2><Well E2>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[20].top(-2)).touch_tip() #183: <Slot B2><Well E3>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[5].top(-2)).touch_tip() #184: <Slot B2><Well F1>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[13].top(-2)).touch_tip() #185: <Slot B2><Well F2>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[21].top(-2)).touch_tip() #186: <Slot B2><Well F3>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[6].top(-2)).touch_tip() #187: <Slot B2><Well G1>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[14].top(-2)).touch_tip() #188: <Slot B2><Well G2>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[22].top(-2)).touch_tip() #189: <Slot B2><Well G3>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[7].top(-2)).touch_tip() #190: <Slot B2><Well H1>

p200.aspirate(180, trough['A3'].bottom(44))
p200.dispense(180, plate2[15].top(-2)).touch_tip() #191: <Slot B2><Well H2>

p200.aspirate(180, trough['A3'].bottom(44))
p200.dispense(180, plate2[23].top(-2)).touch_tip() #192: <Slot B2><Well H3>

p200.aspirate(108, trough['A3'].bottom(44))
p200.dispense(108, plate3[16].top(-2)).touch_tip() #193: <Slot C1><Well A3>

p200.aspirate(108, trough['A3'].bottom(44))
p200.dispense(108, plate3[48].top(-2)).touch_tip() #194: <Slot C1><Well A7>

p200.aspirate(108, trough['A3'].bottom(43))
p200.dispense(108, plate3[80].top(-2)).touch_tip() #195: <Slot C1><Well A11>

p200.aspirate(108, trough['A3'].bottom(43))
p200.dispense(108, plate3[17].top(-2)).touch_tip() #196: <Slot C1><Well B3>

p200.aspirate(108, trough['A3'].bottom(43))
p200.dispense(108, plate3[49].top(-2)).touch_tip() #197: <Slot C1><Well B7>

p200.aspirate(108, trough['A3'].bottom(43))
p200.dispense(108, plate3[81].top(-2)).touch_tip() #198: <Slot C1><Well B11>

p200.aspirate(108, trough['A3'].bottom(43))
p200.dispense(108, plate3[18].top(-2)).touch_tip() #199: <Slot C1><Well C3>

p200.aspirate(108, trough['A3'].bottom(43))
p200.dispense(108, plate3[50].top(-2)).touch_tip() #200: <Slot C1><Well C7>

p200.aspirate(108, trough['A3'].bottom(42))
p200.dispense(108, plate3[82].top(-2)).touch_tip() #201: <Slot C1><Well C11>

p200.aspirate(108, trough['A3'].bottom(42))
p200.dispense(108, plate3[19].top(-2)).touch_tip() #202: <Slot C1><Well D3>

p200.aspirate(108, trough['A3'].bottom(42))
p200.dispense(108, plate3[51].top(-2)).touch_tip() #203: <Slot C1><Well D7>

p200.aspirate(108, trough['A3'].bottom(42))
p200.dispense(108, plate3[83].top(-2)).touch_tip() #204: <Slot C1><Well D11>

p200.aspirate(108, trough['A3'].bottom(42))
p200.dispense(108, plate3[20].top(-2)).touch_tip() #205: <Slot C1><Well E3>

p200.aspirate(108, trough['A3'].bottom(41))
p200.dispense(108, plate3[52].top(-2)).touch_tip() #206: <Slot C1><Well E7>

p200.aspirate(108, trough['A3'].bottom(41))
p200.dispense(108, plate3[84].top(-2)).touch_tip() #207: <Slot C1><Well E11>

p200.aspirate(108, trough['A3'].bottom(41))
p200.dispense(108, plate3[21].top(-2)).touch_tip() #208: <Slot C1><Well F3>

p200.aspirate(108, trough['A3'].bottom(41))
p200.dispense(108, plate3[53].top(-2)).touch_tip() #209: <Slot C1><Well F7>

p200.aspirate(108, trough['A3'].bottom(41))
p200.dispense(108, plate3[85].top(-2)).touch_tip() #210: <Slot C1><Well F11>

p200.aspirate(108, trough['A3'].bottom(40))
p200.dispense(108, plate3[22].top(-2)).touch_tip() #211: <Slot C1><Well G3>

p200.aspirate(108, trough['A3'].bottom(40))
p200.dispense(108, plate3[54].top(-2)).touch_tip() #212: <Slot C1><Well G7>

p200.aspirate(108, trough['A3'].bottom(40))
p200.dispense(108, plate3[86].top(-2)).touch_tip() #213: <Slot C1><Well G11>

p200.aspirate(108, trough['A3'].bottom(40))
p200.dispense(108, plate3[23].top(-2)).touch_tip() #214: <Slot C1><Well H3>

p200.aspirate(108, trough['A3'].bottom(40))
p200.dispense(108, plate3[55].top(-2)).touch_tip() #215: <Slot C1><Well H7>

p200.aspirate(108, trough['A3'].bottom(39))
p200.dispense(108, plate3[87].top(-2)).touch_tip() #216: <Slot C1><Well H11>

p200.aspirate(125, trough['A3'].bottom(39))
p200.dispense(125, plate3[8].top(-2)).touch_tip() #217: <Slot C1><Well A2>

p200.aspirate(125, trough['A3'].bottom(39))
p200.dispense(125, plate3[40].top(-2)).touch_tip() #218: <Slot C1><Well A6>

p200.aspirate(125, trough['A3'].bottom(39))
p200.dispense(125, plate3[72].top(-2)).touch_tip() #219: <Slot C1><Well A10>

p200.aspirate(125, trough['A3'].bottom(38))
p200.dispense(125, plate3[9].top(-2)).touch_tip() #220: <Slot C1><Well B2>

p200.aspirate(125, trough['A3'].bottom(38))
p200.dispense(125, plate3[41].top(-2)).touch_tip() #221: <Slot C1><Well B6>

p200.aspirate(125, trough['A3'].bottom(38))
p200.dispense(125, plate3[73].top(-2)).touch_tip() #222: <Slot C1><Well B10>

p200.aspirate(125, trough['A3'].bottom(38))
p200.dispense(125, plate3[10].top(-2)).touch_tip() #223: <Slot C1><Well C2>

p200.aspirate(125, trough['A3'].bottom(38))
p200.dispense(125, plate3[42].top(-2)).touch_tip() #224: <Slot C1><Well C6>

p200.aspirate(125, trough['A3'].bottom(37))
p200.dispense(125, plate3[74].top(-2)).touch_tip() #225: <Slot C1><Well C10>

p200.aspirate(125, trough['A3'].bottom(37))
p200.dispense(125, plate3[11].top(-2)).touch_tip() #226: <Slot C1><Well D2>

p200.aspirate(125, trough['A3'].bottom(37))
p200.dispense(125, plate3[43].top(-2)).touch_tip() #227: <Slot C1><Well D6>

p200.aspirate(125, trough['A3'].bottom(37))
p200.dispense(125, plate3[75].top(-2)).touch_tip() #228: <Slot C1><Well D10>

p200.aspirate(125, trough['A3'].bottom(36))
p200.dispense(125, plate3[12].top(-2)).touch_tip() #229: <Slot C1><Well E2>

p200.aspirate(125, trough['A3'].bottom(36))
p200.dispense(125, plate3[44].top(-2)).touch_tip() #230: <Slot C1><Well E6>

p200.aspirate(125, trough['A3'].bottom(36))
p200.dispense(125, plate3[76].top(-2)).touch_tip() #231: <Slot C1><Well E10>

p200.aspirate(125, trough['A3'].bottom(36))
p200.dispense(125, plate3[13].top(-2)).touch_tip() #232: <Slot C1><Well F2>

p200.aspirate(125, trough['A3'].bottom(36))
p200.dispense(125, plate3[45].top(-2)).touch_tip() #233: <Slot C1><Well F6>

p200.aspirate(125, trough['A3'].bottom(35))
p200.dispense(125, plate3[77].top(-2)).touch_tip() #234: <Slot C1><Well F10>

p200.aspirate(125, trough['A3'].bottom(35))
p200.dispense(125, plate3[14].top(-2)).touch_tip() #235: <Slot C1><Well G2>

p200.aspirate(125, trough['A3'].bottom(35))
p200.dispense(125, plate3[46].top(-2)).touch_tip() #236: <Slot C1><Well G6>

p200.aspirate(125, trough['A3'].bottom(35))
p200.dispense(125, plate3[78].top(-2)).touch_tip() #237: <Slot C1><Well G10>

p200.aspirate(125, trough['A3'].bottom(34))
p200.dispense(125, plate3[15].top(-2)).touch_tip() #238: <Slot C1><Well H2>

p200.aspirate(125, trough['A3'].bottom(34))
p200.dispense(125, plate3[47].top(-2)).touch_tip() #239: <Slot C1><Well H6>

p200.aspirate(125, trough['A3'].bottom(34))
p200.dispense(125, plate3[79].top(-2)).touch_tip() #240: <Slot C1><Well H10>

p200.aspirate(144, trough['A3'].bottom(34))
p200.dispense(144, plate3[0].top(-2)).touch_tip() #241: <Slot C1><Well A1>

p200.aspirate(144, trough['A3'].bottom(33))
p200.dispense(144, plate3[32].top(-2)).touch_tip() #242: <Slot C1><Well A5>

p200.aspirate(144, trough['A3'].bottom(33))
p200.dispense(144, plate3[64].top(-2)).touch_tip() #243: <Slot C1><Well A9>

p200.aspirate(144, trough['A3'].bottom(33))
p200.dispense(144, plate3[1].top(-2)).touch_tip() #244: <Slot C1><Well B1>

p200.aspirate(144, trough['A3'].bottom(33))
p200.dispense(144, plate3[33].top(-2)).touch_tip() #245: <Slot C1><Well B5>

p200.aspirate(144, trough['A3'].bottom(32))
p200.dispense(144, plate3[65].top(-2)).touch_tip() #246: <Slot C1><Well B9>

p200.aspirate(144, trough['A3'].bottom(32))
p200.dispense(144, plate3[2].top(-2)).touch_tip() #247: <Slot C1><Well C1>

p200.aspirate(144, trough['A3'].bottom(32))
p200.dispense(144, plate3[34].top(-2)).touch_tip() #248: <Slot C1><Well C5>

p200.aspirate(144, trough['A3'].bottom(32))
p200.dispense(144, plate3[66].top(-2)).touch_tip() #249: <Slot C1><Well C9>

p200.aspirate(144, trough['A3'].bottom(31))
p200.dispense(144, plate3[3].top(-2)).touch_tip() #250: <Slot C1><Well D1>

p200.aspirate(144, trough['A3'].bottom(31))
p200.dispense(144, plate3[35].top(-2)).touch_tip() #251: <Slot C1><Well D5>

p200.aspirate(144, trough['A3'].bottom(31))
p200.dispense(144, plate3[67].top(-2)).touch_tip() #252: <Slot C1><Well D9>

p200.aspirate(144, trough['A3'].bottom(31))
p200.dispense(144, plate3[4].top(-2)).touch_tip() #253: <Slot C1><Well E1>

p200.aspirate(144, trough['A3'].bottom(30))
p200.dispense(144, plate3[36].top(-2)).touch_tip() #254: <Slot C1><Well E5>

p200.aspirate(144, trough['A3'].bottom(30))
p200.dispense(144, plate3[68].top(-2)).touch_tip() #255: <Slot C1><Well E9>

p200.aspirate(144, trough['A3'].bottom(30))
p200.dispense(144, plate3[5].top(-2)).touch_tip() #256: <Slot C1><Well F1>

p200.aspirate(144, trough['A3'].bottom(30))
p200.dispense(144, plate3[37].top(-2)).touch_tip() #257: <Slot C1><Well F5>

p200.aspirate(144, trough['A3'].bottom(29))
p200.dispense(144, plate3[69].top(-2)).touch_tip() #258: <Slot C1><Well F9>

p200.aspirate(144, trough['A3'].bottom(29))
p200.dispense(144, plate3[6].top(-2)).touch_tip() #259: <Slot C1><Well G1>

p200.aspirate(144, trough['A3'].bottom(29))
p200.dispense(144, plate3[38].top(-2)).touch_tip() #260: <Slot C1><Well G5>

p200.aspirate(144, trough['A3'].bottom(28))
p200.dispense(144, plate3[70].top(-2)).touch_tip() #261: <Slot C1><Well G9>

p200.aspirate(144, trough['A3'].bottom(28))
p200.dispense(144, plate3[7].top(-2)).touch_tip() #262: <Slot C1><Well H1>

p200.aspirate(144, trough['A3'].bottom(28))
p200.dispense(144, plate3[39].top(-2)).touch_tip() #263: <Slot C1><Well H5>

p200.aspirate(144, trough['A3'].bottom(28))
p200.dispense(144, plate3[71].top(-2)).touch_tip() #264: <Slot C1><Well H9>

p200.aspirate(180, trough['A3'].bottom(27))
p200.dispense(180, plate3[24].top(-2)).touch_tip() #265: <Slot C1><Well A4>

p200.aspirate(180, trough['A3'].bottom(27))
p200.dispense(180, plate3[56].top(-2)).touch_tip() #266: <Slot C1><Well A8>

p200.aspirate(180, trough['A3'].bottom(27))
p200.dispense(180, plate3[88].top(-2)).touch_tip() #267: <Slot C1><Well A12>

p200.aspirate(180, trough['A3'].bottom(26))
p200.dispense(180, plate3[25].top(-2)).touch_tip() #268: <Slot C1><Well B4>

p200.aspirate(180, trough['A3'].bottom(26))
p200.dispense(180, plate3[57].top(-2)).touch_tip() #269: <Slot C1><Well B8>

p200.aspirate(180, trough['A3'].bottom(26))
p200.dispense(180, plate3[89].top(-2)).touch_tip() #270: <Slot C1><Well B12>

p200.aspirate(180, trough['A3'].bottom(25))
p200.dispense(180, plate3[26].top(-2)).touch_tip() #271: <Slot C1><Well C4>

p200.aspirate(180, trough['A3'].bottom(25))
p200.dispense(180, plate3[58].top(-2)).touch_tip() #272: <Slot C1><Well C8>

p200.aspirate(180, trough['A3'].bottom(25))
p200.dispense(180, plate3[90].top(-2)).touch_tip() #273: <Slot C1><Well C12>

p200.aspirate(180, trough['A3'].bottom(24))
p200.dispense(180, plate3[27].top(-2)).touch_tip() #274: <Slot C1><Well D4>

p200.aspirate(180, trough['A3'].bottom(24))
p200.dispense(180, plate3[59].top(-2)).touch_tip() #275: <Slot C1><Well D8>

p200.aspirate(180, trough['A3'].bottom(24))
p200.dispense(180, plate3[91].top(-2)).touch_tip() #276: <Slot C1><Well D12>

p200.aspirate(180, trough['A3'].bottom(23))
p200.dispense(180, plate3[28].top(-2)).touch_tip() #277: <Slot C1><Well E4>

p200.aspirate(180, trough['A3'].bottom(23))
p200.dispense(180, plate3[60].top(-2)).touch_tip() #278: <Slot C1><Well E8>

p200.aspirate(180, trough['A3'].bottom(23))
p200.dispense(180, plate3[92].top(-2)).touch_tip() #279: <Slot C1><Well E12>

p200.aspirate(180, trough['A3'].bottom(22))
p200.dispense(180, plate3[29].top(-2)).touch_tip() #280: <Slot C1><Well F4>

p200.aspirate(180, trough['A3'].bottom(22))
p200.dispense(180, plate3[61].top(-2)).touch_tip() #281: <Slot C1><Well F8>

p200.aspirate(180, trough['A3'].bottom(22))
p200.dispense(180, plate3[93].top(-2)).touch_tip() #282: <Slot C1><Well F12>

p200.aspirate(180, trough['A3'].bottom(21))
p200.dispense(180, plate3[30].top(-2)).touch_tip() #283: <Slot C1><Well G4>

p200.aspirate(180, trough['A3'].bottom(21))
p200.dispense(180, plate3[62].top(-2)).touch_tip() #284: <Slot C1><Well G8>

p200.aspirate(180, trough['A3'].bottom(21))
p200.dispense(180, plate3[94].top(-2)).touch_tip() #285: <Slot C1><Well G12>

p200.aspirate(180, trough['A3'].bottom(21))
p200.dispense(180, plate3[31].top(-2)).touch_tip() #286: <Slot C1><Well H4>

p200.aspirate(180, trough['A3'].bottom(20))
p200.dispense(180, plate3[63].top(-2)).touch_tip() #287: <Slot C1><Well H8>

p200.aspirate(180, trough['A3'].bottom(20))
p200.dispense(180, plate3[95].top(-2)).touch_tip() #288: <Slot C1><Well H12>

p200.aspirate(108, trough['A3'].bottom(20))
p200.dispense(108, plate4[16].top(-2)).touch_tip() #289: <Slot C2><Well A3>

p200.aspirate(108, trough['A3'].bottom(20))
p200.dispense(108, plate4[48].top(-2)).touch_tip() #290: <Slot C2><Well A7>

p200.aspirate(108, trough['A3'].bottom(19))
p200.dispense(108, plate4[80].top(-2)).touch_tip() #291: <Slot C2><Well A11>

p200.aspirate(108, trough['A3'].bottom(19))
p200.dispense(108, plate4[17].top(-2)).touch_tip() #292: <Slot C2><Well B3>

p200.aspirate(108, trough['A3'].bottom(19))
p200.dispense(108, plate4[49].top(-2)).touch_tip() #293: <Slot C2><Well B7>

p200.aspirate(108, trough['A3'].bottom(19))
p200.dispense(108, plate4[81].top(-2)).touch_tip() #294: <Slot C2><Well B11>

p200.aspirate(108, trough['A3'].bottom(19))
p200.dispense(108, plate4[18].top(-2)).touch_tip() #295: <Slot C2><Well C3>

p200.aspirate(108, trough['A3'].bottom(18))
p200.dispense(108, plate4[50].top(-2)).touch_tip() #296: <Slot C2><Well C7>

p200.aspirate(108, trough['A3'].bottom(18))
p200.dispense(108, plate4[82].top(-2)).touch_tip() #297: <Slot C2><Well C11>

p200.aspirate(108, trough['A3'].bottom(18))
p200.dispense(108, plate4[19].top(-2)).touch_tip() #298: <Slot C2><Well D3>

p200.aspirate(108, trough['A4'].bottom(90))
p200.dispense(108, plate4[51].top(-2)).touch_tip() #299: <Slot C2><Well D7>

p200.aspirate(108, trough['A4'].bottom(90))
p200.dispense(108, plate4[83].top(-2)).touch_tip() #300: <Slot C2><Well D11>

p200.aspirate(108, trough['A4'].bottom(89))
p200.dispense(108, plate4[20].top(-2)).touch_tip() #301: <Slot C2><Well E3>

p200.aspirate(108, trough['A4'].bottom(89))
p200.dispense(108, plate4[52].top(-2)).touch_tip() #302: <Slot C2><Well E7>

p200.aspirate(108, trough['A4'].bottom(89))
p200.dispense(108, plate4[84].top(-2)).touch_tip() #303: <Slot C2><Well E11>

p200.aspirate(108, trough['A4'].bottom(89))
p200.dispense(108, plate4[21].top(-2)).touch_tip() #304: <Slot C2><Well F3>

p200.aspirate(108, trough['A4'].bottom(89))
p200.dispense(108, plate4[53].top(-2)).touch_tip() #305: <Slot C2><Well F7>

p200.aspirate(108, trough['A4'].bottom(88))
p200.dispense(108, plate4[85].top(-2)).touch_tip() #306: <Slot C2><Well F11>

p200.aspirate(108, trough['A4'].bottom(88))
p200.dispense(108, plate4[22].top(-2)).touch_tip() #307: <Slot C2><Well G3>

p200.aspirate(108, trough['A4'].bottom(88))
p200.dispense(108, plate4[54].top(-2)).touch_tip() #308: <Slot C2><Well G7>

p200.aspirate(108, trough['A4'].bottom(88))
p200.dispense(108, plate4[86].top(-2)).touch_tip() #309: <Slot C2><Well G11>

p200.aspirate(108, trough['A4'].bottom(88))
p200.dispense(108, plate4[23].top(-2)).touch_tip() #310: <Slot C2><Well H3>

p200.aspirate(108, trough['A4'].bottom(87))
p200.dispense(108, plate4[55].top(-2)).touch_tip() #311: <Slot C2><Well H7>

p200.aspirate(108, trough['A3'].bottom(18))
p200.dispense(108, plate4[87].top(-2)).touch_tip() #312: <Slot C2><Well H11>

p200.aspirate(125, trough['A3'].bottom(18))
p200.dispense(125, plate4[8].top(-2)).touch_tip() #313: <Slot C2><Well A2>

p200.aspirate(125, trough['A3'].bottom(17))
p200.dispense(125, plate4[40].top(-2)).touch_tip() #314: <Slot C2><Well A6>

p200.aspirate(125, trough['A3'].bottom(17))
p200.dispense(125, plate4[72].top(-2)).touch_tip() #315: <Slot C2><Well A10>

p200.aspirate(125, trough['A3'].bottom(17))
p200.dispense(125, plate4[9].top(-2)).touch_tip() #316: <Slot C2><Well B2>

p200.aspirate(125, trough['A3'].bottom(17))
p200.dispense(125, plate4[41].top(-2)).touch_tip() #317: <Slot C2><Well B6>

p200.aspirate(125, trough['A3'].bottom(16))
p200.dispense(125, plate4[73].top(-2)).touch_tip() #318: <Slot C2><Well B10>

p200.aspirate(125, trough['A3'].bottom(16))
p200.dispense(125, plate4[10].top(-2)).touch_tip() #319: <Slot C2><Well C2>

p200.aspirate(125, trough['A3'].bottom(16))
p200.dispense(125, plate4[42].top(-2)).touch_tip() #320: <Slot C2><Well C6>

p200.aspirate(125, trough['A3'].bottom(16))
p200.dispense(125, plate4[74].top(-2)).touch_tip() #321: <Slot C2><Well C10>

p200.aspirate(125, trough['A3'].bottom(16))
p200.dispense(125, plate4[11].top(-2)).touch_tip() #322: <Slot C2><Well D2>

p200.aspirate(125, trough['A4'].bottom(87))
p200.dispense(125, plate4[43].top(-2)).touch_tip() #323: <Slot C2><Well D6>

p200.aspirate(125, trough['A4'].bottom(87))
p200.dispense(125, plate4[75].top(-2)).touch_tip() #324: <Slot C2><Well D10>

p200.aspirate(125, trough['A4'].bottom(87))
p200.dispense(125, plate4[12].top(-2)).touch_tip() #325: <Slot C2><Well E2>

p200.aspirate(125, trough['A4'].bottom(87))
p200.dispense(125, plate4[44].top(-2)).touch_tip() #326: <Slot C2><Well E6>

p200.aspirate(125, trough['A4'].bottom(86))
p200.dispense(125, plate4[76].top(-2)).touch_tip() #327: <Slot C2><Well E10>

p200.aspirate(125, trough['A4'].bottom(86))
p200.dispense(125, plate4[13].top(-2)).touch_tip() #328: <Slot C2><Well F2>

p200.aspirate(125, trough['A4'].bottom(86))
p200.dispense(125, plate4[45].top(-2)).touch_tip() #329: <Slot C2><Well F6>

p200.aspirate(125, trough['A4'].bottom(86))
p200.dispense(125, plate4[77].top(-2)).touch_tip() #330: <Slot C2><Well F10>

p200.aspirate(125, trough['A4'].bottom(85))
p200.dispense(125, plate4[14].top(-2)).touch_tip() #331: <Slot C2><Well G2>

p200.aspirate(125, trough['A4'].bottom(85))
p200.dispense(125, plate4[46].top(-2)).touch_tip() #332: <Slot C2><Well G6>

p200.aspirate(125, trough['A4'].bottom(85))
p200.dispense(125, plate4[78].top(-2)).touch_tip() #333: <Slot C2><Well G10>

p200.aspirate(125, trough['A4'].bottom(85))
p200.dispense(125, plate4[15].top(-2)).touch_tip() #334: <Slot C2><Well H2>

p200.aspirate(125, trough['A4'].bottom(85))
p200.dispense(125, plate4[47].top(-2)).touch_tip() #335: <Slot C2><Well H6>

p200.aspirate(125, trough['A3'].bottom(15))
p200.dispense(125, plate4[79].top(-2)).touch_tip() #336: <Slot C2><Well H10>

p200.aspirate(144, trough['A3'].bottom(15))
p200.dispense(144, plate4[0].top(-2)).touch_tip() #337: <Slot C2><Well A1>

p200.aspirate(144, trough['A3'].bottom(15))
p200.dispense(144, plate4[32].top(-2)).touch_tip() #338: <Slot C2><Well A5>

p200.aspirate(144, trough['A3'].bottom(15))
p200.dispense(144, plate4[64].top(-2)).touch_tip() #339: <Slot C2><Well A9>

p200.aspirate(144, trough['A3'].bottom(14))
p200.dispense(144, plate4[1].top(-2)).touch_tip() #340: <Slot C2><Well B1>

p200.aspirate(144, trough['A3'].bottom(14))
p200.dispense(144, plate4[33].top(-2)).touch_tip() #341: <Slot C2><Well B5>

p200.aspirate(144, trough['A3'].bottom(14))
p200.dispense(144, plate4[65].top(-2)).touch_tip() #342: <Slot C2><Well B9>

p200.aspirate(144, trough['A3'].bottom(14))
p200.dispense(144, plate4[2].top(-2)).touch_tip() #343: <Slot C2><Well C1>

p200.aspirate(144, trough['A3'].bottom(13))
p200.dispense(144, plate4[34].top(-2)).touch_tip() #344: <Slot C2><Well C5>

p200.aspirate(144, trough['A3'].bottom(13))
p200.dispense(144, plate4[66].top(-2)).touch_tip() #345: <Slot C2><Well C9>

p200.aspirate(144, trough['A3'].bottom(13))
p200.dispense(144, plate4[3].top(-2)).touch_tip() #346: <Slot C2><Well D1>

p200.aspirate(144, trough['A4'].bottom(84))
p200.dispense(144, plate4[35].top(-2)).touch_tip() #347: <Slot C2><Well D5>

p200.aspirate(144, trough['A4'].bottom(84))
p200.dispense(144, plate4[67].top(-2)).touch_tip() #348: <Slot C2><Well D9>

p200.aspirate(144, trough['A4'].bottom(84))
p200.dispense(144, plate4[4].top(-2)).touch_tip() #349: <Slot C2><Well E1>

p200.aspirate(144, trough['A4'].bottom(84))
p200.dispense(144, plate4[36].top(-2)).touch_tip() #350: <Slot C2><Well E5>

p200.aspirate(144, trough['A4'].bottom(83))
p200.dispense(144, plate4[68].top(-2)).touch_tip() #351: <Slot C2><Well E9>

p200.aspirate(144, trough['A4'].bottom(83))
p200.dispense(144, plate4[5].top(-2)).touch_tip() #352: <Slot C2><Well F1>

p200.aspirate(144, trough['A4'].bottom(83))
p200.dispense(144, plate4[37].top(-2)).touch_tip() #353: <Slot C2><Well F5>

p200.aspirate(144, trough['A4'].bottom(82))
p200.dispense(144, plate4[69].top(-2)).touch_tip() #354: <Slot C2><Well F9>

p200.aspirate(144, trough['A4'].bottom(82))
p200.dispense(144, plate4[6].top(-2)).touch_tip() #355: <Slot C2><Well G1>

p200.aspirate(144, trough['A4'].bottom(82))
p200.dispense(144, plate4[38].top(-2)).touch_tip() #356: <Slot C2><Well G5>

p200.aspirate(144, trough['A4'].bottom(82))
p200.dispense(144, plate4[70].top(-2)).touch_tip() #357: <Slot C2><Well G9>

p200.aspirate(144, trough['A4'].bottom(81))
p200.dispense(144, plate4[7].top(-2)).touch_tip() #358: <Slot C2><Well H1>

p200.aspirate(144, trough['A4'].bottom(81))
p200.dispense(144, plate4[39].top(-2)).touch_tip() #359: <Slot C2><Well H5>

p200.aspirate(144, trough['A3'].bottom(12))
p200.dispense(144, plate4[71].top(-2)).touch_tip() #360: <Slot C2><Well H9>

p200.aspirate(180, trough['A3'].bottom(12))
p200.dispense(180, plate4[24].top(-2)).touch_tip() #361: <Slot C2><Well A4>

p200.aspirate(180, trough['A3'].bottom(12))
p200.dispense(180, plate4[56].top(-2)).touch_tip() #362: <Slot C2><Well A8>

p200.aspirate(180, trough['A3'].bottom(11))
p200.dispense(180, plate4[88].top(-2)).touch_tip() #363: <Slot C2><Well A12>

p200.aspirate(180, trough['A3'].bottom(11))
p200.dispense(180, plate4[25].top(-2)).touch_tip() #364: <Slot C2><Well B4>

p200.aspirate(180, trough['A3'].bottom(11))
p200.dispense(180, plate4[57].top(-2)).touch_tip() #365: <Slot C2><Well B8>

p200.aspirate(180, trough['A3'].bottom(10))
p200.dispense(180, plate4[89].top(-2)).touch_tip() #366: <Slot C2><Well B12>

p200.aspirate(180, trough['A3'].bottom(10))
p200.dispense(180, plate4[26].top(-2)).touch_tip() #367: <Slot C2><Well C4>

p200.aspirate(180, trough['A3'].bottom(10))
p200.dispense(180, plate4[58].top(-2)).touch_tip() #368: <Slot C2><Well C8>

p200.aspirate(180, trough['A3'].bottom(9))
p200.dispense(180, plate4[90].top(-2)).touch_tip() #369: <Slot C2><Well C12>

p200.aspirate(180, trough['A3'].bottom(9))
p200.dispense(180, plate4[27].top(-2)).touch_tip() #370: <Slot C2><Well D4>

p200.aspirate(180, trough['A4'].bottom(81))
p200.dispense(180, plate4[59].top(-2)).touch_tip() #371: <Slot C2><Well D8>

p200.aspirate(180, trough['A4'].bottom(81))
p200.dispense(180, plate4[91].top(-2)).touch_tip() #372: <Slot C2><Well D12>

p200.aspirate(180, trough['A4'].bottom(80))
p200.dispense(180, plate4[28].top(-2)).touch_tip() #373: <Slot C2><Well E4>

p200.aspirate(180, trough['A4'].bottom(80))
p200.dispense(180, plate4[60].top(-2)).touch_tip() #374: <Slot C2><Well E8>

p200.aspirate(180, trough['A4'].bottom(80))
p200.dispense(180, plate4[92].top(-2)).touch_tip() #375: <Slot C2><Well E12>

p200.aspirate(180, trough['A4'].bottom(79))
p200.dispense(180, plate4[29].top(-2)).touch_tip() #376: <Slot C2><Well F4>

p200.aspirate(180, trough['A4'].bottom(79))
p200.dispense(180, plate4[61].top(-2)).touch_tip() #377: <Slot C2><Well F8>

p200.aspirate(180, trough['A4'].bottom(79))
p200.dispense(180, plate4[93].top(-2)).touch_tip() #378: <Slot C2><Well F12>

p200.aspirate(180, trough['A4'].bottom(78))
p200.dispense(180, plate4[30].top(-2)).touch_tip() #379: <Slot C2><Well G4>

p200.aspirate(180, trough['A4'].bottom(78))
p200.dispense(180, plate4[62].top(-2)).touch_tip() #380: <Slot C2><Well G8>

p200.aspirate(180, trough['A4'].bottom(78))
p200.dispense(180, plate4[94].top(-2)).touch_tip() #381: <Slot C2><Well G12>

p200.aspirate(180, trough['A4'].bottom(77))
p200.dispense(180, plate4[31].top(-2)).touch_tip() #382: <Slot C2><Well H4>

p200.aspirate(180, trough['A4'].bottom(77))
p200.dispense(180, plate4[63].top(-2)).touch_tip() #383: <Slot C2><Well H8>

p200.aspirate(180, trough['A4'].bottom(77))
p200.dispense(180, plate4[95].top(-2)).touch_tip() #384: <Slot C2><Well H12>

p200.drop_tip()
p200.pick_up_tip(p200rack['1'])

# *********** Dispense WS_1000

p200.aspirate(160, trough['B1'].bottom(89))
p200.dispense(20, plate1[72].top(-2)).touch_tip() #385 <Slot B1><Well A10>
p200.dispense(20, plate1[73].top(-2)).touch_tip() #386: <Slot B1><Well B10>
p200.dispense(20, plate1[74].top(-2)).touch_tip() #387: <Slot B1><Well C10>
p200.dispense(20, plate1[75].top(-2)).touch_tip() #388: <Slot B1><Well D10>
p200.dispense(20, plate1[76].top(-2)).touch_tip() #389: <Slot B1><Well E10>
p200.dispense(20, plate1[77].top(-2)).touch_tip() #390: <Slot B1><Well F10>
p200.dispense(20, plate1[78].top(-2)).touch_tip() #391: <Slot B1><Well G10>
p200.dispense(20, plate1[79].top(-2)).touch_tip() #392: <Slot B1><Well H10>

p200.aspirate(156, trough['B1'].bottom(88))
p200.dispense(26, plate1[80].top(-2)).touch_tip() #393: <Slot B1><Well A11>
p200.dispense(26, plate1[81].top(-2)).touch_tip() #394: <Slot B1><Well B11>
p200.dispense(26, plate1[82].top(-2)).touch_tip() #395: <Slot B1><Well C11>
p200.dispense(26, plate1[83].top(-2)).touch_tip() #396: <Slot B1><Well D11>
p200.dispense(26, plate1[84].top(-2)).touch_tip() #397: <Slot B1><Well E11>
p200.dispense(26, plate1[85].top(-2)).touch_tip() #398: <Slot B1><Well F11>

p200.aspirate(151, trough['B1'].bottom(87))
p200.dispense(26, plate1[86].top(-2)).touch_tip() #399: <Slot B1><Well G11>
p200.dispense(26, plate1[87].top(-2)).touch_tip() #400: <Slot B1><Well H11>
p200.dispense(33, plate1[88].top(-2)).touch_tip() #401: <Slot B1><Well A12>
p200.dispense(33, plate1[89].top(-2)).touch_tip() #402: <Slot B1><Well B12>
p200.dispense(33, plate1[90].top(-2)).touch_tip() #403: <Slot B1><Well C12>

p200.aspirate(165, trough['B1'].bottom(86))
p200.dispense(33, plate1[91].top(-2)).touch_tip() #404: <Slot B1><Well D12>
p200.dispense(33, plate1[92].top(-2)).touch_tip() #405: <Slot B1><Well E12>
p200.dispense(33, plate1[93].top(-2)).touch_tip() #406: <Slot B1><Well F12>
p200.dispense(33, plate1[94].top(-2)).touch_tip() #407: <Slot B1><Well G12>
p200.dispense(33, plate1[95].top(-2)).touch_tip() #408: <Slot B1><Well H12>

p200.aspirate(160, trough['B1'].bottom(85))
p200.dispense(20, plate2[72].top(-2)).touch_tip() #409: <Slot B2><Well A10>
p200.dispense(20, plate2[73].top(-2)).touch_tip() #410: <Slot B2><Well B10>
p200.dispense(20, plate2[74].top(-2)).touch_tip() #411: <Slot B2><Well C10>
p200.dispense(20, plate2[75].top(-2)).touch_tip() #412: <Slot B2><Well D10>
p200.dispense(20, plate2[76].top(-2)).touch_tip() #413: <Slot B2><Well E10>
p200.dispense(20, plate2[77].top(-2)).touch_tip() #414: <Slot B2><Well F10>
p200.dispense(20, plate2[78].top(-2)).touch_tip() #415: <Slot B2><Well G10>
p200.dispense(20, plate2[79].top(-2)).touch_tip() #416: <Slot B2><Well H10>

p200.aspirate(156, trough['B1'].bottom(84))
p200.dispense(26, plate2[80].top(-2)).touch_tip() #417: <Slot B2><Well A11>
p200.dispense(26, plate2[81].top(-2)).touch_tip() #418: <Slot B2><Well B11>
p200.dispense(26, plate2[82].top(-2)).touch_tip() #419: <Slot B2><Well C11>
p200.dispense(26, plate2[83].top(-2)).touch_tip() #420: <Slot B2><Well D11>
p200.dispense(26, plate2[84].top(-2)).touch_tip() #421: <Slot B2><Well E11>
p200.dispense(26, plate2[85].top(-2)).touch_tip() #422: <Slot B2><Well F11>

p200.aspirate(151, trough['B1'].bottom(83))
p200.dispense(26, plate2[86].top(-2)).touch_tip() #423: <Slot B2><Well G11>
p200.dispense(26, plate2[87].top(-2)).touch_tip() #424: <Slot B2><Well H11>
p200.dispense(33, plate2[88].top(-2)).touch_tip() #425: <Slot B2><Well A12>
p200.dispense(33, plate2[89].top(-2)).touch_tip() #426: <Slot B2><Well B12>
p200.dispense(33, plate2[90].top(-2)).touch_tip() #427: <Slot B2><Well C12>

p200.aspirate(165, trough['B1'].bottom(82))
p200.dispense(33, plate2[91].top(-2)).touch_tip() #428: <Slot B2><Well D12>
p200.dispense(33, plate2[92].top(-2)).touch_tip() #429: <Slot B2><Well E12>
p200.dispense(33, plate2[93].top(-2)).touch_tip() #430: <Slot B2><Well F12>
p200.dispense(33, plate2[94].top(-2)).touch_tip() #431: <Slot B2><Well G12>
p200.dispense(33, plate2[95].top(-2)).touch_tip() #432: <Slot B2><Well H12>

p200.aspirate(180, trough['B1'].bottom(81))
p200.dispense(36, plate3[0].top(-2)).touch_tip() #433: <Slot C1><Well A1>
p200.dispense(36, plate3[32].top(-2)).touch_tip() #434: <Slot C1><Well A5>
p200.dispense(36, plate3[64].top(-2)).touch_tip() #435: <Slot C1><Well A9>
p200.dispense(36, plate3[1].top(-2)).touch_tip() #436: <Slot C1><Well B1>
p200.dispense(36, plate3[33].top(-2)).touch_tip() #437: <Slot C1><Well B5>

p200.aspirate(180, trough['B1'].bottom(80))
p200.dispense(36, plate3[65].top(-2)).touch_tip() #438: <Slot C1><Well B9>
p200.dispense(36, plate3[2].top(-2)).touch_tip() #439: <Slot C1><Well C1>
p200.dispense(36, plate3[34].top(-2)).touch_tip() #440: <Slot C1><Well C5>
p200.dispense(36, plate3[66].top(-2)).touch_tip() #441: <Slot C1><Well C9>
p200.dispense(36, plate3[3].top(-2)).touch_tip() #442: <Slot C1><Well D1>

p200.aspirate(180, trough['B1'].bottom(79))
p200.dispense(36, plate3[35].top(-2)).touch_tip() #443: <Slot C1><Well D5>
p200.dispense(36, plate3[67].top(-2)).touch_tip() #444: <Slot C1><Well D9>
p200.dispense(36, plate3[4].top(-2)).touch_tip() #445: <Slot C1><Well E1>
p200.dispense(36, plate3[36].top(-2)).touch_tip() #446: <Slot C1><Well E5>
p200.dispense(36, plate3[68].top(-2)).touch_tip() #447: <Slot C1><Well E9>

p200.aspirate(180, trough['B1'].bottom(78))
p200.dispense(36, plate3[5].top(-2)).touch_tip() #448: <Slot C1><Well F1>
p200.dispense(36, plate3[37].top(-2)).touch_tip() #449: <Slot C1><Well F5>
p200.dispense(36, plate3[69].top(-2)).touch_tip() #450: <Slot C1><Well F9>
p200.dispense(36, plate3[6].top(-2)).touch_tip() #451: <Slot C1><Well G1>
p200.dispense(36, plate3[38].top(-2)).touch_tip() #452: <Slot C1><Well G5>

p200.aspirate(144, trough['B1'].bottom(77))
p200.dispense(36, plate3[70].top(-2)).touch_tip() #453: <Slot C1><Well G9>
p200.dispense(36, plate3[7].top(-2)).touch_tip() #454: <Slot C1><Well H1>
p200.dispense(36, plate3[39].top(-2)).touch_tip() #455: <Slot C1><Well H5>
p200.dispense(36, plate3[71].top(-2)).touch_tip() #456: <Slot C1><Well H9>

p200.aspirate(165, trough['B1'].bottom(76))
p200.dispense(55, plate3[8].top(-2)).touch_tip() #457: <Slot C1><Well A2>
p200.dispense(55, plate3[40].top(-2)).touch_tip() #458: <Slot C1><Well A6>
p200.dispense(55, plate3[72].top(-2)).touch_tip() #459: <Slot C1><Well A10>

p200.aspirate(165, trough['B1'].bottom(75))
p200.dispense(55, plate3[9].top(-2)).touch_tip() #460: <Slot C1><Well B2>
p200.dispense(55, plate3[41].top(-2)).touch_tip() #461: <Slot C1><Well B6>
p200.dispense(55, plate3[73].top(-2)).touch_tip() #462: <Slot C1><Well B10>

p200.aspirate(165, trough['B1'].bottom(74))
p200.dispense(55, plate3[10].top(-2)).touch_tip() #463: <Slot C1><Well C2>
p200.dispense(55, plate3[42].top(-2)).touch_tip() #464: <Slot C1><Well C6>
p200.dispense(55, plate3[74].top(-2)).touch_tip() #465: <Slot C1><Well C10>

p200.aspirate(165, trough['B1'].bottom(73))
p200.dispense(55, plate3[11].top(-2)).touch_tip() #466: <Slot C1><Well D2>
p200.dispense(55, plate3[43].top(-2)).touch_tip() #467: <Slot C1><Well D6>
p200.dispense(55, plate3[75].top(-2)).touch_tip() #468: <Slot C1><Well D10>

p200.aspirate(165, trough['B1'].bottom(72))
p200.dispense(55, plate3[12].top(-2)).touch_tip() #469: <Slot C1><Well E2>
p200.dispense(55, plate3[44].top(-2)).touch_tip() #470: <Slot C1><Well E6>
p200.dispense(55, plate3[76].top(-2)).touch_tip() #471: <Slot C1><Well E10>

p200.aspirate(165, trough['B1'].bottom(71))
p200.dispense(55, plate3[13].top(-2)).touch_tip() #472: <Slot C1><Well F2>
p200.dispense(55, plate3[45].top(-2)).touch_tip() #473: <Slot C1><Well F6>
p200.dispense(55, plate3[77].top(-2)).touch_tip() #474: <Slot C1><Well F10>

p200.aspirate(165, trough['B1'].bottom(70))
p200.dispense(55, plate3[14].top(-2)).touch_tip() #475: <Slot C1><Well G2>
p200.dispense(55, plate3[46].top(-2)).touch_tip() #476: <Slot C1><Well G6>
p200.dispense(55, plate3[78].top(-2)).touch_tip() #477: <Slot C1><Well G10>

p200.aspirate(165, trough['B1'].bottom(69))
p200.dispense(55, plate3[15].top(-2)).touch_tip() #478: <Slot C1><Well H2>
p200.dispense(55, plate3[47].top(-2)).touch_tip() #479: <Slot C1><Well H6>
p200.dispense(55, plate3[79].top(-2)).touch_tip() #480: <Slot C1><Well H10>

p200.aspirate(144, trough['B1'].bottom(68))
p200.dispense(72, plate3[16].top(-2)).touch_tip() #481: <Slot C1><Well A3>
p200.dispense(72, plate3[48].top(-2)).touch_tip() #482: <Slot C1><Well A7>

p200.aspirate(144, trough['B1'].bottom(67))
p200.dispense(72, plate3[80].top(-2)).touch_tip() #483: <Slot C1><Well A11>
p200.dispense(72, plate3[17].top(-2)).touch_tip() #484: <Slot C1><Well B3>

p200.aspirate(144, trough['B1'].bottom(66))
p200.dispense(72, plate3[49].top(-2)).touch_tip() #485: <Slot C1><Well B7>
p200.dispense(72, plate3[81].top(-2)).touch_tip() #486: <Slot C1><Well B11>

p200.aspirate(144, trough['B1'].bottom(65))
p200.dispense(72, plate3[18].top(-2)).touch_tip() #487: <Slot C1><Well C3>
p200.dispense(72, plate3[50].top(-2)).touch_tip() #488: <Slot C1><Well C7>

p200.aspirate(144, trough['B1'].bottom(65))
p200.dispense(72, plate3[82].top(-2)).touch_tip() #489: <Slot C1><Well C11>
p200.dispense(72, plate3[19].top(-2)).touch_tip() #490: <Slot C1><Well D3>

p200.aspirate(144, trough['B1'].bottom(64))
p200.dispense(72, plate3[51].top(-2)).touch_tip() #491: <Slot C1><Well D7>
p200.dispense(72, plate3[83].top(-2)).touch_tip() #492: <Slot C1><Well D11>

p200.aspirate(144, trough['B1'].bottom(63))
p200.dispense(72, plate3[20].top(-2)).touch_tip() #493: <Slot C1><Well E3>
p200.dispense(72, plate3[52].top(-2)).touch_tip() #494: <Slot C1><Well E7>

p200.aspirate(144, trough['B1'].bottom(62))
p200.dispense(72, plate3[84].top(-2)).touch_tip() #495: <Slot C1><Well E11>
p200.dispense(72, plate3[21].top(-2)).touch_tip() #496: <Slot C1><Well F3>

p200.aspirate(144, trough['B1'].bottom(61))
p200.dispense(72, plate3[53].top(-2)).touch_tip() #497: <Slot C1><Well F7>
p200.dispense(72, plate3[85].top(-2)).touch_tip() #498: <Slot C1><Well F11>

p200.aspirate(144, trough['B1'].bottom(60))
p200.dispense(72, plate3[22].top(-2)).touch_tip() #499: <Slot C1><Well G3>
p200.dispense(72, plate3[54].top(-2)).touch_tip() #500: <Slot C1><Well G7>

p200.aspirate(144, trough['B1'].bottom(59))
p200.dispense(72, plate3[86].top(-2)).touch_tip() #501: <Slot C1><Well G11>
p200.dispense(72, plate3[23].top(-2)).touch_tip() #502: <Slot C1><Well H3>

p200.aspirate(180, trough['B1'].bottom(59))
p200.dispense(72, plate3[55].top(-2)).touch_tip() #503: <Slot C1><Well H7>
p200.dispense(72, plate3[87].top(-2)).touch_tip() #504: <Slot C1><Well H11>
p200.dispense(36, plate4[0].top(-2)).touch_tip() #505: <Slot C2><Well A1>

p200.aspirate(180, trough['B1'].bottom(57))
p200.dispense(36, plate4[32].top(-2)).touch_tip() #506: <Slot C2><Well A5>
p200.dispense(36, plate4[64].top(-2)).touch_tip() #507: <Slot C2><Well A9>
p200.dispense(36, plate4[1].top(-2)).touch_tip() #508: <Slot C2><Well B1>
p200.dispense(36, plate4[33].top(-2)).touch_tip() #509: <Slot C2><Well B5>
p200.dispense(36, plate4[65].top(-2)).touch_tip() #510: <Slot C2><Well B9>

p200.aspirate(180, trough['B1'].bottom(56))
p200.dispense(36, plate4[2].top(-2)).touch_tip() #511: <Slot C2><Well C1>
p200.dispense(36, plate4[34].top(-2)).touch_tip() #512: <Slot C2><Well C5>
p200.dispense(36, plate4[66].top(-2)).touch_tip() #513: <Slot C2><Well C9>
p200.dispense(36, plate4[3].top(-2)).touch_tip() #514: <Slot C2><Well D1>
p200.dispense(36, plate4[35].top(-2)).touch_tip() #515: <Slot C2><Well D5>

p200.aspirate(180, trough['B1'].bottom(55))
p200.dispense(36, plate4[67].top(-2)).touch_tip() #516: <Slot C2><Well D9>
p200.dispense(36, plate4[4].top(-2)).touch_tip() #517: <Slot C2><Well E1>
p200.dispense(36, plate4[36].top(-2)).touch_tip() #518: <Slot C2><Well E5>
p200.dispense(36, plate4[68].top(-2)).touch_tip() #519: <Slot C2><Well E9>
p200.dispense(36, plate4[5].top(-2)).touch_tip() #520: <Slot C2><Well F1>

p200.aspirate(180, trough['B1'].bottom(54))
p200.dispense(36, plate4[37].top(-2)).touch_tip() #521: <Slot C2><Well F5>
p200.dispense(36, plate4[69].top(-2)).touch_tip() #522: <Slot C2><Well F9>
p200.dispense(36, plate4[6].top(-2)).touch_tip() #523: <Slot C2><Well G1>
p200.dispense(36, plate4[38].top(-2)).touch_tip() #524: <Slot C2><Well G5>
p200.dispense(36, plate4[70].top(-2)).touch_tip() #525: <Slot C2><Well G9>

p200.aspirate(163, trough['B1'].bottom(53))
p200.dispense(36, plate4[7].top(-2)).touch_tip() #526: <Slot C2><Well H1>
p200.dispense(36, plate4[39].top(-2)).touch_tip() #527: <Slot C2><Well H5>
p200.dispense(36, plate4[71].top(-2)).touch_tip() #528: <Slot C2><Well H9>
p200.dispense(55, plate4[8].top(-2)).touch_tip() #529: <Slot C2><Well A2>

p200.aspirate(165, trough['B1'].bottom(52))
p200.dispense(55, plate4[40].top(-2)).touch_tip() #530: <Slot C2><Well A6>
p200.dispense(55, plate4[72].top(-2)).touch_tip() #531: <Slot C2><Well A10>
p200.dispense(55, plate4[9].top(-2)).touch_tip() #532: <Slot C2><Well B2>

p200.aspirate(165, trough['B1'].bottom(51))
p200.dispense(55, plate4[41].top(-2)).touch_tip() #533: <Slot C2><Well B6>
p200.dispense(55, plate4[73].top(-2)).touch_tip() #534: <Slot C2><Well B10>
p200.dispense(55, plate4[10].top(-2)).touch_tip() #535: <Slot C2><Well C2>

p200.aspirate(165, trough['B1'].bottom(50))
p200.dispense(55, plate4[42].top(-2)).touch_tip() #536: <Slot C2><Well C6>
p200.dispense(55, plate4[74].top(-2)).touch_tip() #537: <Slot C2><Well C10>
p200.dispense(55, plate4[11].top(-2)).touch_tip() #538: <Slot C2><Well D2>

p200.aspirate(165, trough['B1'].bottom(49))
p200.dispense(55, plate4[43].top(-2)).touch_tip() #539: <Slot C2><Well D6>
p200.dispense(55, plate4[75].top(-2)).touch_tip() #540: <Slot C2><Well D10>
p200.dispense(55, plate4[12].top(-2)).touch_tip() #541: <Slot C2><Well E2>

p200.aspirate(165, trough['B1'].bottom(48))
p200.dispense(55, plate4[44].top(-2)).touch_tip() #542: <Slot C2><Well E6>
p200.dispense(55, plate4[76].top(-2)).touch_tip() #543: <Slot C2><Well E10>
p200.dispense(55, plate4[13].top(-2)).touch_tip() #544: <Slot C2><Well F2>

p200.aspirate(165, trough['B1'].bottom(47))
p200.dispense(55, plate4[45].top(-2)).touch_tip() #545: <Slot C2><Well F6>
p200.dispense(55, plate4[77].top(-2)).touch_tip() #546: <Slot C2><Well F10>
p200.dispense(55, plate4[14].top(-2)).touch_tip() #547: <Slot C2><Well G2>

p200.aspirate(165, trough['B1'].bottom(46))
p200.dispense(55, plate4[46].top(-2)).touch_tip() #548: <Slot C2><Well G6>
p200.dispense(55, plate4[78].top(-2)).touch_tip() #549: <Slot C2><Well G10>
p200.dispense(55, plate4[15].top(-2)).touch_tip() #550: <Slot C2><Well H2>

p200.aspirate(110, trough['B1'].bottom(45))
p200.dispense(55, plate4[47].top(-2)).touch_tip() #551: <Slot C2><Well H6>
p200.dispense(55, plate4[79].top(-2)).touch_tip() #552: <Slot C2><Well H10>

p200.aspirate(144, trough['B1'].bottom(45))
p200.dispense(72, plate4[16].top(-2)).touch_tip() #553: <Slot C2><Well A3>
p200.dispense(72, plate4[48].top(-2)).touch_tip() #554: <Slot C2><Well A7>

p200.aspirate(144, trough['B1'].bottom(44))
p200.dispense(72, plate4[80].top(-2)).touch_tip() #555: <Slot C2><Well A11>
p200.dispense(72, plate4[17].top(-2)).touch_tip() #556: <Slot C2><Well B3>

p200.aspirate(144, trough['B1'].bottom(43))
p200.dispense(72, plate4[49].top(-2)).touch_tip() #557: <Slot C2><Well B7>
p200.dispense(72, plate4[81].top(-2)).touch_tip() #558: <Slot C2><Well B11>

p200.aspirate(144, trough['B1'].bottom(42))
p200.dispense(72, plate4[18].top(-2)).touch_tip() #559: <Slot C2><Well C3>
p200.dispense(72, plate4[50].top(-2)).touch_tip() #560: <Slot C2><Well C7>

p200.aspirate(144, trough['B1'].bottom(41))
p200.dispense(72, plate4[82].top(-2)).touch_tip() #561: <Slot C2><Well C11>
p200.dispense(72, plate4[19].top(-2)).touch_tip() #562: <Slot C2><Well D3>

p200.aspirate(144, trough['B1'].bottom(40))
p200.dispense(72, plate4[51].top(-2)).touch_tip() #563: <Slot C2><Well D7>
p200.dispense(72, plate4[83].top(-2)).touch_tip() #564: <Slot C2><Well D11>

p200.aspirate(144, trough['B1'].bottom(39))
p200.dispense(72, plate4[20].top(-2)).touch_tip() #565: <Slot C2><Well E3>
p200.dispense(72, plate4[52].top(-2)).touch_tip() #566: <Slot C2><Well E7>

p200.aspirate(144, trough['B1'].bottom(38))
p200.dispense(72, plate4[84].top(-2)).touch_tip() #567: <Slot C2><Well E11>
p200.dispense(72, plate4[21].top(-2)).touch_tip() #568: <Slot C2><Well F3>

p200.aspirate(144, trough['B1'].bottom(38))
p200.dispense(72, plate4[53].top(-2)).touch_tip() #569: <Slot C2><Well F7>
p200.dispense(72, plate4[85].top(-2)).touch_tip() #570: <Slot C2><Well F11>

p200.aspirate(144, trough['B1'].bottom(37))
p200.dispense(72, plate4[22].top(-2)).touch_tip() #571: <Slot C2><Well G3>
p200.dispense(72, plate4[54].top(-2)).touch_tip() #572: <Slot C2><Well G7>

p200.aspirate(144, trough['B1'].bottom(36))
p200.dispense(72, plate4[86].top(-2)).touch_tip() #573: <Slot C2><Well G11>
p200.dispense(72, plate4[23].top(-2)).touch_tip() #574: <Slot C2><Well H3>

p200.aspirate(144, trough['B1'].bottom(35))
p200.dispense(72, plate4[55].top(-2)).touch_tip() #575: <Slot C2><Well H7>
p200.dispense(72, plate4[87].top(-2)).touch_tip() #576: <Slot C2><Well H11>

p200.drop_tip()
p200.pick_up_tip(p200rack['2'])

# *********** Dispense WS_10000

p200.aspirate(180, trough['A1'].bottom(89))
p200.dispense(18, plate1[24].top(-2)).touch_tip() #577 <Slot B1><Well A4>
p200.dispense(18, plate1[25].top(-2)).touch_tip() #578: <Slot B1><Well B4>
p200.dispense(18, plate1[26].top(-2)).touch_tip() #579: <Slot B1><Well C4>
p200.dispense(18, plate1[27].top(-2)).touch_tip() #580: <Slot B1><Well D4>
p200.dispense(18, plate1[28].top(-2)).touch_tip() #581: <Slot B1><Well E4>
p200.dispense(18, plate1[29].top(-2)).touch_tip() #582: <Slot B1><Well F4>
p200.dispense(18, plate1[30].top(-2)).touch_tip() #583: <Slot B1><Well G4>
p200.dispense(18, plate1[31].top(-2)).touch_tip() #584: <Slot B1><Well H4>
p200.dispense(36, plate1[32].top(-2)).touch_tip() #585: <Slot B1><Well A5>

p200.aspirate(180, trough['A1'].bottom(88))
p200.dispense(36, plate1[33].top(-2)).touch_tip() #586: <Slot B1><Well B5>
p200.dispense(36, plate1[34].top(-2)).touch_tip() #587: <Slot B1><Well C5>
p200.dispense(36, plate1[35].top(-2)).touch_tip() #588: <Slot B1><Well D5>
p200.dispense(36, plate1[36].top(-2)).touch_tip() #589: <Slot B1><Well E5>
p200.dispense(36, plate1[37].top(-2)).touch_tip() #590: <Slot B1><Well F5>

p200.aspirate(144, trough['A1'].bottom(87))
p200.dispense(36, plate1[38].top(-2)).touch_tip() #591: <Slot B1><Well G5>
p200.dispense(36, plate1[39].top(-2)).touch_tip() #592: <Slot B1><Well H5>
p200.dispense(72, plate1[40].top(-2)).touch_tip() #593: <Slot B1><Well A6>

p200.aspirate(144, trough['A1'].bottom(86))
p200.dispense(72, plate1[41].top(-2)).touch_tip() #594: <Slot B1><Well B6>
p200.dispense(72, plate1[42].top(-2)).touch_tip() #595: <Slot B1><Well C6>

p200.aspirate(144, trough['A1'].bottom(85))
p200.dispense(72, plate1[43].top(-2)).touch_tip() #596: <Slot B1><Well D6>
p200.dispense(72, plate1[44].top(-2)).touch_tip() #597: <Slot B1><Well E6>

p200.aspirate(144, trough['A1'].bottom(84))
p200.dispense(72, plate1[45].top(-2)).touch_tip() #598: <Slot B1><Well F6>
p200.dispense(72, plate1[46].top(-2)).touch_tip() #599: <Slot B1><Well G6>

p200.aspirate(166, trough['A1'].bottom(83))
p200.dispense(72, plate1[47].top(-2)).touch_tip() #600: <Slot B1><Well H6>
p200.dispense(94, plate1[48].top(-2)).touch_tip() #601: <Slot B1><Well A7>

p200.aspirate(94, trough['A1'].bottom(82))
p200.dispense(94, plate1[49].top(-2)).touch_tip() #602: <Slot B1><Well B7>

p200.aspirate(94, trough['A1'].bottom(82))
p200.dispense(94, plate1[50].top(-2)).touch_tip() #603: <Slot B1><Well C7>

p200.aspirate(94, trough['A1'].bottom(81))
p200.dispense(94, plate1[51].top(-2)).touch_tip() #604: <Slot B1><Well D7>

p200.aspirate(94, trough['A1'].bottom(81))
p200.dispense(94, plate1[52].top(-2)).touch_tip() #605: <Slot B1><Well E7>

p200.aspirate(94, trough['A1'].bottom(80))
p200.dispense(94, plate1[53].top(-2)).touch_tip() #606: <Slot B1><Well F7>

p200.aspirate(94, trough['A1'].bottom(79))
p200.dispense(94, plate1[54].top(-2)).touch_tip() #607: <Slot B1><Well G7>

p200.aspirate(94, trough['A1'].bottom(79))
p200.dispense(94, plate1[55].top(-2)).touch_tip() #608: <Slot B1><Well H7>

p200.aspirate(122, trough['A1'].bottom(78))
p200.dispense(122, plate1[56].top(-2)).touch_tip() #609: <Slot B1><Well A8>

p200.aspirate(122, trough['A1'].bottom(77))
p200.dispense(122, plate1[57].top(-2)).touch_tip() #610: <Slot B1><Well B8>

p200.aspirate(122, trough['A1'].bottom(77))
p200.dispense(122, plate1[58].top(-2)).touch_tip() #611: <Slot B1><Well C8>

p200.aspirate(122, trough['A1'].bottom(76))
p200.dispense(122, plate1[59].top(-2)).touch_tip() #612: <Slot B1><Well D8>

p200.aspirate(122, trough['A1'].bottom(75))
p200.dispense(122, plate1[60].top(-2)).touch_tip() #613: <Slot B1><Well E8>

p200.aspirate(122, trough['A1'].bottom(74))
p200.dispense(122, plate1[61].top(-2)).touch_tip() #614: <Slot B1><Well F8>

p200.aspirate(122, trough['A1'].bottom(74))
p200.dispense(122, plate1[62].top(-2)).touch_tip() #615: <Slot B1><Well G8>

p200.aspirate(122, trough['A1'].bottom(73))
p200.dispense(122, plate1[63].top(-2)).touch_tip() #616: <Slot B1><Well H8>

p200.aspirate(151, trough['A1'].bottom(72))
p200.dispense(151, plate1[64].top(-2)).touch_tip() #617: <Slot B1><Well A9>

p200.aspirate(151, trough['A1'].bottom(71))
p200.dispense(151, plate1[65].top(-2)).touch_tip() #618: <Slot B1><Well B9>

p200.aspirate(151, trough['A1'].bottom(70))
p200.dispense(151, plate1[66].top(-2)).touch_tip() #619: <Slot B1><Well C9>

p200.aspirate(151, trough['A1'].bottom(69))
p200.dispense(151, plate1[67].top(-2)).touch_tip() #620: <Slot B1><Well D9>

p200.aspirate(151, trough['A1'].bottom(68))
p200.dispense(151, plate1[68].top(-2)).touch_tip() #621: <Slot B1><Well E9>

p200.aspirate(151, trough['A1'].bottom(67))
p200.dispense(151, plate1[69].top(-2)).touch_tip() #622: <Slot B1><Well F9>

p200.aspirate(151, trough['A1'].bottom(66))
p200.dispense(151, plate1[70].top(-2)).touch_tip() #623: <Slot B1><Well G9>

p200.aspirate(169, trough['A1'].bottom(66))
p200.dispense(151, plate1[71].top(-2)).touch_tip() #624: <Slot B1><Well H9>
p200.dispense(18, plate2[24].top(-2)).touch_tip() #625: <Slot B2><Well A4>

p200.aspirate(162, trough['A1'].bottom(65))
p200.dispense(18, plate2[25].top(-2)).touch_tip() #626: <Slot B2><Well B4>
p200.dispense(18, plate2[26].top(-2)).touch_tip() #627: <Slot B2><Well C4>
p200.dispense(18, plate2[27].top(-2)).touch_tip() #628: <Slot B2><Well D4>
p200.dispense(18, plate2[28].top(-2)).touch_tip() #629: <Slot B2><Well E4>
p200.dispense(18, plate2[29].top(-2)).touch_tip() #630: <Slot B2><Well F4>
p200.dispense(18, plate2[30].top(-2)).touch_tip() #631: <Slot B2><Well G4>
p200.dispense(18, plate2[31].top(-2)).touch_tip() #632: <Slot B2><Well H4>
p200.dispense(36, plate2[32].top(-2)).touch_tip() #633: <Slot B2><Well A5>

p200.aspirate(180, trough['A1'].bottom(64))
p200.dispense(36, plate2[33].top(-2)).touch_tip() #634: <Slot B2><Well B5>
p200.dispense(36, plate2[34].top(-2)).touch_tip() #635: <Slot B2><Well C5>
p200.dispense(36, plate2[35].top(-2)).touch_tip() #636: <Slot B2><Well D5>
p200.dispense(36, plate2[36].top(-2)).touch_tip() #637: <Slot B2><Well E5>
p200.dispense(36, plate2[37].top(-2)).touch_tip() #638: <Slot B2><Well F5>

p200.aspirate(144, trough['A1'].bottom(63))
p200.dispense(36, plate2[38].top(-2)).touch_tip() #639: <Slot B2><Well G5>
p200.dispense(36, plate2[39].top(-2)).touch_tip() #640: <Slot B2><Well H5>
p200.dispense(72, plate2[40].top(-2)).touch_tip() #641: <Slot B2><Well A6>

p200.aspirate(144, trough['A1'].bottom(62))
p200.dispense(72, plate2[41].top(-2)).touch_tip() #642: <Slot B2><Well B6>
p200.dispense(72, plate2[42].top(-2)).touch_tip() #643: <Slot B2><Well C6>

p200.aspirate(144, trough['A1'].bottom(61))
p200.dispense(72, plate2[43].top(-2)).touch_tip() #644: <Slot B2><Well D6>
p200.dispense(72, plate2[44].top(-2)).touch_tip() #645: <Slot B2><Well E6>

p200.aspirate(144, trough['A1'].bottom(60))
p200.dispense(72, plate2[45].top(-2)).touch_tip() #646: <Slot B2><Well F6>
p200.dispense(72, plate2[46].top(-2)).touch_tip() #647: <Slot B2><Well G6>

p200.aspirate(166, trough['A1'].bottom(59))
p200.dispense(72, plate2[47].top(-2)).touch_tip() #648: <Slot B2><Well H6>
p200.dispense(94, plate2[48].top(-2)).touch_tip() #649: <Slot B2><Well A7>

p200.aspirate(94, trough['A1'].bottom(59))
p200.dispense(94, plate2[49].top(-2)).touch_tip() #650: <Slot B2><Well B7>

p200.aspirate(94, trough['A1'].bottom(58))
p200.dispense(94, plate2[50].top(-2)).touch_tip() #651: <Slot B2><Well C7>

p200.aspirate(94, trough['A1'].bottom(57))
p200.dispense(94, plate2[51].top(-2)).touch_tip() #652: <Slot B2><Well D7>

p200.aspirate(94, trough['A1'].bottom(57))
p200.dispense(94, plate2[52].top(-2)).touch_tip() #653: <Slot B2><Well E7>

p200.aspirate(94, trough['A1'].bottom(56))
p200.dispense(94, plate2[53].top(-2)).touch_tip() #654: <Slot B2><Well F7>

p200.aspirate(94, trough['A1'].bottom(56))
p200.dispense(94, plate2[54].top(-2)).touch_tip() #655: <Slot B2><Well G7>

p200.aspirate(94, trough['A1'].bottom(55))
p200.dispense(94, plate2[55].top(-2)).touch_tip() #656: <Slot B2><Well H7>

p200.aspirate(122, trough['A1'].bottom(54))
p200.dispense(122, plate2[56].top(-2)).touch_tip() #657: <Slot B2><Well A8>

p200.aspirate(122, trough['A1'].bottom(54))
p200.dispense(122, plate2[57].top(-2)).touch_tip() #658: <Slot B2><Well B8>

p200.aspirate(122, trough['A1'].bottom(53))
p200.dispense(122, plate2[58].top(-2)).touch_tip() #659: <Slot B2><Well C8>

p200.aspirate(122, trough['A1'].bottom(52))
p200.dispense(122, plate2[59].top(-2)).touch_tip() #660: <Slot B2><Well D8>

p200.aspirate(122, trough['A1'].bottom(51))
p200.dispense(122, plate2[60].top(-2)).touch_tip() #661: <Slot B2><Well E8>

p200.aspirate(122, trough['A1'].bottom(51))
p200.dispense(122, plate2[61].top(-2)).touch_tip() #662: <Slot B2><Well F8>

p200.aspirate(122, trough['A1'].bottom(50))
p200.dispense(122, plate2[62].top(-2)).touch_tip() #663: <Slot B2><Well G8>

p200.aspirate(122, trough['A1'].bottom(49))
p200.dispense(122, plate2[63].top(-2)).touch_tip() #664: <Slot B2><Well H8>

p200.aspirate(151, trough['A1'].bottom(48))
p200.dispense(151, plate2[64].top(-2)).touch_tip() #665: <Slot B2><Well A9>

p200.aspirate(151, trough['A1'].bottom(47))
p200.dispense(151, plate2[65].top(-2)).touch_tip() #666: <Slot B2><Well B9>

p200.aspirate(151, trough['A1'].bottom(46))
p200.dispense(151, plate2[66].top(-2)).touch_tip() #667: <Slot B2><Well C9>

p200.aspirate(151, trough['A1'].bottom(45))
p200.dispense(151, plate2[67].top(-2)).touch_tip() #668: <Slot B2><Well D9>

p200.aspirate(151, trough['A1'].bottom(44))
p200.dispense(151, plate2[68].top(-2)).touch_tip() #669: <Slot B2><Well E9>

p200.aspirate(151, trough['A1'].bottom(44))
p200.dispense(151, plate2[69].top(-2)).touch_tip() #670: <Slot B2><Well F9>

p200.aspirate(151, trough['A1'].bottom(43))
p200.dispense(151, plate2[70].top(-2)).touch_tip() #671: <Slot B2><Well G9>

p200.aspirate(151, trough['A1'].bottom(43))
p200.dispense(151, plate2[71].top(-2)).touch_tip() #672: <Slot B2><Well H9>

p200.drop_tip()
##