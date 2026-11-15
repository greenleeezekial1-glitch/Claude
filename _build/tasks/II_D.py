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
