# II.D version 2: checkride focused, drag chain flows into wake turbulence.
# Starts from II_D_v1.py and replaces the drag and wake sections.
import copy, os, importlib.util
_sp = importlib.util.spec_from_file_location('v1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'II_D_v1.py'))
_v1 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_v1)
TASK = copy.deepcopy(_v1.TASK)
K1, K2, K4, K6 = 'AI.II.D.K1', 'AI.II.D.K2', 'AI.II.D.K4', 'AI.II.D.K6'
S = {s['title']: s for s in TASK['slides']}

TASK['references'].insert(2, 'AC 90-23G, Aircraft Wake Turbulence (February 10, 2014): paragraphs 3 to 8, Figures 1, 2, and 7. This is the current edition.')
TASK['references'][1] = TASK['references'][1].replace('Chapter 5 (5-1 to 5-20,', 'Chapter 5 (5-1 to 5-20, 5-11, 5-12 ground effect,').replace('Glossary', 'Chapter 6 (6-3, adverse yaw), and Glossary')

# ---- K1: fold airfoil designs into the chord/camber slide
S['Definitions: Chord Line and Camber']['img2'] = 'PHAK_Fig4-6_airfoil_designs'
S['Definitions: Chord Line and Camber']['lp']['teach'].append('Airfoil design characteristics: the shape is chosen for the job. Figure 4-6 shows how airfoils changed from thin early designs to the Clark Y and laminar flow shapes used on light airplanes, to thin supersonic shapes (PHAK 4-7, PHAK Fig 4-6).')

# ---- new drag chain
drag = [
 {'title': 'Drag: Two Kinds', 'img': 'PHAK_Fig5-6_drag_speed', 'cite': 'PHAK 5-6, PHAK 5-8, PHAK Fig 5-6', 'code': K4,
  'bullets': ['Parasite: not from making lift', 'Induced: comes from making lift', 'Total drag = parasite + induced', 'We take them one at a time'],
  'notes': 'Every drag on the airplane falls into one of two buckets. Parasite drag is everything that slows us down that has nothing to do with lift. Induced drag is the price we pay for making lift. We start with parasite because it is the easy one.',
  'lp': {'teach': ['Drag is the force that resists movement of an aircraft through the air. There are two basic types: parasite drag and induced drag. Parasite drag in no way functions to aid flight; induced drag is a result of an airfoil developing lift (PHAK 5-6).',
     'Teach parasite drag first because students can see and touch it. Then induced drag, which leads straight into wingtip vortices and wake turbulence.']}},
 copy.deepcopy(S['Definition: Parasite Drag']),
 {'kind': 'definition', 'title': 'Definition: Induced Drag', 'img': 'PHAK_Fig5-12_wingtip_vortices', 'cite': 'PHAK 5-7, PHAK Fig 5-12', 'code': K4, 'defsize': 17,
  'defs': [('Induced drag', 'Induced drag is inherent whenever an airfoil is producing lift and, in fact, this type of drag is inseparable from the production of lift. Consequently, it is always present if lift is produced.')],
  'plain': 'Induced drag is the price of lift. No lift, no induced drag. Make more lift with more AOA, and you pay more.',
  'notes': 'Key words for the checkride: byproduct of lift, always there when lift is made, increases with AOA. Next slide shows why.',
  'lp': {'teach': ['Read the definition (PHAK 5-7). The PHAK calls it the penalty for producing lift: no system that does work is 100 percent efficient (PHAK 5-7).',
     'Your whiteboard says induced drag is caused by the same factors that produce lift. That matches the PHAK idea that it is inseparable from lift.']}},
 {'title': 'How Induced Drag Happens', 'img': 'PHAK_Fig5-11_downwash_alt_ground', 'cite': 'PHAK 5-7, PHAK 5-8, PHAK Fig 5-11', 'code': f'{K4}, {K6}',
  'bullets': ['1. Air spills around the tip', '2. Vortex pushes air down: downwash', '3. Downwash tilts relative wind down', '4. Lift tilts back: rearward part is drag'],
  'notes': 'Walk it in four steps with your hand. High pressure under the wing curls around the tip into a vortex. The vortex pushes the air coming off the trailing edge down. That downwash bends the relative wind down. Lift is always perpendicular to the relative wind, so the lift arrow tilts back. The part pointing backward is induced drag.',
  'lp': {'teach': ['Step 1: When a wing makes lift, pressure below it is higher than above it. Air flows from below the tip up to the low pressure on top, setting up a vortex at each tip (PHAK 5-7).',
     'Step 2: The vortices push air upward beyond the tip and downward behind the trailing edge. This induced downwash is the source of induced drag (PHAK 5-7).',
     'Step 3: Downwash points the relative wind downward. The more downwash, the more the relative wind points down (PHAK 5-7).',
     'Step 4: Lift is always perpendicular to the relative wind. With more downwash, the lift vector points back more. That rearward part of lift is induced drag (PHAK 5-7, PHAK 5-8).',
     'Figure 5-11 shows it: big vortices, steep downwash, and a lift arrow tilted back at altitude; smaller vortices and less tilt near the ground.'],
   'analogy': 'Lift wants to point straight up, but the wing is sitting in air it already pushed down. It is like trying to stand straight up on a slope: you end up leaning, and part of your push goes the wrong way.'}},
 {'title': 'Induced Drag Increases With AOA', 'img': 'PHAK_Fig5-10_vortex_size', 'cite': 'PHAK 5-8, PHAK 5-9, PHAK Fig 5-10', 'code': K4,
  'bullets': ['More AOA: bigger pressure difference', 'Stronger vortices, more downwash', 'Slow flight: high AOA, high induced drag', 'Inversely with airspeed squared'],
  'notes': 'Same chain, turned up. Raise the AOA and the pressure difference grows, so the vortices get stronger, the downwash gets steeper, and the lift tilts back more. Slow flight means high AOA, so induced drag is highest when slow.',
  'lp': {'teach': ['As AOA increases, there is a greater pressure difference between the top and bottom of the airfoil and a greater lateral flow of air, which causes more violent vortices, more turbulence, and more induced drag (PHAK 5-9).',
     'The lower the airspeed, the greater the AOA needed to make lift equal to weight, so the greater the induced drag. Induced drag varies inversely with the square of the airspeed (PHAK 5-8).',
     'If a symmetrical airfoil were at zero AOA, there would be no pressure differential, no downwash, and no induced drag (PHAK 5-8).']}},
 {'title': 'Total Drag and L/D Max', 'img': 'PHAK_Fig5-6_drag_speed', 'cite': 'PHAK 5-5, PHAK 5-8, PHAK Fig 5-6', 'code': K4,
  'bullets': ['Induced: high when slow', 'Parasite: high when fast', 'Lowest total drag: L/D max', 'Near stall or near VNE: drag climbs'],
  'notes': 'Put the two together. Induced drag falls as speed goes up, parasite drag rises. The bottom of the total drag curve is L/D max, the least drag for the lift we need.',
  'lp': {'teach': ['Parasite drag increases as the square of the airspeed; induced drag varies inversely with the square of the airspeed (PHAK 5-8).',
     'Near the stall, total drag climbs because of induced drag. Near VNE, it climbs because of parasite drag. At L/D max total drag is at its minimum (PHAK 5-5, PHAK 5-8).']}},
 {'title': 'Induced Drag in a Turn: Adverse Yaw', 'img': 'PHAK_Fig6-5_adverse_yaw', 'cite': 'PHAK G-1, PHAK 6-3, PHAK Fig 6-5', 'code': f'{K4}, {K2}',
  'bullets': ['Down aileron: more lift on that wing', 'More lift means more induced drag', 'Nose yaws away from the turn', 'Fix: rudder with aileron'],
  'notes': 'Here is induced drag you can feel. Roll left and the right wing makes more lift, so it also makes more induced drag. The nose swings right, opposite the turn. Coordinate with rudder.',
  'lp': {'teach': ['Adverse yaw: a condition of flight in which the nose of an airplane tends to yaw toward the outside of the turn. This is caused by the higher induced drag on the outside wing, which is also producing more lift (PHAK G-1).',
     'The down aileron makes more lift and more drag, so the airplane yaws toward that wing, opposite the bank. It is more pronounced at low airspeeds (PHAK 6-3).',
     'Your whiteboard definition matches the PHAK glossary word for word.']}},
 {'title': 'Induced Drag Near the Ground: Ground Effect', 'img': 'PHAK_Fig5-16_ground_effect_airflow', 'img2': 'PHAK_Fig5-17_ground_effect_drag_lift', 'cite': 'PHAK 5-11, PHAK 5-12, PHAK Fig 5-16', 'code': K4,
  'bullets': ['Ground blocks vortices and downwash', 'Less induced drag: the float', 'Felt within about one wingspan', 'Leaving it: induced drag comes back'],
  'notes': 'The ground gets in the way of the vortices and downwash, so the lift arrow tilts back less. Less induced drag. That is the float on landing, and the trap on takeoff if you lift off too slow.',
  'lp': {'teach': ['Near the surface the ground restricts the vertical airflow, reducing upwash, downwash, and wingtip vortices, so induced drag drops (PHAK 5-11).',
     'At a height equal to the wingspan, induced drag is only 1.4 percent less. At one-fourth the span it is 23.5 percent less, and at one-tenth the span 47.6 percent less (PHAK 5-11).',
     'Landing: less drag means any excess speed at the flare causes a float (PHAK 5-12).',
     'Takeoff: the airplane may lift off below the recommended speed, then settle back or climb poorly when it leaves ground effect and induced drag returns. Do not force the airplane off with a deficiency of speed (PHAK 5-12).']}},
]

wake = [
 {'title': 'From Wingtip Vortex to Wake Turbulence', 'img': 'AC90-23G_Fig1_rollup', 'cite': 'AC 90-23G par 3 to 5, PHAK 5-9', 'code': K6,
  'bullets': ['Same vortices, left behind', 'Rotation to touchdown', 'Strongest: heavy, clean, slow', 'Weight and speed matter most'],
  'notes': 'The vortices that make induced drag do not stop at the wingtip. They roll up into two spinning tubes that trail behind every airplane. Behind a big airplane, that is wake turbulence.',
  'lp': {'teach': ['Every aircraft in flight generates wake vortices: a pair of counter-rotating vortices trailing from the wing tips (AC 90-23G par 3). They form from the same pressure differential that makes lift (AC 90-23G par 4).',
     'Vortex strength is governed by weight, speed, and wing shape and span. It increases with weight and with lower speed. The greatest strength is when the aircraft is heavy, clean, and slow; a "dirty" configuration hastens wake decay (AC 90-23G par 5).',
     'Vortices exist from rotation to touchdown because they are a by-product of wing lift (AC 90-23G par 7a).']}},
 {'title': 'The Hazard: Induced Roll', 'img': 'AC90-23G_Fig2_induced_roll', 'cite': 'AC 90-23G par 6, AC 90-23G Fig 2', 'code': K6,
  'bullets': ['Main hazard: rolling moment', 'Can exceed your roll control', 'Short wingspan: hardest to counter', 'A C172S behind an airliner'],
  'notes': 'If your wings fit inside the vortex, it can roll you faster than your ailerons can fight it. A C172S has a short wingspan compared to an airliner.',
  'lp': {'teach': ['The most likely hazard is an induced rolling moment that can exceed the roll control capability of the encountering aircraft (AC 90-23G par 6a).',
     'Counter control works best when the encountering aircraft\'s wingspan and ailerons extend beyond the vortex flow field. Aircraft with short wingspans relative to the generating aircraft have a harder time (AC 90-23G par 6b).']}},
 {'title': 'How Vortices Move', 'img': 'PHAK_Fig5-15_vortex_near_ground', 'img2': 'AC90-23G_Fig7_crosswind', 'cite': 'AC 90-23G par 7, PHAK 5-9, PHAK Fig 5-15', 'code': K6,
  'bullets': ['Sink several hundred fpm', 'Near ground: spread out 2 to 3 knots', 'Light crosswind: one stays on runway', 'Light quartering tailwind: worst case'],
  'notes': 'Vortices sink, then spread out near the ground. A light crosswind can stop the upwind one right over the runway. A light quartering tailwind can push them back up the final approach and into the touchdown zone.',
  'lp': {'teach': ['Vortices sink several hundred feet per minute, slowing and weakening with time and distance (AC 90-23G par 7c).',
     'Within 100 to 200 feet of the ground they move outward at 2 or 3 knots (AC 90-23G par 7d).',
     'A light crosswind of 1 to 5 knots can hold the upwind vortex in the touchdown zone. A light quartering tailwind requires maximum caution because it can move vortices into the final approach and touchdown zone (AC 90-23G par 7e).',
     'Vortices drift with the wind; a 10 knot wind moves them about 1,000 feet a minute (PHAK 5-9).']}},
 copy.deepcopy(S['Wake Turbulence Precautions']),
]
wake[-1]['cite'] = 'AIM 7-4-6, AC 90-23G par 8, PHAK 5-9'
wake[-1]['lp']['teach'].append('AC 90-23G par 8 gives the same procedures in more detail. If you accept a clearance to visually follow a preceding aircraft, you accept responsibility for wake turbulence avoidance (AC 90-23G par 8a).')

# ---- stability: bowl method
st = S['Definition: Stability']
static = {'title': 'Static Stability: The Bowl Method', 'img': 'PHAK_Fig5-21_static_stability', 'cite': 'PHAK 5-14, PHAK Fig 5-21', 'code': K2,
  'bullets': ['Bowl: ball rolls back (positive)', 'Flat floor: sidesteps, stays (neutral)', 'Hill: rolls away (negative)', 'Only the first reaction'],
  'notes': 'Push a ball in a bowl and it rolls back to the bottom: positive. Push it on a flat floor and it just sidesteps to a new spot and stays: neutral. Put it on top of an upside down bowl and it rolls away: negative. Static stability is only the first thing it does.',
  'lp': {'teach': ['Static stability is the initial tendency, or direction of movement, back to equilibrium (PHAK 5-14).',
     'Positive static stability: the initial tendency to return to the original state of equilibrium after being disturbed. Neutral: the initial tendency to remain in a new condition. Negative: the initial tendency to continue away from the original state (PHAK 5-14).',
     'Bowl method (from the applicant\'s whiteboard): draw a bowl, a flat floor, and an upside down bowl. On the flat floor the ball just sidesteps to a new spot and stays there, which is neutral.']}}
st['lp']['teach'] = st['lp']['teach'][:1]

order = []
for s in TASK['slides']:
    t = s['title']
    if t in ('Airfoil Design Characteristics', 'Definition: Parasite Drag', 'Induced Drag and the Drag Curve', 'How Wingtip Vortices Form', 'How Vortices Move', 'Wake Turbulence Precautions'):
        if t == 'Definition: Parasite Drag': order += drag
        if t == 'How Wingtip Vortices Form': order += wake
        continue
    order.append(s)
    if t == 'Definition: Stability': order.append(static)
TASK['slides'] = order

# roadmap update
rm = [s for s in order if s['title'].startswith('Lesson Roadmap')][0]
rm['table'] = [['Step', 'Topic', 'Leads to'], ['1', 'Lift (K1)', 'What forces come with lift?'], ['2', 'Forces and drag (K4)', 'Parasite, then induced drag'], ['3', 'Wake turbulence (K6)', 'Induced drag leaves vortices'], ['4', 'Stability (K2)', 'Why it stays balanced'], ['5', 'Turning tendencies (K3)', 'What pulls it off course'], ['6', 'Load factors (K5)', 'Risk (R1) and teach (S1)']]
rm['lp']['table'][2] = ['2', 'Four forces and drag (K4)', 'Parasite drag, then induced drag: vortices, downwash, lift tilts back. Where do those vortices go?']
rm['lp']['table'][3] = ['3', 'Wake turbulence (K6)', 'We know the forces. Why does the airplane stay balanced?']
TASK['lp']['schedule'] = [['Introduction', 'Slides 1 to 3', '5 min'], ['Lift (K1)', 'Step 1', '12 min'], ['Forces and drag chain (K4)', 'Step 2', '18 min'], ['Wake turbulence (K6)', 'Step 3', '10 min'], ['Stability (K2)', 'Step 4', '12 min'], ['Turning tendencies (K3)', 'Step 5', '8 min'], ['Load factors (K5)', 'Step 6', '10 min'], ['Risk, teaching plan, review', 'Final slides', '10 min'], ['Total', '', '85 min']]
TASK['lp']['intro']['overview'] = 'We go in one chain: how the wing makes lift; the forces that come with it; parasite drag, then induced drag and how wingtip vortices tilt lift back; where those vortices go as wake turbulence; why the airplane stays stable (the bowl method); what pulls it left; and how much load it can take. Then the risks and how to teach it.'
TASK['lp']['conclusion'][0] = 'Retrace the chain: the wing makes lift (Bernoulli and Newton). Lift comes with drag: parasite drag from shape, interference, and friction, and induced drag from making lift. Induced drag happens because wingtip vortices create downwash, which tilts the relative wind and the lift vector back; it grows with AOA, shows up as adverse yaw, and shrinks in ground effect. Those same vortices trail behind as wake turbulence. Stability keeps the airplane balanced, turning tendencies pull it left, and load factor limits how hard we can maneuver.'
TASK['lp']['errors'].insert(2, ('Saying induced drag comes from the shape of the wing', 'That is parasite (form) drag. Induced drag comes from making lift and the downwash it creates (PHAK 5-7).'))
TASK['lp']['errors'].insert(3, ('Thinking ground effect gives more power', 'It reduces induced drag. Lifting off too slow can leave the airplane unable to climb once out of ground effect (PHAK 5-12).'))

rm['lp']['teach'] = ['Show the roadmap. Each step answers a question that leads to the next: the wing makes lift; lift comes with forces and drag; we take parasite drag first, then induced drag and how wingtip vortices tilt lift back; those same vortices become wake turbulence; then why the airplane stays stable, what pulls it left, and how much load it can take. Risk management and teaching tie it together.']

# ---- wording pass (v2.1): clearer bullets, no side notes to the applicant
import re as _re
_B = {
 'Objective': ['Explain how a wing makes lift', 'Explain the four forces and drag', 'Explain stability and turning tendencies', 'Apply load factor and wake turbulence'],
 "Newton's Third Law and Downwash": ['Every action has an equal reaction', 'Wing pushes air down (downwash)', 'Air pushes the wing up', 'Bernoulli and Newton work together'],
 'Lift, Speed, and AOA': ['Lift: proportional to airspeed squared', 'Twice the speed: four times the lift', 'Slower: needs a higher AOA', 'Pilot controls lift with AOA and speed'],
 'The Four Forces': ['Thrust: forward, from the propeller', 'Drag: rearward, opposes thrust', 'Lift: perpendicular to the flight path', 'Weight: straight down through the CG'],
 'Forces in Balance and in a Climb': ['Steady flight: opposing forces cancel', 'The four are not all equal', 'Lift and weight are the largest', 'Climbing: part of weight acts as drag'],
 'Drag: Two Kinds': ['Parasite: not caused by lift', 'Induced: caused by making lift', 'Total drag = parasite + induced', 'Parasite first, then induced'],
 'How Induced Drag Happens': ['1. Air curls around the wingtip', '2. Vortex pushes air down (downwash)', '3. Downwash tilts the relative wind', '4. Lift tilts back: that is induced drag'],
 'Induced Drag Increases With AOA': ['Higher AOA: bigger pressure difference', 'Stronger vortices, more downwash', 'Slow flight: most induced drag', 'Varies inversely with airspeed squared'],
 'Total Drag and L/D Max': ['Induced drag: highest when slow', 'Parasite drag: highest when fast', 'L/D max: lowest total drag', 'Drag climbs near stall and near VNE'],
 'Induced Drag in a Turn: Adverse Yaw': ['Lowered aileron: more lift, more drag', 'That wing gets pulled back', 'Nose yaws opposite the turn', 'Fix: coordinate with rudder'],
 'Induced Drag Near the Ground: Ground Effect': ['Ground blocks vortices and downwash', 'Less induced drag: the float', 'Strongest below one wingspan', 'Climbing out: induced drag returns'],
 'From Wingtip Vortex to Wake Turbulence': ['Vortices trail behind every airplane', 'Present from rotation to touchdown', 'Strongest: heavy, clean, slow', 'Flaps out: wake decays faster'],
 'The Hazard: Induced Roll': ['Hazard: an induced rolling moment', 'Can exceed your roll control', 'Short wings: hardest to counter', 'C172S behind an airliner: high risk'],
 'How Vortices Move': ['Sink several hundred fpm', 'Near ground: move outward 2 to 3 kts', 'Light crosswind: one may stay on runway', 'Light quartering tailwind: worst case'],
 'Wake Turbulence Precautions': ['Landing: stay above, land beyond', 'Departing: rotate before their point', 'Climb above their path, turn clear', 'En route: avoid below and behind'],
 'Static Stability: The Bowl Method': ['Bowl: ball rolls back (positive)', 'Flat floor: sidesteps, stays (neutral)', 'Hill: rolls away (negative)', 'Static is the first reaction only'],
 'Dynamic Stability': ['Dynamic: what happens over time', 'Positive: swings get smaller', 'Neutral: swings stay the same', 'Negative: swings get bigger'],
 'Longitudinal Stability (Pitch)': ['Pitch: about the lateral axis', 'CG ahead of the center of lift', 'Tail pushes down to balance', 'Slow down: nose drops, speed returns'],
 'Lateral Stability (Roll)': ['Roll: about the longitudinal axis', 'Dihedral, sweepback, keel effect', 'Lower wing gets more AOA, rises', 'High wing adds keel effect (C172S)'],
 'Directional Stability (Yaw)': ['Yaw: about the vertical axis', 'Fin works like arrow feathers', 'More side area behind the CG', 'Nose weathervanes into the wind'],
 'Turning Tendencies: Torque Reaction': ['Four parts make up "torque"', 'Prop turns clockwise (pilot view)', 'Airplane tries to roll left', 'On the ground: extra left tire drag'],
 'Turning Tendencies: Slipstream and Gyroscopic': ['Slipstream hits left side of the fin', 'Strongest: high power, low speed', 'Precession acts 90 degrees ahead', 'Mostly tailwheel, when tail rises'],
 'Turning Tendencies: P-Factor': ['High AOA: climbs and slow flight', 'Descending blade takes a bigger bite', 'More thrust on the right side', 'Nose yaws left: hold right rudder'],
 'Load Factor in Turns': ['60 degree bank: 2 Gs', 'Climbs fast past 45 to 50 degrees', 'Light airplanes yield near 70 to 75', 'Wing must lift that many Gs'],
 'Load Factor and Stall Speed': ['Stall speed rises with load factor', 'By the square root of load factor', 'C172S wings level: 48 KIAS', 'C172S at 60 degrees: 68 KIAS'],
 'Maneuvering Speed (VA)': ['One full input, one axis, smooth air', 'C172S: 105 KIAS at 2,550 lb', 'Lighter airplane: lower VA', 'No protection from combined inputs'],
 'Risk: Stalls From Load Factor': ['Steep turns raise stall speed', 'Trap: overshooting base to final', 'Keep bank shallow near the ground', 'Recover: reduce the AOA'],
 'Risk: Wake, Turning Tendencies, Spirals': ['Wake: plan your rotation point', 'Left yaw: lead with right rudder', 'Spiral: level the wings, then pull', 'Know your airplane\'s limits'],
 'Teaching It: Three Elements in Flight': ['Stability: trim, push, release', 'P-factor: climb, feel the left yaw', 'Load factor: 45 and 60 degree turns', 'Debrief each one'],
 'Common Errors': ['"All four forces are equal"', '"Stalls are caused by low speed"', 'Drag "inversely" (not squared)', 'VA treated as full protection'],
 'Review Questions': ['State Bernoulli\'s Principle', 'What causes a stall?', 'Load factor at 60 degrees of bank?', 'Departing behind a heavy: rotate where?'],
}
_NOTES = {
 'Static Stability: The Bowl Method': None,
 'Definition: Stability': 'Read the definition. Stability is built in by the designer; the pilot does not add it.',
 'Definition: Load Factor': 'Read the definition. C172S normal category: +3.8 and -1.52 Gs flaps up, +3.0 flaps down. Utility: +4.4 and -1.76.',
 'Maneuvering Speed (VA)': 'VA protects against one full input in one axis only. It does not protect against multiple full inputs or inputs in more than one axis, and it goes down as weight goes down.',
}
_DROP = [r'\s*Your note "Jeep vs\. Ferrari" is a good analogy\.', r', which your whiteboard notes also show']
_KILL = ('Your whiteboard', 'whiteboard wording')
for _s in TASK['slides']:
    if _s['title'] in _B: _s['bullets'] = _B[_s['title']]
    if _NOTES.get(_s['title']): _s['notes'] = _NOTES[_s['title']]
    _t = _s.get('lp', {}).get('teach')
    if _t:
        out = []
        for p in _t:
            if any(k in p for k in _KILL): continue
            for pat in _DROP: p = _re.sub(pat, '', p)
            p = p.replace('Bowl method (from the applicant\'s whiteboard): ', 'Bowl method: ')
            out.append(p)
        _s['lp']['teach'] = out
TASK['references'] = [r for r in TASK['references'] if 'whiteboard' not in r]
TASK['lp']['equipment'][1] = 'Whiteboard and markers'
TASK['lp']['instructor'][1] = 'Build the chain on the whiteboard as you go: airfoil, four forces, drag curve, vortex and downwash, bowl method.'
TASK['lp']['conclusion'][1] = 'Ask the review questions, then have the student walk the whole chain back on the whiteboard from lift to load factor.'
TASK['lp']['objective'] = 'The student will be able to explain how a wing makes lift, the four forces and both types of drag, how wingtip vortices cause induced drag and wake turbulence, airplane stability, turning tendencies, and load factors, and will apply each one to the C172S and manage the risks that come with them.'

for _s in TASK['slides']:
    if _s['title'] == 'Principles of Flight':
        _s['lp']['teach'] = ['Attention: ask the student if they have ever held a hand out of a car window and felt it rise when they tilted it. The PHAK uses the same example (PHAK 4-10). This lesson explains why.']
    if _s['title'] == 'Objective':
        _s['lp']['teach'] = ['State the objective in plain words: by the end, the student can explain how the wing makes lift, what drag it costs, where the wingtip vortices go, why the airplane stays stable, what pulls it left, and how much load it can take.']
    if _s['title'] == 'Definitions: Chord Line and Camber':
        _s['lp']['teach'] = [x.replace('The glossary adds that the curved upper camber', 'The curved upper camber') for x in _s['lp']['teach']]

# ---- v3: checkride format. No questions, no analogies or scenarios, dense wording.
_T = {
 'Principles of Flight': ['Attention: loss of control, stall/spin, wake encounters, and overstress accidents all trace back to these principles.'],
 'Objective': ['Student explains lift, the four forces, parasite and induced drag, wingtip vortices and wake turbulence, stability, turning tendencies, and load factors, applies each to the C172S, and manages the related risks.'],
 'Lesson Roadmap: Each Topic Builds the Next': ['Order follows cause and effect, not ACS number order: lift, then the forces and drag that come with it, then the vortices induced drag leaves behind (wake turbulence), then stability, turning tendencies, and load factors. Risk management and S1 close the lesson.'],
 'Definitions: Chord Line and Camber': ['Leading edge: rounded front. Trailing edge: narrow, tapered rear (PHAK 4-6). Mean camber line: equidistant from upper and lower surfaces (PHAK 4-7).', 'Upper camber is more pronounced, so airflow above the wing is faster than below it (PHAK G-6).', 'Airfoil design depends on purpose: early thin airfoils, Clark Y and laminar flow (subsonic), circular arc and double wedge (supersonic) (PHAK 4-7, PHAK Fig 4-6).'],
 "Definition: Bernoulli's Principle": ['Venturi tube: air speeds up through the narrow throat to move the same mass in the same time, so pressure drops there (PHAK 4-6).'],
 "Newton's Third Law and Downwash": ['Newton\'s Third Law: for every action there is an equal and opposite reaction (PHAK 4-3).', 'Downward backward flow off the upper surface (downwash) produces an upward forward reaction on the airfoil (PHAK 4-8).', 'Bernoulli and Newton both operate whenever lift is produced. Pressure distribution and center of pressure change with AOA (PHAK 4-8, PHAK Fig 4-7).'],
 'Definitions: Relative Wind and Angle of Attack': ['The flight path determines the relative wind (PHAK G-25).', 'Low speed requires a higher AOA for the same lift (PHAK Fig 5-3).', 'Lift acts perpendicular to the relative wind (PHAK 5-8).'],
 'Lift, Speed, and AOA': ['Lift is proportional to the square of velocity: 200 knots gives four times the lift of 100 knots at the same AOA (PHAK 5-4).', 'L = CL x density x V squared x S / 2 (PHAK 5-4). The pilot controls lift with AOA and airspeed.', 'CL increases with AOA to CL max, then drops: the stall (PHAK Fig 5-5).'],
 'Definition: Critical Angle of Attack': ['Beyond the critical AOA, airflow separates and lift decreases: the stall (PHAK 5-7).', 'C172S, 2,550 lb, power off, flaps up: 48 KIAS wings level, 68 KIAS at 60 degrees of bank. Flaps full: 40 KIAS (POH Fig 5-3).'],
 'Drag: Two Kinds': ['Drag resists movement through the air. Parasite drag does not aid flight; induced drag results from producing lift (PHAK 5-6).'],
 'Definition: Parasite Drag': ['Form drag: from the aircraft\'s shape and airflow around it, such as cowlings and antennas (PHAK 5-6).', 'Interference drag: intersecting airstreams create eddy currents and turbulence, such as at the wing root or strut (PHAK 5-6).', 'Skin friction drag: moving air against the surface. Reduced by flush rivets, a smooth finish, and a clean airplane (PHAK 5-6, PHAK 5-7).'],
 'Definition: Induced Drag': ['Induced drag is the penalty for producing lift, since no system doing work is 100 percent efficient (PHAK 5-7).'],
 'How Induced Drag Happens': ['1. Higher pressure below the wing flows around the tip to the low pressure on top, forming a vortex at each tip (PHAK 5-7).', '2. The vortices push air up beyond the tip and down behind the trailing edge. This induced downwash is the source of induced drag (PHAK 5-7).', '3. Downwash points the relative wind downward (PHAK 5-7).', '4. Lift is perpendicular to the relative wind, so the lift vector tilts aft. The rearward component of lift is induced drag (PHAK 5-7, PHAK 5-8).'],
 'Induced Drag Increases With AOA': ['Higher AOA: greater pressure difference and lateral flow, stronger vortices, more induced drag (PHAK 5-9).', 'Lower airspeed requires higher AOA, so induced drag varies inversely with the square of airspeed (PHAK 5-8).', 'Symmetrical airfoil at zero AOA: no pressure differential, no downwash, no induced drag (PHAK 5-8).'],
 'Total Drag and L/D Max': ['Parasite drag increases as the square of airspeed; induced drag varies inversely with the square of airspeed (PHAK 5-8).', 'Near the stall, induced drag dominates; near VNE, parasite drag dominates. Total drag is minimum at L/D max (PHAK 5-5, PHAK 5-8).'],
 'Induced Drag in a Turn: Adverse Yaw': ['Adverse yaw: the nose yaws toward the outside of the turn, caused by higher induced drag on the outside wing, which is producing more lift (PHAK G-1).', 'More pronounced at low airspeed. Corrected with coordinated rudder (PHAK 6-3).'],
 'Induced Drag Near the Ground: Ground Effect': ['The surface restricts vertical airflow, reducing upwash, downwash, and wingtip vortices, so induced drag decreases (PHAK 5-11).', 'Induced drag reduction: 1.4 percent at one wingspan, 23.5 percent at one-fourth span, 47.6 percent at one-tenth span (PHAK 5-11).', 'Landing: excess speed in the flare causes float (PHAK 5-12).', 'Takeoff: the airplane may lift off below the recommended speed, then settle or fail to climb out of ground effect. Do not force it off with a deficiency of speed (PHAK 5-12).'],
 'From Wingtip Vortex to Wake Turbulence': ['Every aircraft in flight generates a pair of counter-rotating wingtip vortices from the lifting pressure differential (AC 90-23G par 3, 4).', 'Strength increases with weight and decreasing speed. Greatest when heavy, clean, and slow; a dirty configuration hastens decay (AC 90-23G par 5).', 'Vortices are generated from rotation to touchdown (AC 90-23G par 7a).'],
 'The Hazard: Induced Roll': ['Primary hazard: an induced rolling moment that can exceed the roll control of the encountering aircraft (AC 90-23G par 6a).', 'Short-wingspan aircraft relative to the generating aircraft have the most difficulty countering it (AC 90-23G par 6b).'],
 'How Vortices Move': ['Sink several hundred fpm, weakening with time and distance (AC 90-23G par 7c).', 'Within 100 to 200 feet of the ground, move laterally outward at 2 to 3 knots (AC 90-23G par 7d).', 'A 1 to 5 knot crosswind can hold the upwind vortex in the touchdown zone. A light quartering tailwind can move vortices into the final approach and touchdown zone: maximum caution (AC 90-23G par 7e).', 'Vortices drift with the wind: 10 knots moves them about 1,000 feet per minute (PHAK 5-9).'],
 'Wake Turbulence Precautions': ['Landing behind a larger aircraft, same runway: stay at or above its approach path, land beyond its touchdown point (AIM 7-4-6).', 'Departing behind a larger aircraft: rotate before its rotation point, climb above its path until clear (AIM 7-4-6).', 'After a larger aircraft low approach, missed approach, or touch-and-go: wait at least 2 minutes (AIM 7-4-6).', 'En route: avoid below and behind; do not follow within 1,000 feet below (AIM 7-4-6, PHAK 5-9).', 'The pilot is expected to avoid wake encounters with or without an ATC caution. Accepting a visual follow clearance accepts wake turbulence responsibility (AIM 7-4-6, AC 90-23G par 8a).'],
 'Definition: Stability': ['Stability is a design characteristic. Two types: static and dynamic (PHAK 5-14).'],
 'Static Stability: The Bowl Method': ['Static stability: the initial tendency after a disturbance (PHAK 5-14).', 'Positive: returns to equilibrium. Neutral: remains in the new condition. Negative: continues away (PHAK 5-14).', 'Bowl method: bowl, ball rolls back (positive); flat floor, ball sidesteps and stays (neutral); upside-down bowl, ball rolls away (negative).'],
 'Dynamic Stability': ['Dynamic stability: the response over time. Positive: oscillations decrease. Neutral: oscillations stay the same, like a worn shock absorber. Negative: oscillations increase (PHAK 5-15).', 'Demonstration: trim hands-off, push slightly, release. Oscillations stop: positive. Continue: neutral. Increase: unstable (PHAK 5-17).'],
 'Longitudinal Stability (Pitch)': ['Pitch stability about the lateral axis. Depends on wing and tail location relative to the CG and tail size (PHAK 5-15).', 'Center of lift aft of the CG makes the airplane nose heavy; the horizontal stabilizer provides a downward balancing force (PHAK 5-16).', 'Speed decreases: less downwash on the tail, nose pitches down, speed returns to trim (PHAK 5-16).'],
 'Lateral Stability (Roll)': ['Roll stability about the longitudinal axis. Factors: dihedral, sweepback, keel effect, weight distribution (PHAK 5-17).', 'Dihedral: a roll causes a sideslip; the low wing meets a higher AOA, gains lift, and rises (PHAK 5-18).', 'High wing (C172S): keel effect, fuselage acts as a pendulum below the wing (PHAK 5-18).'],
 'Directional Stability (Yaw)': ['Yaw stability about the vertical axis; the easiest to achieve in design (PHAK 5-19).', 'Fin and side area aft of the CG weathervane the nose into the relative wind. Larger and farther aft: more stable (PHAK 5-19).'],
 'Definitions: Maneuverability and Controllability': ['Maneuverability depends on weight, inertia, control size and location, structural strength, and powerplant. Controllability is response to pilot inputs regardless of stability (PHAK 5-15).', 'Forward CG: higher stall speed, higher elevator forces. Aft CG: less stable, harder stall recovery (PHAK 5-43, PHAK 5-44).'],
 'Turning Tendencies: Torque Reaction': ['"Torque" (left turning tendency) has four elements: torque reaction, corkscrewing slipstream, gyroscopic action, P-factor (PHAK 5-30, PHAK 5-31).', 'Torque reaction: Newton\'s Third Law. Prop turns clockwise from the pilot\'s seat; the airplane tends to roll left (PHAK 5-31).', 'Takeoff roll: more weight on the left main gear, more friction, left turning moment. Correct with rudder (PHAK 5-31).'],
 'Turning Tendencies: Slipstream and Gyroscopic': ['Corkscrew effect: the spiraling slipstream strikes the vertical fin, strongest at high power and low speed (PHAK 5-31).', 'Gyroscopic precession: a force on the propeller acts 90 degrees ahead in the direction of rotation. Most prominent in tailwheel airplanes when the tail is raised (PHAK 5-31, PHAK 5-32).'],
 'Turning Tendencies: P-Factor': ['High AOA: the descending (right) blade has a greater bite than the ascending blade, moving the center of thrust right and yawing the nose left (PHAK 5-32).', 'All four elements vary with flight condition; correct with the controls in every phase (PHAK 5-32). C172S: right rudder in full power climbs.'],
 'Definition: Load Factor': ['Load factor of 3: the structure carries three times the aircraft weight (PHAK 5-33).', 'Limit load factors are the highest expected in normal operation; the structure must carry 1.5 times these (factor of safety) (PHAK 5-33).', 'Category limits: normal +3.8/-1.52, utility +4.4/-1.76, acrobatic +6.0/-3.00 (PHAK 5-34).', 'C172S: normal flaps up +3.8/-1.52, flaps down +3.0; utility flaps up +4.4/-1.76 (POH 2-11).'],
 'Load Factor in Turns': ['Level coordinated turn: load factor results from centrifugal force and weight (PHAK 5-34).', '60 degrees of bank: 2 Gs. Increases rapidly past 45 to 50 degrees (PHAK 5-34).', 'Average light airplane yield point: 70 to 75 degrees of bank (PHAK 5-36).'],
 'Load Factor and Stall Speed': ['Stall speed increases with the square root of load factor: 50 knots becomes 100 knots at 4 Gs (PHAK 5-35).', 'C172S flaps up, 2,550 lb: 48, 52, 57, 68 KIAS at 0, 30, 45, 60 degrees of bank (POH Fig 5-3).', 'Altitude loss in stall recovery: up to 230 feet (POH Fig 5-3).'],
 'Maneuvering Speed (VA)': ['VA: maximum speed for one full deflection of one control, one time, in one axis, in smooth air, without damage (PHAK 5-35).', 'No protection against multiple full inputs in one axis or inputs in more than one axis (PHAK 5-35).', 'C172S: 105 KIAS at 2,550 lb, 98 at 2,200 lb, 90 at 1,900 lb (POH 2-4).', 'Rapid alternating inputs can cause structural failure at any speed, including below VA (PHAK 5-36).'],
 'Risk: Stalls From Load Factor': ['Load factor and VA knowledge prevents stalls from steep turns near the ground and structural failures from violent maneuvering (PHAK 5-36).', 'Mitigation: plan the pattern to avoid overshoots, limit bank near the ground, go around instead of tightening the turn, reduce AOA at the first stall indication.'],
 'Risk: Wake, Turning Tendencies, Spirals': ['Wake: rotate before a larger aircraft\'s rotation point; wait 2 minutes after its low approach or touch-and-go (AIM 7-4-6).', 'Turning tendencies: anticipate left yaw on takeoff and climb; hold right rudder (PHAK 5-32).', 'Spiral: level the wings before pulling. Back pressure first tightens the turn and raises load factor; improper recovery from spiral instability leading to inflight structural failure has probably contributed to more GA fatalities than any other factor (PHAK 5-20).'],
 'Teaching It: Three Elements in Flight': ['S1: deliver instruction on at least three elements of K1 to K6. C172S plan at a safe altitude:', 'Stability (K2): trim, slight push, release, observe damping (PHAK 5-17).', 'Turning tendency (K3): full power climb, observe left yaw and required right rudder (PHAK 5-32).', 'Load factor (K5): 45 and 60 degree turns, relate G load to stall speeds in the POH table (POH Fig 5-3).'],
 'Common Errors': ['"All four forces are equal": opposing forces cancel; lift and weight exceed thrust and drag (PHAK 5-2).', '"Stalls are caused by low airspeed": a stall occurs at the critical AOA at any airspeed (PHAK G-9).', '"Induced drag varies inversely with airspeed": it varies inversely with the square of airspeed (PHAK 5-8).', '"Below VA is always safe": VA covers one full input in one axis only (PHAK 5-35).'],
 'References': ['All sources listed in the References section of this lesson plan.'],
}
_PLAIN = {
 "Definition: Bernoulli's Principle": 'Faster airflow over the curved upper surface lowers pressure there; higher pressure below pushes the wing up.',
 'Definition: Critical Angle of Attack': 'A stall is caused by exceeding the critical AOA, not by low airspeed. Stall speed varies with weight, bank, and flaps; critical AOA does not.',
 'Definition: Parasite Drag': 'Three types: form (shape), interference (intersecting airstreams), skin friction (surface roughness).',
 'Definition: Induced Drag': 'By-product of lift. Present whenever lift is produced. Increases with AOA.',
 'Definition: Stability': 'Static stability is the initial reaction to a disturbance; dynamic stability is the response over time.',
 'Definition: Load Factor': 'Measured in Gs. C172S normal category: +3.8 to -1.52 G flaps up.',
}
_slides = []
for _s in TASK['slides']:
    if _s['title'] == 'Review Questions': continue
    if _s['title'] in _T: _s['lp']['teach'] = _T[_s['title']]
    if _s['title'] in _PLAIN: _s['plain'] = _PLAIN[_s['title']]
    for _k in ('analogy', 'ask', 'example'): _s.get('lp', {}).pop(_k, None)
    _s['notes'] = ' '.join(_s['lp']['teach']) if _s.get('lp') else _s.get('notes', '')
    if _s['title'] == 'Lesson Roadmap: Each Topic Builds the Next':
        _s['title'] = 'Lesson Roadmap'
        _s['table'] = [['Step', 'Topic', 'Connects to'], ['1', 'Lift (K1)', 'Lift creates the four forces'], ['2', 'Forces and drag (K4)', 'Induced drag creates vortices'], ['3', 'Wake turbulence (K6)', 'Disturbances test stability'], ['4', 'Stability (K2)', 'Prop effects oppose it'], ['5', 'Turning tendencies (K3)', 'Maneuvering adds load'], ['6', 'Load factors (K5)', 'Risk (R1), teaching (S1)']]
        _s['lp']['table'] = _s['table']
    _slides.append(_s)
TASK['slides'] = _slides
TASK['lp']['intro'] = {
 'attention': 'Loss of control, stall/spin, wake turbulence, and overstress accidents all trace back to the principles in this lesson.',
 'motivation': 'Every maneuver flown and taught depends on these principles, and each one carries a specific risk. All elements are tested on the CFI practical test.',
 'overview': 'Lift; the four forces; parasite drag; induced drag (vortex, downwash, lift vector tilts aft) and its effects (AOA, L/D max, adverse yaw, ground effect); wake turbulence; static and dynamic stability about all three axes; turning tendencies; load factors and VA; risk management and in-flight instruction.'}
TASK['lp']['instructor'] = ['Teach in roadmap order; state each transition.', 'Build the diagrams on the whiteboard: airfoil, four forces, drag curve, vortex and downwash, bowl method, load factor chart.', 'Use the model airplane for axes and stability.', 'Brief the S1 in-flight demonstrations for the next flight.']
TASK['lp']['student'] = ['Follow along and draw the key diagrams.', 'Explain the chain from lift to load factor in their own words.', 'Identify each principle in the C172S.']
TASK['lp']['conclusion'] = ['Summary: the wing produces lift (Bernoulli and Newton). Lift brings the four forces and drag. Parasite drag comes from shape, interference, and friction. Induced drag comes from lift: tip vortices create downwash, which tilts the relative wind and the lift vector aft; it increases with AOA, causes adverse yaw, and decreases in ground effect. The same vortices trail behind as wake turbulence. Stability returns the airplane to equilibrium, turning tendencies yaw it left, and load factor limits maneuvering and raises stall speed.', 'The student restates the chain on the whiteboard from lift to load factor.']
TASK['lp']['errors'] = [e for e in TASK['lp']['errors'] if 'shape of the wing' not in e[0]]
TASK['lp']['completion'] = [c for c in TASK['lp']['completion']]

for _s in TASK['slides']:
    if _s['title'] == 'References': _s['bullets'] = ['PHAK Chapters 4, 5, 6', 'AIM 7-4, AC 90-23G', 'C172S POH Sections 2 and 5', 'FAA-S-ACS-25']
