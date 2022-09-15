

###################################################################################
#
# SCRIPT GENERATED ON 06/02/2017 FROM THE FOLLOWING LAYOUT FILES:
#  fileDictName=layouts/EvoAMP_key_dict.txt
#  fileTroughName=layouts/EvoAMP_trough_layout.txt
#  fileLayoutName=layouts/EvoAMP_layout_1plate.txt
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
plate1 = containers.load('96-PCR-flat','C2','plate-1')
trash = containers.load('point','A1','trash')
p200 = instruments.Pipette(name='p200',trash_container=trash,tip_racks=[p200rack],min_volume=18,axis='b',channels=1)

p200.set_max_volume(180)

p200.pick_up_tip(p200rack['0'])
p200.move_to(plate1[0].bottom(), 'arc')
p200.move_to(plate1[95].bottom(), 'arc')

# *********** Dispense M9

p200.aspirate(158, trough['A3'].bottom(90))
p200.dispense(25, plate1[41].top(-2)).touch_tip() #1 <Slot C2><Well B6>
p200.dispense(25, plate1[43].top(-2)).touch_tip() #2: <Slot C2><Well D6>
p200.dispense(25, plate1[45].top(-2)).touch_tip() #3: <Slot C2><Well F6>
p200.dispense(25, plate1[47].top(-2)).touch_tip() #4: <Slot C2><Well H6>
p200.dispense(29, plate1[64].top(-2)).touch_tip() #5: <Slot C2><Well A9>
p200.dispense(29, plate1[66].top(-2)).touch_tip() #6: <Slot C2><Well C9>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(29, plate1[68].top(-2)).touch_tip() #7: <Slot C2><Well E9>
p200.dispense(29, plate1[70].top(-2)).touch_tip() #8: <Slot C2><Well G9>
p200.dispense(58, plate1[56].top(-2)).touch_tip() #9: <Slot C2><Well A8>
p200.dispense(58, plate1[33].top(-2)).touch_tip() #10: <Slot C2><Well B5>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(58, plate1[58].top(-2)).touch_tip() #11: <Slot C2><Well C8>
p200.dispense(58, plate1[35].top(-2)).touch_tip() #12: <Slot C2><Well D5>
p200.dispense(58, plate1[60].top(-2)).touch_tip() #13: <Slot C2><Well E8>

p200.aspirate(174, trough['A3'].bottom(89))
p200.dispense(58, plate1[37].top(-2)).touch_tip() #14: <Slot C2><Well F5>
p200.dispense(58, plate1[62].top(-2)).touch_tip() #15: <Slot C2><Well G8>
p200.dispense(58, plate1[39].top(-2)).touch_tip() #16: <Slot C2><Well H5>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[48].top(-2)).touch_tip() #17: <Slot C2><Well A7>
p200.dispense(86, plate1[25].top(-2)).touch_tip() #18: <Slot C2><Well B4>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[50].top(-2)).touch_tip() #19: <Slot C2><Well C7>
p200.dispense(86, plate1[27].top(-2)).touch_tip() #20: <Slot C2><Well D4>

p200.aspirate(172, trough['A3'].bottom(88))
p200.dispense(86, plate1[52].top(-2)).touch_tip() #21: <Slot C2><Well E7>
p200.dispense(86, plate1[29].top(-2)).touch_tip() #22: <Slot C2><Well F4>

p200.aspirate(172, trough['A3'].bottom(87))
p200.dispense(86, plate1[54].top(-2)).touch_tip() #23: <Slot C2><Well G7>
p200.dispense(86, plate1[31].top(-2)).touch_tip() #24: <Slot C2><Well H4>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[40].top(-2)).touch_tip() #25: <Slot C2><Well A6>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[17].top(-2)).touch_tip() #26: <Slot C2><Well B3>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[89].top(-2)).touch_tip() #27: <Slot C2><Well B12>

p200.aspirate(108, trough['A3'].bottom(87))
p200.dispense(108, plate1[42].top(-2)).touch_tip() #28: <Slot C2><Well C6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[19].top(-2)).touch_tip() #29: <Slot C2><Well D3>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[91].top(-2)).touch_tip() #30: <Slot C2><Well D12>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[44].top(-2)).touch_tip() #31: <Slot C2><Well E6>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[21].top(-2)).touch_tip() #32: <Slot C2><Well F3>

p200.aspirate(108, trough['A3'].bottom(86))
p200.dispense(108, plate1[93].top(-2)).touch_tip() #33: <Slot C2><Well F12>

p200.aspirate(108, trough['A3'].bottom(85))
p200.dispense(108, plate1[46].top(-2)).touch_tip() #34: <Slot C2><Well G6>

p200.aspirate(108, trough['A3'].bottom(85))
p200.dispense(108, plate1[23].top(-2)).touch_tip() #35: <Slot C2><Well H3>

p200.aspirate(108, trough['A3'].bottom(85))
p200.dispense(108, plate1[95].top(-2)).touch_tip() #36: <Slot C2><Well H12>

p200.aspirate(124, trough['A3'].bottom(85))
p200.dispense(124, plate1[81].top(-2)).touch_tip() #37: <Slot C2><Well B11>

p200.aspirate(124, trough['A3'].bottom(85))
p200.dispense(124, plate1[83].top(-2)).touch_tip() #38: <Slot C2><Well D11>

p200.aspirate(124, trough['A3'].bottom(84))
p200.dispense(124, plate1[85].top(-2)).touch_tip() #39: <Slot C2><Well F11>

p200.aspirate(124, trough['A3'].bottom(84))
p200.dispense(124, plate1[87].top(-2)).touch_tip() #40: <Slot C2><Well H11>

p200.aspirate(125, trough['A3'].bottom(84))
p200.dispense(125, plate1[9].top(-2)).touch_tip() #41: <Slot C2><Well B2>

p200.aspirate(125, trough['A3'].bottom(84))
p200.dispense(125, plate1[11].top(-2)).touch_tip() #42: <Slot C2><Well D2>

p200.aspirate(125, trough['A3'].bottom(83))
p200.dispense(125, plate1[13].top(-2)).touch_tip() #43: <Slot C2><Well F2>

p200.aspirate(125, trough['A3'].bottom(83))
p200.dispense(125, plate1[15].top(-2)).touch_tip() #44: <Slot C2><Well H2>

p200.aspirate(137, trough['A3'].bottom(83))
p200.dispense(137, plate1[73].top(-2)).touch_tip() #45: <Slot C2><Well B10>

p200.aspirate(137, trough['A3'].bottom(83))
p200.dispense(137, plate1[75].top(-2)).touch_tip() #46: <Slot C2><Well D10>

p200.aspirate(137, trough['A3'].bottom(82))
p200.dispense(137, plate1[77].top(-2)).touch_tip() #47: <Slot C2><Well F10>

p200.aspirate(137, trough['A3'].bottom(82))
p200.dispense(137, plate1[79].top(-2)).touch_tip() #48: <Slot C2><Well H10>

p200.aspirate(144, trough['A3'].bottom(82))
p200.dispense(144, plate1[32].top(-2)).touch_tip() #49: <Slot C2><Well A5>

p200.aspirate(144, trough['A3'].bottom(82))
p200.dispense(144, plate1[1].top(-2)).touch_tip() #50: <Slot C2><Well B1>

p200.aspirate(144, trough['A3'].bottom(81))
p200.dispense(144, plate1[34].top(-2)).touch_tip() #51: <Slot C2><Well C5>

p200.aspirate(144, trough['A3'].bottom(81))
p200.dispense(144, plate1[3].top(-2)).touch_tip() #52: <Slot C2><Well D1>

p200.aspirate(144, trough['A3'].bottom(81))
p200.dispense(144, plate1[36].top(-2)).touch_tip() #53: <Slot C2><Well E5>

p200.aspirate(144, trough['A3'].bottom(81))
p200.dispense(144, plate1[5].top(-2)).touch_tip() #54: <Slot C2><Well F1>

p200.aspirate(144, trough['A3'].bottom(80))
p200.dispense(144, plate1[38].top(-2)).touch_tip() #55: <Slot C2><Well G5>

p200.aspirate(144, trough['A3'].bottom(80))
p200.dispense(144, plate1[7].top(-2)).touch_tip() #56: <Slot C2><Well H1>

p200.aspirate(147, trough['A3'].bottom(80))
p200.dispense(147, plate1[88].top(-2)).touch_tip() #57: <Slot C2><Well A12>

p200.aspirate(147, trough['A3'].bottom(80))
p200.dispense(147, plate1[65].top(-2)).touch_tip() #58: <Slot C2><Well B9>

p200.aspirate(147, trough['A3'].bottom(79))
p200.dispense(147, plate1[90].top(-2)).touch_tip() #59: <Slot C2><Well C12>

p200.aspirate(147, trough['A3'].bottom(79))
p200.dispense(147, plate1[67].top(-2)).touch_tip() #60: <Slot C2><Well D9>

p200.aspirate(147, trough['A3'].bottom(79))
p200.dispense(147, plate1[92].top(-2)).touch_tip() #61: <Slot C2><Well E12>

p200.aspirate(147, trough['A3'].bottom(78))
p200.dispense(147, plate1[69].top(-2)).touch_tip() #62: <Slot C2><Well F9>

p200.aspirate(147, trough['A3'].bottom(78))
p200.dispense(147, plate1[94].top(-2)).touch_tip() #63: <Slot C2><Well G12>

p200.aspirate(147, trough['A3'].bottom(78))
p200.dispense(147, plate1[71].top(-2)).touch_tip() #64: <Slot C2><Well H9>

p200.aspirate(154, trough['A3'].bottom(78))
p200.dispense(154, plate1[80].top(-2)).touch_tip() #65: <Slot C2><Well A11>

p200.aspirate(154, trough['A3'].bottom(77))
p200.dispense(154, plate1[57].top(-2)).touch_tip() #66: <Slot C2><Well B8>

p200.aspirate(154, trough['A3'].bottom(77))
p200.dispense(154, plate1[82].top(-2)).touch_tip() #67: <Slot C2><Well C11>

p200.aspirate(154, trough['A3'].bottom(77))
p200.dispense(154, plate1[59].top(-2)).touch_tip() #68: <Slot C2><Well D8>

p200.aspirate(154, trough['A3'].bottom(77))
p200.dispense(154, plate1[84].top(-2)).touch_tip() #69: <Slot C2><Well E11>

p200.aspirate(154, trough['A3'].bottom(76))
p200.dispense(154, plate1[61].top(-2)).touch_tip() #70: <Slot C2><Well F8>

p200.aspirate(154, trough['A3'].bottom(76))
p200.dispense(154, plate1[86].top(-2)).touch_tip() #71: <Slot C2><Well G11>

p200.aspirate(154, trough['A3'].bottom(76))
p200.dispense(154, plate1[63].top(-2)).touch_tip() #72: <Slot C2><Well H8>

p200.aspirate(160, trough['A3'].bottom(75))
p200.dispense(160, plate1[72].top(-2)).touch_tip() #73: <Slot C2><Well A10>

p200.aspirate(160, trough['A3'].bottom(75))
p200.dispense(160, plate1[49].top(-2)).touch_tip() #74: <Slot C2><Well B7>

p200.aspirate(160, trough['A3'].bottom(75))
p200.dispense(160, plate1[74].top(-2)).touch_tip() #75: <Slot C2><Well C10>

p200.aspirate(160, trough['A3'].bottom(75))
p200.dispense(160, plate1[51].top(-2)).touch_tip() #76: <Slot C2><Well D7>

p200.aspirate(160, trough['A3'].bottom(74))
p200.dispense(160, plate1[76].top(-2)).touch_tip() #77: <Slot C2><Well E10>

p200.aspirate(160, trough['A3'].bottom(74))
p200.dispense(160, plate1[53].top(-2)).touch_tip() #78: <Slot C2><Well F7>

p200.aspirate(160, trough['A3'].bottom(74))
p200.dispense(160, plate1[78].top(-2)).touch_tip() #79: <Slot C2><Well G10>

p200.aspirate(160, trough['A3'].bottom(73))
p200.dispense(160, plate1[55].top(-2)).touch_tip() #80: <Slot C2><Well H7>

p200.aspirate(162, trough['A3'].bottom(73))
p200.dispense(162, plate1[24].top(-2)).touch_tip() #81: <Slot C2><Well A4>

p200.aspirate(162, trough['A3'].bottom(73))
p200.dispense(162, plate1[26].top(-2)).touch_tip() #82: <Slot C2><Well C4>

p200.aspirate(162, trough['A3'].bottom(73))
p200.dispense(162, plate1[28].top(-2)).touch_tip() #83: <Slot C2><Well E4>

p200.aspirate(162, trough['A3'].bottom(72))
p200.dispense(162, plate1[30].top(-2)).touch_tip() #84: <Slot C2><Well G4>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[0].top(-2)).touch_tip() #85: <Slot C2><Well A1>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[8].top(-2)).touch_tip() #86: <Slot C2><Well A2>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[16].top(-2)).touch_tip() #87: <Slot C2><Well A3>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[2].top(-2)).touch_tip() #88: <Slot C2><Well C1>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[10].top(-2)).touch_tip() #89: <Slot C2><Well C2>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[18].top(-2)).touch_tip() #90: <Slot C2><Well C3>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[4].top(-2)).touch_tip() #91: <Slot C2><Well E1>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[12].top(-2)).touch_tip() #92: <Slot C2><Well E2>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[20].top(-2)).touch_tip() #93: <Slot C2><Well E3>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[6].top(-2)).touch_tip() #94: <Slot C2><Well G1>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[14].top(-2)).touch_tip() #95: <Slot C2><Well G2>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[22].top(-2)).touch_tip() #96: <Slot C2><Well G3>

p200.drop_tip()
p200.pick_up_tip(p200rack['1'])

# *********** Dispense WS_100

p200.aspirate(158, trough['C1'].bottom(89))
p200.dispense(20, plate1[49].top(-2)).touch_tip() #97 <Slot C2><Well B7>
p200.dispense(20, plate1[51].top(-2)).touch_tip() #98: <Slot C2><Well D7>
p200.dispense(20, plate1[53].top(-2)).touch_tip() #99: <Slot C2><Well F7>
p200.dispense(20, plate1[55].top(-2)).touch_tip() #100: <Slot C2><Well H7>
p200.dispense(26, plate1[57].top(-2)).touch_tip() #101: <Slot C2><Well B8>
p200.dispense(26, plate1[59].top(-2)).touch_tip() #102: <Slot C2><Well D8>
p200.dispense(26, plate1[61].top(-2)).touch_tip() #103: <Slot C2><Well F8>

p200.aspirate(158, trough['C1'].bottom(88))
p200.dispense(26, plate1[63].top(-2)).touch_tip() #104: <Slot C2><Well H8>
p200.dispense(33, plate1[65].top(-2)).touch_tip() #105: <Slot C2><Well B9>
p200.dispense(33, plate1[67].top(-2)).touch_tip() #106: <Slot C2><Well D9>
p200.dispense(33, plate1[69].top(-2)).touch_tip() #107: <Slot C2><Well F9>
p200.dispense(33, plate1[71].top(-2)).touch_tip() #108: <Slot C2><Well H9>

p200.aspirate(172, trough['C1'].bottom(87))
p200.dispense(43, plate1[73].top(-2)).touch_tip() #109: <Slot C2><Well B10>
p200.dispense(43, plate1[75].top(-2)).touch_tip() #110: <Slot C2><Well D10>
p200.dispense(43, plate1[77].top(-2)).touch_tip() #111: <Slot C2><Well F10>
p200.dispense(43, plate1[79].top(-2)).touch_tip() #112: <Slot C2><Well H10>

p200.aspirate(168, trough['C1'].bottom(86))
p200.dispense(56, plate1[81].top(-2)).touch_tip() #113: <Slot C2><Well B11>
p200.dispense(56, plate1[83].top(-2)).touch_tip() #114: <Slot C2><Well D11>
p200.dispense(56, plate1[85].top(-2)).touch_tip() #115: <Slot C2><Well F11>

p200.aspirate(128, trough['C1'].bottom(85))
p200.dispense(56, plate1[87].top(-2)).touch_tip() #116: <Slot C2><Well H11>
p200.dispense(72, plate1[89].top(-2)).touch_tip() #117: <Slot C2><Well B12>

p200.aspirate(144, trough['C1'].bottom(84))
p200.dispense(72, plate1[91].top(-2)).touch_tip() #118: <Slot C2><Well D12>
p200.dispense(72, plate1[93].top(-2)).touch_tip() #119: <Slot C2><Well F12>

p200.aspirate(72, trough['C1'].bottom(84))
p200.dispense(72, plate1[95].top(-2)).touch_tip() #120: <Slot C2><Well H12>

p200.drop_tip()
p200.pick_up_tip(p200rack['2'])

# *********** Dispense WS_1000

p200.aspirate(158, trough['B1'].bottom(89))
p200.dispense(20, plate1[72].top(-2)).touch_tip() #121 <Slot C2><Well A10>
p200.dispense(20, plate1[74].top(-2)).touch_tip() #122: <Slot C2><Well C10>
p200.dispense(20, plate1[76].top(-2)).touch_tip() #123: <Slot C2><Well E10>
p200.dispense(20, plate1[78].top(-2)).touch_tip() #124: <Slot C2><Well G10>
p200.dispense(26, plate1[80].top(-2)).touch_tip() #125: <Slot C2><Well A11>
p200.dispense(26, plate1[82].top(-2)).touch_tip() #126: <Slot C2><Well C11>
p200.dispense(26, plate1[84].top(-2)).touch_tip() #127: <Slot C2><Well E11>

p200.aspirate(158, trough['B1'].bottom(88))
p200.dispense(26, plate1[86].top(-2)).touch_tip() #128: <Slot C2><Well G11>
p200.dispense(33, plate1[88].top(-2)).touch_tip() #129: <Slot C2><Well A12>
p200.dispense(33, plate1[90].top(-2)).touch_tip() #130: <Slot C2><Well C12>
p200.dispense(33, plate1[92].top(-2)).touch_tip() #131: <Slot C2><Well E12>
p200.dispense(33, plate1[94].top(-2)).touch_tip() #132: <Slot C2><Well G12>

p200.aspirate(144, trough['B1'].bottom(87))
p200.dispense(36, plate1[1].top(-2)).touch_tip() #133: <Slot C2><Well B1>
p200.dispense(36, plate1[3].top(-2)).touch_tip() #134: <Slot C2><Well D1>
p200.dispense(36, plate1[5].top(-2)).touch_tip() #135: <Slot C2><Well F1>
p200.dispense(36, plate1[7].top(-2)).touch_tip() #136: <Slot C2><Well H1>

p200.aspirate(165, trough['B1'].bottom(86))
p200.dispense(55, plate1[9].top(-2)).touch_tip() #137: <Slot C2><Well B2>
p200.dispense(55, plate1[11].top(-2)).touch_tip() #138: <Slot C2><Well D2>
p200.dispense(55, plate1[13].top(-2)).touch_tip() #139: <Slot C2><Well F2>

p200.aspirate(127, trough['B1'].bottom(85))
p200.dispense(55, plate1[15].top(-2)).touch_tip() #140: <Slot C2><Well H2>
p200.dispense(72, plate1[17].top(-2)).touch_tip() #141: <Slot C2><Well B3>

p200.aspirate(144, trough['B1'].bottom(84))
p200.dispense(72, plate1[19].top(-2)).touch_tip() #142: <Slot C2><Well D3>
p200.dispense(72, plate1[21].top(-2)).touch_tip() #143: <Slot C2><Well F3>

p200.aspirate(166, trough['B1'].bottom(83))
p200.dispense(72, plate1[23].top(-2)).touch_tip() #144: <Slot C2><Well H3>
p200.dispense(94, plate1[25].top(-2)).touch_tip() #145: <Slot C2><Well B4>

p200.aspirate(94, trough['B1'].bottom(82))
p200.dispense(94, plate1[27].top(-2)).touch_tip() #146: <Slot C2><Well D4>

p200.aspirate(94, trough['B1'].bottom(82))
p200.dispense(94, plate1[29].top(-2)).touch_tip() #147: <Slot C2><Well F4>

p200.aspirate(94, trough['B1'].bottom(81))
p200.dispense(94, plate1[31].top(-2)).touch_tip() #148: <Slot C2><Well H4>

p200.aspirate(122, trough['B1'].bottom(80))
p200.dispense(122, plate1[33].top(-2)).touch_tip() #149: <Slot C2><Well B5>

p200.aspirate(122, trough['B1'].bottom(80))
p200.dispense(122, plate1[35].top(-2)).touch_tip() #150: <Slot C2><Well D5>

p200.aspirate(122, trough['B1'].bottom(79))
p200.dispense(122, plate1[37].top(-2)).touch_tip() #151: <Slot C2><Well F5>

p200.aspirate(122, trough['B1'].bottom(78))
p200.dispense(122, plate1[39].top(-2)).touch_tip() #152: <Slot C2><Well H5>

p200.aspirate(155, trough['B1'].bottom(77))
p200.dispense(155, plate1[41].top(-2)).touch_tip() #153: <Slot C2><Well B6>

p200.aspirate(155, trough['B1'].bottom(76))
p200.dispense(155, plate1[43].top(-2)).touch_tip() #154: <Slot C2><Well D6>

p200.aspirate(155, trough['B1'].bottom(75))
p200.dispense(155, plate1[45].top(-2)).touch_tip() #155: <Slot C2><Well F6>

p200.aspirate(155, trough['B1'].bottom(75))
p200.dispense(155, plate1[47].top(-2)).touch_tip() #156: <Slot C2><Well H6>

p200.drop_tip()
p200.pick_up_tip(p200rack['3'])

# *********** Dispense WS_10000

p200.aspirate(180, trough['A1'].bottom(89))
p200.dispense(18, plate1[24].top(-2)).touch_tip() #157 <Slot C2><Well A4>
p200.dispense(18, plate1[26].top(-2)).touch_tip() #158: <Slot C2><Well C4>
p200.dispense(18, plate1[28].top(-2)).touch_tip() #159: <Slot C2><Well E4>
p200.dispense(18, plate1[30].top(-2)).touch_tip() #160: <Slot C2><Well G4>
p200.dispense(36, plate1[32].top(-2)).touch_tip() #161: <Slot C2><Well A5>
p200.dispense(36, plate1[34].top(-2)).touch_tip() #162: <Slot C2><Well C5>
p200.dispense(36, plate1[36].top(-2)).touch_tip() #163: <Slot C2><Well E5>

p200.aspirate(180, trough['A1'].bottom(87))
p200.dispense(36, plate1[38].top(-2)).touch_tip() #164: <Slot C2><Well G5>
p200.dispense(72, plate1[40].top(-2)).touch_tip() #165: <Slot C2><Well A6>
p200.dispense(72, plate1[42].top(-2)).touch_tip() #166: <Slot C2><Well C6>

p200.aspirate(144, trough['A1'].bottom(86))
p200.dispense(72, plate1[44].top(-2)).touch_tip() #167: <Slot C2><Well E6>
p200.dispense(72, plate1[46].top(-2)).touch_tip() #168: <Slot C2><Well G6>

p200.aspirate(94, trough['A1'].bottom(86))
p200.dispense(94, plate1[48].top(-2)).touch_tip() #169: <Slot C2><Well A7>

p200.aspirate(94, trough['A1'].bottom(85))
p200.dispense(94, plate1[50].top(-2)).touch_tip() #170: <Slot C2><Well C7>

p200.aspirate(94, trough['A1'].bottom(85))
p200.dispense(94, plate1[52].top(-2)).touch_tip() #171: <Slot C2><Well E7>

p200.aspirate(94, trough['A1'].bottom(84))
p200.dispense(94, plate1[54].top(-2)).touch_tip() #172: <Slot C2><Well G7>

p200.aspirate(122, trough['A1'].bottom(83))
p200.dispense(122, plate1[56].top(-2)).touch_tip() #173: <Slot C2><Well A8>

p200.aspirate(122, trough['A1'].bottom(83))
p200.dispense(122, plate1[58].top(-2)).touch_tip() #174: <Slot C2><Well C8>

p200.aspirate(122, trough['A1'].bottom(82))
p200.dispense(122, plate1[60].top(-2)).touch_tip() #175: <Slot C2><Well E8>

p200.aspirate(122, trough['A1'].bottom(81))
p200.dispense(122, plate1[62].top(-2)).touch_tip() #176: <Slot C2><Well G8>

p200.aspirate(151, trough['A1'].bottom(80))
p200.dispense(151, plate1[64].top(-2)).touch_tip() #177: <Slot C2><Well A9>

p200.aspirate(151, trough['A1'].bottom(79))
p200.dispense(151, plate1[66].top(-2)).touch_tip() #178: <Slot C2><Well C9>

p200.aspirate(151, trough['A1'].bottom(78))
p200.dispense(151, plate1[68].top(-2)).touch_tip() #179: <Slot C2><Well E9>

p200.aspirate(151, trough['A1'].bottom(78))
p200.dispense(151, plate1[70].top(-2)).touch_tip() #180: <Slot C2><Well G9>

p200.drop_tip()
##