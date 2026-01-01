"""
Golden Ratio Magnet Positioning Template Generator
Creates printable PDF template for precise φ-spaced magnet placement
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Rectangle
from matplotlib.backends.backend_pdf import PdfPages

# Constants
PHI = (1 + np.sqrt(5)) / 2
GOLDEN_ANGLE = 137.5  # degrees

def create_rotor_template(rotor_diameter_mm=250, magnet_radius_mm=85, n_magnets=13, 
                          magnet_size=(25, 10), output_file="rotor_template.pdf"):
    """
    Generate printable template for precise magnet positioning
    
    Parameters:
    -----------
    rotor_diameter_mm : float
        Diameter of rotor disc in mm
    magnet_radius_mm : float
        Radius from center where magnets are placed
    n_magnets : int
        Number of magnets (should be Fibonacci number)
    magnet_size : tuple
        (length, width) of magnets in mm
    output_file : str
        Output PDF filename
    """
    
    # Convert to inches for printing (1 inch = 25.4 mm)
    scale = 25.4  # mm per inch
    rotor_diameter_in = rotor_diameter_mm / scale
    magnet_radius_in = magnet_radius_mm / scale
    magnet_length_in = magnet_size[0] / scale
    magnet_width_in = magnet_size[1] / scale
    
    # Create figure (8.5x11 inch paper)
    fig = plt.figure(figsize=(8.5, 11))
    ax = fig.add_subplot(111, aspect='equal')
    
    # Title and instructions
    fig.text(0.5, 0.98, 'Golden Ratio Motor - Rotor Magnet Positioning Template', 
             ha='center', va='top', fontsize=16, fontweight='bold')
    
    instructions = [
        "INSTRUCTIONS:",
        f"1. Print this page at 100% scale (NO SCALING)",
        f"2. Cut out the circle template",
        f"3. Tape to center of {rotor_diameter_mm}mm aluminum disc",
        f"4. Use center cross-hair for precise alignment",
        f"5. Place magnets in marked rectangles",
        f"6. Check polarity: N-S-N-S alternating",
        f"7. Glue with epoxy (JB Weld recommended)",
        "",
        f"SPECIFICATIONS:",
        f"- Rotor Diameter: {rotor_diameter_mm}mm",
        f"- Magnet Circle Radius: {magnet_radius_mm}mm",
        f"- Number of Magnets: {n_magnets}",
        f"- Magnet Size: {magnet_size[0]}mm × {magnet_size[1]}mm",
        f"- Angular Spacing: {GOLDEN_ANGLE}° (Golden Angle)",
        f"- Pattern: Fibonacci spiral (φ = {PHI:.6f})",
    ]
    
    y_pos = 0.92
    for line in instructions:
        fig.text(0.1, y_pos, line, ha='left', va='top', fontsize=9, family='monospace')
        y_pos -= 0.018
    
    # Center the rotor template
    ax.set_xlim(-rotor_diameter_in/2 - 0.5, rotor_diameter_in/2 + 0.5)
    ax.set_ylim(-rotor_diameter_in/2 - 0.5, rotor_diameter_in/2 + 0.5)
    
    # Draw rotor outline
    rotor_circle = Circle((0, 0), rotor_diameter_in/2, fill=False, 
                         edgecolor='black', linewidth=2)
    ax.add_patch(rotor_circle)
    
    # Draw center cross-hair
    ax.plot([-0.3, 0.3], [0, 0], 'k-', linewidth=1)
    ax.plot([0, 0], [-0.3, 0.3], 'k-', linewidth=1)
    ax.plot(0, 0, 'ko', markersize=8)
    
    # Draw magnet positions
    magnet_angles = []
    for i in range(n_magnets):
        angle_deg = i * GOLDEN_ANGLE
        angle_rad = np.radians(angle_deg)
        magnet_angles.append(angle_deg % 360)
        
        # Calculate magnet center position
        x_center = magnet_radius_in * np.cos(angle_rad)
        y_center = magnet_radius_in * np.sin(angle_rad)
        
        # Draw magnet outline (rectangle rotated to point toward center)
        magnet_rect = Rectangle(
            (x_center - magnet_width_in/2, y_center - magnet_length_in/2),
            magnet_width_in, magnet_length_in,
            angle=angle_deg,
            fill=True,
            facecolor='lightblue' if i % 2 == 0 else 'lightcoral',
            edgecolor='black',
            linewidth=1.5,
            alpha=0.7
        )
        ax.add_patch(magnet_rect)
        
        # Label magnet number and polarity
        label_radius = magnet_radius_in + 0.4
        label_x = label_radius * np.cos(angle_rad)
        label_y = label_radius * np.sin(angle_rad)
        
        polarity = 'N' if i % 2 == 0 else 'S'
        label_text = f'{i}\n{polarity}'
        ax.text(label_x, label_y, label_text, 
               ha='center', va='center', 
               fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Draw radial line to help alignment
        ax.plot([0, x_center * 0.7], [0, y_center * 0.7], 
               'k--', linewidth=0.5, alpha=0.3)
    
    # Draw magnet circle
    magnet_circle = Circle((0, 0), magnet_radius_in, fill=False,
                          edgecolor='blue', linewidth=1, linestyle='--')
    ax.add_patch(magnet_circle)
    
    # Add legend
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, fc='lightblue', ec='black', label='North Pole (N)'),
        plt.Rectangle((0, 0), 1, 1, fc='lightcoral', ec='black', label='South Pole (S)')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9)
    
    ax.axis('off')
    
    # Create angle reference table
    fig.text(0.1, 0.15, 'ANGLE VERIFICATION TABLE:', fontsize=10, fontweight='bold')
    fig.text(0.1, 0.13, 'Use protractor to verify these angles from 0° reference (magnet 0):', fontsize=8)
    
    # Print angle table in columns
    y_pos = 0.11
    for i in range(0, n_magnets, 3):
        line = ""
        for j in range(3):
            if i + j < n_magnets:
                angle = magnet_angles[i + j]
                polarity = 'N' if (i + j) % 2 == 0 else 'S'
                line += f"Mag {i+j:2d} ({polarity}): {angle:6.1f}°    "
        fig.text(0.1, y_pos, line, fontsize=8, family='monospace')
        y_pos -= 0.015
    
    # Add scale verification box
    scale_box_y = 0.04
    fig.text(0.1, scale_box_y, 'SCALE VERIFICATION:', fontsize=10, fontweight='bold')
    fig.text(0.1, scale_box_y - 0.02, 
            'Measure this line with a ruler. It should be EXACTLY 100mm (3.937 inches).', 
            fontsize=8)
    
    # Draw 100mm verification line
    line_y = scale_box_y - 0.04
    line_length = 100 / scale  # 100mm in inches
    fig.plot([0.1, 0.1 + line_length], [line_y, line_y], 'k-', linewidth=2)
    fig.plot([0.1, 0.1], [line_y - 0.005, line_y + 0.005], 'k-', linewidth=2)
    fig.plot([0.1 + line_length, 0.1 + line_length], 
            [line_y - 0.005, line_y + 0.005], 'k-', linewidth=2)
    fig.text(0.1 + line_length/2, line_y - 0.015, '100mm / 3.937"', 
            ha='center', fontsize=9, fontweight='bold')
    
    # Save as PDF
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Template saved as: {output_file}")
    print(f"\n✓ Print at 100% scale (NO SCALING)")
    print(f"✓ Verify scale using the 100mm reference line")
    print(f"✓ Magnet positions are marked with alternating N/S poles")
    print(f"✓ Angular spacing: {GOLDEN_ANGLE}° (Golden Angle φ)")
    
    plt.show()
    
    return magnet_angles

if __name__ == "__main__":
    print("=" * 60)
    print("GOLDEN RATIO MOTOR - ROTOR TEMPLATE GENERATOR")
    print("=" * 60)
    print(f"\nGolden Ratio (φ): {PHI:.6f}")
    print(f"Golden Angle: {GOLDEN_ANGLE}°")
    print("\nGenerating template...")
    
    angles = create_rotor_template(
        rotor_diameter_mm=250,   # Rotor disc diameter
        magnet_radius_mm=85,     # Distance from center to magnets
        n_magnets=13,            # Fibonacci number
        magnet_size=(25, 10),    # 25mm x 10mm magnets
        output_file="rotor_positioning_template.pdf"
    )
    
    print("\nAngular Verification:")
    print("-" * 60)
    for i, angle in enumerate(angles):
        polarity = 'N' if i % 2 == 0 else 'S'
        print(f"Magnet {i:2d} ({polarity}): {angle:7.2f}°")
    
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("1. Print rotor_positioning_template.pdf at 100% scale")
    print("2. Verify scale using 100mm reference line")
    print("3. Cut out circular template")
    print("4. Tape to aluminum rotor disc (align center marks)")
    print("5. Place magnets in marked positions")
    print("6. Verify polarity (N-S-N-S alternating)")
    print("7. Glue magnets with epoxy")
    print("8. Let cure 24 hours before use")
    print("=" * 60)
