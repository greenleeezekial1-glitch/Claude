SECTIONS = {
 'Definitions: Chord Line and Camber': {'code': 'Step 1 of 6  |  AI.II.D.K1', 'title': 'Airfoil Design and Lift', 'img': 'PHAK_Fig4-5_airfoil_section', 'cite': 'PHAK 4-6 to 4-8, PHAK 5-4',
   'goals': ['Parts of an airfoil', 'Bernoulli and Newton', 'Relative wind and AOA', 'Critical AOA and the stall'],
   'why': 'Start here: everything else in this lesson comes from how the wing makes lift.'},
 'The Four Forces': {'code': 'Step 2 of 6  |  AI.II.D.K4', 'title': 'Forces Acting on an Airplane', 'img': 'PHAK_Fig5-1_four_forces', 'cite': 'PHAK 5-1 to 5-8',
   'goals': ['Thrust, drag, lift, weight', 'Forces in balance and in a climb', 'Parasite drag: form, interference, skin friction', 'Induced drag and L/D max'],
   'why': 'Coming from step 1: the wing makes lift, but lift never comes alone. Here are the forces that come with it.'},
 'How Wingtip Vortices Form': {'code': 'Step 3 of 6  |  AI.II.D.K6', 'title': 'Wingtip Vortices', 'img': 'PHAK_Fig5-12_wingtip_vortices', 'cite': 'PHAK 5-7 to 5-10, AIM 7-4',
   'goals': ['How vortices form', 'How they move and sink', 'Wake turbulence precautions'],
   'why': 'Coming from step 2: induced drag comes from air spilling around the wingtip. That spill is a wingtip vortex.'},
 'Definition: Stability': {'code': 'Step 4 of 6  |  AI.II.D.K2', 'title': 'Stability, Maneuverability, Controllability', 'img': 'PHAK_Fig5-21_static_stability', 'cite': 'PHAK 5-14 to 5-19',
   'goals': ['Static and dynamic stability', 'Pitch, roll, and yaw stability', 'Maneuverability and controllability', 'How CG changes them'],
   'why': 'Coming from step 3: we know what forces act. Now, why does the airplane stay in balance when a gust hits it?'},
 'Turning Tendencies: Torque Reaction': {'code': 'Step 5 of 6  |  AI.II.D.K3', 'title': 'Turning Tendencies', 'img': 'PHAK_Fig5-51_p_factor', 'cite': 'PHAK 5-30 to 5-32',
   'goals': ['Torque reaction', 'Corkscrewing slipstream', 'Gyroscopic precession', 'P-factor'],
   'why': 'Coming from step 4: the airplane is built to be stable, but the engine and propeller keep trying to pull it left.'},
 'Definition: Load Factor': {'code': 'Step 6 of 6  |  AI.II.D.K5', 'title': 'Load Factors', 'img': 'PHAK_Fig5-53_bank_load_factor', 'cite': 'PHAK 5-33 to 5-36, POH 2-4, POH 2-11',
   'goals': ['Load factor and design limits', 'Load factor in turns', 'Load factor and stall speed', 'Maneuvering speed'],
   'why': 'Coming from step 5: once we can control the airplane, how hard can we maneuver it before something breaks or stalls?'},
 'Risk: Stalls From Load Factor': {'code': 'AI.II.D.R1, S1', 'title': 'Risk Management and Teaching It', 'img': 'PHAK_Fig5-54_stall_speed', 'cite': 'PHAK 5-20, PHAK 5-35, AIM 7-4-6',
   'goals': ['Stalls from load factor', 'Wake, turning tendencies, spirals', 'Teaching three elements in flight'],
   'why': 'Putting it together: every principle comes with a risk. Here is how to manage each one and how to teach it.'},
}

CHECKS = {
 'Definition: Critical Angle of Attack': {'code': 'AI.II.D.K1', 'cite': 'PHAK 4-6, PHAK 4-8, PHAK 5-4, PHAK G-9', 'qa': [
   ('State Bernoulli\'s Principle.', 'As the velocity of a moving fluid increases, the pressure within the fluid decreases (PHAK 4-6).'),
   ('If you double your airspeed at the same AOA, what happens to lift?', 'It becomes four times as much (PHAK 5-4).'),
   ('Can a wing stall at high airspeed?', 'Yes. It stalls at the critical AOA regardless of airspeed, attitude, or weight (PHAK G-9).')]},
 'Induced Drag and the Drag Curve': {'code': 'AI.II.D.K4', 'cite': 'PHAK 5-2, PHAK 5-6, PHAK 5-8', 'qa': [
   ('In straight and level flight, are all four forces equal?', 'No. Lift equals weight and thrust equals drag, but lift and weight are larger (PHAK 5-2).'),
   ('Name the three types of parasite drag.', 'Form, interference, and skin friction (PHAK 5-6).'),
   ('You slow down toward a stall. Which drag rises sharply?', 'Induced drag (PHAK 5-8).')]},
 'Wake Turbulence Precautions': {'code': 'AI.II.D.K6', 'cite': 'PHAK 5-9, AIM 7-4-4, AIM 7-4-6', 'qa': [
   ('When are wingtip vortices strongest?', 'When the generating aircraft is heavy, clean, and slow (PHAK 5-9).'),
   ('Landing behind a larger aircraft on the same runway: where do you touch down?', 'Beyond its touchdown point, staying at or above its approach path (AIM 7-4-6).'),
   ('A larger aircraft just did a touch-and-go. How long do you wait?', 'At least 2 minutes (AIM 7-4-6).')]},
 'Definitions: Maneuverability and Controllability': {'code': 'AI.II.D.K2', 'cite': 'PHAK 5-14 to 5-19', 'qa': [
   ('The nose returns toward level after a push, then the swings die out. Static and dynamic stability?', 'Positive static and positive dynamic (PHAK 5-14, PHAK 5-17).'),
   ('Which axis is pitch stability about?', 'The lateral axis (PHAK 5-15).'),
   ('What makes a C172S laterally stable?', 'Dihedral and keel effect from the high wing (PHAK 5-18).')]},
 'Turning Tendencies: P-Factor': {'code': 'AI.II.D.K3', 'cite': 'PHAK 5-31, PHAK 5-32', 'qa': [
   ('Name the four turning tendencies.', 'Torque reaction, corkscrewing slipstream, gyroscopic precession, P-factor (PHAK 5-31).'),
   ('Gyroscopic precession: where does the resulting force act?', '90 degrees ahead in the direction of rotation (PHAK 5-31).'),
   ('In a full power climb, which way does the nose yaw and what fixes it?', 'Left. Right rudder (PHAK 5-32).')]},
 'Maneuvering Speed (VA)': {'code': 'AI.II.D.K5', 'cite': 'PHAK 5-34, PHAK 5-35, POH 2-4, POH Fig 5-3', 'qa': [
   ('Load factor in a level 60 degree bank?', '2 Gs (PHAK 5-34).'),
   ('C172S flaps up stall speed: wings level vs. 60 degrees of bank?', '48 KIAS vs. 68 KIAS (POH Fig 5-3).'),
   ('C172S VA at 2,550 lb, and does it protect against two full inputs at once?', '105 KIAS. No (POH 2-4, PHAK 5-35).')]},
}

NEXT = {
 'Definition: Critical Angle of Attack': 'Next up, the four forces. The wing makes lift, but lift never comes alone. What else is acting on the airplane?',
 'Induced Drag and the Drag Curve': 'Next up, wingtip vortices. Induced drag comes from air spilling around the wingtip. Where does that air go?',
 'Wake Turbulence Precautions': 'Next up, stability. We know the forces. Why does the airplane stay balanced when a gust hits it?',
 'Definitions: Maneuverability and Controllability': 'Next up, turning tendencies. The airplane is built stable, so what keeps pulling the nose to the left?',
 'Turning Tendencies: P-Factor': 'Next up, load factors. Now that we can control it, how hard can we maneuver before it stalls or breaks?',
 'Maneuvering Speed (VA)': 'Next up, risk management. Each principle comes with a risk. Let us manage them and plan how to teach this.',
 'Lesson Roadmap: Each Topic Builds the Next': 'Start with step 1: how the wing makes lift.',
}

KNOW = {
 'Definitions: Relative Wind and Angle of Attack': 'Lift always acts perpendicular to the relative wind, and the relative wind comes from the flight path, not the nose.',
 'Lift, Speed, and AOA': 'Lift is proportional to the square of the velocity. Twice the speed, four times the lift (PHAK 5-4).',
 'Forces in Balance and in a Climb': 'Opposing forces cancel. Lift and weight are bigger than thrust and drag (PHAK 5-2).',
 'Induced Drag and the Drag Curve': 'Induced drag: inversely with the square of airspeed. Parasite drag: as the square of airspeed (PHAK 5-8).',
 'How Vortices Move': 'A light quartering crosswind is the worst case. It can hold a vortex over the runway.',
 'Longitudinal Stability (Pitch)': 'CG ahead of the center of lift plus a tail-down force: the airplane tries to return to a safe attitude (PHAK 5-17).',
 'Load Factor in Turns': '60 degrees of bank = 2 Gs. Past 45 to 50 degrees it rises very fast (PHAK 5-34).',
 'Maneuvering Speed (VA)': 'VA is not protection against multiple full inputs or full inputs in more than one axis at once (PHAK 5-35).',
 'Turning Tendencies: Torque Reaction': 'Four parts of "torque": torque reaction, slipstream, gyroscopic precession, P-factor.',
}

MEMORY = {
 'Definition: Bernoulli\'s Principle': 'Speed up, pressure down.',
 'Definition: Stability': 'Bowl, table, hill: positive, neutral, negative.',
 'Wake Turbulence Precautions': 'Land beyond, lift off before, stay above.',
 'Directional Stability (Yaw)': 'Weather vane or arrow: more area behind the pivot point.',
}

SCENARIO = {
 'Risk: Stalls From Load Factor': 'Your student overshoots the turn from base to final, steepens to 45 degrees, and pulls back. Ask what just happened to the stall speed and what they should do instead.',
 'Wake Turbulence Precautions': 'You are cleared for takeoff right after a regional jet departs. Ask your student where they plan to rotate and which way to turn after takeoff.',
}

IMG2 = {}
PLAIN = {}
