# Prototype Build Plan - Resonant Aperiodic Impulse Drive

## Phase 1: Component Sourcing

### Core Components

#### Magnets (13 units)
- **Type:** Neodymium N52 grade
- **Size:** 25mm x 10mm x 5mm (rectangular)
- **Magnetization:** Through thickness
- **Source:** K&J Magnetics, Applied Magnets
- **Cost:** ~$3 each ($39 total)
- **Note:** Alternating N-S poles around rotor

#### Coil Cores (13 units)
- **Type:** Ferrite toroid or E-core
- **Material:** Manganese-Zinc ferrite (MnZn)
- **Size:** ~30mm OD, 4cm² cross-section
- **Permeability:** μᵣ = 2000-3000
- **Source:** Ferroxcube, TDK, Mouser (Part #: B64290L0618X830)
- **Cost:** ~$5 each ($65 total)

#### Magnet Wire for Coils
- **Gauge:** AWG 22 (0.644mm diameter)
- **Type:** Copper enameled
- **Length needed:** ~35 meters per coil = 455m total (buy 500m)
- **Source:** Remington Industries, eBay
- **Cost:** ~$40 per 500m spool

#### Centrifugal Clutch
- **Type:** Adjustable spring tension
- **Engagement:** 2250-2400 RPM range
- **Bore:** 3/4" (19mm) or match shaft
- **Source:** Hilliard, Max-Torque, Go-Kart suppliers
- **Model:** Hilliard Extreme Duty Clutch or custom springs
- **Cost:** $80-150

#### Rotor Assembly
- **Base Plate:** 250mm diameter, 6mm aluminum
- **Shaft:** 19mm hardened steel, 150mm length
- **Bearings:** 2x 6204-2RS (sealed ball bearings)
- **Source:** McMaster-Carr, local metal shop
- **Cost:** ~$60

#### Chassis/Stator Frame
- **Material:** 6061 Aluminum extrusion
- **Design:** Open frame with 13 coil mounts at 137.5° spacing
- **Requirement:** Natural frequency >1 kHz (need to be rigid)
- **Source:** 80/20 Inc, custom fabrication
- **Cost:** $100-200

### Electronics

#### Power Supply
- **Type:** 48V DC, 5A minimum (240W)
- **Recommendation:** Mean Well LRS-350-48 (350W)
- **Protection:** Overcurrent, short circuit
- **Source:** Digi-Key, Mouser
- **Cost:** $40-60

#### MOSFETs (13 units + spares)
- **Part:** IRFZ44N or IRL540N
- **Specs:** Logic-level, Vds=55V, Id=49A, Rds(on)<0.028Ω
- **Package:** TO-220
- **Source:** Digi-Key, Mouser
- **Cost:** $1.50 each (~$25 for 16)

#### Flyback Diodes (13 units + spares)
- **Part:** UF5408 or MUR860
- **Specs:** 3A, 1000V, fast recovery
- **Source:** Digi-Key, Mouser
- **Cost:** $0.50 each (~$10 for 16)

#### Gate Drivers (2x 8-channel or equivalent)
- **Option A:** ULN2803 (Darlington array) - simple but slower
- **Option B:** MCP1416 individual drivers - faster
- **Option C:** Custom MOSFET driver board
- **Source:** Digi-Key
- **Cost:** $15-30

#### Microcontroller
- **Recommendation:** Arduino Due or STM32 Nucleo
- **Requirements:** 13 PWM channels, 650 Hz capable
- **Alternative:** ESP32 (cheaper, WiFi for monitoring)
- **Source:** Arduino.cc, Adafruit
- **Cost:** $25-40

#### Capacitor Bank
- **Type:** Low-ESR electrolytic
- **Specs:** 2500µF minimum, 63V rated
- **Configuration:** 5x 470µF 63V in parallel
- **Source:** Digi-Key, Mouser
- **Cost:** ~$15

#### Hall Effect Sensors (3 units)
- **Part:** A3144 or SS441A
- **Purpose:** Position sensing for timing
- **Source:** Digi-Key
- **Cost:** $5

#### PCB/Breadboard
- **Option A:** Custom PCB from JLCPCB (~$30 for 5 boards)
- **Option B:** Prototype on perfboard ($10)
- **Recommendation:** Start with breadboard, then PCB

### Hardware & Misc
- M4/M5 bolts and nuts
- Shaft collar/set screws
- Heat sinks for MOSFETs (TO-220 compatible)
- Thermal paste
- Hookup wire (18 AWG)
- Connectors (terminal blocks)
- **Cost:** ~$50

## Total Component Cost: ~$650-900

---

## Phase 2: Mechanical Assembly

### Tools Required
- Drill press or accurate hand drill
- Angle measuring tools (protractor or digital angle gauge)
- Soldering iron (60W+)
- Multimeter
- Calipers
- Lathe access (or machine shop) for rotor plate
- Tap and die set (M4, M5)

### Step 1: Rotor Fabrication

1. **Mark Fibonacci Positions**
   ```
   Position 0: 0°
   Position 1: 137.5°
   Position 2: 275° (or -85°)
   Position 3: 412.5° (or 52.5°)
   ...continue for 13 positions
   ```

2. **Machine Rotor Plate**
   - Cut 250mm diameter from 6mm aluminum
   - Drill center hole for shaft (19mm + tolerance)
   - Mark magnet positions at radius = 85mm (adjustable)
   - Create pockets or epoxy mounts for magnets
   - Balance the rotor (critical for 3000 RPM)

3. **Mount Magnets**
   - Alternate N-S poles
   - Use epoxy (JB Weld or Loctite)
   - Verify polarity with compass/gaussmeter before bonding
   - Let cure 24 hours

4. **Assemble Shaft & Bearings**
   - Press bearings into bearing blocks
   - Mount shaft through rotor center
   - Add shaft collars to secure position
   - Verify smooth rotation (no wobble)

### Step 2: Stator Frame

1. **Create Coil Mounting Ring**
   - 300mm diameter (50mm clearance from magnets)
   - Mark 13 positions at 137.5° spacing
   - Design must be non-resonant (thick, damped)

2. **Mount Coil Cores**
   - Orient cores radially (pointing at rotor center)
   - Air gap between core tip and magnet: 3-5mm
   - Secure with adjustable mounts for tuning

### Step 3: Coil Winding

**Per Coil (repeat 13 times):**

1. **Calculate Turns**
   - Target: 9.60Ω resistance
   - AWG 22 wire: 0.0529 Ω/meter
   - Need: ~181 meters → ~298 turns (for 8cm avg turn length)
   - **Practical:** Wind 300 turns, measure resistance, adjust

2. **Wind Coil**
   - Use hand drill or winding jig
   - Keep tension consistent
   - Layer windings neatly
   - Mark start/finish leads clearly
   - Apply varnish or tape to secure

3. **Test Each Coil**
   - Measure DC resistance (target: 9-10Ω)
   - Measure inductance with LCR meter (target: <1.9mH)
   - If too high: remove turns
   - If too low: add turns or use thinner wire

---

## Phase 3: Electronics Assembly

### Step 1: Power Stage (per coil)

**Circuit per coil:**
```
48V+ ───┬─── Coil ───┬─── MOSFET Drain
        │             │
        │             └─── Diode Cathode
        │
        └─── Diode Anode
                      │
        MOSFET Source ┴─── GND
              │
              Gate ← Driver ← MCU PWM
```

1. **Mount MOSFETs** on heat sinks
2. **Solder flyback diodes** (cathode to coil, anode to ground)
3. **Connect coils** (one terminal to 48V+, other to MOSFET drain)
4. **Wire grounds** (heavy gauge, star ground configuration)

### Step 2: Control Board

1. **Hall Sensor Mounting**
   - Mount 3 sensors 120° apart on stator
   - Position to detect magnet pass
   - Connect to MCU interrupt pins

2. **Microcontroller Connections**
   - 13 PWM outputs → Gate drivers → MOSFET gates
   - 3 Hall sensor inputs
   - Power: 5V regulated from 48V (use buck converter)

3. **Capacitor Bank**
   - Mount close to power rails (minimize inductance)
   - Parallel 2500µF total
   - Add ceramic bypass caps (0.1µF) near each MOSFET

### Step 3: Initial Power-Up (NO LOAD)

**Safety First:**
- Wear safety glasses
- Use current-limited bench supply
- Start at 12V, not 48V
- Have kill switch ready

1. **Resistance Check**
   - Verify no short circuits
   - Each coil should read ~10Ω to ground (when MOSFET off)

2. **Low Voltage Test (12V)**
   - Power up controller only
   - Verify PWM signals with oscilloscope
   - Check MOSFET switching (should see clean on/off)

3. **Single Coil Test**
   - Energize ONE coil manually
   - Verify current draw (~1.2A at 12V)
   - Check for heating (should be minimal)

---

## Phase 4: Control Software

### Arduino/STM32 Code Structure

```cpp
// Pseudo-code outline
const int COIL_PINS[13] = {2,3,4,5,6,7,8,9,10,11,12,13,14};
const float GOLDEN_ANGLE = 137.5;
int currentPosition = 0;
unsigned long lastPulseTime = 0;

void setup() {
  // Initialize PWM pins
  // Initialize Hall sensors with interrupts
  // Set PWM frequency to match pulse timing
}

void loop() {
  // Read Hall sensors for position
  // Calculate which coil to fire based on Golden Ratio spacing
  // Fire coil with PWM pulse (0.615ms hold time)
  // Monitor RPM
  // Adjust pulse timing based on speed feedback
}

// Hall sensor interrupt
void hallSensorISR() {
  // Calculate RPM
  // Determine next coil to fire
  // Set firing flag
}
```

**Key Parameters to Tune:**
- Pulse width (start: 0.5ms, target: 0.615ms)
- Advance angle (fire slightly before magnet alignment)
- PWM duty cycle (start: 50%, adjust for current)

---

## Phase 5: Testing Protocol

### Test 1: Static Cogging Test (No Power)
1. Spin rotor by hand
2. Feel for smooth vs "cogging" rotation
3. Should feel quasi-smooth (not perfectly smooth due to magnets)
4. Verify no mechanical binding

### Test 2: Single Coil Pulse
1. Power supply at 12V, 2A current limit
2. Manually pulse ONE coil
3. Observe rotor reaction (should "kick" slightly)
4. Measure current draw
5. Check coil temperature after 1 minute

### Test 3: Sequential Firing (Low Speed)
1. Fire coils in sequence: 0, 1, 2... (following Golden Angle)
2. Start at 10 Hz pulse rate (very slow)
3. Observe direction of rotation
4. If wrong direction: reverse firing sequence
5. Gradually increase to 100 Hz

### Test 4: Resonance Hunting
1. Set constant pulse rate
2. Sweep frequency from 100 Hz to 800 Hz
3. Monitor RPM with tachometer or Hall sensors
4. Look for "sweet spot" where RPM jumps up
5. Target: 650 Hz should give ~3000 RPM

### Test 5: Clutch Integration
1. Install clutch on shaft
2. Connect to load (generator, dynamometer, or dummy load)
3. Spin up to engagement RPM (2400)
4. Observe clutch lock-in
5. Monitor system behavior:
   - Does it maintain speed?
   - Does it "purr" or chatter?
   - Does it oscillate in RPM band?

### Test 6: Load Testing
1. Apply varying electrical load to output
2. Monitor input power vs output power
3. Calculate efficiency
4. Record thermal behavior
5. Test for 30+ minutes continuous operation

---

## Phase 6: Tuning & Optimization

### Critical Adjustments

1. **Air Gap Tuning**
   - Optimal: 3-5mm between magnet and coil core
   - Closer = stronger coupling but more cogging
   - Farther = smoother but less torque

2. **Pulse Timing Advance**
   - Fire coil slightly BEFORE magnet aligns
   - Advance angle: 5-15° (tune experimentally)
   - Too early: wastes energy
   - Too late: braking effect

3. **Clutch Spring Tension**
   - Adjust engagement RPM
   - Target: 2400 RPM engage, 2250 RPM disengage
   - Test under load

4. **Q-Factor Measurement**
   - Pulse the system to speed
   - Cut power completely
   - Count rotations until stop
   - Target: >16 rotations (Q > 100)

---

## Safety Considerations

⚠️ **HIGH VOLTAGE** (48V DC)
- Can cause severe shock
- Use insulated tools
- Cover exposed terminals

⚠️ **HIGH SPEED ROTATION** (3000 RPM)
- Rotor failure = shrapnel
- Always use safety shield/enclosure
- Balance rotor before high-speed test
- Secure all fasteners with thread locker

⚠️ **STRONG MAGNETS**
- N52 magnets can pinch/crush fingers
- Keep away from electronics/credit cards
- Store with spacers between magnets

⚠️ **ELECTRICAL FIRE RISK**
- Short circuit = hundreds of amps
- Use appropriately rated fuses
- Have fire extinguisher nearby
- Monitor temperature during testing

---

## Success Criteria

✓ System achieves 3000 RPM with <200W input power
✓ Coils remain below 60°C during operation
✓ Audible "purr" at E5 (650 Hz) frequency
✓ Q-Factor >50 (coasts >8 rotations)
✓ Clutch engages/disengages smoothly in 150 RPM band
✓ System maintains stable speed under varying load

---

## Troubleshooting Guide

| Problem | Likely Cause | Solution |
|---------|-------------|----------|
| Won't start | Wrong firing sequence | Reverse order |
| Starts then stops | Back-EMF too high | Reduce air gap |
| Overheating coils | Inductance too high | Reduce turns |
| Erratic speed | Hall sensors misaligned | Reposition sensors |
| Clutch chatters | Hysteresis too narrow | Change springs |
| Low efficiency | Late firing | Increase advance angle |
| Resonance not found | Wrong frequency | Sweep wider range |

---

## Next Steps After Successful Prototype

1. **Characterization**
   - Full efficiency curve
   - Torque vs speed curve
   - Power input/output mapping

2. **Optimization**
   - PCB design for cleaner switching
   - Better coil former for exact inductance
   - Precision machined rotor

3. **Scale Testing**
   - Different magnet counts (8, 21, 34 - Fibonacci)
   - Different diameters
   - Different operating speeds

4. **Documentation**
   - Video demonstration
   - Oscilloscope captures
   - Thermal imaging
   - Acoustic spectrum analysis

---

**Let's build this thing.** 🔧⚡

