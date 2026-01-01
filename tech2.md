This is the "Green Light" moment. The math has converged, the constraints are defined, and the physics is valid. We are moving from **Research** to **Procurement**.

Here is the **Bill of Materials (BOM)** to build the Alpha Prototype of the "Phi-Harmonic" Drive.

### 1. The Magnetic Cores (The Heart)

*Target: 4cm² Cross-section, Low Hysteresis at 650Hz.*
We need a standard geometry that is easy to wind. **E-Cores** are the industry standard here.

* **Part:** **Ferrite Core E 55/28/21** (Material N87 or 3C90)
* **Supplier:** TDK / EPCOS / Ferroxcube (via DigiKey/Mouser)
* **Why:** The E55 core has an effective cross-section () of ~3.5–4.2 cm² (depending on manufacturer), perfectly matching your 4cm² target. Material N87 is optimized for power frequencies and will run cool at 650Hz.
* **Quantity:** 13 (Buy 15 for spares).



### 2. The Wire (The Veins)

*Target: ~9.6Ω Resistance, ~300 Turns.*
The user analysis flagged a critical mismatch: getting high resistance with low inductance.

* **Part:** **22 AWG Magnet Wire (Heavy Build Enameled Copper)**
* **Spec:** NEMA MW-35-C (Class 200°C rating).
* **Why:** 22 AWG has a resistance of ~53 mΩ/meter. To get 9.6Ω, you need ~180 meters. **Correction:** This contradicts your constraint. If you use 25m of wire, you only get ~1.3Ω.
* **Critical Adjustment:** To hit 9.6Ω with 25m of wire, you would need insanely thin wire (like 34 AWG), which creates heat and melts.
* **Better Approach:** **Keep the resistance LOW (1-2Ω) and use a Current Limiting Driver (PWM chopping).**
* *However, adhering to your strict request for 9.6Ω:* You need **26 AWG** wire (133 mΩ/m). ~72 meters of 26 AWG = ~9.6Ω.
* **Recommendation:** Buy **24 AWG**. It’s a safer middle ground. 25m = ~2.1Ω. *We will handle the current limiting in software/MOSFETs, or else your resistive losses (Heat) will be massive.*



### 3. The Switching Stage (The Muscles)

*Target: 48V Bus, fast switching, logic control.*
*Warning: A 48V battery can spike to 60V+ during regenerative braking/pulses. A 55V MOSFET (IRFZ44N) is operating in the "Danger Zone."*

* **Part:** **IRF540N (or IRFB4110 for high efficiency)**
* **Spec:** 100V N-Channel MOSFET.
* **Why:** The 100V rating gives you "headroom" for the inductive kickback spikes. The IRFB4110 has incredibly low resistance (), meaning it won't get hot.
* **Quantity:** 13.


* **Gate Driver:** **TC4427 or similar**
* **Why:** You cannot drive these big MOSFETs directly from an Arduino/ESP32 at the microsecond precision you need. The Gate Driver acts as an amplifier to snap the MOSFET open/closed instantly (preserving your 0.201ms time constant).



### 4. Protection (The Immune System)

*Target: Handle 3kW back-EMF spikes.*

* **Part:** **MUR460 or UF5408**
* **Spec:** Ultra-Fast Recovery Diode (600V, 4A continuous, high surge).
* **Why:** "Standard" diodes are too slow. By the time they turn on to catch the spike, your MOSFET is already dead. The "Ultra-Fast" designation is mandatory.


* **Capacitor Bank:** **Panasonic FM Series (Low ESR)**
* **Spec:** 1000µF, 63V (x3 per driver group).
* **Why:** When you pulse 3kW, you can't pull that from the battery instantly (wire inductance). These local capacitors act as "buckets" right next to the coils to dump energy instantly.



### 5. The Brain (The Conductor)

*Target: Microsecond timing, 13 independent outputs.*

* **Part:** **Teensy 4.0 or 4.1**
* **Spec:** ARM Cortex-M7 at 600MHz.
* **Why:** An Arduino Uno runs at 16MHz. It is too slow to calculate the floating-point Golden Ratio math *and* fire pulses with <10µs jitter. The Teensy is a supercomputer by comparison and will handle the 1.54ms windows easily.



---

### Phase 1 Assembly: The "Static Test"

Before you build the spinning rotor, I recommend the **"Single Pulse Test."**

**The Setup:**

1. Wind **one** E-Core with your wire.
2. Connect it to your MOSFET + Diode + Capacitor + Teensy.
3. Place a permanent magnet 1mm away from the core face.

**The Test Code:**
Write a script to fire a **single 1.5ms pulse**.

* **Success Criteria:** The magnet should jump violently (or launch across the room—wear safety glasses).
* **Failure Criteria:** The MOSFET gets hot, or the pulse "ramps" too slowly (monitored via oscilloscope).

**Would you like the wiring diagram for this specific "Single Pulse" test bench?**