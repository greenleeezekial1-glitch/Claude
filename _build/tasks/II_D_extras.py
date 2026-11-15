SECTIONS = {
 'Definitions: Chord Line and Camber': {'code': 'Step 1 of 6  |  AI.II.D.K1', 'title': 'How a Wing Makes Lift', 'img': 'PHAK_Fig4-5_airfoil_section', 'cite': 'PHAK 4-6 to 4-8, PHAK 5-4',
   'goals': ['Parts and design of an airfoil', 'Bernoulli and Newton', 'Relative wind and AOA', 'Critical AOA and the stall'],
   'why': 'Start here: everything else in this lesson comes from how the wing makes lift.'},
 'The Four Forces': {'code': 'Step 2 of 6  |  AI.II.D.K4', 'title': 'Forces and Drag', 'img': 'PHAK_Fig5-11_downwash_alt_ground', 'cite': 'PHAK 5-1 to 5-12, PHAK 6-3',
   'goals': ['The four forces', 'Parasite drag', 'Induced drag: vortices, downwash, lift tilts back', 'Adverse yaw and ground effect'],
   'why': 'Coming from step 1: the wing makes lift, but lift never comes free. Here are the forces and the drag that come with it.'},
 'From Wingtip Vortex to Wake Turbulence': {'code': 'Step 3 of 6  |  AI.II.D.K6', 'title': 'Wake Turbulence', 'img': 'AC90-23G_Fig1_rollup', 'cite': 'AC 90-23G, AIM 7-4, PHAK 5-9',
   'goals': ['Where the vortices go', 'The induced roll hazard', 'How vortices sink and drift', 'Avoidance procedures'],
   'why': 'Coming from step 2: the vortices that cause induced drag do not disappear. They trail behind every airplane as wake turbulence.'},
 'Definition: Stability': {'code': 'Step 4 of 6  |  AI.II.D.K2', 'title': 'Stability, Maneuverability, Controllability', 'img': 'PHAK_Fig5-21_static_stability', 'cite': 'PHAK 5-14 to 5-19',
   'goals': ['Static stability: the bowl method', 'Dynamic stability', 'Pitch, roll, and yaw stability', 'Maneuverability, controllability, CG'],
   'why': 'Coming from step 3: we know what forces act on the airplane. Now, why does it stay balanced when a gust or a wake hits it?'},
 'Turning Tendencies: Torque Reaction': {'code': 'Step 5 of 6  |  AI.II.D.K3', 'title': 'Turning Tendencies', 'img': 'PHAK_Fig5-51_p_factor', 'cite': 'PHAK 5-30 to 5-32',
   'goals': ['Torque reaction', 'Corkscrewing slipstream', 'Gyroscopic precession', 'P-factor'],
   'why': 'Coming from step 4: the airplane is built to be stable, but the engine and propeller keep trying to pull it left.'},
 'Definition: Load Factor': {'code': 'Step 6 of 6  |  AI.II.D.K5', 'title': 'Load Factors', 'img': 'PHAK_Fig5-53_bank_load_factor', 'cite': 'PHAK 5-33 to 5-36, POH 2-4, POH 2-11',
   'goals': ['Load factor and design limits', 'Load factor in turns', 'Load factor and stall speed', 'Maneuvering speed'],
   'why': 'Coming from step 5: once we can control the airplane, how hard can we maneuver it before it stalls or breaks?'},
 'Risk: Stalls From Load Factor': {'code': 'AI.II.D.R1, S1', 'title': 'Risk Management and Teaching It', 'img': 'PHAK_Fig5-54_stall_speed', 'cite': 'PHAK 5-20, PHAK 5-35, AIM 7-4-6',
   'goals': ['Stalls from load factor', 'Wake, turning tendencies, spirals', 'Teaching three elements in flight'],
   'why': 'Putting it together: every principle comes with a risk. Here is how to manage each one and how to teach it.'},
}

CHECKS = {
 'Definition: Critical Angle of Attack': {'code': 'AI.II.D.K1', 'cite': 'PHAK 4-6, PHAK 5-4, PHAK G-9', 'qa': [
   ('State Bernoulli\'s Principle.', 'As the velocity of a moving fluid increases, the pressure within the fluid decreases (PHAK 4-6).'),
   ('If you double your airspeed at the same AOA, what happens to lift?', 'It becomes four times as much (PHAK 5-4).'),
   ('Can a wing stall at high airspeed?', 'Yes. It stalls at the critical AOA regardless of airspeed, attitude, or weight (PHAK G-9).')]},
 'Induced Drag Near the Ground: Ground Effect': {'code': 'AI.II.D.K4', 'cite': 'PHAK 5-6 to 5-12, PHAK G-1', 'qa': [
   ('Name the three types of parasite drag.', 'Form, interference, and skin friction (PHAK 5-6).'),
   ('Explain induced drag in four steps.', 'Air spills around the tip into a vortex, the vortex makes downwash, downwash tilts the relative wind down, and lift tilts back. The rearward part is induced drag (PHAK 5-7).'),
   ('You raise the AOA. What happens to induced drag and why?', 'It increases: bigger pressure difference, stronger vortices, more downwash (PHAK 5-9).'),
   ('Why does the airplane float in the flare?', 'Ground effect reduces downwash and vortices, so induced drag drops (PHAK 5-11).')]},
 'Wake Turbulence Precautions': {'code': 'AI.II.D.K6', 'cite': 'AC 90-23G, AIM 7-4-6', 'qa': [
   ('When are wake vortices strongest?', 'When the generating aircraft is heavy, clean, and slow (AC 90-23G par 5).'),
   ('What is the main hazard to a C172S?', 'An induced roll that can exceed its roll control (AC 90-23G par 6).'),
   ('Which wind is the worst case?', 'A light quartering tailwind (AC 90-23G par 7e).'),
   ('Landing behind a larger aircraft on the same runway: where do you touch down?', 'Beyond its touchdown point, staying at or above its path (AIM 7-4-6).')]},
 'Definitions: Maneuverability and Controllability': {'code': 'AI.II.D.K2', 'cite': 'PHAK 5-14 to 5-19', 'qa': [
   ('Bowl method: ball on a flat floor sidesteps and stays. Which static stability?', 'Neutral (PHAK 5-14).'),
   ('Nose returns after a push and the swings die out. Static and dynamic?', 'Positive static and positive dynamic (PHAK 5-14, PHAK 5-17).'),
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
 'Definition: Critical Angle of Attack': 'Next up, forces and drag. Lift never comes free. What else acts on the airplane, and what does making lift cost us?',
 'Definition: Parasite Drag': 'Next up, induced drag. Parasite drag has nothing to do with lift. Induced drag is the price of making lift.',
 'Induced Drag in a Turn: Adverse Yaw': 'Next up, what makes induced drag smaller: getting close to the ground.',
 'Induced Drag Near the Ground: Ground Effect': 'Next up, wake turbulence. The vortices that cause induced drag trail behind every airplane. Where do they go?',
 'Wake Turbulence Precautions': 'Next up, stability. We know the forces. Why does the airplane stay balanced when a gust or a wake hits it?',
 'Definitions: Maneuverability and Controllability': 'Next up, turning tendencies. The airplane is built stable, so what keeps pulling the nose left?',
 'Turning Tendencies: P-Factor': 'Next up, load factors. How hard can we maneuver before it stalls or breaks?',
 'Maneuvering Speed (VA)': 'Next up, risk management. Each principle comes with a risk. Let us manage them and plan how to teach this.',
}

KNOW = {
 'Definitions: Relative Wind and Angle of Attack': 'Lift always acts perpendicular to the relative wind, and the relative wind comes from the flight path, not the nose.',
 'Lift, Speed, and AOA': 'Lift is proportional to the square of the velocity. Twice the speed, four times the lift (PHAK 5-4).',
 'Forces in Balance and in a Climb': 'Opposing forces cancel. Lift and weight are bigger than thrust and drag (PHAK 5-2).',
 'Definition: Induced Drag': 'Byproduct of lift. Always there when lift is made. Increases with AOA.',
 'Induced Drag Increases With AOA': 'Induced drag varies inversely with the square of airspeed (PHAK 5-8).',
 'Total Drag and L/D Max': 'Parasite drag increases as the square of airspeed. L/D max is the lowest total drag (PHAK 5-5, PHAK 5-8).',
 'The Hazard: Induced Roll': 'The roll from a large airplane\'s wake can be more than a C172S can counter with full aileron.',
 'How Vortices Move': 'Light quartering tailwind: maximum caution (AC 90-23G par 7e).',
 'Longitudinal Stability (Pitch)': 'CG ahead of the center of lift plus a tail-down force: the airplane tries to return to a safe attitude (PHAK 5-17).',
 'Load Factor in Turns': '60 degrees of bank = 2 Gs. Past 45 to 50 degrees it rises very fast (PHAK 5-34).',
 'Maneuvering Speed (VA)': 'VA is not protection against multiple full inputs or full inputs in more than one axis at once (PHAK 5-35).',
 'Turning Tendencies: Torque Reaction': 'Four parts of "torque": torque reaction, slipstream, gyroscopic precession, P-factor.',
 'Induced Drag Near the Ground: Ground Effect': 'Do not force the airplane off the ground below the recommended takeoff speed (PHAK 5-12).',
}

MEMORY = {
 'Definition: Bernoulli\'s Principle': 'Speed up, pressure down.',
 'Static Stability: The Bowl Method': 'Bowl rolls back. Floor sidesteps and stays. Hill rolls away.',
 'Wake Turbulence Precautions': 'Land beyond, lift off before, stay above.',
 'From Wingtip Vortex to Wake Turbulence': 'Heavy, clean, slow.',
 'Directional Stability (Yaw)': 'Weather vane or arrow: more area behind the pivot point.',
 'Definition: Parasite Drag': 'Form: Jeep vs. Ferrari. Interference: wing meets strut. Skin friction: rivets and paint chips.',
}

SCENARIO = {
 'Risk: Stalls From Load Factor': 'Your student overshoots the turn from base to final, steepens to 45 degrees, and pulls back. Ask what just happened to the stall speed and what they should do instead.',
 'Wake Turbulence Precautions': 'You are cleared for takeoff right after a regional jet departs. Ask your student where they plan to rotate and which way to turn after takeoff.',
 'Induced Drag Near the Ground: Ground Effect': 'Hot day, heavy airplane. Your student pulls the C172S off at 45 knots. It flies in ground effect, then will not climb. Ask why.',
}

IMG2 = {}
PLAIN = {}
