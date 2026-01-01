# Parts List - Resonant Aperiodic Impulse Drive

## Shopping List with Links

### Magnets
- [ ] **Neodymium N52 Magnets** (13 qty)
  - Size: 25mm x 10mm x 5mm
  - [K&J Magnetics BX084](https://www.kjmagnetics.com/)
  - Amazon: Search "N52 25mm x 10mm x 5mm block magnets"
  - **Cost: $39**

### Magnetic Cores
- [ ] **Ferrite E-Cores or Toroids** (13 qty)
  - Mouser #: B64290L0618X830 (TDK)
  - Alternative: Ferroxcube E25/13/7
  - [Mouser Electronics](https://www.mouser.com/)
  - **Cost: $65**

### Wire
- [ ] **Magnet Wire AWG 22** (500m spool)
  - Remington Industries
  - [Amazon](https://www.amazon.com/s?k=magnet+wire+awg+22)
  - **Cost: $40**

### Mechanical
- [ ] **Centrifugal Clutch** (1 qty)
  - Hilliard Extreme Duty or Max-Torque
  - 3/4" bore, adjustable springs
  - [Go Kart supply stores](https://www.gopowersports.com/)
  - **Cost: $80-150**

- [ ] **Aluminum Plate** (250mm x 6mm)
  - 6061-T6 aluminum
  - McMaster-Carr or local metal supplier
  - **Cost: $20**

- [ ] **Steel Shaft** (3/4" x 6", hardened)
  - McMaster-Carr
  - **Cost: $15**

- [ ] **Ball Bearings** 6204-2RS (2 qty)
  - [Amazon](https://www.amazon.com/s?k=6204-2RS+bearing)
  - **Cost: $15**

- [ ] **Aluminum Extrusion** (for frame)
  - 80/20 Inc or Misumi
  - Approx 3 meters total
  - **Cost: $100**

### Electronics - Power

- [ ] **48V Power Supply**
  - Mean Well LRS-350-48
  - Digi-Key #: 1866-3313-ND
  - [Digi-Key Link](https://www.digikey.com/en/products/detail/mean-well-usa-inc/LRS-350-48/7705009)
  - **Cost: $47**

- [ ] **Electrolytic Capacitors** 470µF 63V (5 qty)
  - Panasonic EEU-FR1J471
  - Digi-Key or Mouser
  - **Cost: $15**

- [ ] **Ceramic Capacitors** 0.1µF 50V (15 qty)
  - Any general purpose
  - **Cost: $3**

### Electronics - Semiconductors

- [ ] **N-Channel MOSFETs** IRFZ44N (16 qty)
  - Digi-Key #: IRFZ44NPBF-ND
  - [Digi-Key Link](https://www.digikey.com/en/products/detail/infineon-technologies/IRFZ44NPBF/811747)
  - **Cost: $25**

- [ ] **Fast Diodes** UF5408 (16 qty)
  - Digi-Key #: UF5408-E3/54GICT-ND
  - [Digi-Key Link](https://www.digikey.com/en/products/detail/vishay-semiconductor-diodes-division/UF5408-E3-54/1532191)
  - **Cost: $10**

- [ ] **MOSFET Drivers** MCP1416 (13 qty) OR ULN2803 (2 qty)
  - Digi-Key: MCP1416T-E/OT
  - Alternative: ULN2803A (cheaper, slower)
  - **Cost: $20**

### Electronics - MCU & Sensors

- [ ] **Microcontroller**
  - Option A: Arduino Due [Amazon](https://www.amazon.com/Arduino-Due/dp/B00A6C3JN2)
  - Option B: STM32 Nucleo-F446RE [Digi-Key](https://www.digikey.com/)
  - Option C: ESP32 DevKit [Amazon](https://www.amazon.com/s?k=esp32+devkit)
  - **Cost: $25-40**

- [ ] **Hall Effect Sensors** A3144 (3 qty)
  - Digi-Key #: 620-1432-ND
  - [Digi-Key Link](https://www.digikey.com/en/products/detail/allegro-microsystems/A3144ELHLX-T/1885059)
  - **Cost: $5**

- [ ] **5V Buck Converter**
  - LM2596 module
  - [Amazon](https://www.amazon.com/s?k=lm2596+buck+converter)
  - **Cost: $8**

### Hardware

- [ ] **TO-220 Heat Sinks** (13 qty)
  - [Amazon](https://www.amazon.com/s?k=TO-220+heatsink)
  - **Cost: $10**

- [ ] **M4 Bolts & Nuts** (assorted)
  - **Cost: $10**

- [ ] **Terminal Blocks**
  - Phoenix Contact or similar
  - **Cost: $10**

- [ ] **Hookup Wire** 18 AWG (red/black)
  - **Cost: $15**

- [ ] **Shaft Collars** 3/4" (2 qty)
  - McMaster-Carr
  - **Cost: $8**

### Tools (if not owned)

- [ ] **LCR Meter** (for measuring inductance)
  - [Amazon: DE-5000](https://www.amazon.com/s?k=de-5000+lcr+meter)
  - **Cost: $80** (one-time investment)

- [ ] **Digital Tachometer**
  - [Amazon](https://www.amazon.com/s?k=laser+tachometer)
  - **Cost: $25**

- [ ] **Bench Power Supply** (variable, 0-50V, 5A)
  - Tekpower or similar
  - **Cost: $60-100** (if not owned)

---

## Total Budget Breakdown

| Category | Low | High |
|----------|-----|------|
| Magnets & Cores | $104 | $104 |
| Mechanical Parts | $150 | $200 |
| Power Electronics | $100 | $120 |
| Control Electronics | $60 | $80 |
| Hardware/Misc | $50 | $70 |
| **TOTAL (without tools)** | **$464** | **$574** |
| Tools (if needed) | +$165 | +$205 |
| **TOTAL (with tools)** | **$629** | **$779** |

---

## Phased Purchase Plan

### Phase 1: Electronics Testing ($150)
Start with electronics to verify control before mechanical build:
- Microcontroller
- 1x MOSFET, diode, driver
- Breadboard & components
- 12V power supply (cheaper for testing)
- 1x ferrite core + wire

**Test:** Verify PWM control and coil driving circuit

### Phase 2: Mechanical Prototype ($200)
Once electronics validated:
- Aluminum stock
- Shaft & bearings  
- 3-5 magnets (partial array for testing)
- Basic frame materials

**Test:** Verify mechanical assembly and balance

### Phase 3: Full System ($250)
Complete the build:
- Remaining magnets (10 more)
- All coils and cores (12 more)
- All MOSFETs/drivers (12 more)
- 48V power supply
- Clutch assembly

**Test:** Full system integration

---

## Alternative Budget Options

### Ultra-Budget Version (~$200)
- 8 magnets instead of 13 (still Fibonacci)
- ESP32 ($8 instead of Arduino Due $40)
- ULN2803 drivers (cheaper than individual)
- 3D printed frame instead of aluminum
- Smaller magnets
- 24V system instead of 48V

### Performance Version (~$1200)
- Precision machined aluminum rotor
- Custom PCB with integrated drivers
- Higher grade ferrite cores
- Industrial clutch with precise engagement
- Professional power supply with monitoring
- Quality bearings and shaft

---

## Vendor Quick Reference

| Vendor | Good For | Shipping |
|--------|----------|----------|
| **Digi-Key** | Electronics | Fast, reliable |
| **Mouser** | Electronics, cores | Fast |
| **McMaster-Carr** | Mechanical parts | Next-day possible |
| **Amazon** | General parts, magnets | 2-day with Prime |
| **K&J Magnetics** | Quality magnets | Standard |
| **AliExpress** | Budget electronics | Slow (2-4 weeks) |
| **80/20 Inc** | Aluminum extrusion | Standard |

---

## Print This Checklist

```
SHOPPING LIST - RESONANT APERIODIC IMPULSE DRIVE
------------------------------------------------
Electronics:
☐ Arduino Due/STM32/ESP32
☐ 16x IRFZ44N MOSFETs
☐ 16x UF5408 Diodes  
☐ MOSFET Drivers (13x or 2x ULN2803)
☐ 3x Hall Sensors A3144
☐ Mean Well LRS-350-48 PSU
☐ 5x 470µF 63V Capacitors
☐ Terminal blocks, wire, heat sinks

Magnets & Cores:
☐ 13x N52 25x10x5mm Magnets
☐ 13x Ferrite Cores
☐ 500m AWG 22 Magnet Wire

Mechanical:
☐ 250mm x 6mm Aluminum Plate
☐ 3/4" x 6" Steel Shaft
☐ 2x 6204-2RS Bearings
☐ Aluminum Extrusion (frame)
☐ Centrifugal Clutch 3/4"
☐ Shaft Collars, Hardware

Tools (if needed):
☐ LCR Meter
☐ Tachometer
☐ Bench Power Supply
```

Save this file and check off items as purchased!
