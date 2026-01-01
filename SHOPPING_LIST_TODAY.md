# PHASE 0 SHOPPING LIST - Order Today

## Total: $38-45 (depending on shipping)

---

## PRIORITY 1: Order These NOW

### Electronics (from Amazon - arrives in 2 days with Prime)

**ESP32 Development Board**
- Search: "ESP32-WROOM-32 DevKit"
- Price: $8-10 for 1
- Link: https://www.amazon.com/s?k=esp32+devkit+v1
- **Buy:** 1 unit (or 2 if you want a backup)

**24V Power Supply (2A minimum)**
- Search: "24V 2A DC power adapter"
- Price: $10-12
- Link: https://www.amazon.com/s?k=24v+2a+power+supply
- **Buy:** 1 unit
- Note: Must have barrel jack or screw terminals

**N52 Neodymium Magnet**
- Search: "N52 25mm x 10mm x 5mm block magnet"
- Price: $3 each or $20 for 10-pack
- Link: https://www.amazon.com/s?k=N52+25x10x5mm+magnet
- **Buy:** 10-pack (you'll need them for full build)
- **⚠️ DANGER:** N52 magnets are BRITTLE (ceramic/glass). They will shatter if they snap together from distance. SLIDE them apart, never pull. Can pinch/break fingers!

**Magnet Wire AWG 24**
- Search: "magnet wire 24 AWG enameled copper"
- Price: $8 for 100ft
- Link: https://www.amazon.com/s?k=magnet+wire+24+awg
- **Buy:** 1 spool (100ft minimum)

**Breadboard Jumper Wire Kit**
- Search: "breadboard jumper wire kit"
- Price: $6
- Link: https://

**Kapton Tape or Electrical Tape**
- Search: "kapton tape polyimide" or "electrical tape"
- Price: $5-8 for Kapton, $3 for electrical
- Link: https://www.amazon.com/s?k=kapton+tape
- **Buy:** 1 roll
- **PURPOSE:** Insulate ferrite core before winding (prevents wire scraping/shorting on sharp edges)www.amazon.com/s?k=breadboard+jumper+wire
- **Buy:** 1 kit

---

### Electronics (from Digi-Key - order together, $5 shipping)

**Go to:** https://www.digikey.com

**MOSFET - IRFB4110PBF**
- Part #: IRFB4110PBF-ND
- Direct Link: https://www.digikey.com/en/products/detail/infineon-technologies/IRFB4110PBF/2127466
- Price: $2.43
- **Qty:** 2 (1 for test, 1 spare)

**Diode - MUR460**
- Part #: MUR460-E3/54GICT-ND
- Direct Link: https://www.digikey.com/en/products/detail/vishay-semiconductor-diodes-division/MUR460-E3-54/1532232
- Price: $1.23
- **Qty:** 2

**Ferrite E-Core (E55/28/21)**
- Search: "E55 ferrite core N87" on Digi-Key
- Alternative: B65801A0000R087 (EPCOS)
- Price: $5-7
- **Qty:** 2 (E-cores often sold as HALVES - need 2 for one complete core!)
- **⚠️ CRITICAL:** Check if listed as "set" or "single half"
- **BONUS:** Add bobbin if available (E55 coil former) - $1, makes winding 100x easier

**Optional: 0.01Ω Shunt Resistor**
- Part #: WSLP3921L0100FEA
- Price: $2.50
- **Qty:** 1

**Digi-Key Subtotal:** ~$15-18 + $5 shipping

---

## PRIORITY 2: Already Have or Can Wait

### If You Have These - Great!
- [ ] Multimeter (essential for testing)
- [ ] Wire strippers
- [ ] Soldering iron (can breadboard without for Phase 0)
- [ ] USB cable for ESP32 (micro-USB or USB-C depending on model)

### Nice to Have (Order Later)
- [ ] Heat sink for TO-220 package - $1
- [ ] Oscilloscope or logic analyzer (for pulse measurement)
- [ ] LCR meter (for inductance measurement)
- [ ] Small clamp or vise (for holding core while winding)

---

## ALTERNATIVE: Ultra-Budget Option ($25)

If money is tight right now:

**Replace Ferrite Core with Salvage**
- Old computer power supply transformer
- Microwave transformer (dangerous - use only outer core)
- CRT TV flyback transformer core
- **Savings: $6**

**Use Arduino Nano Instead of ESP32**
- Price: $4-5 on Amazon
- Slower but adequate for Phase 0
- **Savings: $3-4**

**Single Magnet Instead of 10-pack**
- Price: $3
- **Savings: $17**

**Ultra-Budget Total: ~$23-28**

---

## ORDERING STRATEGY

### Plan A: Fast (Recommended)
1. **Today:** Order everything from Amazon (arrives Thursday)
2. **Today:** Order Digi-Key parts (arrives Friday/Monday)
3. **Weekend:** Wind coil, setup breadboard while waiting
4. **Next Week:** Assemble and test

### Plan B: Cheap
1. **Today:** Order only ESP32 and magnets from Amazon
2. **This Week:** Salvage ferrite core from old electronics
3. **Next Week:** Order MOSFETs/diodes from eBay/AliExpress (slow but $0.50 each)
4. **In 3-4 weeks:** Assemble and test

---

## SHOPPING CART CHECKLIST

Print this and check off as you order:

```
AMAZON CART:
☐ ESP32 DevKit (x1 or x2)
☐ 24V 2A Power Supply
☐ N52 Magnets 25x10x5mm (x10)
☐ Magnet Wire AWG 24 (100ft min)
☐ Jumper Wire Kit
☐ [Optional] Breadboard
☐ [Optional] Heat sinks TO-220

DIGI-KEY CART:
☐ IRFB4110PBF MOSFET (x2)
☐ MUR460 Diode (x2)
☐ E55 Ferrite Core N87 (x1)
☐ 0.01Ω Shunt Resistor (x1)

TOTAL: $____
```

---

## WHILE YOU WAIT FOR PARTS

### Download Software (20 minutes)

1. **Install Arduino IDE 2.x**
   - Go to: https://www.arduino.cc/en/software
   - Download and install

2. **Add ESP32 Board Support**
   - Open Arduino IDE
   - Go to File → Preferences
   - Add to "Additional Board Manager URLs":
     ```
     https://espressif.github.io/arduino-esp32/package_esp32_index.json
     ```
   - Go to Tools → Board → Boards Manager
   - Search "ESP32"
   - Install "esp32 by Espressif Systems"

3. **Test Upload (without hardware)**
   - Open `test_bench.ino`
   - Click "Verify" (checkmark button)
   - Should compile without errors

### Study the Guides

- [ ] Read `TEST_BENCH_GUIDE.md` completely
- [ ] Watch YouTube: "How to wind a transformer coil"
- [ ] Watch YouTube: "ESP32 getting started"
- [ ] Review `test_bench.ino` code comments

### Prep Your Workspace

- [ ] Clear a 2ft x 2ft workspace
- [ ] Gather tools: wire strippers, multimeter, tape
- [ ] Set up non-conductive work surface (wood or plastic mat)
- [ ] Organize small containers for screws/parts

---

## PARTS ARRIVAL CHECKLIST

When parts arrive, verify you have everything:

```
ELECTRONICS:
☐ ESP32 powers on when plugged into USB
☐ 24V supply outputs correct voltage (measure with meter)
☐ MOSFET has 3 pins, no visible damage
☐ Diode has stripe on one end (cathode marking)
☐ Wire spool is enameled copper (shiny coating)
☐ Magnets are STRONG (careful with fingers!)

CORE:
☐ Ferrite core has two halves (E + I shape)
☐ Center post is where you'll wind wire
☐ No cracks or chips visible
```

---

## DAY 1 WHEN PARTS ARRIVE

### Morning (2 hours): Wind the Coil

1. Follow TEST_BENCH_GUIDE.md coil winding section
2. Wind 150 turns on center post of E-core
3. Keep wire tight and neat
4. Mark start/end with tape/labels
5. Measure resistance: target 1-2Ω

### Afternoon (1 hour): Breadboard Assembly

1. Follow wiring diagram in TEST_BENCH_GUIDE.md
2. Double-check all connections
3. MOSFET pins: Gate, Drain, Source (check datasheet!)
4. Diode stripe (cathode) goes to coil
5. Do NOT connect 24V yet

### Evening (30 minutes): Software Upload

1. Connect ESP32 via USB
2. Open Arduino IDE
3. Select Board: "ESP32 Dev Module"
4. Select Port: (check Device Manager)
5. Upload test_bench.ino
6. Open Serial Monitor (115200 baud)
7. Should see startup message

---

## DAY 2: FIRST TEST

### Pre-Flight Checklist

- [ ] All connections verified
- [ ] MOSFET has heat sink (optional but recommended)
- [ ] Magnet secured 2-3mm from core face
- [ ] Safety glasses on
- [ ] Serial monitor open
- [ ] Fire extinguisher within reach (just in case)

### The Moment of Truth

1. Connect 24V power supply (last connection)
2. Press BOOT button on ESP32
3. Watch serial monitor
4. **LOOK AT THE MAGNET**

**Expected Result:**
- Serial shows "FIRING..."
- Current reading: 4-6A
- **MAGNET JUMPS OR VIBRATES**
- MOSFET stays cool

**If nothing happens:** See troubleshooting in TEST_BENCH_GUIDE.md

---

## AFTER SUCCESSFUL TEST

Post your results:
1. Take a video of magnet jumping
2. Screenshot of serial output
3. Share on GitHub repo (create an issue)
4. Decision point: Proceed to full build or iterate

---

## EMERGENCY CONTACTS

If you get stuck:

1. **GitHub Issues:** Post on the repo
2. **Reddit:** r/electronics, r/AskElectronics
3. **Discord:** Arduino/ESP32 communities
4. **YouTube:** Search specific error messages

---

## BUDGET TRACKING

```
Item                    Budgeted    Actual    Status
========================================================
ESP32                   $8          $___      [ ]
Power Supply            $10         $___      [ ]
Magnets (10pk)          $20         $___      [ ]
Magnet Wire             $8          $___      [ ]
Jumpers                 $6          $___      [ ]
MOSFET (x2)             $5          $___      [ ]
Diode (x2)              $3          $___      [ ]
Ferrite Core            $6          $___      [ ]
Shipping                $5          $___      [ ]
========================================================
TOTAL                   $71         $___      [ ]

Target: <$45 if you already have jumpers/wire
```

---

## TIMELINE

```
Day 0 (Today):     Order parts ✓
Day 1-2:           Study guides, setup software
Day 3-5:           Parts arrive (Amazon)
Day 5-7:           Parts arrive (Digi-Key)
Day 7:             Wind coil, breadboard circuit
Day 8:             First test - MAKE MAGNET JUMP
Day 9-10:          Iterate/tune
Day 11:            Document results
Day 12:            DECISION: Full build or pivot
```

---

**GO/NO-GO: Are you ordering today?**

If yes, start with Amazon cart (fastest shipping).
If you want to wait, that's fine - but the parts won't age. :)

**The hardest part is clicking "checkout."**

Let me know when orders are placed and I'll help with assembly when parts arrive!
