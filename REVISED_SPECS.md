# REVISED SPECIFICATIONS - RAID Motor v2.0
## Critical Design Changes Based on Engineering Review

### SUMMARY OF CHANGES

**What Changed:**
1. **Voltage:** 48V → 24V (safer, more practical)
2. **Coil Strategy:** High-resistance → Low-resistance + PWM current control
3. **MOSFETs:** 55V → 100V rated (inductive spike protection)
4. **Controller:** Arduino → Teensy 4.1 or ESP32 (faster timing)
5. **Added:** Single-pulse test bench protocol

---

## ELECTRICAL SPECIFICATIONS v2.0

### Power System
- **Bus Voltage:** 24V DC (safer than 48V, adequate torque)
- **Target Current:** 5A per coil
- **Peak Power:** 1560W (13 coils × 120W)
- **Average Power:** 94W (6% duty cycle)
- **Pulse Strategy:** PWM current chopping (not resistive limiting)

### Coil Design
**Cores:**
- Type: E 55/28/21 Ferrite (Material N87 or 3C90)
- Effective Area: 3.5-4.2 cm²
- Supplier: TDK/EPCOS via Digi-Key
- Part Number: B65801A0000R087 (or equivalent)

**Wire:**
- Gauge: AWG 24 (0.511mm diameter)
- Type: Heavy build enameled copper (MW-35-C, Class 200°C)
- Resistance: 84.2 mΩ/meter
- Turns: ~150 turns (practical winding)
- Wire length per coil: ~12 meters
- Target resistance per coil: ~1.0Ω

**Inductance:**
- Maximum: 1.926 mH (unchanged constraint)
- With 150 turns on E55 core: ~1.5-1.8 mH (within spec)

### Timing & Control
- **Pulse Period:** 1.54ms (650 Hz)
- **PWM Rise Time:** <0.4ms (to 90% current)
- **Hold Time:** 0.6ms (at target current)
- **Fall Time:** <0.4ms (field collapse)
- **L/R Time Constant:** 1.5-1.8ms (acceptable with PWM)

### Power Electronics

**MOSFETs:**
- Part: **IRFB4110PBF** or **IRF540N**
- Voltage Rating: 100V (inductive spike protection)
- Current Rating: 180A (massive headroom)
- Rds(on): 3.7mΩ (IRFB4110) - ultra-low loss
- Package: TO-220
- Quantity: 16 (13 + 3 spares)

**Diodes:**
- Part: **MUR460** (preferred) or **UF5408**
- Type: Ultra-Fast Recovery
- Rating: 600V, 4A continuous
- Recovery Time: <75ns
- Quantity: 16 (13 + 3 spares)

**Gate Drivers:**
- Part: **TC4427** or **MCP1416**
- Type: Dual high-speed MOSFET driver
- Output Current: 1.5A (fast gate charging)
- Quantity: 7 (covers 13 MOSFETs with 1 spare)

**Bus Capacitors:**
- Part: Panasonic FM Series or equivalent low-ESR
- Spec: 1000µF, 35V (2x safety margin)
- Configuration: 3x 1000µF in parallel
- ESR: <50mΩ
- Quantity: 3 units

### Microcontroller Options

**Option A: Teensy 4.1 (RECOMMENDED)**
- Processor: ARM Cortex-M7 @ 600MHz
- PWM Channels: 14 available (perfect for 13 coils)
- Timing Resolution: ~1.6ns
- Memory: 1MB RAM, 8MB Flash
- Advantages: Rock-solid timing, plenty of headroom
- Cost: $31

**Option B: ESP32 DevKitC**
- Processor: Dual-core Xtensa @ 240MHz
- PWM Channels: 16 (LEDC peripheral)
- Timing Resolution: ~25ns (adequate)
- Advantages: WiFi/Bluetooth monitoring, $8 cost
- Trade-off: Needs careful RTOS tuning

**Option C: STM32F446 Nucleo**
- Processor: ARM Cortex-M4 @ 180MHz
- PWM Channels: 17 timer outputs
- Advantages: Professional development ecosystem
- Cost: $25

**Decision: Start with ESP32 for Phase 1 (budget), plan Teensy for Phase 2 (performance)**

---

## UPDATED BILL OF MATERIALS

| Category | Item | Qty | Unit Cost | Total |
|----------|------|-----|-----------|-------|
| **Cores** | E55/28/21 Ferrite N87 | 15 | $6 | $90 |
| **Wire** | AWG 24 Magnet Wire (500m) | 1 | $35 | $35 |
| **MOSFETs** | IRFB4110PBF | 16 | $2.50 | $40 |
| **Diodes** | MUR460 | 16 | $1.20 | $20 |
| **Gate Drivers** | TC4427 | 7 | $2 | $14 |
| **Capacitors** | 1000µF 35V Low-ESR | 3 | $5 | $15 |
| **MCU** | ESP32 DevKitC | 1 | $8 | $8 |
| **Power Supply** | Mean Well LRS-200-24 | 1 | $30 | $30 |
| **Magnets** | N52 25x10x5mm | 15 | $3 | $45 |
| **Mechanical** | Aluminum, shaft, bearings | - | - | $100 |
| **Hardware** | Heat sinks, wire, terminals | - | - | $50 |
| **Clutch** | Centrifugal clutch | 1 | $100 | $100 |
| **TOTAL** | | | | **$547** |

**Savings from v1.0:** ~$100 (24V supply cheaper, simpler components)

---

## CRITICAL DESIGN IMPROVEMENTS

### 1. PWM Current Control Strategy

Instead of limiting current with resistance (wastes power as heat):

**Algorithm:**
```
Target Current: 5A
Measure actual current with shunt resistor (0.01Ω)
If current < 5A: PWM duty = 100%
If current > 5A: PWM duty = (5A / measured) × 100%
Update at 10kHz rate
```

**Benefits:**
- Coils stay cool (minimal I²R loss)
- Precise current control
- Adaptive to coil variations
- Faster response time

### 2. Current Sensing

**Add per Phase 1:**
- 0.01Ω shunt resistors (13x) - $10 total
- INA219 current sensor modules (2x 8-channel) - $15 total
- Real-time current monitoring and protection

### 3. Voltage Spike Protection

Why 100V MOSFETs are mandatory:

```
Inductive Kickback Voltage = L × (dI/dt)

Worst case:
L = 1.8mH
dI/dt = 5A / 0.0001s (fast shutdown) = 50,000 A/s
V_spike = 0.0018 × 50,000 = 90V

Plus 24V supply = 114V total!

55V MOSFET would explode.
100V MOSFET survives comfortably.
```

### 4. The Single-Pulse Test Bench

**BEFORE building the full motor, validate electronics:**

**Test Setup:**
1. Wind ONE coil (150 turns AWG 24 on E55 core)
2. Wire: 24V supply → Coil → MOSFET → Current sense → GND
3. Add flyback diode across coil
4. Connect ESP32 with oscilloscope

**Test Code (Arduino/ESP32):**
```cpp
const int COIL_PIN = 5;
const int PULSE_WIDTH_US = 600; // 0.6ms

void setup() {
  pinMode(COIL_PIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  Serial.println("Firing pulse...");
  digitalWrite(COIL_PIN, HIGH);
  delayMicroseconds(PULSE_WIDTH_US);
  digitalWrite(COIL_PIN, LOW);
  delay(2000); // Wait 2 seconds between pulses
}
```

**Success Criteria:**
- Place N52 magnet 2mm from core face
- Press button
- **Magnet should jump violently** (or launch if not secured)
- Oscilloscope shows clean rise/fall
- MOSFET stays cool (<40°C)
- Current peaks at ~5A

**Failure Modes:**
- Magnet doesn't move → coil wound wrong, check polarity
- MOSFET heats up → gate drive insufficient
- Slow rise time → inductance too high, reduce turns
- Current >10A → short circuit, check wiring

---

## PHASE 1 PROTOTYPE PLAN

### Week 1: Electronics Validation
**Budget: $100**
- Order: ESP32, 1x MOSFET, 1x diode, 1x gate driver, 1x E55 core, wire
- Build single-pulse test bench
- Validate timing with oscilloscope
- Tune PWM parameters

### Week 2: Coil Development
**Budget: $150**
- Wind 3 test coils with different turn counts
- Measure inductance (LCR meter)
- Measure resistance
- Test magnetic field strength (gaussmeter or phone app)
- Select optimal coil design

### Week 3: Mechanical Prototype
**Budget: $200**
- Order remaining components
- Machine rotor (aluminum plate)
- Mount 8 magnets (partial array for testing)
- Create test frame
- Install 3 coils (120° spacing for initial test)

### Week 4: Integration & Testing
**Budget: $100**
- Assemble full electronics (8 channels)
- Load control software
- Test sequential firing
- Hunt for resonance frequency
- Document results

**Phase 1 Target:** Achieve sustained rotation at 1000+ RPM with <100W input

---

## NEXT IMMEDIATE ACTION

I'm creating the **Single-Pulse Test Bench Schematic** and initial ESP32 code.

This lets you validate the core concept for <$50 before committing to the full build.

Stand by...
