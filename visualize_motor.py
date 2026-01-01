"""
Golden Ratio Motor Visualization
Demonstrates the "chasing" spiral concept with magnetic field interactions
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import matplotlib.patches as mpatches

# Golden Ratio
PHI = (1 + np.sqrt(5)) / 2
GOLDEN_ANGLE = 137.5  # degrees

def fibonacci_spiral(n_points=100, rotations=3, scale=1.0):
    """Generate points along a Fibonacci/Golden spiral"""
    theta = np.linspace(0, rotations * 2 * np.pi, n_points)
    r = scale * np.exp(theta / (2 * np.pi / np.log(PHI)))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y, theta, r

def create_static_visualization():
    """Create static visualization of the dual spiral system"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle('Golden Ratio Motor Concept', fontsize=16, fontweight='bold')
    
    # 1. Dual Spiral Configuration (Rotor vs Stator)
    ax1 = axes[0, 0]
    x1, y1, theta1, r1 = fibonacci_spiral(n_points=200, rotations=2.5, scale=1.0)
    x2, y2, theta2, r2 = fibonacci_spiral(n_points=200, rotations=2.5, scale=1.05)
    
    ax1.plot(x1, y1, 'b-', linewidth=2, label='Rotor Spiral', alpha=0.7)
    ax1.plot(x2, y2, 'r-', linewidth=2, label='Stator Spiral', alpha=0.7)
    
    # Add magnet positions using Fibonacci spacing
    n_magnets = 13  # Fibonacci number
    magnet_angles = np.array([i * GOLDEN_ANGLE for i in range(n_magnets)]) * np.pi / 180
    magnet_radius = 5.0
    
    for i, angle in enumerate(magnet_angles):
        x_mag = magnet_radius * np.cos(angle)
        y_mag = magnet_radius * np.sin(angle)
        circle = Circle((x_mag, y_mag), 0.3, color='blue' if i % 2 == 0 else 'red', 
                       alpha=0.8, edgecolor='black', linewidth=2)
        ax1.add_patch(circle)
    
    ax1.set_xlim(-10, 10)
    ax1.set_ylim(-10, 10)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_title('Dual Spiral Configuration\n(Rotor + Stator with Fibonacci Magnet Spacing)')
    
    # 2. Variable Gap Analysis
    ax2 = axes[0, 1]
    gap = np.abs(r2 - r1)
    angles_deg = theta1 * 180 / np.pi
    
    ax2.plot(angles_deg, gap, 'g-', linewidth=2)
    ax2.fill_between(angles_deg, gap, alpha=0.3, color='green')
    ax2.set_xlabel('Rotation Angle (degrees)')
    ax2.set_ylabel('Gap Distance (arbitrary units)')
    ax2.set_title('Variable Reluctance Gap\n(The "Chasing" Effect)')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=np.mean(gap), color='r', linestyle='--', label=f'Mean Gap: {np.mean(gap):.2f}')
    ax2.legend()
    
    # 3. Fibonacci Magnet Positions (Top View)
    ax3 = axes[1, 0]
    circle = Circle((0, 0), magnet_radius, fill=False, edgecolor='black', 
                   linewidth=2, linestyle='--', label='Rotor Circle')
    ax3.add_patch(circle)
    
    for i, angle in enumerate(magnet_angles):
        x_mag = magnet_radius * np.cos(angle)
        y_mag = magnet_radius * np.sin(angle)
        
        # Magnet
        mag_circle = Circle((x_mag, y_mag), 0.4, 
                           color='red' if i % 2 == 0 else 'blue',
                           alpha=0.7, edgecolor='black', linewidth=2)
        ax3.add_patch(mag_circle)
        
        # Label
        ax3.text(x_mag, y_mag, str(i), ha='center', va='center', 
                fontsize=8, fontweight='bold', color='white')
        
        # Direction line
        ax3.plot([0, x_mag], [0, y_mag], 'k-', alpha=0.2, linewidth=0.5)
    
    ax3.set_xlim(-8, 8)
    ax3.set_ylim(-8, 8)
    ax3.set_aspect('equal')
    ax3.grid(True, alpha=0.3)
    ax3.set_title(f'Fibonacci Magnet Array\n({n_magnets} magnets at {GOLDEN_ANGLE}° spacing)')
    ax3.legend()
    
    # 4. Flux Pulse Pattern (Simulated)
    ax4 = axes[1, 1]
    time = np.linspace(0, 4, 1000)
    
    # Simulate the "breathing" pulse pattern
    # Using a combination of rotation and clutch engagement
    rpm = 3000
    frequency = rpm / 60  # Hz
    clutch_freq = frequency / n_magnets
    
    # Create pulse train
    rotation_phase = 2 * np.pi * frequency * time
    flux_pulse = np.zeros_like(time)
    
    for i in range(n_magnets):
        pulse_time = i / clutch_freq
        pulse_width = 0.1 / clutch_freq
        mask = np.abs(time % (1/clutch_freq) - pulse_time % (1/clutch_freq)) < pulse_width
        flux_pulse += mask * np.exp(-((time % (1/clutch_freq) - pulse_time % (1/clutch_freq))**2) / (2 * (pulse_width/3)**2))
    
    # Add smooth baseline
    baseline = 0.3 + 0.1 * np.sin(rotation_phase)
    flux_output = baseline + flux_pulse
    
    ax4.plot(time, flux_output, 'purple', linewidth=2, label='Flux Output')
    ax4.fill_between(time, flux_output, alpha=0.3, color='purple')
    ax4.set_xlabel('Time (seconds)')
    ax4.set_ylabel('Magnetic Flux Intensity')
    ax4.set_title(f'Predicted Flux Output Pattern\n("Breathing" at {int(clutch_freq)} Hz)')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    plt.tight_layout()
    return fig

def create_animation():
    """Create animated visualization of the rotating system"""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    
    # Static stator spiral
    x_stator, y_stator, _, _ = fibonacci_spiral(n_points=200, rotations=2.5, scale=1.05)
    stator_line, = ax.plot(x_stator, y_stator, 'r-', linewidth=2, 
                           label='Stator (Fixed)', alpha=0.5)
    
    # Rotor spiral (will rotate)
    x_rotor, y_rotor, _, _ = fibonacci_spiral(n_points=200, rotations=2.5, scale=1.0)
    rotor_line, = ax.plot([], [], 'b-', linewidth=2, label='Rotor (Rotating)', alpha=0.7)
    
    # Magnets
    n_magnets = 13
    magnet_angles = np.array([i * GOLDEN_ANGLE for i in range(n_magnets)]) * np.pi / 180
    magnet_radius = 5.0
    magnet_patches = []
    
    for i in range(n_magnets):
        circle = Circle((0, 0), 0.4, color='blue' if i % 2 == 0 else 'red',
                       alpha=0.8, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        magnet_patches.append(circle)
    
    # Flux lines (will update)
    flux_lines = []
    for i in range(5):
        line, = ax.plot([], [], 'g-', linewidth=1, alpha=0.3)
        flux_lines.append(line)
    
    title = ax.text(0.5, 1.05, '', transform=ax.transAxes, 
                   ha='center', fontsize=14, fontweight='bold')
    
    ax.legend(loc='upper right')
    
    def init():
        rotor_line.set_data([], [])
        for line in flux_lines:
            line.set_data([], [])
        return [rotor_line] + flux_lines + magnet_patches
    
    def animate(frame):
        # Rotation angle
        angle = frame * 2 * np.pi / 60  # Complete rotation every 60 frames
        
        # Rotate rotor spiral
        cos_a, sin_a = np.cos(angle), np.sin(angle)
        x_rot = x_rotor * cos_a - y_rotor * sin_a
        y_rot = x_rotor * sin_a + y_rotor * cos_a
        rotor_line.set_data(x_rot, y_rot)
        
        # Update magnet positions
        for i, circle in enumerate(magnet_patches):
            mag_angle = magnet_angles[i] + angle
            x_mag = magnet_radius * np.cos(mag_angle)
            y_mag = magnet_radius * np.sin(mag_angle)
            circle.center = (x_mag, y_mag)
        
        # Update flux lines (emanating from magnets)
        for i, line in enumerate(flux_lines):
            if i < len(magnet_patches):
                mag_angle = magnet_angles[i] + angle
                x_start = magnet_radius * np.cos(mag_angle)
                y_start = magnet_radius * np.sin(mag_angle)
                x_end = (magnet_radius + 2) * np.cos(mag_angle)
                y_end = (magnet_radius + 2) * np.sin(mag_angle)
                line.set_data([x_start, x_end], [y_start, y_end])
        
        # Update title with RPM
        rpm = (frame % 60) / 60 * 3000
        title.set_text(f'Golden Ratio Motor Rotation\nSimulated RPM: {int(rpm)}')
        
        return [rotor_line, title] + flux_lines + magnet_patches
    
    anim = FuncAnimation(fig, animate, init_func=init, frames=240, 
                        interval=50, blit=True, repeat=True)
    
    return fig, anim

def print_specifications():
    """Print calculated specifications"""
    print("=" * 60)
    print("GOLDEN RATIO MOTOR - CALCULATED SPECIFICATIONS")
    print("=" * 60)
    print(f"\nGeometric Constants:")
    print(f"  φ (Phi):              {PHI:.6f}")
    print(f"  Golden Angle:         {GOLDEN_ANGLE}°")
    print(f"  Radians:              {GOLDEN_ANGLE * np.pi / 180:.6f}")
    
    print(f"\nMagnet Configuration:")
    n_magnets = 13
    print(f"  Number of magnets:    {n_magnets} (Fibonacci number)")
    print(f"  Angular spacing:      {GOLDEN_ANGLE}°")
    print(f"  Turns per cycle:      {360 / GOLDEN_ANGLE:.2f}")
    
    print(f"\nResonance Calculations (at 3000 RPM):")
    rpm = 3000
    freq = rpm / 60
    print(f"  Rotation frequency:   {freq:.1f} Hz")
    print(f"  Pulse frequency:      {freq * n_magnets:.1f} Hz")
    print(f"  Period per pulse:     {1000 / (freq * n_magnets):.2f} ms")
    
    print(f"\nQ-Factor Estimation:")
    print(f"  Target Q-factor:      > 100 (High-Q oscillator)")
    print(f"  Decay time (est):     {100 / (2 * np.pi * freq):.3f} seconds")
    
    print(f"\nClutch Engagement:")
    engagement_rpm = rpm * 0.8
    print(f"  Engage at:            {engagement_rpm:.0f} RPM ({engagement_rpm/60:.1f} Hz)")
    print(f"  Disengage at:         {rpm * 0.75:.0f} RPM")
    print(f"  Operating band:       {rpm * 0.05:.0f} RPM")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    print_specifications()
    
    # Create static visualization
    print("\nGenerating static visualization...")
    fig_static = create_static_visualization()
    
    # Ask user for animation
    print("\nStatic visualization complete.")
    show_animation = input("Generate animation? (y/n): ").lower().strip()
    
    if show_animation == 'y':
        print("Generating animation...")
        fig_anim, anim = create_animation()
        print("Animation ready. Close the windows when done.")
    
    plt.show()
    
    print("\nVisualization complete!")
