SECTIONS = {
 'Where the Numbers Live': {'code': 'AI.II.F.K1, K2', 'title': 'Performance Charts and Factors', 'img': 'POH_Fig5-5_short_field_takeoff_table', 'cite': 'PHAK 11-1 to 11-20, POH Section 5',
   'goals': ['Where performance data lives', 'How to read and interpolate charts', 'Density altitude, technique, configuration', 'Runway, wind, and weight'],
   'why': 'Why it matters: these charts tell you if the runway is long enough before you are rolling down it.'},
 'The Type Certificate Data Sheet': {'code': 'AI.II.F.K3 to K5', 'title': 'Weight and Balance', 'img': 'POH_Fig6-7_cg_moment_envelope', 'cite': 'PHAK 10-1 to 10-11, POH 2-8, TCDS 3A12',
   'goals': ['The TCDS and C172S limits', 'Weight and balance terms', 'Three ways to compute CG', 'Forward and aft CG effects'],
   'why': 'Why it matters: an airplane loaded out of limits can be hard or impossible to control.'},
 'Example: C172S Takeoff Setup': {'code': 'AI.II.F.S1, S2', 'title': 'Worked C172S Examples', 'img': 'POH_Fig5-8_cruise_performance', 'cite': 'POH 5-3 to 5-8, POH 6-10',
   'goals': ['Takeoff distance with wind', 'Climb fuel and cruise', 'Total fuel required', 'Loading, CG, and fuel burn'],
   'why': 'Why it matters: this is exactly what you will do with a student before a cross-country.'},
 'Risk: Charts vs. Real Life': {'code': 'AI.II.F.R1 to R6', 'title': 'Risk Management', 'img': 'POH_5-3_performance_intro', 'cite': 'POH 5-3, PHAK 10-1 to 10-4',
   'goals': ['Charts versus real life', 'Limits and overweight', 'CG limits and shifting weight'],
   'why': 'Why it matters: the numbers are only as safe as the margins you add.'},
}

CHECKS = {
 'Loading and Weight': {'code': 'AI.II.F.K1, K2', 'cite': 'PHAK 11-2, POH Fig 5-5', 'qa': [
   ('What three things does thin air take away?', 'Power, thrust, and lift (PHAK 11-2).'),
   ('Your takeoff distance is 2,000 feet with no wind. You have an 18 knot headwind. New distance?', '18 / 9 x 10% = 20% shorter, so about 1,600 feet (POH Fig 5-5).'),
   ('Taking off from dry grass, what correction does the C172S chart give?', 'Add 15 percent of the ground roll figure (POH Fig 5-5).')]},
 'Aerodynamics: Aft CG': {'code': 'AI.II.F.K3 to K5', 'cite': 'PHAK 10-7, POH 2-8, PHAK 5-44', 'qa': [
   ('How do you find the CG?', 'Total moment divided by total weight (PHAK 10-7).'),
   ('What is the C172S forward CG limit at 2,550 lb?', '41.0 inches aft of datum (POH 2-8).'),
   ('Does a forward CG raise or lower the stall speed?', 'Raises it (PHAK 5-44).')]},
 'Fixing an Out-of-Limits CG': {'code': 'AI.II.F.S1, S2', 'cite': 'POH 5-6, POH 5-7, POH 6-10', 'qa': [
   ('Climb fuel from 2,000 to 8,000 feet at 16 degrees above standard?', '2.2 gallons plus 16 percent = 2.6 gallons (POH 5-6).'),
   ('Total fuel required for the POH sample trip?', '39.2 gallons (POH 5-7).'),
   ('CG of the POH sample load at takeoff?', '112,800 / 2,550 = 44.2 inches (POH 6-10).')]},
 'Risk: CG Limits and Shifting Weight': {'code': 'AI.II.F.R1 to R6', 'cite': 'POH 5-3, PHAK 10-4, PHAK 10-11', 'qa': [
   ('How much can real performance differ from the charts?', 'The POH says variations of 10 percent or more in range and endurance (POH 5-3).'),
   ('Which regulation requires following the AFM limits?', '14 CFR 91.9 (PHAK 10-4).'),
   ('A passenger adds a bag after you finished the weight and balance. What now?', 'Recompute. Adding weight changes both weight and CG (PHAK 10-11).')]},
}

KNOW = {
 'Reading Tables and Interpolating': 'Not sure? Read the chart at the next higher weight, altitude, and temperature (POH 5-4).',
 'Loading and Weight': 'Extra weight means a higher lift-off speed, more mass to accelerate, and more drag and friction (PHAK 11-15).',
 'C172S Weight and CG Limits': 'Max takeoff 2,550 lb. CG range 35.0 to 47.3 inches aft of the firewall (POH 2-8).',
 'Aerodynamics: Forward CG': 'Forward CG: higher stall speed and heavier control forces (PHAK 5-44).',
 'Aerodynamics: Aft CG': 'Aft CG: less stable, light controls, harder stall and spin recovery (PHAK 10-3).',
 'Example: Total Fuel Required': 'The POH sample adds start, taxi, and takeoff fuel plus a 45 minute reserve (POH 5-7).',
 'How the Charts Are Made': 'Chart numbers come from a new airplane flown with average skill (PHAK 11-19).',
 'Airplane Configuration': 'Flaps up landing in the C172S: add 9 KIAS and allow 35 percent more distance (POH Fig 5-11).',
}

MEMORY = {
 'Density Altitude in Plain Words': 'Hot, high, and humid means poor performance.',
 'Airport Environment: Wind': 'Headwind: minus 10 percent per 9 knots. Tailwind: plus 10 percent per 2 knots (POH Fig 5-5).',
 'Moment and CG in Plain Words': 'Moment = Weight x Arm. CG = Total Moment / Total Weight.',
 'Fixing an Out-of-Limits CG': 'Weight moved / total weight = CG change / distance moved (PHAK 10-11).',
}

IMG2 = {
 'Loading and Weight': 'POH_Fig5-5_short_field_takeoff_table',
 'Airport Environment: Surface and Slope': 'PHAK_Fig11-16_runway_surface',
 'The Type Certificate Data Sheet': 'TCDS_3A12_p30_172S_cg_datum',
}

PLAIN = {
 'Definition: Density Altitude': 'Density altitude is the altitude the airplane feels like it is at. Hot, high, and humid air makes it feel higher, so it performs worse.',
 'Definitions: Datum and Arm': 'The datum is the zero point on a tape measure. The arm is how far each seat, tank, or bag sits from that zero point.',
 'Definitions: Moment and CG': 'Moment is how hard a weight tries to tip the airplane. The CG is the balance point of everything combined.',
 'Definitions: CG Limits and Maximum Weight': 'CG limits are the front and back edges of the safe balance zone. Maximum weight is the heaviest the airplane may be.',
 'Definitions: Basic Empty Weight and Useful Load': 'Basic empty weight is the airplane with unusable fuel and full oil, nothing else. Useful load is what is left for people, bags, and fuel.',
}
