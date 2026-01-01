# Single-Pulse Test Bench - Quick Start Guide

## What This Tests

Before building the full $500+ motor, this $40 test validates:
- ✓ Can we generate enough magnetic force?
- ✓ Is our timing control accurate?
- ✓ Do the MOSFETs switch fast enough?
- ✓ Is the coil inductance within spec?

**If this test fails, we save $450 by finding out now.**

---

## Parts Needed ($40 total)

### Essential
- [ ] **ESP32 DevKit** - $8 ([Amazon](https://amazon.com/s?k=esp32+devkit))
- [ ] **Ferrite E-Core** (E55 or E42) - $6 ([Mouser](https://mouser.com))
- [ ] **Magnet Wire AWG 24** (50m) - $8 ([Amazon](https://amazon.com/s?k=magnet+wire+24))
- [ ] **MOSFET IRFB4110** or IRF540N - $3 ([Digi-Key](https://digikey.com))
- [ ] **Diode MUR460** or UF5408 - $1.50
- [ ] **N52 Magnet** 25x10x5mm (1 piece) - $3
- [ ] **24V Power Supply** (2A min) - $10 ([Amazon](https://amazon.com/s?k=24v+2a+power))

### Optional (Highly Recommended)
- [ ] **0.01Ω Shunt Resistor** - $2 (for current measurement)
- [ ] **Heat sink TO-220** - $1
- [ ] **Breadboard + jumper wires** - $5

---

## Assembly Instructions

### Step 1: Wind the Coil (30 minutes)

**By Hand:**
1. Count 150 turns around the center leg of E-core
2. Keep wire taut and neat
3. Mark start/finish leads clearly
4. Measure resistance with multimeter: Target 1-2Ω

**With Drill (easier):**
1. Clamp E-core to bench
2. Chuck wire spool in hand drill
3. Guide wire while drill winds (low speed)
4. Count turns with tally counter or manual counting

**Test Coil:**
- Resistance should be 1-2Ω
- If you have an LCR meter, inductance should be <2mH

### Step 2: Wire the Circuit

```
24V+ ──┬─────── Coil (start) ───┬──── Coil (finish) ───┬──── MOSFET Drain
       │                        │                      │
       │                        └─ Diode Cathode      │
       │                           (black band)       │
       │                                              │
       └────────── Diode Anode ─────────────────────┘
       
MOSFET Source ──┬──── 0.01Ω Shunt ──── GND
                │
                └──── ESP32 GPIO 34 (for current sensing)

MOSFET Gate ────── ESP32 GPIO 5

ESP32 GND ──────── Power Supply GND
```

**Critical Connections:**
1. **Diode polarity matters!** Black band (cathode) goes to coil
2. **MOSFET orientation:** Drain (center pin) to coil, Source to GND
3. **Shunt resistor:** Use thick wire leads (carries 5A)

### Step 3: Upload the Code

1. Install Arduino IDE
2. Add ESP32 board support: [Instructions](https://randomnerdtutorials.com/installing-esp32-arduino-ide-2-0/)
3. Open `test_bench.ino`
4. Select board: "ESP32 Dev Module"
5. Select port (check Device Manager on Windows)
6. Click Upload

### Step 4: Safety Setup

⚠️ **BEFORE POWERING ON:**

1. **Eye Protection:** Magnet can launch at high speed
2. **Secure Magnet:** Tape or clamp 2-3mm from coil face
3. **Clear Area:** Remove metal objects within 30cm
4. **Fire Extinguisher:** Have one nearby (unlikely, but proper safety)
5. **Insulated Mat:** Place circuit on non-conductive surface

---

## Running the Test

1. **Power On**
   - Connect 24V supply last
   - ESP32 should boot (blue LED flashes)
   - Open Serial Monitor (115200 baud)

2. **First Pulse**
   - Press the BOOT button on ESP32
   - Should see "FIRING..." in serial monitor
   - **Magnet should jump or vibrate**

3. **Observe**
   - Serial output shows current measurement
   - Peak current should be 4-6A
   - MOSFET should stay cool

4. **Multiple Pulses**
   - Fire 10 pulses
   - Check MOSFET temperature (should be warm, not hot)
   - Watch for consistent magnet movement

---

## Success Criteria

### ✓ PASS (Ready for full build)
- Magnet jumps visibly on each pulse
- Peak current: 4-6A
- Pulse width: 0.55-0.65ms
- MOSFET temperature: <45°C after 10 pulses
- Consistent behavior across multiple pulses

### ⚠️ MARGINAL (Tune before proceeding)
- Magnet moves weakly → increase current or reduce gap
- Current 2-4A → acceptable but tune coil resistance
- Pulse width 0.7-0.9ms → reduce inductance slightly
- MOSFET warm (45-60°C) → add heat sink

### ✗ FAIL (Debug before continuing)

**Problem:** Magnet doesn't move at all
- **Check:** Coil polarity (swap wire ends and retry)
- **Check:** Power supply voltage (should read 24V)
- **Check:** MOSFET conducting (measure voltage drain-to-source when firing)

**Problem:** Current >10A
- **Check:** Short circuit in coil winding
- **Check:** Coil resistance <0.5Ω (too low, add turns)
- **ACTION:** Reduce voltage to 12V for testing

**Problem:** MOSFET overheats (>70°C)
- **Check:** Using logic-level MOSFET (IRF540N, IRFB4110)
- **Check:** Gate voltage reaches 3.3V (measure with meter)
- **ACTION:** Add gate driver IC (TC4427)

**Problem:** Pulse width >1.5ms
- **Check:** Inductance >2mH (measure with LCR meter)
- **ACTION:** Reduce coil turns to 100 and retest

---

## Data to Record

Create a test log:

```
Test Bench Results - [Date]
===============================
Coil Specs:
  - Turns: ___
  - Wire: AWG ___
  - Resistance: ___ Ω
  - Inductance: ___ mH (if measured)

Test Results:
  - Peak Current: ___ A
  - Avg Current: ___ A
  - Pulse Width: ___ ms
  - MOSFET Temp: ___ °C
  - Magnet Gap: ___ mm
  - Magnet Movement: [Strong/Weak/None]

Power:
  - Voltage: ___ V
  - Energy per Pulse: ___ mJ

Pass/Fail: ________
Notes: _________________
```

---

## Next Steps After Success

Once test bench passes:

1. **Order Remaining Parts** - Full parts list in `PARTS_LIST.md`
2. **Wind 12 More Coils** - Use same parameters as test coil
3. **Design Mechanical Layout** - Fibonacci spacing at 137.5°
4. **Build Frame** - Non-resonant aluminum structure
5. **Assemble Phase 2** - 3-coil test with rotating magnet

---

## Troubleshooting Video Guides

Search YouTube for:
- "How to wind a coil on ferrite core"
- "MOSFET testing with Arduino"
- "Measuring inductance without LCR meter"

---

## Cost Breakdown

| Item | Cost | Where to Save |
|------|------|---------------|
| ESP32 | $8 | Use Arduino Nano ($4) |
| Ferrite core | $6 | Salvage from old transformer |
| Wire | $8 | Buy 1kg spool ($25) for full project |
| MOSFET | $3 | Must buy new (safety critical) |
| Magnet | $3 | Buy 10-pack ($20 total) |
| Power supply | $10 | Use laptop charger (19V works) |
| **TOTAL** | **$38** | **Budget: $25-30** |

---

## When to Abort

Stop and reassess if:
- Smoke/burning smell (disconnect immediately)
- MOSFET melts/explodes (wrong part or wiring error)
- ESP32 won't boot after connecting circuit (check for short)
- Magnet launches >1 meter (reduce voltage or increase gap)

**Remember:** This is a $40 test. If it fails, we learned something valuable without risking the full build.

---

**GO/NO-GO Decision Point:**

If this test bench works reliably, you have validated:
1. ✓ Magnetic force generation
2. ✓ Electronic timing
3. ✓ Component selection
4. ✓ Your ability to wind coils

**You are cleared to proceed to full prototype.**

If it doesn't work after troubleshooting, we revisit the design before spending more.

---

Ready to order parts?
