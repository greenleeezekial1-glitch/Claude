SECTIONS = {
 'Definition: Perceptions': {'code': 'FI.I.B.K3', 'title': 'Perceptions and Insight', 'img': 'AIH_Fig3-5_senses', 'cite': 'AIH 3-7 to 3-9',
   'goals': ['What perceptions are', 'Five factors that affect perception', 'What insight is', 'How you build insight'],
   'why': 'Why it matters: every lesson you teach goes in through your student\'s senses. Knowing what blocks perception makes you a better instructor.'},
 'Definition: Stability': {'code': 'AI.II.D.K2', 'title': 'Stability, Maneuverability, and Controllability', 'img': 'PHAK_Fig5-21_static_stability', 'cite': 'PHAK 5-14, PHAK 5-15',
   'goals': ['Static vs. dynamic stability', 'Positive, neutral, negative', 'Maneuverability and controllability', 'How CG changes all three'],
   'why': 'Why it matters: this is why the C172S settles back down after a bump, and why loading it wrong makes it harder to fly.'},
 'C172S Engine': {'code': 'AI.II.E.K1c', 'title': 'Powerplant and Propeller', 'img': 'PHAK_Fig7-2_opposed_engine', 'cite': 'POH 7-28, POH 7-36, PHAK 7-1 to 7-5',
   'goals': ['The C172S engine', 'Throttle and mixture', 'How a propeller works', 'Fixed pitch and the tachometer'],
   'why': 'Why it matters: you have to explain the engine and prop of the airplane you fly, and the C172S is simpler than most study guides describe.'},
 'Definitions: Datum and Arm': {'code': 'AI.II.F.K3', 'title': 'Weight and Balance Terms', 'img': 'PHAK_Fig10-2_weight_and_balance', 'cite': 'PHAK 10-4, PHAK 10-5',
   'goals': ['Datum and arm', 'Moment and CG', 'Basic empty weight and useful load', 'CG limits and maximum weight'],
   'why': 'Why it matters: examiners ask for these word for word. Learn the PHAK wording, then the plain words.'},
 'VOR: Identification and Accuracy': {'code': 'AI.II.H.K1', 'title': 'Ground-Based Navigation', 'img': 'PHAK_Fig16-29_vor_indicator', 'cite': 'AIM 1-1-2 to 1-1-4, PHAK 16-23 to 16-26',
   'goals': ['Identify a VOR', 'Read the CDI and HSI', 'Track a radial in wind', 'VOR checks, NDB, interference'],
   'why': 'Why it matters: when GPS fails, the VOR is your backup. Your students need to use it without reverse sensing mistakes.'},
 'Definition: True Course': {'code': 'AI.II.I.K3', 'title': 'Plotting a Course', 'img': 'PHAK_Fig16-25_sectional_course', 'cite': 'PHAK 16-5 to 16-7, PHAK 16-12, PHAK 16-18',
   'goals': ['True course', 'Using the plotter', 'Magnetic variation', 'True to magnetic'],
   'why': 'Why it matters: every nav log starts with a course line. Get the variation backward and you fly the wrong way.'},
 'Choosing a Power Setting': {'code': 'AI.II.I.K4', 'title': 'Power Setting Selection', 'img': 'POH_Fig4-3_cruise_table', 'cite': 'POH 4-33 to 4-35, POH Fig 5-8, PHAK 7-5',
   'goals': ['Use the POH cruise tables', 'Power in a fixed-pitch airplane', 'Read the chart notes', 'Speed versus fuel'],
   'why': 'Why it matters: the power setting you pick sets your speed, fuel burn, and range for the whole trip.'},
 'Required Inspections': {'code': 'AI.III.B.K1b', 'title': 'Inspections and Logbooks', 'img': 'POH_8-7_inspection_periods', 'cite': '14 CFR 91.409, 91.413, 91.417',
   'goals': ['Annual and 100-hour', 'Transponder, ELT, other checks', 'ADs', 'What goes in the logbook'],
   'why': 'Why it matters: as a CFI you must confirm the airplane is legal before every lesson. The logbooks are how you prove it.'},
 'ELT Operations': {'code': 'AI.XII.D.K1', 'title': 'Emergency Locator Transmitter', 'img': 'POH_FigS1-2_elt', 'cite': 'AIM 6-2-4, 14 CFR 91.207, POH Supplement 1',
   'goals': ['How the ELT works', 'Using the C172S ELT', 'Limitations', 'Testing and inspection rules'],
   'why': 'Why it matters: the ELT is how search and rescue finds you. Your students should know how to turn it on and when they may test it.'},
}

CHECKS = {
 'How Instructors Build Insight': {'code': 'FI.I.B.K3', 'cite': 'AIH 3-7 to 3-9, AIH Fig 3-5', 'qa': [
   ('Which sense accounts for most learning?', 'Sight, about 75 percent (AIH Fig 3-5).'),
   ('Your student stares at the altimeter during their first steep turns. Which factor is at work?', 'Element of threat. Fear narrows perception (AIH 3-8).'),
   ('What is insight?', 'Grouping perceptions into meaningful wholes (AIH 3-9).')]},
 'Putting the Three Together': {'code': 'AI.II.D.K2', 'cite': 'PHAK 5-14, PHAK 5-15, PHAK 5-44', 'qa': [
   ('A ball resting on a flat table shows which static stability?', 'Neutral. It stays in its new position (PHAK 5-14).'),
   ('The airplane oscillates and each swing gets bigger. What is that?', 'Negative dynamic stability (PHAK 5-15).'),
   ('The CG moves aft. More stable or less stable?', 'Less stable (PHAK 5-44).')]},
 'C172S Propeller': {'code': 'AI.II.E.K1c', 'cite': 'POH 7-28, PHAK 7-4, PHAK 7-5', 'qa': [
   ('What engine does the C172S have, and how much power?', 'Lycoming IO-360-L2A, 180 hp at 2,700 RPM (POH 7-28).'),
   ('What instrument shows engine power in the C172S?', 'The tachometer (PHAK 7-5).'),
   ('Why is the propeller blade twisted?', 'For even lift from hub to tip, because the tip travels faster (PHAK 7-4).')]},
 'C172S Weight and Balance Numbers': {'code': 'AI.II.F.K3', 'cite': 'TCDS 3A12 p30, PHAK 10-6, POH 6-10', 'qa': [
   ('Where is the C172S datum?', 'Lower portion of the front face of the firewall (TCDS 3A12 p30).'),
   ('A 120 lb bag is 95 inches aft of the datum. What is its moment?', '120 x 95 = 11,400 in-lb.'),
   ('Basic empty weight is 1,642 lb and maximum weight is 2,550 lb. What is the useful load?', '908 lb.')]},
 'Interference and Signal Integrity': {'code': 'AI.II.H.K1', 'cite': 'AIM 1-1-3, AIM 1-1-4, AIM 1-1-2', 'qa': [
   ('What is the only positive way to identify a VOR?', 'Its Morse code identifier or recorded voice ID with the word "VOR" (AIM 1-1-3).'),
   ('With the CDI centered on a VOT, what should the OBS read?', '0 FROM or 180 TO (AIM 1-1-4).'),
   ('The CDI swings back and forth at one RPM. What do you try first?', 'Change the RPM slightly (AIM 1-1-3).'),
   ('Why must you keep listening to an NDB identifier?', 'The ADF has no warning flag for bad bearings (AIM 1-1-2).')]},
 'True Course to Magnetic Course': {'code': 'AI.II.I.K3', 'cite': 'PHAK 16-5, PHAK 16-7', 'qa': [
   ('When you measure with a plotter, are you referencing true or magnetic north?', 'True north. The result is the true course (PHAK 16-5).'),
   ('True course 090, variation 9 degrees east. Magnetic course?', '081 (PHAK 16-7).'),
   ('On a long route, where do you measure the course?', 'At a meridian near the midpoint (PHAK 16-5).')]},
 'Example: Read the Notes': {'code': 'AI.II.I.K4', 'cite': 'POH 4-33, POH Fig 5-8, PHAK 7-5', 'qa': [
   ('What should your student look at first to pick a power setting?', 'The POH cruise performance table and charts (POH 4-33).'),
   ('Above 75 percent power, how do you set the mixture?', 'Full rich (POH Fig 5-8).'),
   ('Same RPM, higher altitude: more or less power?', 'Less, because the air is less dense (PHAK 7-5).')]},
 'Logbook Documentation': {'code': 'AI.III.B.K1b', 'cite': '14 CFR 91.409, 91.413, 91.417', 'qa': [
   ('How often is an annual inspection required?', 'Within the preceding 12 calendar months (14 CFR 91.409).'),
   ('You give paid instruction in an airplane you provide. What other inspection applies?', 'The 100-hour inspection (14 CFR 91.409).'),
   ('How often must the transponder be checked?', 'Every 24 calendar months (14 CFR 91.413).'),
   ('What three things must a maintenance entry include?', 'Description of work, date, and the signature and certificate number of the person approving return to service (14 CFR 91.417).')]},
 'ELT Testing and Rules': {'code': 'AI.XII.D.K1', 'cite': 'AIM 6-2-4, 14 CFR 91.207, POH S1-8', 'qa': [
   ('When may you test an analog ELT?', 'In the first 5 minutes after the hour, no more than three sweeps (AIM 6-2-4).'),
   ('When must the ELT battery be replaced?', 'After more than 1 cumulative hour of use, or at 50 percent of its useful life (14 CFR 91.207).'),
   ('You are about to make a forced landing in the mountains. What do you do with the ELT?', 'Set the remote switch to ON (POH S1-8).')]},
}

KNOW = {
 'Definition: Perceptions': 'Sight is about 75 percent of learning. Sight and hearing together are about 88 percent (AIH Fig 3-5).',
 'Dynamic Stability': 'Static stability is the first reaction. Dynamic stability is what happens over time.',
 'Engine Controls': 'The throttle controls fuel-air flow and RPM. The C172S has no propeller control.',
 'C172S Propeller': 'Fixed pitch means the tachometer is your power gauge (PHAK 7-5).',
 'Orientation: CDI and HSI': 'Fly TO when going to the station and FROM when going away, or the needle reverses (PHAK 16-26).',
 'Tests and Regulations': 'Ground check: 4 degrees. Airborne check: 6 degrees. Dual VOR: 4 degrees. Within 30 days for IFR (14 CFR 91.171).',
 'NDB and ADF': 'The ADF has no warning flag. Keep listening to the identifier (AIM 1-1-2).',
 'Plotting the Course': 'Knots go with nautical miles. Use the NM scale on the plotter.',
 'Example: Read the Notes': 'Always read the chart notes before you choose a power setting.',
 'Required Inspections': 'Annual: every 12 calendar months. 100-hour: carrying people for hire, or paid instruction in an airplane you provide.',
 'ELT Limitations': 'Satellites stopped listening to 121.5 MHz in 2009. A 121.5 ELT depends on someone hearing it (AIM 6-2-4).',
 'C172S Engine': 'Lycoming IO-360-L2A, 180 hp at 2,700 RPM, four cylinder, horizontally opposed, fuel injected (POH 7-28).',
 'Choosing a Power Setting': 'Pick the altitude with the best winds, then pick the power. Lower power saves fuel (POH 4-33).',
 'Logbook Documentation': 'Every maintenance entry: what was done, the date, and the signature and certificate number.',
}

MEMORY = {
 'Factors That Affect Perception': 'GSTEP (from your study guide): Goals and values, Self-concept, Time and opportunity, Element of threat, Physical organism.',
 'Static Stability': 'Ball in a bowl rolls back: positive. Ball on a table stays put: neutral. Ball on a hill rolls away: negative.',
 'C172S Weight and Balance Numbers': 'Moment = Weight x Arm. CG = Total Moment / Total Weight.',
 'True Course to Magnetic Course': 'East is least (subtract). West is best (add) (PHAK 16-7).',
 'ELT Testing and Rules': '5, 3, 12, 1, 50: first 5 minutes, 3 sweeps, 12 month inspection, 1 hour of use, 50 percent battery life.',
 'Other Required Checks': 'Transponder 24, ELT 12, altimeter and static 24 (IFR), VOR 30 days (IFR).',
}

SCENARIO = {
 'Power in a Fixed-Pitch Airplane': 'Your student sets 2,400 RPM at 8,000 feet and expects the same speed as 2,400 RPM at sea level. Ask why the airplane is slower and where to find the real numbers.',
 'Using the C172S ELT': 'After a forced landing in a field, your student is about to call on the radio with the ELT running. Walk them through the POH steps.',
 'Course Determination: Tracking': 'Your student keeps chasing the needle and flies S-turns down the radial. Show them how to bracket and hold a wind correction.',
}

IMG2 = {
 'C172S Engine': 'POH_7-28_engine',
 'Definition: True Course': 'PHAK_Fig16-18_plotter',
 'ELT Operations': 'POH_7-71_elt',
 'Orientation: CDI and HSI': 'PHAK_Fig16-29_vor_indicator',
}

PLAIN = {
 'Definition: Perceptions': 'Everything a student learns comes in through the senses. Show it, say it, and let them touch it, and it sticks faster.',
 'Definition: Insight': 'Insight is the moment the pieces click. The student stops seeing throttle, RPM, and pitch as separate facts and sees how they work together.',
 'Definition: Stability': 'A stable airplane wants to go back to what it was doing after a bump. The designer builds this in.',
 'Definitions: Maneuverability and Controllability': 'Maneuverability: how easily the airplane can be maneuvered and handle the stress. Controllability: how well it does what the pilot asks.',
 'Definitions: Propeller and Fixed Pitch': 'The propeller is a spinning wing that pulls the airplane forward. On the C172S the blade angle is set at the factory and never changes.',
 'Definitions: Datum and Arm': 'The datum is the zero point on a tape measure. The arm is how far each seat, tank, or bag sits from that zero point.',
 'Definitions: Moment and CG': 'Moment is how hard a weight tries to tip the airplane. The CG is the balance point of everything combined.',
 'Definitions: Basic Empty Weight and Useful Load': 'Basic empty weight is the airplane with unusable fuel and full oil, nothing else. Useful load is what is left for people, bags, and fuel.',
 'Definitions: CG Limits and Maximum Weight': 'CG limits are the front and back edges of the safe balance zone. Maximum weight is the heaviest the airplane may be.',
 'Definition: True Course': 'The line you draw on the chart, measured from true north with the plotter.',
 'Definition: Variation': 'True north and magnetic north are in different places. Variation is the angle between them, and the chart shows how much.',
}
