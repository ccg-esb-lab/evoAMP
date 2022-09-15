

###################################################################################
#
# SCRIPT GENERATED ON 16/01/2018 FROM THE FOLLOWING LAYOUT FILES:
#  fileDictName=layouts/KeyTest.txt
#  fileTroughName=layouts/Trough_Test.txt
#  fileLayoutName=layouts/Layout_test_4plates.txt
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
p200.dispense(180, plate1[80].top(-2)).touch_tip() #3: <Slot D1><Well A11>

p200.aspirate(180, trough['A3'].bottom(88))
p200.dispense(180, plate1[88].top(-2)).touch_tip() #4: <Slot D1><Well A12>

p200.aspirate(180, trough['A3'].bottom(88))
p200.dispense(180, plate1[17].top(-2)).touch_tip() #5: <Slot D1><Well B3>

p200.aspirate(180, trough['A3'].bottom(88))
p200.dispense(180, plate1[25].top(-2)).touch_tip() #6: <Slot D1><Well B4>

p200.aspirate(180, trough['A3'].bottom(87))
p200.dispense(180, plate1[65].top(-2)).touch_tip() #7: <Slot D1><Well B9>

p200.aspirate(180, trough['A3'].bottom(87))
p200.dispense(180, plate1[73].top(-2)).touch_tip() #8: <Slot D1><Well B10>

p200.aspirate(180, trough['A3'].bottom(87))
p200.dispense(180, plate1[34].top(-2)).touch_tip() #9: <Slot D1><Well C5>

p200.aspirate(180, trough['A3'].bottom(86))
p200.dispense(180, plate1[58].top(-2)).touch_tip() #10: <Slot D1><Well C8>

p200.aspirate(180, trough['A3'].bottom(86))
p200.dispense(180, plate1[43].top(-2)).touch_tip() #11: <Slot D1><Well D6>

p200.aspirate(180, trough['A3'].bottom(86))
p200.dispense(180, plate1[51].top(-2)).touch_tip() #12: <Slot D1><Well D7>

p200.aspirate(180, trough['A3'].bottom(85))
p200.dispense(180, plate1[44].top(-2)).touch_tip() #13: <Slot D1><Well E6>

p200.aspirate(180, trough['A3'].bottom(85))
p200.dispense(180, plate1[52].top(-2)).touch_tip() #14: <Slot D1><Well E7>

p200.aspirate(180, trough['A3'].bottom(85))
p200.dispense(180, plate1[37].top(-2)).touch_tip() #15: <Slot D1><Well F5>

p200.aspirate(180, trough['A3'].bottom(84))
p200.dispense(180, plate1[61].top(-2)).touch_tip() #16: <Slot D1><Well F8>

p200.aspirate(180, trough['A3'].bottom(84))
p200.dispense(180, plate1[22].top(-2)).touch_tip() #17: <Slot D1><Well G3>

p200.aspirate(180, trough['A3'].bottom(84))
p200.dispense(180, plate1[30].top(-2)).touch_tip() #18: <Slot D1><Well G4>

p200.aspirate(180, trough['A3'].bottom(84))
p200.dispense(180, plate1[70].top(-2)).touch_tip() #19: <Slot D1><Well G9>

p200.aspirate(180, trough['A3'].bottom(83))
p200.dispense(180, plate1[78].top(-2)).touch_tip() #20: <Slot D1><Well G10>

p200.aspirate(180, trough['A3'].bottom(83))
p200.dispense(180, plate1[7].top(-2)).touch_tip() #21: <Slot D1><Well H1>

p200.aspirate(180, trough['A3'].bottom(83))
p200.dispense(180, plate1[15].top(-2)).touch_tip() #22: <Slot D1><Well H2>

p200.aspirate(180, trough['A3'].bottom(82))
p200.dispense(180, plate1[87].top(-2)).touch_tip() #23: <Slot D1><Well H11>

p200.aspirate(180, trough['A3'].bottom(82))
p200.dispense(180, plate1[95].top(-2)).touch_tip() #24: <Slot D1><Well H12>

p200.aspirate(180, trough['A3'].bottom(82))
p200.dispense(180, plate2[0].top(-2)).touch_tip() #25: <Slot C1><Well A1>

p200.aspirate(180, trough['A3'].bottom(81))
p200.dispense(180, plate2[8].top(-2)).touch_tip() #26: <Slot C1><Well A2>

p200.aspirate(180, trough['A3'].bottom(81))
p200.dispense(180, plate2[80].top(-2)).touch_tip() #27: <Slot C1><Well A11>

p200.aspirate(180, trough['A3'].bottom(81))
p200.dispense(180, plate2[88].top(-2)).touch_tip() #28: <Slot C1><Well A12>

p200.aspirate(180, trough['A3'].bottom(80))
p200.dispense(180, plate2[17].top(-2)).touch_tip() #29: <Slot C1><Well B3>

p200.aspirate(180, trough['A3'].bottom(80))
p200.dispense(180, plate2[25].top(-2)).touch_tip() #30: <Slot C1><Well B4>

p200.aspirate(180, trough['A3'].bottom(80))
p200.dispense(180, plate2[65].top(-2)).touch_tip() #31: <Slot C1><Well B9>

p200.aspirate(180, trough['A3'].bottom(79))
p200.dispense(180, plate2[73].top(-2)).touch_tip() #32: <Slot C1><Well B10>

p200.aspirate(180, trough['A3'].bottom(79))
p200.dispense(180, plate2[34].top(-2)).touch_tip() #33: <Slot C1><Well C5>

p200.aspirate(180, trough['A3'].bottom(79))
p200.dispense(180, plate2[58].top(-2)).touch_tip() #34: <Slot C1><Well C8>

p200.aspirate(180, trough['A3'].bottom(78))
p200.dispense(180, plate2[43].top(-2)).touch_tip() #35: <Slot C1><Well D6>

p200.aspirate(180, trough['A3'].bottom(78))
p200.dispense(180, plate2[51].top(-2)).touch_tip() #36: <Slot C1><Well D7>

p200.aspirate(180, trough['A3'].bottom(78))
p200.dispense(180, plate2[44].top(-2)).touch_tip() #37: <Slot C1><Well E6>

p200.aspirate(180, trough['A3'].bottom(77))
p200.dispense(180, plate2[52].top(-2)).touch_tip() #38: <Slot C1><Well E7>

p200.aspirate(180, trough['A3'].bottom(77))
p200.dispense(180, plate2[37].top(-2)).touch_tip() #39: <Slot C1><Well F5>

p200.aspirate(180, trough['A3'].bottom(77))
p200.dispense(180, plate2[61].top(-2)).touch_tip() #40: <Slot C1><Well F8>

p200.aspirate(180, trough['A3'].bottom(76))
p200.dispense(180, plate2[22].top(-2)).touch_tip() #41: <Slot C1><Well G3>

p200.aspirate(180, trough['A3'].bottom(76))
p200.dispense(180, plate2[30].top(-2)).touch_tip() #42: <Slot C1><Well G4>

p200.aspirate(180, trough['A3'].bottom(76))
p200.dispense(180, plate2[70].top(-2)).touch_tip() #43: <Slot C1><Well G9>

p200.aspirate(180, trough['A3'].bottom(75))
p200.dispense(180, plate2[78].top(-2)).touch_tip() #44: <Slot C1><Well G10>

p200.aspirate(180, trough['A3'].bottom(75))
p200.dispense(180, plate2[7].top(-2)).touch_tip() #45: <Slot C1><Well H1>

p200.aspirate(180, trough['A3'].bottom(75))
p200.dispense(180, plate2[15].top(-2)).touch_tip() #46: <Slot C1><Well H2>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate2[87].top(-2)).touch_tip() #47: <Slot C1><Well H11>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate2[95].top(-2)).touch_tip() #48: <Slot C1><Well H12>

p200.aspirate(180, trough['A3'].bottom(74))
p200.dispense(180, plate3[0].top(-2)).touch_tip() #49: <Slot B1><Well A1>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate3[8].top(-2)).touch_tip() #50: <Slot B1><Well A2>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate3[80].top(-2)).touch_tip() #51: <Slot B1><Well A11>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate3[88].top(-2)).touch_tip() #52: <Slot B1><Well A12>

p200.aspirate(180, trough['A3'].bottom(73))
p200.dispense(180, plate3[17].top(-2)).touch_tip() #53: <Slot B1><Well B3>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate3[25].top(-2)).touch_tip() #54: <Slot B1><Well B4>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate3[65].top(-2)).touch_tip() #55: <Slot B1><Well B9>

p200.aspirate(180, trough['A3'].bottom(72))
p200.dispense(180, plate3[73].top(-2)).touch_tip() #56: <Slot B1><Well B10>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate3[34].top(-2)).touch_tip() #57: <Slot B1><Well C5>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate3[58].top(-2)).touch_tip() #58: <Slot B1><Well C8>

p200.aspirate(180, trough['A3'].bottom(71))
p200.dispense(180, plate3[43].top(-2)).touch_tip() #59: <Slot B1><Well D6>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate3[51].top(-2)).touch_tip() #60: <Slot B1><Well D7>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate3[44].top(-2)).touch_tip() #61: <Slot B1><Well E6>

p200.aspirate(180, trough['A3'].bottom(70))
p200.dispense(180, plate3[52].top(-2)).touch_tip() #62: <Slot B1><Well E7>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate3[37].top(-2)).touch_tip() #63: <Slot B1><Well F5>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate3[61].top(-2)).touch_tip() #64: <Slot B1><Well F8>

p200.aspirate(180, trough['A3'].bottom(69))
p200.dispense(180, plate3[22].top(-2)).touch_tip() #65: <Slot B1><Well G3>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate3[30].top(-2)).touch_tip() #66: <Slot B1><Well G4>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate3[70].top(-2)).touch_tip() #67: <Slot B1><Well G9>

p200.aspirate(180, trough['A3'].bottom(68))
p200.dispense(180, plate3[78].top(-2)).touch_tip() #68: <Slot B1><Well G10>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate3[7].top(-2)).touch_tip() #69: <Slot B1><Well H1>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate3[15].top(-2)).touch_tip() #70: <Slot B1><Well H2>

p200.aspirate(180, trough['A3'].bottom(67))
p200.dispense(180, plate3[87].top(-2)).touch_tip() #71: <Slot B1><Well H11>

p200.aspirate(180, trough['A3'].bottom(66))
p200.dispense(180, plate3[95].top(-2)).touch_tip() #72: <Slot B1><Well H12>

p200.aspirate(180, trough['A3'].bottom(66))
p200.dispense(180, plate4[0].top(-2)).touch_tip() #73: <Slot A1><Well A1>

p200.aspirate(180, trough['A3'].bottom(66))
p200.dispense(180, plate4[8].top(-2)).touch_tip() #74: <Slot A1><Well A2>

p200.aspirate(180, trough['A3'].bottom(65))
p200.dispense(180, plate4[80].top(-2)).touch_tip() #75: <Slot A1><Well A11>

p200.aspirate(180, trough['A3'].bottom(65))
p200.dispense(180, plate4[88].top(-2)).touch_tip() #76: <Slot A1><Well A12>

p200.aspirate(180, trough['A3'].bottom(65))
p200.dispense(180, plate4[17].top(-2)).touch_tip() #77: <Slot A1><Well B3>

p200.aspirate(180, trough['A3'].bottom(64))
p200.dispense(180, plate4[25].top(-2)).touch_tip() #78: <Slot A1><Well B4>

p200.aspirate(180, trough['A3'].bottom(64))
p200.dispense(180, plate4[65].top(-2)).touch_tip() #79: <Slot A1><Well B9>

p200.aspirate(180, trough['A3'].bottom(64))
p200.dispense(180, plate4[73].top(-2)).touch_tip() #80: <Slot A1><Well B10>

p200.aspirate(180, trough['A3'].bottom(63))
p200.dispense(180, plate4[34].top(-2)).touch_tip() #81: <Slot A1><Well C5>

p200.aspirate(180, trough['A3'].bottom(63))
p200.dispense(180, plate4[58].top(-2)).touch_tip() #82: <Slot A1><Well C8>

p200.aspirate(180, trough['A3'].bottom(63))
p200.dispense(180, plate4[43].top(-2)).touch_tip() #83: <Slot A1><Well D6>

p200.aspirate(180, trough['A3'].bottom(62))
p200.dispense(180, plate4[51].top(-2)).touch_tip() #84: <Slot A1><Well D7>

p200.aspirate(180, trough['A3'].bottom(62))
p200.dispense(180, plate4[44].top(-2)).touch_tip() #85: <Slot A1><Well E6>

p200.aspirate(180, trough['A3'].bottom(62))
p200.dispense(180, plate4[52].top(-2)).touch_tip() #86: <Slot A1><Well E7>

p200.aspirate(180, trough['A3'].bottom(61))
p200.dispense(180, plate4[37].top(-2)).touch_tip() #87: <Slot A1><Well F5>

p200.aspirate(180, trough['A3'].bottom(61))
p200.dispense(180, plate4[61].top(-2)).touch_tip() #88: <Slot A1><Well F8>

p200.aspirate(180, trough['A3'].bottom(61))
p200.dispense(180, plate4[22].top(-2)).touch_tip() #89: <Slot A1><Well G3>

p200.aspirate(180, trough['A3'].bottom(61))
p200.dispense(180, plate4[30].top(-2)).touch_tip() #90: <Slot A1><Well G4>

p200.aspirate(180, trough['A3'].bottom(60))
p200.dispense(180, plate4[70].top(-2)).touch_tip() #91: <Slot A1><Well G9>

p200.aspirate(180, trough['A3'].bottom(60))
p200.dispense(180, plate4[78].top(-2)).touch_tip() #92: <Slot A1><Well G10>

p200.aspirate(180, trough['A3'].bottom(60))
p200.dispense(180, plate4[7].top(-2)).touch_tip() #93: <Slot A1><Well H1>

p200.aspirate(180, trough['A3'].bottom(59))
p200.dispense(180, plate4[15].top(-2)).touch_tip() #94: <Slot A1><Well H2>

p200.aspirate(180, trough['A3'].bottom(59))
p200.dispense(180, plate4[87].top(-2)).touch_tip() #95: <Slot A1><Well H11>

p200.aspirate(180, trough['A3'].bottom(59))
p200.dispense(180, plate4[95].top(-2)).touch_tip() #96: <Slot A1><Well H12>

p200.drop_tip()
##