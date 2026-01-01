/*
 * RAID MOTOR - Single Pulse Test Bench
 * Phase 1: Electronics Validation
 * 
 * Hardware:
 * - ESP32 DevKit or Arduino
 * - 1x E55 Ferrite Core with ~150 turns AWG 24 wire
 * - 1x IRFB4110 or IRF540N MOSFET
 * - 1x MUR460 or UF5408 diode
 * - 24V power supply
 * - 0.01 ohm current sense resistor
 * - 1x N52 magnet (25x10x5mm)
 * 
 * Test: Press button → Coil fires 0.6ms pulse → Magnet jumps
 */

// Pin Definitions
const int COIL_PIN = 5;          // PWM output to MOSFET gate
const int BUTTON_PIN = 0;        // Boot button on ESP32 (or external button)
const int CURRENT_SENSE_PIN = 34; // ADC pin for current measurement

// Timing Constants (microseconds)
const int PULSE_WIDTH_US = 600;   // 0.6ms hold time
const int PULSE_DELAY_MS = 2000;  // 2 seconds between pulses

// Current Sensing
const float SHUNT_RESISTANCE = 0.01;  // 0.01 ohm
const float ADC_VOLTAGE_REF = 3.3;    // ESP32 ADC reference
const int ADC_RESOLUTION = 4095;      // 12-bit ADC

// Statistics
unsigned long pulseCount = 0;
float maxCurrent = 0.0;
float avgCurrent = 0.0;

void setup() {
  Serial.begin(115200);
  delay(1000);
  
  pinMode(COIL_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(CURRENT_SENSE_PIN, INPUT);
  
  digitalWrite(COIL_PIN, LOW); // Ensure MOSFET starts OFF
  
  Serial.println("\n===========================================");
  Serial.println("RAID Motor - Single Pulse Test Bench v1.0");
  Serial.println("===========================================\n");
  Serial.println("Press BOOT button to fire pulse");
  Serial.println("Place magnet 2-5mm from coil core\n");
  
  Serial.println("Configuration:");
  Serial.printf("  Pulse Width: %d µs (%.2f ms)\n", PULSE_WIDTH_US, PULSE_WIDTH_US / 1000.0);
  Serial.printf("  Pulse Delay: %d ms\n", PULSE_DELAY_MS);
  Serial.printf("  Shunt Resistance: %.3f Ω\n", SHUNT_RESISTANCE);
  Serial.println("===========================================\n");
}

void loop() {
  // Wait for button press
  if (digitalRead(BUTTON_PIN) == LOW) {
    delay(50); // Debounce
    if (digitalRead(BUTTON_PIN) == LOW) {
      firePulse();
      
      // Wait for button release
      while (digitalRead(BUTTON_PIN) == LOW) {
        delay(10);
      }
      
      delay(PULSE_DELAY_MS);
    }
  }
}

void firePulse() {
  pulseCount++;
  
  Serial.println("----------------------------------------");
  Serial.printf("Pulse #%lu - FIRING...\n", pulseCount);
  Serial.println("----------------------------------------");
  
  unsigned long startTime = micros();
  float peakCurrent = 0.0;
  float currentSum = 0.0;
  int sampleCount = 0;
  
  // Fire the pulse and sample current during hold time
  digitalWrite(COIL_PIN, HIGH);
  
  // Sample current during pulse
  unsigned long pulseStart = micros();
  while (micros() - pulseStart < PULSE_WIDTH_US) {
    float current = readCurrent();
    if (current > peakCurrent) {
      peakCurrent = current;
    }
    currentSum += current;
    sampleCount++;
    delayMicroseconds(10); // Sample every 10µs
  }
  
  digitalWrite(COIL_PIN, LOW);
  unsigned long endTime = micros();
  
  // Calculate statistics
  float actualPulseWidth = (endTime - startTime) / 1000.0; // ms
  float averageCurrent = (sampleCount > 0) ? currentSum / sampleCount : 0.0;
  
  // Update global stats
  if (peakCurrent > maxCurrent) {
    maxCurrent = peakCurrent;
  }
  avgCurrent = ((avgCurrent * (pulseCount - 1)) + averageCurrent) / pulseCount;
  
  // Report results
  Serial.println("\nResults:");
  Serial.printf("  Actual Pulse Width: %.3f ms\n", actualPulseWidth);
  Serial.printf("  Peak Current:       %.2f A\n", peakCurrent);
  Serial.printf("  Average Current:    %.2f A\n", averageCurrent);
  Serial.printf("  Samples Taken:      %d\n", sampleCount);
  
  // Energy calculation
  float energy_mJ = 24.0 * averageCurrent * (actualPulseWidth / 1000.0) * 1000.0;
  Serial.printf("  Energy per Pulse:   %.2f mJ\n", energy_mJ);
  
  // Global statistics
  Serial.println("\nSession Statistics:");
  Serial.printf("  Total Pulses:       %lu\n", pulseCount);
  Serial.printf("  Max Current Ever:   %.2f A\n", maxCurrent);
  Serial.printf("  Avg Current (all):  %.2f A\n", avgCurrent);
  
  // Safety warnings
  if (peakCurrent > 8.0) {
    Serial.println("\n⚠️  WARNING: Current >8A detected!");
    Serial.println("   Check for short circuit or wrong coil resistance");
  }
  if (peakCurrent < 2.0) {
    Serial.println("\n⚠️  WARNING: Current <2A detected!");
    Serial.println("   Check connections or increase voltage");
  }
  if (actualPulseWidth > PULSE_WIDTH_US * 1.2 / 1000.0) {
    Serial.println("\n⚠️  WARNING: Pulse width longer than expected!");
    Serial.println("   Check for slow MOSFET switching");
  }
  
  Serial.println("========================================\n");
}

float readCurrent() {
  // Read voltage across shunt resistor
  int adcValue = analogRead(CURRENT_SENSE_PIN);
  float voltage = (adcValue / (float)ADC_RESOLUTION) * ADC_VOLTAGE_REF;
  
  // Calculate current using Ohm's law: I = V / R
  float current = voltage / SHUNT_RESISTANCE;
  
  return current;
}

/*
 * EXPECTED RESULTS:
 * 
 * Good Test:
 * - Peak Current: 4-6A
 * - Magnet jumps visibly (or launches if unsecured)
 * - MOSFET stays cool (<40°C after 10 pulses)
 * - Clean pulse width ~0.6ms
 * 
 * Bad Test Scenarios:
 * 
 * 1. Magnet doesn't move:
 *    - Wrong coil polarity (swap wire ends)
 *    - Not enough turns (add more windings)
 *    - Magnet too far (move closer to 2mm)
 * 
 * 2. MOSFET overheats:
 *    - Gate drive insufficient (need gate driver IC)
 *    - Wrong MOSFET type (use logic-level)
 *    - No heat sink installed
 * 
 * 3. Current >10A:
 *    - Short circuit in coil
 *    - Coil resistance too low (<0.5 ohm)
 *    - Check wiring
 * 
 * 4. Current <2A:
 *    - Poor connections (check crimps)
 *    - Coil resistance too high (>5 ohm)
 *    - Power supply current limited
 * 
 * 5. Pulse width >1ms:
 *    - Inductance too high (reduce turns)
 *    - MOSFET switching slowly (need driver)
 *    - L/R time constant exceeded spec
 */
