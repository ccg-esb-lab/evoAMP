

###################################################################################
#
# SCRIPT GENERATED ON 16/01/2018 FROM THE FOLLOWING LAYOUT FILES:
#  fileDictName=layouts/Key(EvoAmp)_M9.txt
#  fileTroughName=layouts/Trough_M9.txt
#  fileLayoutName=layouts/Layout_M9_4plates.txt
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
plate1 = containers.load('96-PCR-flat','D1','plate-1')
plate2 = containers.load('96-PCR-flat','C1','plate-2')
plate3 = containers.load('96-PCR-flat','B1','plate-3')
plate4 = containers.load('96-PCR-flat','A1','plate-4')
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

p200.aspirate(180, trough['A3'].bottom(89))
p200.dispense(180, plate1[0].top(-2)).touch_tip() #1 <Slot D1><Well A1>

p200.aspirate(180, trough['A3'].bottom(89))
p200.dispense(180, plate1[8].top(-2)).touch_tip() #2: <Slot D1><Well A2>

p200.aspirate(180, trough['A3'].bottom(89))
p200.dispense(180, plate1[16].top(-2)).touch_tip() #3: <Slot D1><Well A3>

p200.aspirate(180, trough['A3'].bottom(88))
p200.dispense(180, plate1[24].top(-2)).touch_tip() #4: <Slot D1><Well A4>

p200.aspirate(180, trough['A3'].bottom(88))
p200.dispense(180, plate1[32].top(-2)).touch_tip() #5: <Slot D1><Well A5>

p200.aspirate(180, trough['A3'].bottom(88))
p200.dispense(180, plate1[40].top(-2)).touch_tip() #6: <Slot D1><Well A6>

p200.aspirate(180, trough['A3'].bottom(87))
p200.dispense(180, plate1[48].top(-2)).touch_tip() #7: <Slot D1><Well A7>

p200.aspirate(180, trough['A3'].bottom(87))
p200.dispense(180, plate1[56].top(-2)).touch_tip() #8: <Slot D1><Well A8>

p200.aspirate(180, trough['A3'].bottom(87))
p200.dispense(180, plate1[64].top(-2)).touch_tip() #9: <Slot D1><Well A9>

p200.aspirate(180, trough['A3'].bottom(86))
p200.dispense(180, plate1[72].top(-2)).touch_tip() #10: <Slot D1><Well A10>

p200.aspirate(180, trough['A3'].bottom(86))
p200.dispense(180, plate1[80].top(-2)).touch_tip() #11: <Slot D1><Well A11>

p200.aspirate(180, trough['A3'].bottom(86))
p200.dispense(180, plate1[88].top(-2)).touch_tip() #12: <Slot D1><Well A12>

p200.aspirate(180, trough['A3'].bottom(85))
p200.dispense(180, plate1[1].top(-2)).touch_tip() #13: <Slot D1><Well B1>

p200.aspirate(180, trough['A3'].bottom(85))
p200.dispense(180, plate1[9].top(-2)).touch_tip() #14: <Slot D1><Well B2>

p200.aspirate(180, trough['A3'].bottom(85))
p200.dispense(180, plate1[17].top(-2)).touch_tip() #15: <Slot D1><Well B3>

p200.aspirate(180, trough['A3'].bottom(84))
p200.dispense(180, plate1[25].top(-2)).touch_tip() #16: <Slot D1><Well B4>

p200.aspirate(180, trough['A3'].bottom(84))
p200.dispense(180, plate1[33].top(-2)).touch_tip() #17: <Slot D1><Well B5>

p200.aspirate(180, trough['A3'].bottom(84))
p200.dispense(180, plate1[41].top(-2)).touch_tip() #18: <Slot D1><Well B6>

p200.aspirate(180, trough['A3'].bottom(84))
p200.dispense(180, plate1[49].top(-2)).touch_tip() #19: <Slot D1><Well B7>

p200.aspirate(180, trough['A3'].bottom(83))
p200.dispense(180, plate1[57].top(-2)).touch_tip() #20: <Slot D1><Well B8>

p200.aspirate(180, trough['A3'].bottom(83))
p200.dispense(180, plate1[65].top(-2)).touch_tip() #21: <Slot D1><Well B9>

p200.aspirate(180, trough['A3'].bottom(83))
p200.dispense(180, plate1[73].top(-2)).touch_tip() #22: <Slot D1><Well B10>

p200.aspirate(180, trough['A3'].bottom(82))
p200.dispense(180, plate1[81].top(-2)).touch_tip() #23: <Slot D1><Well B11>

p200.aspirate(180, trough['A3'].bottom(82))
p200.dispense(180, plate1[89].top(-2)).touch_tip() #24: <Slot D1><Well B12>

p200.aspirate(180, trough['A3'].bottom(82))
p200.dispense(180, plate1[2].top(-2)).touch_tip() #25: <Slot D1><Well C1>

p200.aspirate(180, trough['A3'].bottom(81))
p200.dispense(180, plate1[10].top(-2)).touch_tip() #26: <Slot D1><Well C2>

p200.aspirate(180, trough['A3'].bottom(81))
p200.dispense(180, plate1[18].top(-2)).touch_tip() #27: <Slot D1><Well C3>

p200.aspirate(180, trough['A3'].bottom(81))
p200.dispense(180, plate1[26].top(-2)).touch_tip() #28: <Slot D1><Well C4>

p200.aspirate(180, trough['A3'].bottom(80))
p200.dispense(180, plate1[34].top(-2)).touch_tip() #29: <Slot D1><Well C5>

p200.aspirate(180, trough['A3'].bottom(80))
p200.dispense(180, plate1[42].top(-2)).touch_tip() #30: <Slot D1><Well C6>

p200.aspirate(180, trough['A3'].bottom(80))
p200.dispense(180, plate1[50].top(-2)).touch_tip() #31: <Slot D1><Well C7>

p200.aspirate(180, trough['A3'].bottom(79))
p200.dispense(180, plate1[58].top(-2)).touch_tip() #32: <Slot D1><Well C8>

p200.aspirate(180, trough['A3'].bottom(79))
p200.dispense(180, plate1[66].top(-2)).touch_tip() #33: <Slot D1><Well C9>

p200.aspirate(180, trough['A3'].bottom(79))
p200.dispense(180, plate1[74].top(-2)).touch_tip() #34: <Slot D1><Well C10>

p200.aspirate(180, trough['A3'].bottom(78))
p200.dispense(180, plate1[82].top(-2)).touch_tip() #35: <Slot D1><Well C11>

p200.aspirate(180, trough['A3'].bottom(78))
p200.dispense(180, plate1[90].top(-2)).touch_tip() #36: <Slot D1><Well C12>

p200.aspirate(180, trough['A3'].bottom(78))
p200.dispense(180, plate1[3].top(-2)).touch_tip() #37: <Slot D1><Well D1>

p200.aspirate(180, trough['A3'].bottom(77))
p200.dispense(180, plate1[11].top(-2)).touch_tip() #38: <Slot D1><Well D2>

p200.aspirate(180, trough['A3'].bottom(77))
p200.dispense(180, plate1[19].top(-2)).touch_tip() #39: <Slot D1><Well D3>

p200.aspirate(180, trough['A3'].bottom(77))
p200.dispense(180, plate1[27].top(-2)).touch_tip() #40: <Slot D1><Well D4>

p200.aspirate(180, trough['A3'].bottom(76))
p200.dispense(180, plate1[35].top(-2)).touch_tip() #41: <Slot D1><Well D5>

p200.aspirate(180, trough['A3'].bottom(76))
p200.dispense(180, plate1[43].top(-2)).touch_tip() #42: <Slot D1><Well D6>

p200.aspirate(180, trough['A3'].bottom(76))
p200.dispense(180, plate1[51].top(-2)).touch_tip() #43: <Slot D1><Well D7>

p200.aspirate(180, trough['A3'].bottom(75))
p200.dispense(180, plate1[59].top(-2)).touch_tip() #44: <Slot D1><Well D8>

p200.aspirate(180, trough['A3'].bottom(75))
p200.dispense(180, plate1[67].top(-2)).touch_tip() #45: <Slot D1><Well D9>

p200.aspirate(180, trough['A3'].bottom(75))
p200.dispense(180, plate1[75].top(-2)).touch_tip() #46: <Slot D1><Well D10>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[83].top(-2)).touch_tip() #47: <Slot D1><Well D11>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[91].top(-2)).touch_tip() #48: <Slot D1><Well D12>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate1[4].top(-2)).touch_tip() #49: <Slot D1><Well E1>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[12].top(-2)).touch_tip() #50: <Slot D1><Well E2>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[20].top(-2)).touch_tip() #51: <Slot D1><Well E3>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[28].top(-2)).touch_tip() #52: <Slot D1><Well E4>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate1[36].top(-2)).touch_tip() #53: <Slot D1><Well E5>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[44].top(-2)).touch_tip() #54: <Slot D1><Well E6>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[52].top(-2)).touch_tip() #55: <Slot D1><Well E7>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate1[60].top(-2)).touch_tip() #56: <Slot D1><Well E8>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[68].top(-2)).touch_tip() #57: <Slot D1><Well E9>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[76].top(-2)).touch_tip() #58: <Slot D1><Well E10>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate1[84].top(-2)).touch_tip() #59: <Slot D1><Well E11>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[92].top(-2)).touch_tip() #60: <Slot D1><Well E12>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[5].top(-2)).touch_tip() #61: <Slot D1><Well F1>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate1[13].top(-2)).touch_tip() #62: <Slot D1><Well F2>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[21].top(-2)).touch_tip() #63: <Slot D1><Well F3>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[29].top(-2)).touch_tip() #64: <Slot D1><Well F4>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate1[37].top(-2)).touch_tip() #65: <Slot D1><Well F5>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[45].top(-2)).touch_tip() #66: <Slot D1><Well F6>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[53].top(-2)).touch_tip() #67: <Slot D1><Well F7>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate1[61].top(-2)).touch_tip() #68: <Slot D1><Well F8>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[69].top(-2)).touch_tip() #69: <Slot D1><Well F9>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[77].top(-2)).touch_tip() #70: <Slot D1><Well F10>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate1[85].top(-2)).touch_tip() #71: <Slot D1><Well F11>

p200.aspirate(180, trough['A3'].bottom(66))
p200.dispense(180, plate1[93].top(-2)).touch_tip() #72: <Slot D1><Well F12>

p200.aspirate(180, trough['A3'].bottom(66))
p200.dispense(180, plate1[6].top(-2)).touch_tip() #73: <Slot D1><Well G1>

p200.aspirate(180, trough['A3'].bottom(66))
p200.dispense(180, plate1[14].top(-2)).touch_tip() #74: <Slot D1><Well G2>

p200.aspirate(180, trough['A3'].bottom(65))
p200.dispense(180, plate1[22].top(-2)).touch_tip() #75: <Slot D1><Well G3>

p200.aspirate(180, trough['A3'].bottom(65))
p200.dispense(180, plate1[30].top(-2)).touch_tip() #76: <Slot D1><Well G4>

p200.aspirate(180, trough['A3'].bottom(65))
p200.dispense(180, plate1[38].top(-2)).touch_tip() #77: <Slot D1><Well G5>

p200.aspirate(180, trough['A3'].bottom(64))
p200.dispense(180, plate1[46].top(-2)).touch_tip() #78: <Slot D1><Well G6>

p200.aspirate(180, trough['A3'].bottom(64))
p200.dispense(180, plate1[54].top(-2)).touch_tip() #79: <Slot D1><Well G7>

p200.aspirate(180, trough['A3'].bottom(64))
p200.dispense(180, plate1[62].top(-2)).touch_tip() #80: <Slot D1><Well G8>

p200.aspirate(180, trough['A3'].bottom(63))
p200.dispense(180, plate1[70].top(-2)).touch_tip() #81: <Slot D1><Well G9>

p200.aspirate(180, trough['A3'].bottom(63))
p200.dispense(180, plate1[78].top(-2)).touch_tip() #82: <Slot D1><Well G10>

p200.aspirate(180, trough['A3'].bottom(63))
p200.dispense(180, plate1[86].top(-2)).touch_tip() #83: <Slot D1><Well G11>

p200.aspirate(180, trough['A3'].bottom(62))
p200.dispense(180, plate1[94].top(-2)).touch_tip() #84: <Slot D1><Well G12>

p200.aspirate(180, trough['A3'].bottom(62))
p200.dispense(180, plate1[7].top(-2)).touch_tip() #85: <Slot D1><Well H1>

p200.aspirate(180, trough['A3'].bottom(62))
p200.dispense(180, plate1[15].top(-2)).touch_tip() #86: <Slot D1><Well H2>

p200.aspirate(180, trough['A3'].bottom(61))
p200.dispense(180, plate1[23].top(-2)).touch_tip() #87: <Slot D1><Well H3>

p200.aspirate(180, trough['A3'].bottom(61))
p200.dispense(180, plate1[31].top(-2)).touch_tip() #88: <Slot D1><Well H4>

p200.aspirate(180, trough['A3'].bottom(61))
p200.dispense(180, plate1[39].top(-2)).touch_tip() #89: <Slot D1><Well H5>

p200.aspirate(180, trough['A3'].bottom(61))
p200.dispense(180, plate1[47].top(-2)).touch_tip() #90: <Slot D1><Well H6>

p200.aspirate(180, trough['A3'].bottom(60))
p200.dispense(180, plate1[55].top(-2)).touch_tip() #91: <Slot D1><Well H7>

p200.aspirate(180, trough['A3'].bottom(60))
p200.dispense(180, plate1[63].top(-2)).touch_tip() #92: <Slot D1><Well H8>

p200.aspirate(180, trough['A3'].bottom(60))
p200.dispense(180, plate1[71].top(-2)).touch_tip() #93: <Slot D1><Well H9>

p200.aspirate(180, trough['A3'].bottom(59))
p200.dispense(180, plate1[79].top(-2)).touch_tip() #94: <Slot D1><Well H10>

p200.aspirate(180, trough['A3'].bottom(59))
p200.dispense(180, plate1[87].top(-2)).touch_tip() #95: <Slot D1><Well H11>

p200.aspirate(180, trough['A3'].bottom(59))
p200.dispense(180, plate1[95].top(-2)).touch_tip() #96: <Slot D1><Well H12>

p200.aspirate(180, trough['A3'].bottom(58))
p200.dispense(180, plate2[0].top(-2)).touch_tip() #97: <Slot C1><Well A1>

p200.aspirate(180, trough['A3'].bottom(58))
p200.dispense(180, plate2[8].top(-2)).touch_tip() #98: <Slot C1><Well A2>

p200.aspirate(180, trough['A3'].bottom(58))
p200.dispense(180, plate2[16].top(-2)).touch_tip() #99: <Slot C1><Well A3>

p200.aspirate(180, trough['A3'].bottom(57))
p200.dispense(180, plate2[24].top(-2)).touch_tip() #100: <Slot C1><Well A4>

p200.aspirate(180, trough['A3'].bottom(57))
p200.dispense(180, plate2[32].top(-2)).touch_tip() #101: <Slot C1><Well A5>

p200.aspirate(180, trough['A3'].bottom(57))
p200.dispense(180, plate2[40].top(-2)).touch_tip() #102: <Slot C1><Well A6>

p200.aspirate(180, trough['A3'].bottom(56))
p200.dispense(180, plate2[48].top(-2)).touch_tip() #103: <Slot C1><Well A7>

p200.aspirate(180, trough['A3'].bottom(56))
p200.dispense(180, plate2[56].top(-2)).touch_tip() #104: <Slot C1><Well A8>

p200.aspirate(180, trough['A3'].bottom(56))
p200.dispense(180, plate2[64].top(-2)).touch_tip() #105: <Slot C1><Well A9>

p200.aspirate(180, trough['A3'].bottom(55))
p200.dispense(180, plate2[72].top(-2)).touch_tip() #106: <Slot C1><Well A10>

p200.aspirate(180, trough['A3'].bottom(55))
p200.dispense(180, plate2[80].top(-2)).touch_tip() #107: <Slot C1><Well A11>

p200.aspirate(180, trough['A3'].bottom(55))
p200.dispense(180, plate2[88].top(-2)).touch_tip() #108: <Slot C1><Well A12>

p200.aspirate(180, trough['A3'].bottom(54))
p200.dispense(180, plate2[1].top(-2)).touch_tip() #109: <Slot C1><Well B1>

p200.aspirate(180, trough['A3'].bottom(54))
p200.dispense(180, plate2[9].top(-2)).touch_tip() #110: <Slot C1><Well B2>

p200.aspirate(180, trough['A3'].bottom(54))
p200.dispense(180, plate2[17].top(-2)).touch_tip() #111: <Slot C1><Well B3>

p200.aspirate(180, trough['A3'].bottom(53))
p200.dispense(180, plate2[25].top(-2)).touch_tip() #112: <Slot C1><Well B4>

p200.aspirate(180, trough['A3'].bottom(53))
p200.dispense(180, plate2[33].top(-2)).touch_tip() #113: <Slot C1><Well B5>

p200.aspirate(180, trough['A3'].bottom(53))
p200.dispense(180, plate2[41].top(-2)).touch_tip() #114: <Slot C1><Well B6>

p200.aspirate(180, trough['A3'].bottom(52))
p200.dispense(180, plate2[49].top(-2)).touch_tip() #115: <Slot C1><Well B7>

p200.aspirate(180, trough['A3'].bottom(52))
p200.dispense(180, plate2[57].top(-2)).touch_tip() #116: <Slot C1><Well B8>

p200.aspirate(180, trough['A3'].bottom(52))
p200.dispense(180, plate2[65].top(-2)).touch_tip() #117: <Slot C1><Well B9>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[73].top(-2)).touch_tip() #118: <Slot C1><Well B10>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[81].top(-2)).touch_tip() #119: <Slot C1><Well B11>

p200.aspirate(180, trough['A3'].bottom(51))
p200.dispense(180, plate2[89].top(-2)).touch_tip() #120: <Slot C1><Well B12>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[2].top(-2)).touch_tip() #121: <Slot C1><Well C1>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[10].top(-2)).touch_tip() #122: <Slot C1><Well C2>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[18].top(-2)).touch_tip() #123: <Slot C1><Well C3>

p200.aspirate(180, trough['A3'].bottom(50))
p200.dispense(180, plate2[26].top(-2)).touch_tip() #124: <Slot C1><Well C4>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[34].top(-2)).touch_tip() #125: <Slot C1><Well C5>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[42].top(-2)).touch_tip() #126: <Slot C1><Well C6>

p200.aspirate(180, trough['A3'].bottom(49))
p200.dispense(180, plate2[50].top(-2)).touch_tip() #127: <Slot C1><Well C7>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[58].top(-2)).touch_tip() #128: <Slot C1><Well C8>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[66].top(-2)).touch_tip() #129: <Slot C1><Well C9>

p200.aspirate(180, trough['A3'].bottom(48))
p200.dispense(180, plate2[74].top(-2)).touch_tip() #130: <Slot C1><Well C10>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[82].top(-2)).touch_tip() #131: <Slot C1><Well C11>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[90].top(-2)).touch_tip() #132: <Slot C1><Well C12>

p200.aspirate(180, trough['A3'].bottom(47))
p200.dispense(180, plate2[3].top(-2)).touch_tip() #133: <Slot C1><Well D1>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[11].top(-2)).touch_tip() #134: <Slot C1><Well D2>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[19].top(-2)).touch_tip() #135: <Slot C1><Well D3>

p200.aspirate(180, trough['A3'].bottom(46))
p200.dispense(180, plate2[27].top(-2)).touch_tip() #136: <Slot C1><Well D4>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[35].top(-2)).touch_tip() #137: <Slot C1><Well D5>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[43].top(-2)).touch_tip() #138: <Slot C1><Well D6>

p200.aspirate(180, trough['A3'].bottom(45))
p200.dispense(180, plate2[51].top(-2)).touch_tip() #139: <Slot C1><Well D7>

p200.aspirate(180, trough['A3'].bottom(44))
p200.dispense(180, plate2[59].top(-2)).touch_tip() #140: <Slot C1><Well D8>

p200.aspirate(180, trough['A3'].bottom(44))
p200.dispense(180, plate2[67].top(-2)).touch_tip() #141: <Slot C1><Well D9>

p200.aspirate(180, trough['A3'].bottom(44))
p200.dispense(180, plate2[75].top(-2)).touch_tip() #142: <Slot C1><Well D10>

p200.aspirate(180, trough['A3'].bottom(43))
p200.dispense(180, plate2[83].top(-2)).touch_tip() #143: <Slot C1><Well D11>

p200.aspirate(180, trough['A3'].bottom(43))
p200.dispense(180, plate2[91].top(-2)).touch_tip() #144: <Slot C1><Well D12>

p200.aspirate(180, trough['A3'].bottom(43))
p200.dispense(180, plate2[4].top(-2)).touch_tip() #145: <Slot C1><Well E1>

p200.aspirate(180, trough['A3'].bottom(42))
p200.dispense(180, plate2[12].top(-2)).touch_tip() #146: <Slot C1><Well E2>

p200.aspirate(180, trough['A3'].bottom(42))
p200.dispense(180, plate2[20].top(-2)).touch_tip() #147: <Slot C1><Well E3>

p200.aspirate(180, trough['A3'].bottom(42))
p200.dispense(180, plate2[28].top(-2)).touch_tip() #148: <Slot C1><Well E4>

p200.aspirate(180, trough['A3'].bottom(41))
p200.dispense(180, plate2[36].top(-2)).touch_tip() #149: <Slot C1><Well E5>

p200.aspirate(180, trough['A3'].bottom(41))
p200.dispense(180, plate2[44].top(-2)).touch_tip() #150: <Slot C1><Well E6>

p200.aspirate(180, trough['A3'].bottom(41))
p200.dispense(180, plate2[52].top(-2)).touch_tip() #151: <Slot C1><Well E7>

p200.aspirate(180, trough['A3'].bottom(40))
p200.dispense(180, plate2[60].top(-2)).touch_tip() #152: <Slot C1><Well E8>

p200.aspirate(180, trough['A3'].bottom(40))
p200.dispense(180, plate2[68].top(-2)).touch_tip() #153: <Slot C1><Well E9>

p200.aspirate(180, trough['A3'].bottom(40))
p200.dispense(180, plate2[76].top(-2)).touch_tip() #154: <Slot C1><Well E10>

p200.aspirate(180, trough['A3'].bottom(39))
p200.dispense(180, plate2[84].top(-2)).touch_tip() #155: <Slot C1><Well E11>

p200.aspirate(180, trough['A3'].bottom(39))
p200.dispense(180, plate2[92].top(-2)).touch_tip() #156: <Slot C1><Well E12>

p200.aspirate(180, trough['A3'].bottom(39))
p200.dispense(180, plate2[5].top(-2)).touch_tip() #157: <Slot C1><Well F1>

p200.aspirate(180, trough['A3'].bottom(38))
p200.dispense(180, plate2[13].top(-2)).touch_tip() #158: <Slot C1><Well F2>

p200.aspirate(180, trough['A3'].bottom(38))
p200.dispense(180, plate2[21].top(-2)).touch_tip() #159: <Slot C1><Well F3>

p200.aspirate(180, trough['A3'].bottom(38))
p200.dispense(180, plate2[29].top(-2)).touch_tip() #160: <Slot C1><Well F4>

p200.aspirate(180, trough['A3'].bottom(38))
p200.dispense(180, plate2[37].top(-2)).touch_tip() #161: <Slot C1><Well F5>

p200.aspirate(180, trough['A3'].bottom(37))
p200.dispense(180, plate2[45].top(-2)).touch_tip() #162: <Slot C1><Well F6>

p200.aspirate(180, trough['A3'].bottom(37))
p200.dispense(180, plate2[53].top(-2)).touch_tip() #163: <Slot C1><Well F7>

p200.aspirate(180, trough['A3'].bottom(37))
p200.dispense(180, plate2[61].top(-2)).touch_tip() #164: <Slot C1><Well F8>

p200.aspirate(180, trough['A3'].bottom(36))
p200.dispense(180, plate2[69].top(-2)).touch_tip() #165: <Slot C1><Well F9>

p200.aspirate(180, trough['A3'].bottom(36))
p200.dispense(180, plate2[77].top(-2)).touch_tip() #166: <Slot C1><Well F10>

p200.aspirate(180, trough['A3'].bottom(36))
p200.dispense(180, plate2[85].top(-2)).touch_tip() #167: <Slot C1><Well F11>

p200.aspirate(180, trough['A3'].bottom(35))
p200.dispense(180, plate2[93].top(-2)).touch_tip() #168: <Slot C1><Well F12>

p200.aspirate(180, trough['A3'].bottom(35))
p200.dispense(180, plate2[6].top(-2)).touch_tip() #169: <Slot C1><Well G1>

p200.aspirate(180, trough['A3'].bottom(35))
p200.dispense(180, plate2[14].top(-2)).touch_tip() #170: <Slot C1><Well G2>

p200.aspirate(180, trough['A3'].bottom(34))
p200.dispense(180, plate2[22].top(-2)).touch_tip() #171: <Slot C1><Well G3>

p200.aspirate(180, trough['A3'].bottom(34))
p200.dispense(180, plate2[30].top(-2)).touch_tip() #172: <Slot C1><Well G4>

p200.aspirate(180, trough['A3'].bottom(34))
p200.dispense(180, plate2[38].top(-2)).touch_tip() #173: <Slot C1><Well G5>

p200.aspirate(180, trough['A3'].bottom(33))
p200.dispense(180, plate2[46].top(-2)).touch_tip() #174: <Slot C1><Well G6>

p200.aspirate(180, trough['A3'].bottom(33))
p200.dispense(180, plate2[54].top(-2)).touch_tip() #175: <Slot C1><Well G7>

p200.aspirate(180, trough['A3'].bottom(33))
p200.dispense(180, plate2[62].top(-2)).touch_tip() #176: <Slot C1><Well G8>

p200.aspirate(180, trough['A3'].bottom(32))
p200.dispense(180, plate2[70].top(-2)).touch_tip() #177: <Slot C1><Well G9>

p200.aspirate(180, trough['A3'].bottom(32))
p200.dispense(180, plate2[78].top(-2)).touch_tip() #178: <Slot C1><Well G10>

p200.aspirate(180, trough['A3'].bottom(32))
p200.dispense(180, plate2[86].top(-2)).touch_tip() #179: <Slot C1><Well G11>

p200.aspirate(180, trough['A3'].bottom(31))
p200.dispense(180, plate2[94].top(-2)).touch_tip() #180: <Slot C1><Well G12>

p200.aspirate(180, trough['A3'].bottom(31))
p200.dispense(180, plate2[7].top(-2)).touch_tip() #181: <Slot C1><Well H1>

p200.aspirate(180, trough['A3'].bottom(31))
p200.dispense(180, plate2[15].top(-2)).touch_tip() #182: <Slot C1><Well H2>

p200.aspirate(180, trough['A3'].bottom(30))
p200.dispense(180, plate2[23].top(-2)).touch_tip() #183: <Slot C1><Well H3>

p200.aspirate(180, trough['A3'].bottom(30))
p200.dispense(180, plate2[31].top(-2)).touch_tip() #184: <Slot C1><Well H4>

p200.aspirate(180, trough['A3'].bottom(30))
p200.dispense(180, plate2[39].top(-2)).touch_tip() #185: <Slot C1><Well H5>

p200.aspirate(180, trough['A3'].bottom(29))
p200.dispense(180, plate2[47].top(-2)).touch_tip() #186: <Slot C1><Well H6>

p200.aspirate(180, trough['A3'].bottom(29))
p200.dispense(180, plate2[55].top(-2)).touch_tip() #187: <Slot C1><Well H7>

p200.aspirate(180, trough['A3'].bottom(29))
p200.dispense(180, plate2[63].top(-2)).touch_tip() #188: <Slot C1><Well H8>

p200.aspirate(180, trough['A3'].bottom(28))
p200.dispense(180, plate2[71].top(-2)).touch_tip() #189: <Slot C1><Well H9>

p200.aspirate(180, trough['A3'].bottom(28))
p200.dispense(180, plate2[79].top(-2)).touch_tip() #190: <Slot C1><Well H10>

p200.aspirate(180, trough['A3'].bottom(28))
p200.dispense(180, plate2[87].top(-2)).touch_tip() #191: <Slot C1><Well H11>

p200.aspirate(180, trough['A3'].bottom(27))
p200.dispense(180, plate2[95].top(-2)).touch_tip() #192: <Slot C1><Well H12>

p200.aspirate(180, trough['A3'].bottom(27))
p200.dispense(180, plate3[0].top(-2)).touch_tip() #193: <Slot B1><Well A1>

p200.aspirate(180, trough['A3'].bottom(27))
p200.dispense(180, plate3[8].top(-2)).touch_tip() #194: <Slot B1><Well A2>

p200.aspirate(180, trough['A3'].bottom(26))
p200.dispense(180, plate3[16].top(-2)).touch_tip() #195: <Slot B1><Well A3>

p200.aspirate(180, trough['A3'].bottom(26))
p200.dispense(180, plate3[24].top(-2)).touch_tip() #196: <Slot B1><Well A4>

p200.aspirate(180, trough['A3'].bottom(26))
p200.dispense(180, plate3[32].top(-2)).touch_tip() #197: <Slot B1><Well A5>

p200.aspirate(180, trough['A3'].bottom(26))
p200.dispense(180, plate3[40].top(-2)).touch_tip() #198: <Slot B1><Well A6>

p200.aspirate(180, trough['A3'].bottom(25))
p200.dispense(180, plate3[48].top(-2)).touch_tip() #199: <Slot B1><Well A7>

p200.aspirate(180, trough['A3'].bottom(25))
p200.dispense(180, plate3[56].top(-2)).touch_tip() #200: <Slot B1><Well A8>

p200.aspirate(180, trough['A3'].bottom(25))
p200.dispense(180, plate3[64].top(-2)).touch_tip() #201: <Slot B1><Well A9>

p200.aspirate(180, trough['A3'].bottom(24))
p200.dispense(180, plate3[72].top(-2)).touch_tip() #202: <Slot B1><Well A10>

p200.aspirate(180, trough['A3'].bottom(24))
p200.dispense(180, plate3[80].top(-2)).touch_tip() #203: <Slot B1><Well A11>

p200.aspirate(180, trough['A3'].bottom(24))
p200.dispense(180, plate3[88].top(-2)).touch_tip() #204: <Slot B1><Well A12>

p200.aspirate(180, trough['A3'].bottom(23))
p200.dispense(180, plate3[1].top(-2)).touch_tip() #205: <Slot B1><Well B1>

p200.aspirate(180, trough['A3'].bottom(23))
p200.dispense(180, plate3[9].top(-2)).touch_tip() #206: <Slot B1><Well B2>

p200.aspirate(180, trough['A3'].bottom(23))
p200.dispense(180, plate3[17].top(-2)).touch_tip() #207: <Slot B1><Well B3>

p200.aspirate(180, trough['A3'].bottom(22))
p200.dispense(180, plate3[25].top(-2)).touch_tip() #208: <Slot B1><Well B4>

p200.aspirate(180, trough['A3'].bottom(22))
p200.dispense(180, plate3[33].top(-2)).touch_tip() #209: <Slot B1><Well B5>

p200.aspirate(180, trough['A3'].bottom(22))
p200.dispense(180, plate3[41].top(-2)).touch_tip() #210: <Slot B1><Well B6>

p200.aspirate(180, trough['A3'].bottom(21))
p200.dispense(180, plate3[49].top(-2)).touch_tip() #211: <Slot B1><Well B7>

p200.aspirate(180, trough['A3'].bottom(21))
p200.dispense(180, plate3[57].top(-2)).touch_tip() #212: <Slot B1><Well B8>

p200.aspirate(180, trough['A3'].bottom(21))
p200.dispense(180, plate3[65].top(-2)).touch_tip() #213: <Slot B1><Well B9>

p200.aspirate(180, trough['A3'].bottom(20))
p200.dispense(180, plate3[73].top(-2)).touch_tip() #214: <Slot B1><Well B10>

p200.aspirate(180, trough['A3'].bottom(20))
p200.dispense(180, plate3[81].top(-2)).touch_tip() #215: <Slot B1><Well B11>

p200.aspirate(180, trough['A3'].bottom(20))
p200.dispense(180, plate3[89].top(-2)).touch_tip() #216: <Slot B1><Well B12>

p200.aspirate(180, trough['A3'].bottom(19))
p200.dispense(180, plate3[2].top(-2)).touch_tip() #217: <Slot B1><Well C1>

p200.aspirate(180, trough['A3'].bottom(19))
p200.dispense(180, plate3[10].top(-2)).touch_tip() #218: <Slot B1><Well C2>

p200.aspirate(180, trough['A3'].bottom(19))
p200.dispense(180, plate3[18].top(-2)).touch_tip() #219: <Slot B1><Well C3>

p200.aspirate(180, trough['A3'].bottom(18))
p200.dispense(180, plate3[26].top(-2)).touch_tip() #220: <Slot B1><Well C4>

p200.aspirate(180, trough['A3'].bottom(18))
p200.dispense(180, plate3[34].top(-2)).touch_tip() #221: <Slot B1><Well C5>

p200.aspirate(180, trough['A3'].bottom(18))
p200.dispense(180, plate3[42].top(-2)).touch_tip() #222: <Slot B1><Well C6>

p200.aspirate(180, trough['A3'].bottom(17))
p200.dispense(180, plate3[50].top(-2)).touch_tip() #223: <Slot B1><Well C7>

p200.aspirate(180, trough['A3'].bottom(17))
p200.dispense(180, plate3[58].top(-2)).touch_tip() #224: <Slot B1><Well C8>

p200.aspirate(180, trough['A3'].bottom(17))
p200.dispense(180, plate3[66].top(-2)).touch_tip() #225: <Slot B1><Well C9>

p200.aspirate(180, trough['A3'].bottom(16))
p200.dispense(180, plate3[74].top(-2)).touch_tip() #226: <Slot B1><Well C10>

p200.aspirate(180, trough['A3'].bottom(16))
p200.dispense(180, plate3[82].top(-2)).touch_tip() #227: <Slot B1><Well C11>

p200.aspirate(180, trough['A3'].bottom(16))
p200.dispense(180, plate3[90].top(-2)).touch_tip() #228: <Slot B1><Well C12>

p200.aspirate(180, trough['A3'].bottom(15))
p200.dispense(180, plate3[3].top(-2)).touch_tip() #229: <Slot B1><Well D1>

p200.aspirate(180, trough['A3'].bottom(15))
p200.dispense(180, plate3[11].top(-2)).touch_tip() #230: <Slot B1><Well D2>

p200.aspirate(180, trough['A3'].bottom(15))
p200.dispense(180, plate3[19].top(-2)).touch_tip() #231: <Slot B1><Well D3>

p200.aspirate(180, trough['A3'].bottom(15))
p200.dispense(180, plate3[27].top(-2)).touch_tip() #232: <Slot B1><Well D4>

p200.aspirate(180, trough['A3'].bottom(14))
p200.dispense(180, plate3[35].top(-2)).touch_tip() #233: <Slot B1><Well D5>

p200.aspirate(180, trough['A3'].bottom(14))
p200.dispense(180, plate3[43].top(-2)).touch_tip() #234: <Slot B1><Well D6>

p200.aspirate(180, trough['A3'].bottom(14))
p200.dispense(180, plate3[51].top(-2)).touch_tip() #235: <Slot B1><Well D7>

p200.aspirate(180, trough['A3'].bottom(13))
p200.dispense(180, plate3[59].top(-2)).touch_tip() #236: <Slot B1><Well D8>

p200.aspirate(180, trough['A3'].bottom(13))
p200.dispense(180, plate3[67].top(-2)).touch_tip() #237: <Slot B1><Well D9>

p200.aspirate(180, trough['A3'].bottom(13))
p200.dispense(180, plate3[75].top(-2)).touch_tip() #238: <Slot B1><Well D10>

p200.aspirate(180, trough['A3'].bottom(12))
p200.dispense(180, plate3[83].top(-2)).touch_tip() #239: <Slot B1><Well D11>

p200.aspirate(180, trough['A3'].bottom(12))
p200.dispense(180, plate3[91].top(-2)).touch_tip() #240: <Slot B1><Well D12>

p200.aspirate(180, trough['A3'].bottom(12))
p200.dispense(180, plate3[4].top(-2)).touch_tip() #241: <Slot B1><Well E1>

p200.aspirate(180, trough['A3'].bottom(11))
p200.dispense(180, plate3[12].top(-2)).touch_tip() #242: <Slot B1><Well E2>

p200.aspirate(180, trough['A3'].bottom(11))
p200.dispense(180, plate3[20].top(-2)).touch_tip() #243: <Slot B1><Well E3>

p200.aspirate(180, trough['A3'].bottom(11))
p200.dispense(180, plate3[28].top(-2)).touch_tip() #244: <Slot B1><Well E4>

p200.aspirate(180, trough['A3'].bottom(10))
p200.dispense(180, plate3[36].top(-2)).touch_tip() #245: <Slot B1><Well E5>

p200.aspirate(180, trough['A3'].bottom(10))
p200.dispense(180, plate3[44].top(-2)).touch_tip() #246: <Slot B1><Well E6>

p200.aspirate(180, trough['A3'].bottom(10))
p200.dispense(180, plate3[52].top(-2)).touch_tip() #247: <Slot B1><Well E7>

p200.aspirate(180, trough['A3'].bottom(9))
p200.dispense(180, plate3[60].top(-2)).touch_tip() #248: <Slot B1><Well E8>

p200.aspirate(180, trough['A3'].bottom(9))
p200.dispense(180, plate3[68].top(-2)).touch_tip() #249: <Slot B1><Well E9>

p200.aspirate(180, trough['A4'].bottom(90))
p200.dispense(180, plate3[76].top(-2)).touch_tip() #250: <Slot B1><Well E10>

p200.aspirate(180, trough['A4'].bottom(89))
p200.dispense(180, plate3[84].top(-2)).touch_tip() #251: <Slot B1><Well E11>

p200.aspirate(180, trough['A4'].bottom(89))
p200.dispense(180, plate3[92].top(-2)).touch_tip() #252: <Slot B1><Well E12>

p200.aspirate(180, trough['A4'].bottom(89))
p200.dispense(180, plate3[5].top(-2)).touch_tip() #253: <Slot B1><Well F1>

p200.aspirate(180, trough['A4'].bottom(88))
p200.dispense(180, plate3[13].top(-2)).touch_tip() #254: <Slot B1><Well F2>

p200.aspirate(180, trough['A4'].bottom(88))
p200.dispense(180, plate3[21].top(-2)).touch_tip() #255: <Slot B1><Well F3>

p200.aspirate(180, trough['A4'].bottom(88))
p200.dispense(180, plate3[29].top(-2)).touch_tip() #256: <Slot B1><Well F4>

p200.aspirate(180, trough['A4'].bottom(87))
p200.dispense(180, plate3[37].top(-2)).touch_tip() #257: <Slot B1><Well F5>

p200.aspirate(180, trough['A4'].bottom(87))
p200.dispense(180, plate3[45].top(-2)).touch_tip() #258: <Slot B1><Well F6>

p200.aspirate(180, trough['A4'].bottom(87))
p200.dispense(180, plate3[53].top(-2)).touch_tip() #259: <Slot B1><Well F7>

p200.aspirate(180, trough['A4'].bottom(86))
p200.dispense(180, plate3[61].top(-2)).touch_tip() #260: <Slot B1><Well F8>

p200.aspirate(180, trough['A4'].bottom(86))
p200.dispense(180, plate3[69].top(-2)).touch_tip() #261: <Slot B1><Well F9>

p200.aspirate(180, trough['A4'].bottom(86))
p200.dispense(180, plate3[77].top(-2)).touch_tip() #262: <Slot B1><Well F10>

p200.aspirate(180, trough['A4'].bottom(85))
p200.dispense(180, plate3[85].top(-2)).touch_tip() #263: <Slot B1><Well F11>

p200.aspirate(180, trough['A4'].bottom(85))
p200.dispense(180, plate3[93].top(-2)).touch_tip() #264: <Slot B1><Well F12>

p200.aspirate(180, trough['A4'].bottom(85))
p200.dispense(180, plate3[6].top(-2)).touch_tip() #265: <Slot B1><Well G1>

p200.aspirate(180, trough['A4'].bottom(84))
p200.dispense(180, plate3[14].top(-2)).touch_tip() #266: <Slot B1><Well G2>

p200.aspirate(180, trough['A4'].bottom(84))
p200.dispense(180, plate3[22].top(-2)).touch_tip() #267: <Slot B1><Well G3>

p200.aspirate(180, trough['A4'].bottom(84))
p200.dispense(180, plate3[30].top(-2)).touch_tip() #268: <Slot B1><Well G4>

p200.aspirate(180, trough['A4'].bottom(84))
p200.dispense(180, plate3[38].top(-2)).touch_tip() #269: <Slot B1><Well G5>

p200.aspirate(180, trough['A4'].bottom(83))
p200.dispense(180, plate3[46].top(-2)).touch_tip() #270: <Slot B1><Well G6>

p200.aspirate(180, trough['A4'].bottom(83))
p200.dispense(180, plate3[54].top(-2)).touch_tip() #271: <Slot B1><Well G7>

p200.aspirate(180, trough['A4'].bottom(83))
p200.dispense(180, plate3[62].top(-2)).touch_tip() #272: <Slot B1><Well G8>

p200.aspirate(180, trough['A4'].bottom(82))
p200.dispense(180, plate3[70].top(-2)).touch_tip() #273: <Slot B1><Well G9>

p200.aspirate(180, trough['A4'].bottom(82))
p200.dispense(180, plate3[78].top(-2)).touch_tip() #274: <Slot B1><Well G10>

p200.aspirate(180, trough['A4'].bottom(82))
p200.dispense(180, plate3[86].top(-2)).touch_tip() #275: <Slot B1><Well G11>

p200.aspirate(180, trough['A4'].bottom(81))
p200.dispense(180, plate3[94].top(-2)).touch_tip() #276: <Slot B1><Well G12>

p200.aspirate(180, trough['A4'].bottom(81))
p200.dispense(180, plate3[7].top(-2)).touch_tip() #277: <Slot B1><Well H1>

p200.aspirate(180, trough['A4'].bottom(81))
p200.dispense(180, plate3[15].top(-2)).touch_tip() #278: <Slot B1><Well H2>

p200.aspirate(180, trough['A4'].bottom(80))
p200.dispense(180, plate3[23].top(-2)).touch_tip() #279: <Slot B1><Well H3>

p200.aspirate(180, trough['A4'].bottom(80))
p200.dispense(180, plate3[31].top(-2)).touch_tip() #280: <Slot B1><Well H4>

p200.aspirate(180, trough['A4'].bottom(80))
p200.dispense(180, plate3[39].top(-2)).touch_tip() #281: <Slot B1><Well H5>

p200.aspirate(180, trough['A4'].bottom(79))
p200.dispense(180, plate3[47].top(-2)).touch_tip() #282: <Slot B1><Well H6>

p200.aspirate(180, trough['A4'].bottom(79))
p200.dispense(180, plate3[55].top(-2)).touch_tip() #283: <Slot B1><Well H7>

p200.aspirate(180, trough['A4'].bottom(79))
p200.dispense(180, plate3[63].top(-2)).touch_tip() #284: <Slot B1><Well H8>

p200.aspirate(180, trough['A4'].bottom(78))
p200.dispense(180, plate3[71].top(-2)).touch_tip() #285: <Slot B1><Well H9>

p200.aspirate(180, trough['A4'].bottom(78))
p200.dispense(180, plate3[79].top(-2)).touch_tip() #286: <Slot B1><Well H10>

p200.aspirate(180, trough['A4'].bottom(78))
p200.dispense(180, plate3[87].top(-2)).touch_tip() #287: <Slot B1><Well H11>

p200.aspirate(180, trough['A4'].bottom(77))
p200.dispense(180, plate3[95].top(-2)).touch_tip() #288: <Slot B1><Well H12>

p200.aspirate(180, trough['A4'].bottom(77))
p200.dispense(180, plate4[0].top(-2)).touch_tip() #289: <Slot A1><Well A1>

p200.aspirate(180, trough['A4'].bottom(77))
p200.dispense(180, plate4[8].top(-2)).touch_tip() #290: <Slot A1><Well A2>

p200.aspirate(180, trough['A4'].bottom(76))
p200.dispense(180, plate4[16].top(-2)).touch_tip() #291: <Slot A1><Well A3>

p200.aspirate(180, trough['A4'].bottom(76))
p200.dispense(180, plate4[24].top(-2)).touch_tip() #292: <Slot A1><Well A4>

p200.aspirate(180, trough['A4'].bottom(76))
p200.dispense(180, plate4[32].top(-2)).touch_tip() #293: <Slot A1><Well A5>

p200.aspirate(180, trough['A4'].bottom(75))
p200.dispense(180, plate4[40].top(-2)).touch_tip() #294: <Slot A1><Well A6>

p200.aspirate(180, trough['A4'].bottom(75))
p200.dispense(180, plate4[48].top(-2)).touch_tip() #295: <Slot A1><Well A7>

p200.aspirate(180, trough['A4'].bottom(75))
p200.dispense(180, plate4[56].top(-2)).touch_tip() #296: <Slot A1><Well A8>

p200.aspirate(180, trough['A4'].bottom(74))
p200.dispense(180, plate4[64].top(-2)).touch_tip() #297: <Slot A1><Well A9>

p200.aspirate(180, trough['A4'].bottom(74))
p200.dispense(180, plate4[72].top(-2)).touch_tip() #298: <Slot A1><Well A10>

p200.aspirate(180, trough['A4'].bottom(74))
p200.dispense(180, plate4[80].top(-2)).touch_tip() #299: <Slot A1><Well A11>

p200.aspirate(180, trough['A4'].bottom(73))
p200.dispense(180, plate4[88].top(-2)).touch_tip() #300: <Slot A1><Well A12>

p200.aspirate(180, trough['A4'].bottom(73))
p200.dispense(180, plate4[1].top(-2)).touch_tip() #301: <Slot A1><Well B1>

p200.aspirate(180, trough['A4'].bottom(73))
p200.dispense(180, plate4[9].top(-2)).touch_tip() #302: <Slot A1><Well B2>

p200.aspirate(180, trough['A4'].bottom(73))
p200.dispense(180, plate4[17].top(-2)).touch_tip() #303: <Slot A1><Well B3>

p200.aspirate(180, trough['A4'].bottom(72))
p200.dispense(180, plate4[25].top(-2)).touch_tip() #304: <Slot A1><Well B4>

p200.aspirate(180, trough['A4'].bottom(72))
p200.dispense(180, plate4[33].top(-2)).touch_tip() #305: <Slot A1><Well B5>

p200.aspirate(180, trough['A4'].bottom(72))
p200.dispense(180, plate4[41].top(-2)).touch_tip() #306: <Slot A1><Well B6>

p200.aspirate(180, trough['A4'].bottom(71))
p200.dispense(180, plate4[49].top(-2)).touch_tip() #307: <Slot A1><Well B7>

p200.aspirate(180, trough['A4'].bottom(71))
p200.dispense(180, plate4[57].top(-2)).touch_tip() #308: <Slot A1><Well B8>

p200.aspirate(180, trough['A4'].bottom(71))
p200.dispense(180, plate4[65].top(-2)).touch_tip() #309: <Slot A1><Well B9>

p200.aspirate(180, trough['A4'].bottom(70))
p200.dispense(180, plate4[73].top(-2)).touch_tip() #310: <Slot A1><Well B10>

p200.aspirate(180, trough['A4'].bottom(70))
p200.dispense(180, plate4[81].top(-2)).touch_tip() #311: <Slot A1><Well B11>

p200.aspirate(180, trough['A4'].bottom(70))
p200.dispense(180, plate4[89].top(-2)).touch_tip() #312: <Slot A1><Well B12>

p200.aspirate(180, trough['A4'].bottom(69))
p200.dispense(180, plate4[2].top(-2)).touch_tip() #313: <Slot A1><Well C1>

p200.aspirate(180, trough['A4'].bottom(69))
p200.dispense(180, plate4[10].top(-2)).touch_tip() #314: <Slot A1><Well C2>

p200.aspirate(180, trough['A4'].bottom(69))
p200.dispense(180, plate4[18].top(-2)).touch_tip() #315: <Slot A1><Well C3>

p200.aspirate(180, trough['A4'].bottom(68))
p200.dispense(180, plate4[26].top(-2)).touch_tip() #316: <Slot A1><Well C4>

p200.aspirate(180, trough['A4'].bottom(68))
p200.dispense(180, plate4[34].top(-2)).touch_tip() #317: <Slot A1><Well C5>

p200.aspirate(180, trough['A4'].bottom(68))
p200.dispense(180, plate4[42].top(-2)).touch_tip() #318: <Slot A1><Well C6>

p200.aspirate(180, trough['A4'].bottom(67))
p200.dispense(180, plate4[50].top(-2)).touch_tip() #319: <Slot A1><Well C7>

p200.aspirate(180, trough['A4'].bottom(67))
p200.dispense(180, plate4[58].top(-2)).touch_tip() #320: <Slot A1><Well C8>

p200.aspirate(180, trough['A4'].bottom(67))
p200.dispense(180, plate4[66].top(-2)).touch_tip() #321: <Slot A1><Well C9>

p200.aspirate(180, trough['A4'].bottom(66))
p200.dispense(180, plate4[74].top(-2)).touch_tip() #322: <Slot A1><Well C10>

p200.aspirate(180, trough['A4'].bottom(66))
p200.dispense(180, plate4[82].top(-2)).touch_tip() #323: <Slot A1><Well C11>

p200.aspirate(180, trough['A4'].bottom(66))
p200.dispense(180, plate4[90].top(-2)).touch_tip() #324: <Slot A1><Well C12>

p200.aspirate(180, trough['A4'].bottom(65))
p200.dispense(180, plate4[3].top(-2)).touch_tip() #325: <Slot A1><Well D1>

p200.aspirate(180, trough['A4'].bottom(65))
p200.dispense(180, plate4[11].top(-2)).touch_tip() #326: <Slot A1><Well D2>

p200.aspirate(180, trough['A4'].bottom(65))
p200.dispense(180, plate4[19].top(-2)).touch_tip() #327: <Slot A1><Well D3>

p200.aspirate(180, trough['A4'].bottom(64))
p200.dispense(180, plate4[27].top(-2)).touch_tip() #328: <Slot A1><Well D4>

p200.aspirate(180, trough['A4'].bottom(64))
p200.dispense(180, plate4[35].top(-2)).touch_tip() #329: <Slot A1><Well D5>

p200.aspirate(180, trough['A4'].bottom(64))
p200.dispense(180, plate4[43].top(-2)).touch_tip() #330: <Slot A1><Well D6>

p200.aspirate(180, trough['A4'].bottom(63))
p200.dispense(180, plate4[51].top(-2)).touch_tip() #331: <Slot A1><Well D7>

p200.aspirate(180, trough['A4'].bottom(63))
p200.dispense(180, plate4[59].top(-2)).touch_tip() #332: <Slot A1><Well D8>

p200.aspirate(180, trough['A4'].bottom(63))
p200.dispense(180, plate4[67].top(-2)).touch_tip() #333: <Slot A1><Well D9>

p200.aspirate(180, trough['A4'].bottom(62))
p200.dispense(180, plate4[75].top(-2)).touch_tip() #334: <Slot A1><Well D10>

p200.aspirate(180, trough['A4'].bottom(62))
p200.dispense(180, plate4[83].top(-2)).touch_tip() #335: <Slot A1><Well D11>

p200.aspirate(180, trough['A4'].bottom(62))
p200.dispense(180, plate4[91].top(-2)).touch_tip() #336: <Slot A1><Well D12>

p200.aspirate(180, trough['A4'].bottom(61))
p200.dispense(180, plate4[4].top(-2)).touch_tip() #337: <Slot A1><Well E1>

p200.aspirate(180, trough['A4'].bottom(61))
p200.dispense(180, plate4[12].top(-2)).touch_tip() #338: <Slot A1><Well E2>

p200.aspirate(180, trough['A4'].bottom(61))
p200.dispense(180, plate4[20].top(-2)).touch_tip() #339: <Slot A1><Well E3>

p200.aspirate(180, trough['A4'].bottom(61))
p200.dispense(180, plate4[28].top(-2)).touch_tip() #340: <Slot A1><Well E4>

p200.aspirate(180, trough['A4'].bottom(60))
p200.dispense(180, plate4[36].top(-2)).touch_tip() #341: <Slot A1><Well E5>

p200.aspirate(180, trough['A4'].bottom(60))
p200.dispense(180, plate4[44].top(-2)).touch_tip() #342: <Slot A1><Well E6>

p200.aspirate(180, trough['A4'].bottom(60))
p200.dispense(180, plate4[52].top(-2)).touch_tip() #343: <Slot A1><Well E7>

p200.aspirate(180, trough['A4'].bottom(59))
p200.dispense(180, plate4[60].top(-2)).touch_tip() #344: <Slot A1><Well E8>

p200.aspirate(180, trough['A4'].bottom(59))
p200.dispense(180, plate4[68].top(-2)).touch_tip() #345: <Slot A1><Well E9>

p200.aspirate(180, trough['A4'].bottom(59))
p200.dispense(180, plate4[76].top(-2)).touch_tip() #346: <Slot A1><Well E10>

p200.aspirate(180, trough['A4'].bottom(58))
p200.dispense(180, plate4[84].top(-2)).touch_tip() #347: <Slot A1><Well E11>

p200.aspirate(180, trough['A4'].bottom(58))
p200.dispense(180, plate4[92].top(-2)).touch_tip() #348: <Slot A1><Well E12>

p200.aspirate(180, trough['A4'].bottom(58))
p200.dispense(180, plate4[5].top(-2)).touch_tip() #349: <Slot A1><Well F1>

p200.aspirate(180, trough['A4'].bottom(57))
p200.dispense(180, plate4[13].top(-2)).touch_tip() #350: <Slot A1><Well F2>

p200.aspirate(180, trough['A4'].bottom(57))
p200.dispense(180, plate4[21].top(-2)).touch_tip() #351: <Slot A1><Well F3>

p200.aspirate(180, trough['A4'].bottom(57))
p200.dispense(180, plate4[29].top(-2)).touch_tip() #352: <Slot A1><Well F4>

p200.aspirate(180, trough['A4'].bottom(56))
p200.dispense(180, plate4[37].top(-2)).touch_tip() #353: <Slot A1><Well F5>

p200.aspirate(180, trough['A4'].bottom(56))
p200.dispense(180, plate4[45].top(-2)).touch_tip() #354: <Slot A1><Well F6>

p200.aspirate(180, trough['A4'].bottom(56))
p200.dispense(180, plate4[53].top(-2)).touch_tip() #355: <Slot A1><Well F7>

p200.aspirate(180, trough['A4'].bottom(55))
p200.dispense(180, plate4[61].top(-2)).touch_tip() #356: <Slot A1><Well F8>

p200.aspirate(180, trough['A4'].bottom(55))
p200.dispense(180, plate4[69].top(-2)).touch_tip() #357: <Slot A1><Well F9>

p200.aspirate(180, trough['A4'].bottom(55))
p200.dispense(180, plate4[77].top(-2)).touch_tip() #358: <Slot A1><Well F10>

p200.aspirate(180, trough['A4'].bottom(54))
p200.dispense(180, plate4[85].top(-2)).touch_tip() #359: <Slot A1><Well F11>

p200.aspirate(180, trough['A4'].bottom(54))
p200.dispense(180, plate4[93].top(-2)).touch_tip() #360: <Slot A1><Well F12>

p200.aspirate(180, trough['A4'].bottom(54))
p200.dispense(180, plate4[6].top(-2)).touch_tip() #361: <Slot A1><Well G1>

p200.aspirate(180, trough['A4'].bottom(53))
p200.dispense(180, plate4[14].top(-2)).touch_tip() #362: <Slot A1><Well G2>

p200.aspirate(180, trough['A4'].bottom(53))
p200.dispense(180, plate4[22].top(-2)).touch_tip() #363: <Slot A1><Well G3>

p200.aspirate(180, trough['A4'].bottom(53))
p200.dispense(180, plate4[30].top(-2)).touch_tip() #364: <Slot A1><Well G4>

p200.aspirate(180, trough['A4'].bottom(52))
p200.dispense(180, plate4[38].top(-2)).touch_tip() #365: <Slot A1><Well G5>

p200.aspirate(180, trough['A4'].bottom(52))
p200.dispense(180, plate4[46].top(-2)).touch_tip() #366: <Slot A1><Well G6>

p200.aspirate(180, trough['A4'].bottom(52))
p200.dispense(180, plate4[54].top(-2)).touch_tip() #367: <Slot A1><Well G7>

p200.aspirate(180, trough['A4'].bottom(51))
p200.dispense(180, plate4[62].top(-2)).touch_tip() #368: <Slot A1><Well G8>

p200.aspirate(180, trough['A4'].bottom(51))
p200.dispense(180, plate4[70].top(-2)).touch_tip() #369: <Slot A1><Well G9>

p200.aspirate(180, trough['A4'].bottom(51))
p200.dispense(180, plate4[78].top(-2)).touch_tip() #370: <Slot A1><Well G10>

p200.aspirate(180, trough['A4'].bottom(50))
p200.dispense(180, plate4[86].top(-2)).touch_tip() #371: <Slot A1><Well G11>

p200.aspirate(180, trough['A4'].bottom(50))
p200.dispense(180, plate4[94].top(-2)).touch_tip() #372: <Slot A1><Well G12>

p200.aspirate(180, trough['A4'].bottom(50))
p200.dispense(180, plate4[7].top(-2)).touch_tip() #373: <Slot A1><Well H1>

p200.aspirate(180, trough['A4'].bottom(50))
p200.dispense(180, plate4[15].top(-2)).touch_tip() #374: <Slot A1><Well H2>

p200.aspirate(180, trough['A4'].bottom(49))
p200.dispense(180, plate4[23].top(-2)).touch_tip() #375: <Slot A1><Well H3>

p200.aspirate(180, trough['A4'].bottom(49))
p200.dispense(180, plate4[31].top(-2)).touch_tip() #376: <Slot A1><Well H4>

p200.aspirate(180, trough['A4'].bottom(49))
p200.dispense(180, plate4[39].top(-2)).touch_tip() #377: <Slot A1><Well H5>

p200.aspirate(180, trough['A4'].bottom(48))
p200.dispense(180, plate4[47].top(-2)).touch_tip() #378: <Slot A1><Well H6>

p200.aspirate(180, trough['A4'].bottom(48))
p200.dispense(180, plate4[55].top(-2)).touch_tip() #379: <Slot A1><Well H7>

p200.aspirate(180, trough['A4'].bottom(48))
p200.dispense(180, plate4[63].top(-2)).touch_tip() #380: <Slot A1><Well H8>

p200.aspirate(180, trough['A4'].bottom(47))
p200.dispense(180, plate4[71].top(-2)).touch_tip() #381: <Slot A1><Well H9>

p200.aspirate(180, trough['A4'].bottom(47))
p200.dispense(180, plate4[79].top(-2)).touch_tip() #382: <Slot A1><Well H10>

p200.aspirate(180, trough['A4'].bottom(47))
p200.dispense(180, plate4[87].top(-2)).touch_tip() #383: <Slot A1><Well H11>

p200.aspirate(180, trough['A4'].bottom(47))
p200.dispense(180, plate4[95].top(-2)).touch_tip() #384: <Slot A1><Well H12>

p200.drop_tip()
##