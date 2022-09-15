

###################################################################################
#
# SCRIPT GENERATED ON 17/01/2018 FROM THE FOLLOWING LAYOUT FILES:
#  fileDictName=layouts/EvoAmp_key_dictD1-D9.txt
#  fileTroughName=layouts/EvoAmp_trough.txt
#  fileLayoutName=layouts/EvoAmp_Layout_2platesD1-D9.txt
#
###################################################################################
from opentrons import Robot
from opentrons import containers, instruments
from itertools import chain

robot = Robot()

p200rack = containers.load('tiprack-200ul', 'A2', 'tiprack')
trough = containers.load('tube-rack-15_50ml','B2','trough')
for tube in trough:
	tube.properties['height']+=50
plate1 = containers.load('96-PCR-flat','C1','plate-1')
plate2 = containers.load('96-PCR-flat','D1','plate-2')
trash = containers.load('point','D2','trash')
p200 = instruments.Pipette(name='p200',trash_container=trash,tip_racks=[p200rack],min_volume=18,axis='b',channels=1)

p200.set_max_volume(180)

p200.pick_up_tip(p200rack['0'])
p200.move_to(plate1[0].bottom(), 'arc')
p200.move_to(plate1[95].bottom(), 'arc')
p200.move_to(plate2[0].bottom(), 'arc')
p200.move_to(plate2[95].bottom(), 'arc')

# *********** Dispense M

p200.aspirate(174, trough['A3'].bottom(90))
p200.dispense(29, plate1[64].top(-2)).touch_tip() #1 <Slot C1><Well A9>
p200.dispense(29, plate1[65].top(-2)).touch_tip() #2: <Slot C1><Well B9>
p200.dispense(29, plate1[66].top(-2)).touch_tip() #3: <Slot C1><Well C9>
p200.dispense(29, plate1[67].top(-2)).touch_tip() #4: <Slot C1><Well D9>
p200.dispense(29, plate1[68].top(-2)).touch_tip() #5: <Slot C1><Well E9>
p200.dispense(29, plate1[69].top(-2)).touch_tip() #6: <Slot C1><Well F9>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(29, plate1[70].top(-2)).touch_tip() #7: <Slot C1><Well G9>
p200.dispense(29, plate1[71].top(-2)).touch_tip() #8: <Slot C1><Well H9>
p200.dispense(58, plate1[56].top(-2)).touch_tip() #9: <Slot C1><Well A8>
p200.dispense(58, plate1[57].top(-2)).touch_tip() #10: <Slot C1><Well B8>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(58, plate1[58].top(-2)).touch_tip() #11: <Slot C1><Well C8>
p200.dispense(58, plate1[59].top(-2)).touch_tip() #12: <Slot C1><Well D8>
p200.dispense(58, plate1[60].top(-2)).touch_tip() #13: <Slot C1><Well E8>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(58, plate1[61].top(-2)).touch_tip() #14: <Slot C1><Well F8>
p200.dispense(58, plate1[62].top(-2)).touch_tip() #15: <Slot C1><Well G8>
p200.dispense(58, plate1[63].top(-2)).touch_tip() #16: <Slot C1><Well H8>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[48].top(-2)).touch_tip() #17: <Slot C1><Well A7>
p200.dispense(86, plate1[49].top(-2)).touch_tip() #18: <Slot C1><Well B7>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[50].top(-2)).touch_tip() #19: <Slot C1><Well C7>
p200.dispense(86, plate1[51].top(-2)).touch_tip() #20: <Slot C1><Well D7>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[52].top(-2)).touch_tip() #21: <Slot C1><Well E7>
p200.dispense(86, plate1[53].top(-2)).touch_tip() #22: <Slot C1><Well F7>

p200.aspirate(172, trough['A3'].bottom(87))
p200.dispense(86, plate1[54].top(-2)).touch_tip() #23: <Slot C1><Well G7>
p200.dispense(86, plate1[55].top(-2)).touch_tip() #24: <Slot C1><Well H7>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[40].top(-2)).touch_tip() #25: <Slot C1><Well A6>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[41].top(-2)).touch_tip() #26: <Slot C1><Well B6>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[42].top(-2)).touch_tip() #27: <Slot C1><Well C6>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[43].top(-2)).touch_tip() #28: <Slot C1><Well D6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[44].top(-2)).touch_tip() #29: <Slot C1><Well E6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[45].top(-2)).touch_tip() #30: <Slot C1><Well F6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[46].top(-2)).touch_tip() #31: <Slot C1><Well G6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[47].top(-2)).touch_tip() #32: <Slot C1><Well H6>

p200.aspirate(144, trough['A3'].bottom(85))
p200.dispense(144, plate1[32].top(-2)).touch_tip() #33: <Slot C1><Well A5>

p200.aspirate(144, trough['A3'].bottom(85))
p200.dispense(144, plate1[33].top(-2)).touch_tip() #34: <Slot C1><Well B5>

p200.aspirate(144, trough['A3'].bottom(85))
p200.dispense(144, plate1[34].top(-2)).touch_tip() #35: <Slot C1><Well C5>

p200.aspirate(144, trough['A3'].bottom(85))
p200.dispense(144, plate1[35].top(-2)).touch_tip() #36: <Slot C1><Well D5>

p200.aspirate(144, trough['A3'].bottom(84))
p200.dispense(144, plate1[36].top(-2)).touch_tip() #37: <Slot C1><Well E5>

p200.aspirate(144, trough['A3'].bottom(84))
p200.dispense(144, plate1[37].top(-2)).touch_tip() #38: <Slot C1><Well F5>

p200.aspirate(144, trough['A3'].bottom(84))
p200.dispense(144, plate1[38].top(-2)).touch_tip() #39: <Slot C1><Well G5>

p200.aspirate(144, trough['A3'].bottom(84))
p200.dispense(144, plate1[39].top(-2)).touch_tip() #40: <Slot C1><Well H5>

p200.aspirate(147, trough['A3'].bottom(83))
p200.dispense(147, plate1[88].top(-2)).touch_tip() #41: <Slot C1><Well A12>

p200.aspirate(147, trough['A3'].bottom(83))
p200.dispense(147, plate1[89].top(-2)).touch_tip() #42: <Slot C1><Well B12>

p200.aspirate(147, trough['A3'].bottom(83))
p200.dispense(147, plate1[90].top(-2)).touch_tip() #43: <Slot C1><Well C12>

p200.aspirate(147, trough['A3'].bottom(83))
p200.dispense(147, plate1[91].top(-2)).touch_tip() #44: <Slot C1><Well D12>

p200.aspirate(147, trough['A3'].bottom(82))
p200.dispense(147, plate1[92].top(-2)).touch_tip() #45: <Slot C1><Well E12>

p200.aspirate(147, trough['A3'].bottom(82))
p200.dispense(147, plate1[93].top(-2)).touch_tip() #46: <Slot C1><Well F12>

p200.aspirate(147, trough['A3'].bottom(82))
p200.dispense(147, plate1[94].top(-2)).touch_tip() #47: <Slot C1><Well G12>

p200.aspirate(147, trough['A3'].bottom(81))
p200.dispense(147, plate1[95].top(-2)).touch_tip() #48: <Slot C1><Well H12>

p200.aspirate(154, trough['A3'].bottom(81))
p200.dispense(154, plate1[80].top(-2)).touch_tip() #49: <Slot C1><Well A11>

p200.aspirate(154, trough['A3'].bottom(81))
p200.dispense(154, plate1[81].top(-2)).touch_tip() #50: <Slot C1><Well B11>

p200.aspirate(154, trough['A3'].bottom(81))
p200.dispense(154, plate1[82].top(-2)).touch_tip() #51: <Slot C1><Well C11>

p200.aspirate(154, trough['A3'].bottom(80))
p200.dispense(154, plate1[83].top(-2)).touch_tip() #52: <Slot C1><Well D11>

p200.aspirate(154, trough['A3'].bottom(80))
p200.dispense(154, plate1[84].top(-2)).touch_tip() #53: <Slot C1><Well E11>

p200.aspirate(154, trough['A3'].bottom(80))
p200.dispense(154, plate1[85].top(-2)).touch_tip() #54: <Slot C1><Well F11>

p200.aspirate(154, trough['A3'].bottom(80))
p200.dispense(154, plate1[86].top(-2)).touch_tip() #55: <Slot C1><Well G11>

p200.aspirate(154, trough['A3'].bottom(79))
p200.dispense(154, plate1[87].top(-2)).touch_tip() #56: <Slot C1><Well H11>

p200.aspirate(160, trough['A3'].bottom(79))
p200.dispense(160, plate1[72].top(-2)).touch_tip() #57: <Slot C1><Well A10>

p200.aspirate(160, trough['A3'].bottom(79))
p200.dispense(160, plate1[73].top(-2)).touch_tip() #58: <Slot C1><Well B10>

p200.aspirate(160, trough['A3'].bottom(78))
p200.dispense(160, plate1[74].top(-2)).touch_tip() #59: <Slot C1><Well C10>

p200.aspirate(160, trough['A3'].bottom(78))
p200.dispense(160, plate1[75].top(-2)).touch_tip() #60: <Slot C1><Well D10>

p200.aspirate(160, trough['A3'].bottom(78))
p200.dispense(160, plate1[76].top(-2)).touch_tip() #61: <Slot C1><Well E10>

p200.aspirate(160, trough['A3'].bottom(78))
p200.dispense(160, plate1[77].top(-2)).touch_tip() #62: <Slot C1><Well F10>

p200.aspirate(160, trough['A3'].bottom(77))
p200.dispense(160, plate1[78].top(-2)).touch_tip() #63: <Slot C1><Well G10>

p200.aspirate(160, trough['A3'].bottom(77))
p200.dispense(160, plate1[79].top(-2)).touch_tip() #64: <Slot C1><Well H10>

p200.aspirate(162, trough['A3'].bottom(77))
p200.dispense(162, plate1[24].top(-2)).touch_tip() #65: <Slot C1><Well A4>

p200.aspirate(162, trough['A3'].bottom(76))
p200.dispense(162, plate1[25].top(-2)).touch_tip() #66: <Slot C1><Well B4>

p200.aspirate(162, trough['A3'].bottom(76))
p200.dispense(162, plate1[26].top(-2)).touch_tip() #67: <Slot C1><Well C4>

p200.aspirate(162, trough['A3'].bottom(76))
p200.dispense(162, plate1[27].top(-2)).touch_tip() #68: <Slot C1><Well D4>

p200.aspirate(162, trough['A3'].bottom(75))
p200.dispense(162, plate1[28].top(-2)).touch_tip() #69: <Slot C1><Well E4>

p200.aspirate(162, trough['A3'].bottom(75))
p200.dispense(162, plate1[29].top(-2)).touch_tip() #70: <Slot C1><Well F4>

p200.aspirate(162, trough['A3'].bottom(75))
p200.dispense(162, plate1[30].top(-2)).touch_tip() #71: <Slot C1><Well G4>

p200.aspirate(162, trough['A3'].bottom(75))
p200.dispense(162, plate1[31].top(-2)).touch_tip() #72: <Slot C1><Well H4>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[0].top(-2)).touch_tip() #73: <Slot C1><Well A1>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[8].top(-2)).touch_tip() #74: <Slot C1><Well A2>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[16].top(-2)).touch_tip() #75: <Slot C1><Well A3>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[1].top(-2)).touch_tip() #76: <Slot C1><Well B1>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[9].top(-2)).touch_tip() #77: <Slot C1><Well B2>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[17].top(-2)).touch_tip() #78: <Slot C1><Well B3>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[2].top(-2)).touch_tip() #79: <Slot C1><Well C1>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[10].top(-2)).touch_tip() #80: <Slot C1><Well C2>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[18].top(-2)).touch_tip() #81: <Slot C1><Well C3>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[3].top(-2)).touch_tip() #82: <Slot C1><Well D1>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[11].top(-2)).touch_tip() #83: <Slot C1><Well D2>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[19].top(-2)).touch_tip() #84: <Slot C1><Well D3>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[4].top(-2)).touch_tip() #85: <Slot C1><Well E1>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[12].top(-2)).touch_tip() #86: <Slot C1><Well E2>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[20].top(-2)).touch_tip() #87: <Slot C1><Well E3>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[5].top(-2)).touch_tip() #88: <Slot C1><Well F1>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[13].top(-2)).touch_tip() #89: <Slot C1><Well F2>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[21].top(-2)).touch_tip() #90: <Slot C1><Well F3>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[6].top(-2)).touch_tip() #91: <Slot C1><Well G1>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[14].top(-2)).touch_tip() #92: <Slot C1><Well G2>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[22].top(-2)).touch_tip() #93: <Slot C1><Well G3>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[7].top(-2)).touch_tip() #94: <Slot C1><Well H1>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[15].top(-2)).touch_tip() #95: <Slot C1><Well H2>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[23].top(-2)).touch_tip() #96: <Slot C1><Well H3>

p200.aspirate(174, trough['A3'].bottom(67))
p200.dispense(29, plate2[64].top(-2)).touch_tip() #97: <Slot D1><Well A9>
p200.dispense(29, plate2[65].top(-2)).touch_tip() #98: <Slot D1><Well B9>
p200.dispense(29, plate2[66].top(-2)).touch_tip() #99: <Slot D1><Well C9>
p200.dispense(29, plate2[67].top(-2)).touch_tip() #100: <Slot D1><Well D9>
p200.dispense(29, plate2[68].top(-2)).touch_tip() #101: <Slot D1><Well E9>
p200.dispense(29, plate2[69].top(-2)).touch_tip() #102: <Slot D1><Well F9>

p200.aspirate(174, trough['A3'].bottom(66))
p200.dispense(29, plate2[70].top(-2)).touch_tip() #103: <Slot D1><Well G9>
p200.dispense(29, plate2[71].top(-2)).touch_tip() #104: <Slot D1><Well H9>
p200.dispense(58, plate2[56].top(-2)).touch_tip() #105: <Slot D1><Well A8>
p200.dispense(58, plate2[57].top(-2)).touch_tip() #106: <Slot D1><Well B8>

p200.aspirate(174, trough['A3'].bottom(66))
p200.dispense(58, plate2[58].top(-2)).touch_tip() #107: <Slot D1><Well C8>
p200.dispense(58, plate2[59].top(-2)).touch_tip() #108: <Slot D1><Well D8>
p200.dispense(58, plate2[60].top(-2)).touch_tip() #109: <Slot D1><Well E8>

p200.aspirate(174, trough['A3'].bottom(66))
p200.dispense(58, plate2[61].top(-2)).touch_tip() #110: <Slot D1><Well F8>
p200.dispense(58, plate2[62].top(-2)).touch_tip() #111: <Slot D1><Well G8>
p200.dispense(58, plate2[63].top(-2)).touch_tip() #112: <Slot D1><Well H8>

p200.aspirate(172, trough['A3'].bottom(65))
p200.dispense(86, plate2[48].top(-2)).touch_tip() #113: <Slot D1><Well A7>
p200.dispense(86, plate2[49].top(-2)).touch_tip() #114: <Slot D1><Well B7>

p200.aspirate(172, trough['A3'].bottom(65))
p200.dispense(86, plate2[50].top(-2)).touch_tip() #115: <Slot D1><Well C7>
p200.dispense(86, plate2[51].top(-2)).touch_tip() #116: <Slot D1><Well D7>

p200.aspirate(172, trough['A3'].bottom(65))
p200.dispense(86, plate2[52].top(-2)).touch_tip() #117: <Slot D1><Well E7>
p200.dispense(86, plate2[53].top(-2)).touch_tip() #118: <Slot D1><Well F7>

p200.aspirate(172, trough['A3'].bottom(64))
p200.dispense(86, plate2[54].top(-2)).touch_tip() #119: <Slot D1><Well G7>
p200.dispense(86, plate2[55].top(-2)).touch_tip() #120: <Slot D1><Well H7>

p200.aspirate(108, trough['A3'].bottom(64))
p200.dispense(108, plate2[40].top(-2)).touch_tip() #121: <Slot D1><Well A6>

p200.aspirate(108, trough['A3'].bottom(64))
p200.dispense(108, plate2[41].top(-2)).touch_tip() #122: <Slot D1><Well B6>

p200.aspirate(108, trough['A3'].bottom(64))
p200.dispense(108, plate2[42].top(-2)).touch_tip() #123: <Slot D1><Well C6>

p200.aspirate(108, trough['A3'].bottom(64))
p200.dispense(108, plate2[43].top(-2)).touch_tip() #124: <Slot D1><Well D6>

p200.aspirate(108, trough['A3'].bottom(63))
p200.dispense(108, plate2[44].top(-2)).touch_tip() #125: <Slot D1><Well E6>

p200.aspirate(108, trough['A3'].bottom(63))
p200.dispense(108, plate2[45].top(-2)).touch_tip() #126: <Slot D1><Well F6>

p200.aspirate(108, trough['A3'].bottom(63))
p200.dispense(108, plate2[46].top(-2)).touch_tip() #127: <Slot D1><Well G6>

p200.aspirate(108, trough['A3'].bottom(63))
p200.dispense(108, plate2[47].top(-2)).touch_tip() #128: <Slot D1><Well H6>

p200.aspirate(144, trough['A3'].bottom(63))
p200.dispense(144, plate2[32].top(-2)).touch_tip() #129: <Slot D1><Well A5>

p200.aspirate(144, trough['A3'].bottom(62))
p200.dispense(144, plate2[33].top(-2)).touch_tip() #130: <Slot D1><Well B5>

p200.aspirate(144, trough['A3'].bottom(62))
p200.dispense(144, plate2[34].top(-2)).touch_tip() #131: <Slot D1><Well C5>

p200.aspirate(144, trough['A3'].bottom(62))
p200.dispense(144, plate2[35].top(-2)).touch_tip() #132: <Slot D1><Well D5>

p200.aspirate(144, trough['A3'].bottom(62))
p200.dispense(144, plate2[36].top(-2)).touch_tip() #133: <Slot D1><Well E5>

p200.aspirate(144, trough['A3'].bottom(61))
p200.dispense(144, plate2[37].top(-2)).touch_tip() #134: <Slot D1><Well F5>

p200.aspirate(144, trough['A3'].bottom(61))
p200.dispense(144, plate2[38].top(-2)).touch_tip() #135: <Slot D1><Well G5>

p200.aspirate(144, trough['A3'].bottom(61))
p200.dispense(144, plate2[39].top(-2)).touch_tip() #136: <Slot D1><Well H5>

p200.aspirate(147, trough['A3'].bottom(60))
p200.dispense(147, plate2[88].top(-2)).touch_tip() #137: <Slot D1><Well A12>

p200.aspirate(147, trough['A3'].bottom(60))
p200.dispense(147, plate2[89].top(-2)).touch_tip() #138: <Slot D1><Well B12>

p200.aspirate(147, trough['A3'].bottom(60))
p200.dispense(147, plate2[90].top(-2)).touch_tip() #139: <Slot D1><Well C12>

p200.aspirate(147, trough['A3'].bottom(60))
p200.dispense(147, plate2[91].top(-2)).touch_tip() #140: <Slot D1><Well D12>

p200.aspirate(147, trough['A3'].bottom(59))
p200.dispense(147, plate2[92].top(-2)).touch_tip() #141: <Slot D1><Well E12>

p200.aspirate(147, trough['A3'].bottom(59))
p200.dispense(147, plate2[93].top(-2)).touch_tip() #142: <Slot D1><Well F12>

p200.aspirate(147, trough['A3'].bottom(59))
p200.dispense(147, plate2[94].top(-2)).touch_tip() #143: <Slot D1><Well G12>

p200.aspirate(147, trough['A3'].bottom(59))
p200.dispense(147, plate2[95].top(-2)).touch_tip() #144: <Slot D1><Well H12>

p200.aspirate(154, trough['A3'].bottom(58))
p200.dispense(154, plate2[80].top(-2)).touch_tip() #145: <Slot D1><Well A11>

p200.aspirate(154, trough['A3'].bottom(58))
p200.dispense(154, plate2[81].top(-2)).touch_tip() #146: <Slot D1><Well B11>

p200.aspirate(154, trough['A3'].bottom(58))
p200.dispense(154, plate2[82].top(-2)).touch_tip() #147: <Slot D1><Well C11>

p200.aspirate(154, trough['A3'].bottom(58))
p200.dispense(154, plate2[83].top(-2)).touch_tip() #148: <Slot D1><Well D11>

p200.aspirate(154, trough['A3'].bottom(57))
p200.dispense(154, plate2[84].top(-2)).touch_tip() #149: <Slot D1><Well E11>

p200.aspirate(154, trough['A3'].bottom(57))
p200.dispense(154, plate2[85].top(-2)).touch_tip() #150: <Slot D1><Well F11>

p200.aspirate(154, trough['A3'].bottom(57))
p200.dispense(154, plate2[86].top(-2)).touch_tip() #151: <Slot D1><Well G11>

p200.aspirate(154, trough['A3'].bottom(56))
p200.dispense(154, plate2[87].top(-2)).touch_tip() #152: <Slot D1><Well H11>

p200.aspirate(160, trough['A3'].bottom(56))
p200.dispense(160, plate2[72].top(-2)).touch_tip() #153: <Slot D1><Well A10>

p200.aspirate(160, trough['A3'].bottom(56))
p200.dispense(160, plate2[73].top(-2)).touch_tip() #154: <Slot D1><Well B10>

p200.aspirate(160, trough['A3'].bottom(56))
p200.dispense(160, plate2[74].top(-2)).touch_tip() #155: <Slot D1><Well C10>

p200.aspirate(160, trough['A3'].bottom(55))
p200.dispense(160, plate2[75].top(-2)).touch_tip() #156: <Slot D1><Well D10>

p200.aspirate(160, trough['A3'].bottom(55))
p200.dispense(160, plate2[76].top(-2)).touch_tip() #157: <Slot D1><Well E10>

p200.aspirate(160, trough['A3'].bottom(55))
p200.dispense(160, plate2[77].top(-2)).touch_tip() #158: <Slot D1><Well F10>

p200.aspirate(160, trough['A3'].bottom(54))
p200.dispense(160, plate2[78].top(-2)).touch_tip() #159: <Slot D1><Well G10>

p200.aspirate(160, trough['A3'].bottom(54))
p200.dispense(160, plate2[79].top(-2)).touch_tip() #160: <Slot D1><Well H10>

p200.aspirate(162, trough['A3'].bottom(54))
p200.dispense(162, plate2[24].top(-2)).touch_tip() #161: <Slot D1><Well A4>

p200.aspirate(162, trough['A3'].bottom(53))
p200.dispense(162, plate2[25].top(-2)).touch_tip() #162: <Slot D1><Well B4>

p200.aspirate(162, trough['A3'].bottom(53))
p200.dispense(162, plate2[26].top(-2)).touch_tip() #163: <Slot D1><Well C4>

p200.aspirate(162, trough['A3'].bottom(53))
p200.dispense(162, plate2[27].top(-2)).touch_tip() #164: <Slot D1><Well D4>

p200.aspirate(162, trough['A3'].bottom(53))
p200.dispense(162, plate2[28].top(-2)).touch_tip() #165: <Slot D1><Well E4>

p200.aspirate(162, trough['A3'].bottom(52))
p200.dispense(162, plate2[29].top(-2)).touch_tip() #166: <Slot D1><Well F4>

p200.aspirate(162, trough['A3'].bottom(52))
p200.dispense(162, plate2[30].top(-2)).touch_tip() #167: <Slot D1><Well G4>

p200.aspirate(162, trough['A3'].bottom(52))
p200.dispense(162, plate2[31].top(-2)).touch_tip() #168: <Slot D1><Well H4>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[0].top(-2)).touch_tip() #169: <Slot D1><Well A1>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[8].top(-2)).touch_tip() #170: <Slot D1><Well A2>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[16].top(-2)).touch_tip() #171: <Slot D1><Well A3>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[1].top(-2)).touch_tip() #172: <Slot D1><Well B1>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[9].top(-2)).touch_tip() #173: <Slot D1><Well B2>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[17].top(-2)).touch_tip() #174: <Slot D1><Well B3>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[2].top(-2)).touch_tip() #175: <Slot D1><Well C1>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[10].top(-2)).touch_tip() #176: <Slot D1><Well C2>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[18].top(-2)).touch_tip() #177: <Slot D1><Well C3>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[3].top(-2)).touch_tip() #178: <Slot D1><Well D1>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[11].top(-2)).touch_tip() #179: <Slot D1><Well D2>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[19].top(-2)).touch_tip() #180: <Slot D1><Well D3>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[4].top(-2)).touch_tip() #181: <Slot D1><Well E1>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[12].top(-2)).touch_tip() #182: <Slot D1><Well E2>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[20].top(-2)).touch_tip() #183: <Slot D1><Well E3>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[5].top(-2)).touch_tip() #184: <Slot D1><Well F1>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[13].top(-2)).touch_tip() #185: <Slot D1><Well F2>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[21].top(-2)).touch_tip() #186: <Slot D1><Well F3>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[6].top(-2)).touch_tip() #187: <Slot D1><Well G1>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[14].top(-2)).touch_tip() #188: <Slot D1><Well G2>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[22].top(-2)).touch_tip() #189: <Slot D1><Well G3>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[7].top(-2)).touch_tip() #190: <Slot D1><Well H1>

p200.aspirate(180, trough['A3'].bottom(44))
p200.dispense(180, plate2[15].top(-2)).touch_tip() #191: <Slot D1><Well H2>

p200.aspirate(180, trough['A3'].bottom(44))
p200.dispense(180, plate2[23].top(-2)).touch_tip() #192: <Slot D1><Well H3>

p200.drop_tip()
p200.pick_up_tip(p200rack['1'])

# *********** Dispense WS_1000

p200.aspirate(160, trough['B1'].bottom(89))
p200.dispense(20, plate1[72].top(-2)).touch_tip() #193 <Slot C1><Well A10>
p200.dispense(20, plate1[73].top(-2)).touch_tip() #194: <Slot C1><Well B10>
p200.dispense(20, plate1[74].top(-2)).touch_tip() #195: <Slot C1><Well C10>
p200.dispense(20, plate1[75].top(-2)).touch_tip() #196: <Slot C1><Well D10>
p200.dispense(20, plate1[76].top(-2)).touch_tip() #197: <Slot C1><Well E10>
p200.dispense(20, plate1[77].top(-2)).touch_tip() #198: <Slot C1><Well F10>
p200.dispense(20, plate1[78].top(-2)).touch_tip() #199: <Slot C1><Well G10>
p200.dispense(20, plate1[79].top(-2)).touch_tip() #200: <Slot C1><Well H10>

p200.aspirate(156, trough['B1'].bottom(88))
p200.dispense(26, plate1[80].top(-2)).touch_tip() #201: <Slot C1><Well A11>
p200.dispense(26, plate1[81].top(-2)).touch_tip() #202: <Slot C1><Well B11>
p200.dispense(26, plate1[82].top(-2)).touch_tip() #203: <Slot C1><Well C11>
p200.dispense(26, plate1[83].top(-2)).touch_tip() #204: <Slot C1><Well D11>
p200.dispense(26, plate1[84].top(-2)).touch_tip() #205: <Slot C1><Well E11>
p200.dispense(26, plate1[85].top(-2)).touch_tip() #206: <Slot C1><Well F11>

p200.aspirate(151, trough['B1'].bottom(87))
p200.dispense(26, plate1[86].top(-2)).touch_tip() #207: <Slot C1><Well G11>
p200.dispense(26, plate1[87].top(-2)).touch_tip() #208: <Slot C1><Well H11>
p200.dispense(33, plate1[88].top(-2)).touch_tip() #209: <Slot C1><Well A12>
p200.dispense(33, plate1[89].top(-2)).touch_tip() #210: <Slot C1><Well B12>
p200.dispense(33, plate1[90].top(-2)).touch_tip() #211: <Slot C1><Well C12>

p200.aspirate(165, trough['B1'].bottom(86))
p200.dispense(33, plate1[91].top(-2)).touch_tip() #212: <Slot C1><Well D12>
p200.dispense(33, plate1[92].top(-2)).touch_tip() #213: <Slot C1><Well E12>
p200.dispense(33, plate1[93].top(-2)).touch_tip() #214: <Slot C1><Well F12>
p200.dispense(33, plate1[94].top(-2)).touch_tip() #215: <Slot C1><Well G12>
p200.dispense(33, plate1[95].top(-2)).touch_tip() #216: <Slot C1><Well H12>

p200.aspirate(160, trough['B1'].bottom(85))
p200.dispense(20, plate2[72].top(-2)).touch_tip() #217: <Slot D1><Well A10>
p200.dispense(20, plate2[73].top(-2)).touch_tip() #218: <Slot D1><Well B10>
p200.dispense(20, plate2[74].top(-2)).touch_tip() #219: <Slot D1><Well C10>
p200.dispense(20, plate2[75].top(-2)).touch_tip() #220: <Slot D1><Well D10>
p200.dispense(20, plate2[76].top(-2)).touch_tip() #221: <Slot D1><Well E10>
p200.dispense(20, plate2[77].top(-2)).touch_tip() #222: <Slot D1><Well F10>
p200.dispense(20, plate2[78].top(-2)).touch_tip() #223: <Slot D1><Well G10>
p200.dispense(20, plate2[79].top(-2)).touch_tip() #224: <Slot D1><Well H10>

p200.aspirate(156, trough['B1'].bottom(84))
p200.dispense(26, plate2[80].top(-2)).touch_tip() #225: <Slot D1><Well A11>
p200.dispense(26, plate2[81].top(-2)).touch_tip() #226: <Slot D1><Well B11>
p200.dispense(26, plate2[82].top(-2)).touch_tip() #227: <Slot D1><Well C11>
p200.dispense(26, plate2[83].top(-2)).touch_tip() #228: <Slot D1><Well D11>
p200.dispense(26, plate2[84].top(-2)).touch_tip() #229: <Slot D1><Well E11>
p200.dispense(26, plate2[85].top(-2)).touch_tip() #230: <Slot D1><Well F11>

p200.aspirate(151, trough['B1'].bottom(83))
p200.dispense(26, plate2[86].top(-2)).touch_tip() #231: <Slot D1><Well G11>
p200.dispense(26, plate2[87].top(-2)).touch_tip() #232: <Slot D1><Well H11>
p200.dispense(33, plate2[88].top(-2)).touch_tip() #233: <Slot D1><Well A12>
p200.dispense(33, plate2[89].top(-2)).touch_tip() #234: <Slot D1><Well B12>
p200.dispense(33, plate2[90].top(-2)).touch_tip() #235: <Slot D1><Well C12>

p200.aspirate(165, trough['B1'].bottom(82))
p200.dispense(33, plate2[91].top(-2)).touch_tip() #236: <Slot D1><Well D12>
p200.dispense(33, plate2[92].top(-2)).touch_tip() #237: <Slot D1><Well E12>
p200.dispense(33, plate2[93].top(-2)).touch_tip() #238: <Slot D1><Well F12>
p200.dispense(33, plate2[94].top(-2)).touch_tip() #239: <Slot D1><Well G12>
p200.dispense(33, plate2[95].top(-2)).touch_tip() #240: <Slot D1><Well H12>

p200.drop_tip()
p200.pick_up_tip(p200rack['2'])

# *********** Dispense WS_10000

p200.aspirate(180, trough['A1'].bottom(89))
p200.dispense(18, plate1[24].top(-2)).touch_tip() #241 <Slot C1><Well A4>
p200.dispense(18, plate1[25].top(-2)).touch_tip() #242: <Slot C1><Well B4>
p200.dispense(18, plate1[26].top(-2)).touch_tip() #243: <Slot C1><Well C4>
p200.dispense(18, plate1[27].top(-2)).touch_tip() #244: <Slot C1><Well D4>
p200.dispense(18, plate1[28].top(-2)).touch_tip() #245: <Slot C1><Well E4>
p200.dispense(18, plate1[29].top(-2)).touch_tip() #246: <Slot C1><Well F4>
p200.dispense(18, plate1[30].top(-2)).touch_tip() #247: <Slot C1><Well G4>
p200.dispense(18, plate1[31].top(-2)).touch_tip() #248: <Slot C1><Well H4>
p200.dispense(36, plate1[32].top(-2)).touch_tip() #249: <Slot C1><Well A5>

p200.aspirate(180, trough['A1'].bottom(88))
p200.dispense(36, plate1[33].top(-2)).touch_tip() #250: <Slot C1><Well B5>
p200.dispense(36, plate1[34].top(-2)).touch_tip() #251: <Slot C1><Well C5>
p200.dispense(36, plate1[35].top(-2)).touch_tip() #252: <Slot C1><Well D5>
p200.dispense(36, plate1[36].top(-2)).touch_tip() #253: <Slot C1><Well E5>
p200.dispense(36, plate1[37].top(-2)).touch_tip() #254: <Slot C1><Well F5>

p200.aspirate(144, trough['A1'].bottom(87))
p200.dispense(36, plate1[38].top(-2)).touch_tip() #255: <Slot C1><Well G5>
p200.dispense(36, plate1[39].top(-2)).touch_tip() #256: <Slot C1><Well H5>
p200.dispense(72, plate1[40].top(-2)).touch_tip() #257: <Slot C1><Well A6>

p200.aspirate(144, trough['A1'].bottom(86))
p200.dispense(72, plate1[41].top(-2)).touch_tip() #258: <Slot C1><Well B6>
p200.dispense(72, plate1[42].top(-2)).touch_tip() #259: <Slot C1><Well C6>

p200.aspirate(144, trough['A1'].bottom(85))
p200.dispense(72, plate1[43].top(-2)).touch_tip() #260: <Slot C1><Well D6>
p200.dispense(72, plate1[44].top(-2)).touch_tip() #261: <Slot C1><Well E6>

p200.aspirate(144, trough['A1'].bottom(84))
p200.dispense(72, plate1[45].top(-2)).touch_tip() #262: <Slot C1><Well F6>
p200.dispense(72, plate1[46].top(-2)).touch_tip() #263: <Slot C1><Well G6>

p200.aspirate(166, trough['A1'].bottom(83))
p200.dispense(72, plate1[47].top(-2)).touch_tip() #264: <Slot C1><Well H6>
p200.dispense(94, plate1[48].top(-2)).touch_tip() #265: <Slot C1><Well A7>

p200.aspirate(94, trough['A1'].bottom(82))
p200.dispense(94, plate1[49].top(-2)).touch_tip() #266: <Slot C1><Well B7>

p200.aspirate(94, trough['A1'].bottom(82))
p200.dispense(94, plate1[50].top(-2)).touch_tip() #267: <Slot C1><Well C7>

p200.aspirate(94, trough['A1'].bottom(81))
p200.dispense(94, plate1[51].top(-2)).touch_tip() #268: <Slot C1><Well D7>

p200.aspirate(94, trough['A1'].bottom(81))
p200.dispense(94, plate1[52].top(-2)).touch_tip() #269: <Slot C1><Well E7>

p200.aspirate(94, trough['A1'].bottom(80))
p200.dispense(94, plate1[53].top(-2)).touch_tip() #270: <Slot C1><Well F7>

p200.aspirate(94, trough['A1'].bottom(79))
p200.dispense(94, plate1[54].top(-2)).touch_tip() #271: <Slot C1><Well G7>

p200.aspirate(94, trough['A1'].bottom(79))
p200.dispense(94, plate1[55].top(-2)).touch_tip() #272: <Slot C1><Well H7>

p200.aspirate(122, trough['A1'].bottom(78))
p200.dispense(122, plate1[56].top(-2)).touch_tip() #273: <Slot C1><Well A8>

p200.aspirate(122, trough['A1'].bottom(77))
p200.dispense(122, plate1[57].top(-2)).touch_tip() #274: <Slot C1><Well B8>

p200.aspirate(122, trough['A1'].bottom(77))
p200.dispense(122, plate1[58].top(-2)).touch_tip() #275: <Slot C1><Well C8>

p200.aspirate(122, trough['A1'].bottom(76))
p200.dispense(122, plate1[59].top(-2)).touch_tip() #276: <Slot C1><Well D8>

p200.aspirate(122, trough['A1'].bottom(75))
p200.dispense(122, plate1[60].top(-2)).touch_tip() #277: <Slot C1><Well E8>

p200.aspirate(122, trough['A1'].bottom(74))
p200.dispense(122, plate1[61].top(-2)).touch_tip() #278: <Slot C1><Well F8>

p200.aspirate(122, trough['A1'].bottom(74))
p200.dispense(122, plate1[62].top(-2)).touch_tip() #279: <Slot C1><Well G8>

p200.aspirate(122, trough['A1'].bottom(73))
p200.dispense(122, plate1[63].top(-2)).touch_tip() #280: <Slot C1><Well H8>

p200.aspirate(151, trough['A1'].bottom(72))
p200.dispense(151, plate1[64].top(-2)).touch_tip() #281: <Slot C1><Well A9>

p200.aspirate(151, trough['A1'].bottom(71))
p200.dispense(151, plate1[65].top(-2)).touch_tip() #282: <Slot C1><Well B9>

p200.aspirate(151, trough['A1'].bottom(70))
p200.dispense(151, plate1[66].top(-2)).touch_tip() #283: <Slot C1><Well C9>

p200.aspirate(151, trough['A1'].bottom(69))
p200.dispense(151, plate1[67].top(-2)).touch_tip() #284: <Slot C1><Well D9>

p200.aspirate(151, trough['A1'].bottom(68))
p200.dispense(151, plate1[68].top(-2)).touch_tip() #285: <Slot C1><Well E9>

p200.aspirate(151, trough['A1'].bottom(67))
p200.dispense(151, plate1[69].top(-2)).touch_tip() #286: <Slot C1><Well F9>

p200.aspirate(151, trough['A1'].bottom(66))
p200.dispense(151, plate1[70].top(-2)).touch_tip() #287: <Slot C1><Well G9>

p200.aspirate(169, trough['A1'].bottom(66))
p200.dispense(151, plate1[71].top(-2)).touch_tip() #288: <Slot C1><Well H9>
p200.dispense(18, plate2[24].top(-2)).touch_tip() #289: <Slot D1><Well A4>

p200.aspirate(162, trough['A1'].bottom(65))
p200.dispense(18, plate2[25].top(-2)).touch_tip() #290: <Slot D1><Well B4>
p200.dispense(18, plate2[26].top(-2)).touch_tip() #291: <Slot D1><Well C4>
p200.dispense(18, plate2[27].top(-2)).touch_tip() #292: <Slot D1><Well D4>
p200.dispense(18, plate2[28].top(-2)).touch_tip() #293: <Slot D1><Well E4>
p200.dispense(18, plate2[29].top(-2)).touch_tip() #294: <Slot D1><Well F4>
p200.dispense(18, plate2[30].top(-2)).touch_tip() #295: <Slot D1><Well G4>
p200.dispense(18, plate2[31].top(-2)).touch_tip() #296: <Slot D1><Well H4>
p200.dispense(36, plate2[32].top(-2)).touch_tip() #297: <Slot D1><Well A5>

p200.aspirate(180, trough['A1'].bottom(64))
p200.dispense(36, plate2[33].top(-2)).touch_tip() #298: <Slot D1><Well B5>
p200.dispense(36, plate2[34].top(-2)).touch_tip() #299: <Slot D1><Well C5>
p200.dispense(36, plate2[35].top(-2)).touch_tip() #300: <Slot D1><Well D5>
p200.dispense(36, plate2[36].top(-2)).touch_tip() #301: <Slot D1><Well E5>
p200.dispense(36, plate2[37].top(-2)).touch_tip() #302: <Slot D1><Well F5>

p200.aspirate(144, trough['A1'].bottom(63))
p200.dispense(36, plate2[38].top(-2)).touch_tip() #303: <Slot D1><Well G5>
p200.dispense(36, plate2[39].top(-2)).touch_tip() #304: <Slot D1><Well H5>
p200.dispense(72, plate2[40].top(-2)).touch_tip() #305: <Slot D1><Well A6>

p200.aspirate(144, trough['A1'].bottom(62))
p200.dispense(72, plate2[41].top(-2)).touch_tip() #306: <Slot D1><Well B6>
p200.dispense(72, plate2[42].top(-2)).touch_tip() #307: <Slot D1><Well C6>

p200.aspirate(144, trough['A1'].bottom(61))
p200.dispense(72, plate2[43].top(-2)).touch_tip() #308: <Slot D1><Well D6>
p200.dispense(72, plate2[44].top(-2)).touch_tip() #309: <Slot D1><Well E6>

p200.aspirate(144, trough['A1'].bottom(60))
p200.dispense(72, plate2[45].top(-2)).touch_tip() #310: <Slot D1><Well F6>
p200.dispense(72, plate2[46].top(-2)).touch_tip() #311: <Slot D1><Well G6>

p200.aspirate(166, trough['A1'].bottom(59))
p200.dispense(72, plate2[47].top(-2)).touch_tip() #312: <Slot D1><Well H6>
p200.dispense(94, plate2[48].top(-2)).touch_tip() #313: <Slot D1><Well A7>

p200.aspirate(94, trough['A1'].bottom(59))
p200.dispense(94, plate2[49].top(-2)).touch_tip() #314: <Slot D1><Well B7>

p200.aspirate(94, trough['A1'].bottom(58))
p200.dispense(94, plate2[50].top(-2)).touch_tip() #315: <Slot D1><Well C7>

p200.aspirate(94, trough['A1'].bottom(57))
p200.dispense(94, plate2[51].top(-2)).touch_tip() #316: <Slot D1><Well D7>

p200.aspirate(94, trough['A1'].bottom(57))
p200.dispense(94, plate2[52].top(-2)).touch_tip() #317: <Slot D1><Well E7>

p200.aspirate(94, trough['A1'].bottom(56))
p200.dispense(94, plate2[53].top(-2)).touch_tip() #318: <Slot D1><Well F7>

p200.aspirate(94, trough['A1'].bottom(56))
p200.dispense(94, plate2[54].top(-2)).touch_tip() #319: <Slot D1><Well G7>

p200.aspirate(94, trough['A1'].bottom(55))
p200.dispense(94, plate2[55].top(-2)).touch_tip() #320: <Slot D1><Well H7>

p200.aspirate(122, trough['A1'].bottom(54))
p200.dispense(122, plate2[56].top(-2)).touch_tip() #321: <Slot D1><Well A8>

p200.aspirate(122, trough['A1'].bottom(54))
p200.dispense(122, plate2[57].top(-2)).touch_tip() #322: <Slot D1><Well B8>

p200.aspirate(122, trough['A1'].bottom(53))
p200.dispense(122, plate2[58].top(-2)).touch_tip() #323: <Slot D1><Well C8>

p200.aspirate(122, trough['A1'].bottom(52))
p200.dispense(122, plate2[59].top(-2)).touch_tip() #324: <Slot D1><Well D8>

p200.aspirate(122, trough['A1'].bottom(51))
p200.dispense(122, plate2[60].top(-2)).touch_tip() #325: <Slot D1><Well E8>

p200.aspirate(122, trough['A1'].bottom(51))
p200.dispense(122, plate2[61].top(-2)).touch_tip() #326: <Slot D1><Well F8>

p200.aspirate(122, trough['A1'].bottom(50))
p200.dispense(122, plate2[62].top(-2)).touch_tip() #327: <Slot D1><Well G8>

p200.aspirate(122, trough['A1'].bottom(49))
p200.dispense(122, plate2[63].top(-2)).touch_tip() #328: <Slot D1><Well H8>

p200.aspirate(151, trough['A1'].bottom(48))
p200.dispense(151, plate2[64].top(-2)).touch_tip() #329: <Slot D1><Well A9>

p200.aspirate(151, trough['A1'].bottom(47))
p200.dispense(151, plate2[65].top(-2)).touch_tip() #330: <Slot D1><Well B9>

p200.aspirate(151, trough['A1'].bottom(46))
p200.dispense(151, plate2[66].top(-2)).touch_tip() #331: <Slot D1><Well C9>

p200.aspirate(151, trough['A1'].bottom(45))
p200.dispense(151, plate2[67].top(-2)).touch_tip() #332: <Slot D1><Well D9>

p200.aspirate(151, trough['A1'].bottom(44))
p200.dispense(151, plate2[68].top(-2)).touch_tip() #333: <Slot D1><Well E9>

p200.aspirate(151, trough['A1'].bottom(44))
p200.dispense(151, plate2[69].top(-2)).touch_tip() #334: <Slot D1><Well F9>

p200.aspirate(151, trough['A1'].bottom(43))
p200.dispense(151, plate2[70].top(-2)).touch_tip() #335: <Slot D1><Well G9>

p200.aspirate(151, trough['A1'].bottom(43))
p200.dispense(151, plate2[71].top(-2)).touch_tip() #336: <Slot D1><Well H9>

p200.drop_tip()
##