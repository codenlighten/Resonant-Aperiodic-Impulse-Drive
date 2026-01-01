# Resonant Aperiodic Impulse Drive

A Golden Ratio-based motor design utilizing parametric resonance and centrifugal clutch load management for high-efficiency energy transfer.

## Concept

This motor design applies biomimetic principles from fluid dynamics to magnetic field geometry, creating a "breathing" resonant system that operates with minimal energy input through:

- **Golden Ratio spiral geometry** for magnetic flux optimization
- **Fibonacci-spaced magnet array** (13 magnets at 137.5° intervals)
- **Centrifugal clutch** for dynamic load management
- **Parametric resonance** achieving High-Q oscillation

## Specifications

- **Operating Speed**: 3000 RPM
- **Pulse Frequency**: 650 Hz (musical note E5)
- **Power**: ~187W average, 3120W peak
- **Q-Factor**: >100 (coasts for ~16 rotations per impulse)
- **Efficiency**: 94% coast / 6% active work cycle

## Technical Details

### Electrical
- Drive Voltage: 48 VDC
- Coil Inductance: <1.926 mH (critical constraint)
- Target Resistance: 9.60 Ω per coil
- Operating Current: 5.0 A
- Pulse Width: 1.54 ms window

### Mechanical
- 13 magnets arranged in Fibonacci spiral
- Ferrite or laminated silicon steel cores
- Centrifugal clutch engagement: 2250-2400 RPM band
- Non-resonant chassis (>1 kHz natural frequency)

## Repository Contents

- `overview.md` - Conceptual explanation and physics principles
- `visualize_motor.py` - Python visualization of spiral geometry and magnetic field
- `electrical_specs.py` - Electrical engineering calculations and coil design
- `results.md` - Analysis and engineering constraints
- `requirements.txt` - Python dependencies

## Status

**Prototype Phase** - Theoretical design with calculated specifications. Ready for component sourcing and physical prototyping.

## Key Innovation

The "quasi-periodic" nature of Golden Ratio spacing prevents resonant dead spots and creates a self-averaging magnetic field distribution that maintains efficiency across rotation cycles.

---

*"Not perpetual motion - just really good impedance matching."*
