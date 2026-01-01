"""
Electrical Engineering Specifications for Golden Ratio Motor
Calculates maximum inductance, wire gauge, and drive requirements
Based on 1.54ms pulse window at 650 Hz
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical Constants
PHI = (1 + np.sqrt(5)) / 2
GOLDEN_ANGLE = 137.5  # degrees

# Motor Specifications (from visualization)
RPM = 3000
ROTATION_FREQ = RPM / 60  # Hz
N_MAGNETS = 13
PULSE_FREQ = ROTATION_FREQ * N_MAGNETS  # Hz
PULSE_PERIOD = 1 / PULSE_FREQ  # seconds

# Time Budget Breakdown
# We have 1.54ms per pulse, but need to account for:
# - Rise time (current ramps up)
# - Hold time (coil at full power)
# - Fall time (current collapses)

PULSE_PERIOD_MS = PULSE_PERIOD * 1000
RISE_TIME_BUDGET = 0.3 * PULSE_PERIOD_MS  # 30% for rise
HOLD_TIME_BUDGET = 0.4 * PULSE_PERIOD_MS  # 40% for hold
FALL_TIME_BUDGET = 0.3 * PULSE_PERIOD_MS  # 30% for fall

print("=" * 70)
print("ELECTRICAL ENGINEERING ANALYSIS - COIL DESIGN")
print("=" * 70)

print(f"\n{'TIMING CONSTRAINTS':^70}")
print("-" * 70)
print(f"Pulse frequency:          {PULSE_FREQ:.1f} Hz")
print(f"Period per pulse:         {PULSE_PERIOD_MS:.3f} ms ({PULSE_PERIOD*1e6:.1f} µs)")
print(f"\nTime Budget Allocation:")
print(f"  Rise time (0-90%):      {RISE_TIME_BUDGET:.3f} ms ({RISE_TIME_BUDGET/PULSE_PERIOD_MS*100:.0f}%)")
print(f"  Hold time (active):     {HOLD_TIME_BUDGET:.3f} ms ({HOLD_TIME_BUDGET/PULSE_PERIOD_MS*100:.0f}%)")
print(f"  Fall time (90-0%):      {FALL_TIME_BUDGET:.3f} ms ({FALL_TIME_BUDGET/PULSE_PERIOD_MS*100:.0f}%)")

# L/R Time Constant Calculation
# For an RL circuit, current rises as: I(t) = I_max * (1 - e^(-t/(L/R)))
# To reach 90% of max current: 0.9 = 1 - e^(-t/(L/R))
# Solving: t = (L/R) * ln(10) ≈ 2.3 * (L/R)

# We need: rise_time = 2.3 * (L/R)
# Therefore: L/R = rise_time / 2.3

TIME_CONSTANTS_FOR_90_PERCENT = 2.3
TAU_MAX_RISE = (RISE_TIME_BUDGET / 1000) / TIME_CONSTANTS_FOR_90_PERCENT  # seconds
TAU_MAX_FALL = (FALL_TIME_BUDGET / 1000) / TIME_CONSTANTS_FOR_90_PERCENT  # seconds

print(f"\n{'L/R TIME CONSTANT':^70}")
print("-" * 70)
print(f"Maximum τ (tau) for rise: {TAU_MAX_RISE*1000:.3f} ms ({TAU_MAX_RISE*1e6:.1f} µs)")
print(f"Maximum τ (tau) for fall: {TAU_MAX_FALL*1000:.3f} ms ({TAU_MAX_FALL*1e6:.1f} µs)")

# Voltage and Resistance Trade-off
# Higher voltage = faster switching, but requires more robust components
# We'll calculate for multiple voltage scenarios

VOLTAGES = [12, 24, 48, 96]  # Common DC bus voltages
TARGET_CURRENT = 5  # Amps (typical for small motor)

print(f"\n{'RESISTANCE & INDUCTANCE LIMITS':^70}")
print("-" * 70)
print(f"Target current:           {TARGET_CURRENT:.1f} A")
print(f"\nFor various drive voltages:")
print(f"{'Voltage':>8} | {'Resistance':>12} | {'Max Inductance':>15} | {'Power':>10}")
print("-" * 70)

voltage_data = []
for V in VOLTAGES:
    R = V / TARGET_CURRENT  # Ohms
    L_max = TAU_MAX_RISE * R  # Henrys
    L_max_mH = L_max * 1000  # milliHenrys
    P = V * TARGET_CURRENT  # Watts
    print(f"{V:7}V | {R:10.2f} Ω | {L_max_mH:12.3f} mH | {P:8.0f} W")
    voltage_data.append({'V': V, 'R': R, 'L_max': L_max, 'L_max_mH': L_max_mH, 'P': P})

# Wire Gauge Recommendations
# Based on resistance per unit length and current capacity

print(f"\n{'WIRE GAUGE RECOMMENDATIONS':^70}")
print("-" * 70)
print(f"Target current:           {TARGET_CURRENT:.1f} A")
print(f"Recommended wire sizes (for {TARGET_CURRENT}A continuous):")
print(f"\n  AWG 14:  2.5 mm²  (15A capacity, 8.3 Ω/km @ 20°C)")
print(f"  AWG 16:  1.3 mm²  (10A capacity, 13.2 Ω/km @ 20°C)")
print(f"  AWG 18:  0.8 mm²  (7A capacity, 21.0 Ω/km @ 20°C)")
print(f"\nFor HIGH-SPEED switching (low inductance):")
print(f"  → Use LITZ WIRE (multiple fine strands) to reduce skin effect")
print(f"  → OR use flat/ribbon wire for minimal self-inductance")

# Core Material Selection
print(f"\n{'CORE MATERIAL REQUIREMENTS':^70}")
print("-" * 70)
print(f"Operating frequency:      {PULSE_FREQ:.0f} Hz")
print(f"\nCore material must have low losses at {PULSE_FREQ:.0f} Hz:")
print(f"\n  ✓ LAMINATED SILICON STEEL (0.35mm sheets)")
print(f"    - Used in: transformers, motors")
print(f"    - Loss at 650 Hz: ~10 W/kg (acceptable)")
print(f"    - Permeability: 2000-8000")
print(f"\n  ✓ FERRITE (Manganese-Zinc or Nickel-Zinc)")
print(f"    - Used in: high-frequency inductors")
print(f"    - Loss at 650 Hz: ~1 W/kg (excellent)")
print(f"    - Permeability: 1000-3000")
print(f"\n  ✗ SOLID IRON (DO NOT USE)")
print(f"    - Eddy current losses: >100 W/kg at 650 Hz")
print(f"    - Will overheat and kill efficiency")
print(f"\n  ✓ SOFT MAGNETIC COMPOSITE (SMC/Powder Core)")
print(f"    - Used in: high-frequency motors")
print(f"    - Loss at 650 Hz: ~5 W/kg (good)")
print(f"    - Can be molded into complex Golden Ratio shapes")

# Recommended Design
print(f"\n{'RECOMMENDED COIL DESIGN':^70}")
print("-" * 70)

# Select optimal voltage (48V is good balance)
optimal_idx = 2  # 48V
optimal = voltage_data[optimal_idx]

print(f"\nOptimal Drive Voltage:    {optimal['V']} VDC")
print(f"Target Coil Resistance:   {optimal['R']:.2f} Ω")
print(f"Maximum Inductance:       {optimal['L_max_mH']:.3f} mH")
print(f"Operating Current:        {TARGET_CURRENT:.1f} A")
print(f"Power per Coil:           {optimal['P']:.0f} W")
print(f"\nAssuming {N_MAGNETS} coils (one per magnet):")
print(f"Peak System Power:        {optimal['P'] * N_MAGNETS:.0f} W")
print(f"Average Power (6% duty):  {optimal['P'] * N_MAGNETS * 0.06:.0f} W")

# Practical Coil Winding
# Estimate number of turns needed

# For a coil: L = (μ₀ * μᵣ * N² * A) / l
# Where: N = turns, A = core area, l = magnetic path length, μᵣ = permeability

# Typical values for small motor coil
CORE_AREA_CM2 = 4  # cm²
CORE_LENGTH_CM = 5  # cm
MU_R_FERRITE = 2000  # relative permeability

CORE_AREA = CORE_AREA_CM2 * 1e-4  # m²
CORE_LENGTH = CORE_LENGTH_CM * 1e-2  # m
MU_0 = 4 * np.pi * 1e-7  # H/m

# Solve for N: N = sqrt(L * l / (μ₀ * μᵣ * A))
L_target = optimal['L_max']
N_turns = np.sqrt(L_target * CORE_LENGTH / (MU_0 * MU_R_FERRITE * CORE_AREA))

# Wire length per turn (approximate)
AVG_TURN_LENGTH_CM = 8  # cm (depends on coil diameter)
TOTAL_WIRE_LENGTH_M = N_turns * AVG_TURN_LENGTH_CM / 100

# Wire resistance (AWG 16 copper)
RESISTANCE_PER_M = 0.0132  # Ω/m for AWG 16
CALCULATED_RESISTANCE = TOTAL_WIRE_LENGTH_M * RESISTANCE_PER_M

print(f"\n{'COIL WINDING CALCULATIONS':^70}")
print("-" * 70)
print(f"Core dimensions:          {CORE_AREA_CM2} cm² × {CORE_LENGTH_CM} cm path")
print(f"Core material:            Ferrite (μᵣ = {MU_R_FERRITE})")
print(f"Number of turns:          {N_turns:.0f} turns")
print(f"Wire length per coil:     {TOTAL_WIRE_LENGTH_M:.1f} m")
print(f"Wire gauge:               AWG 16 (1.3mm diameter)")
print(f"Calculated resistance:    {CALCULATED_RESISTANCE:.2f} Ω")
print(f"Target resistance:        {optimal['R']:.2f} Ω")

if abs(CALCULATED_RESISTANCE - optimal['R']) / optimal['R'] > 0.3:
    print(f"\n⚠️  Resistance mismatch > 30%")
    print(f"   Adjust: turns={N_turns * np.sqrt(optimal['R']/CALCULATED_RESISTANCE):.0f} or wire gauge")
else:
    print(f"\n✓  Resistance match within spec")

# Driver Circuit Requirements
print(f"\n{'DRIVER CIRCUIT REQUIREMENTS':^70}")
print("-" * 70)
print(f"Switching frequency:      {PULSE_FREQ:.0f} Hz")
print(f"Rise time requirement:    < {RISE_TIME_BUDGET:.3f} ms")
print(f"Current capacity:         {TARGET_CURRENT:.1f} A per channel")
print(f"Number of channels:       {N_MAGNETS} (one per coil)")
print(f"\nRecommended Components:")
print(f"  • MOSFET/IGBT:          Logic-level N-channel, Rds(on) < 0.1Ω")
print(f"                          (e.g., IRFZ44N, IRL540N)")
print(f"  • Flyback Diode:        Fast recovery, {TARGET_CURRENT*2:.0f}A rated")
print(f"                          (e.g., UF5408, MUR860)")
print(f"  • Gate Driver:          High-speed driver IC")
print(f"                          (e.g., IR2104, MCP1416)")
print(f"  • Microcontroller:      PWM capable, {PULSE_FREQ*2:.0f}+ Hz timer")
print(f"                          (e.g., Arduino Due, STM32, ESP32)")

# Energy Storage (for pulse generation)
# Calculate capacitor size needed to supply pulse current

PULSE_DURATION = HOLD_TIME_BUDGET / 1000  # seconds
ENERGY_PER_PULSE = optimal['P'] * PULSE_DURATION  # Joules
VOLTAGE_DROOP_PERCENT = 5  # Allow 5% voltage drop

# E = 0.5 * C * V²
# For voltage droop: ΔE = 0.5 * C * (V² - (V-ΔV)²)
# Simplify: C ≈ 2 * E / (2*V*ΔV)

DV = optimal['V'] * (VOLTAGE_DROOP_PERCENT / 100)
C_min = ENERGY_PER_PULSE / (optimal['V'] * DV)  # Farads
C_min_uF = C_min * 1e6

print(f"\n{'POWER SUPPLY & ENERGY STORAGE':^70}")
print("-" * 70)
print(f"Energy per pulse:         {ENERGY_PER_PULSE*1000:.2f} mJ")
print(f"Bus voltage:              {optimal['V']} VDC")
print(f"Minimum bus capacitor:    {C_min_uF:.0f} µF")
print(f"Recommended:              {C_min_uF*2:.0f} µF (2x safety margin)")
print(f"Type:                     Electrolytic, {optimal['V']*1.5:.0f}V rated, low ESR")

# Create visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Electrical Design Parameters', fontsize=16, fontweight='bold')

# 1. Current Rise/Fall Curve
ax1 = axes[0, 0]
t_rise = np.linspace(0, PULSE_PERIOD_MS, 1000)
i_rise = TARGET_CURRENT * (1 - np.exp(-t_rise / (TAU_MAX_RISE * 1000)))

ax1.plot(t_rise, i_rise, 'b-', linewidth=2, label='Current Rise')
ax1.axhline(TARGET_CURRENT * 0.9, color='r', linestyle='--', 
           label='90% Current', alpha=0.7)
ax1.axvline(RISE_TIME_BUDGET, color='g', linestyle='--', 
           label=f'Rise Budget ({RISE_TIME_BUDGET:.2f}ms)', alpha=0.7)
ax1.fill_between(t_rise, 0, i_rise, alpha=0.3)
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Current (A)')
ax1.set_title('Coil Current Rise Time')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. Inductance vs Voltage Trade-off
ax2 = axes[0, 1]
voltages = [v['V'] for v in voltage_data]
inductances = [v['L_max_mH'] for v in voltage_data]

ax2.bar(voltages, inductances, color='steelblue', alpha=0.7, edgecolor='black')
ax2.set_xlabel('Drive Voltage (V)')
ax2.set_ylabel('Maximum Inductance (mH)')
ax2.set_title('Max Inductance vs Drive Voltage')
ax2.grid(True, alpha=0.3, axis='y')
for i, (v, l) in enumerate(zip(voltages, inductances)):
    ax2.text(v, l + 0.005, f'{l:.3f}', ha='center', va='bottom', fontweight='bold')

# 3. Power Dissipation by Component
ax3 = axes[1, 0]
components = ['Coil\nResistance', 'MOSFET\nRds(on)', 'Wire\nResistance', 'Diode\nForward Drop']
power_losses = [
    optimal['P'] * 0.60,  # 60% in coil
    optimal['P'] * 0.15,  # 15% in MOSFET
    optimal['P'] * 0.15,  # 15% in wire
    optimal['P'] * 0.10   # 10% in diode
]

colors = ['#ff6b6b', '#ee5a6f', '#d44f73', '#b94377']
ax3.pie(power_losses, labels=components, autopct='%1.0f%%',
        colors=colors, startangle=90)
ax3.set_title(f'Power Loss Distribution\n(per coil, {optimal["P"]:.0f}W total)')

# 4. Pulse Timing Diagram
ax4 = axes[1, 1]
t_total = np.linspace(0, PULSE_PERIOD_MS * 3, 1000)
pulse_signal = np.zeros_like(t_total)

for n in range(3):
    t_offset = n * PULSE_PERIOD_MS
    mask = (t_total >= t_offset) & (t_total < t_offset + RISE_TIME_BUDGET + HOLD_TIME_BUDGET)
    pulse_signal[mask] = 1

ax4.plot(t_total, pulse_signal, 'purple', linewidth=2)
ax4.fill_between(t_total, 0, pulse_signal, alpha=0.3, color='purple')
ax4.set_xlabel('Time (ms)')
ax4.set_ylabel('Gate Signal')
ax4.set_title(f'Pulse Train @ {PULSE_FREQ:.0f} Hz')
ax4.set_ylim(-0.1, 1.3)
ax4.grid(True, alpha=0.3)
ax4.axhline(0.5, color='gray', linestyle=':', alpha=0.5)
ax4.text(PULSE_PERIOD_MS / 2, 1.15, f'{PULSE_PERIOD_MS:.2f}ms', 
         ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()

print(f"\n{'='*70}")
print("CRITICAL DESIGN SUMMARY")
print(f"{'='*70}")
print(f"\n✓ Use {optimal['V']}V drive with {TARGET_CURRENT}A coils")
print(f"✓ Maximum inductance: {optimal['L_max_mH']:.3f} mH")
print(f"✓ Target resistance: {optimal['R']:.2f} Ω")
print(f"✓ Wind ~{N_turns:.0f} turns on ferrite core")
print(f"✓ Use AWG 16 wire (or thicker)")
print(f"✓ Fast-switching MOSFETs (< 100ns rise time)")
print(f"✓ Bus capacitor: >{C_min_uF*2:.0f} µF")
print(f"\n⚠️  FAILURE MODES TO AVOID:")
print(f"   • Inductance > {optimal['L_max_mH']:.3f} mH → Late pulse → braking")
print(f"   • Solid iron core → Eddy currents → overheating")
print(f"   • Slow MOSFETs → Overlap → shoot-through")
print(f"   • Insufficient capacitor → Voltage sag → weak pulse")
print(f"\n{'='*70}\n")

plt.savefig('electrical_specifications.png', dpi=150, bbox_inches='tight')
print("📊 Electrical specifications graph saved as 'electrical_specifications.png'")
print("\nVisualization ready. Close the window when done.")
plt.show()
