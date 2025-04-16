# Concrete Block Material Calculator
# This script calculates the materials required for different types of concrete blocks based on their dimensions and strength grade.
# Define default block dimensions for each block type (in mm)
def get_block_dimensions(block_type):
    defaults = {
        "Splitface Block": (400, 200, 200),
        "Bullnose Block": (390, 190, 190),
        "Partition Block": (400, 150, 200),
        "Fly Ash Block": (400, 200, 200),
        "Aerated Autoclaved Block": (600, 200, 250),
        "Paving Block": (200, 100, 80),
        "Cellular Lightweight Block": (600, 200, 200),
        "Expanded Block": (400, 200, 200),
        "Solid Concrete Block": (400, 200, 200),
        "Hollow Concrete Block": (400, 200, 200),
        "Stretcher Block": (390, 190, 190),
        "Pillar Block": (390, 190, 190),
        "Lintel Block": (400, 200, 150),
        "Jamb Block": (400, 200, 200),
        "Column Block": (400, 200, 200),
        "Corner Block": (400, 200, 200)
    }
    return defaults.get(block_type, (400, 200, 200))

BLOCK_VOLUME_FACTORS = {
    "Splitface Block": 0.85,
    "Bullnose Block": 0.85,
    "Partition Block": 0.75,
    "Fly Ash Block": 0.95,
    "Aerated Autoclaved Block": 0.7,
    "Paving Block": 0.9,
    "Cellular Lightweight Block": 0.65,
    "Expanded Block": 0.7,
    "Solid Concrete Block": 1.0,
    "Hollow Concrete Block": 0.6,
    "Stretcher Block": 0.65,
    "Pillar Block": 0.9,
    "Lintel Block": 0.8,
    "Jamb Block": 0.75,
    "Column Block": 0.6,
    "Corner Block": 0.8,
}

# Concrete mix design per strength grade (MPa)
MIX_RATIOS = {
    10: (1, 3, 6, 250),
    15: (1, 2, 4, 280),
    20: (1, 1.5, 3, 320),
    25: (1, 1, 2, 360),
    30: (1, 0.75, 1.5, 380),
    35: (1, 0.5, 1, 400),
}

def get_mix_ratio(strength_m):
    """Return mix ratio and cement per m³ based on grade."""
    if strength_m in MIX_RATIOS:
        return MIX_RATIOS[strength_m]
    else:
        # Default to M25 if unknown
        return (1, 1, 2, 360)

def calculate_materials(block_type, length_mm, width_mm, height_mm, strength_m, formwork_thickness):
    """Calculate material quantities for a specific block type."""
    length = length_mm / 1000
    width = width_mm / 1000
    height = height_mm / 1000
    gross_volume = length * width * height

    volume_factor = BLOCK_VOLUME_FACTORS.get(block_type, 1.0)
    net_volume = gross_volume * volume_factor

    c, s, a, cement_per_m3 = get_mix_ratio(strength_m)
    total_parts = c + s + a

    cement = round((c / total_parts) * cement_per_m3 * net_volume, 2)
    sand = round((s / total_parts) * cement_per_m3 * net_volume, 2)
    aggregate = round((a / total_parts) * cement_per_m3 * net_volume, 2)
    water = round(0.5 * cement, 2)

    return cement, sand, aggregate, water, net_volume

def calculate_formwork(length_mm, width_mm, height_mm, formwork_thickness):
    """Calculate formwork dimensions with buffer."""
    
    return length_mm + formwork_thickness , width_mm + formwork_thickness , height_mm + formwork_thickness

def generate_report(block_type, length, width, height, strength_m):
    cement, sand, aggregate, water, net_volume = calculate_materials(block_type, length, width, height, strength_m)
    f_length, f_width, f_height = calculate_formwork(length, width, height)

    report = f"""
    <b>Block Type:</b> {block_type}<br>
    <b>Block Dimensions:</b> {length} mm x {width} mm x {height} mm<br>
    <b>Strength Grade:</b> M{strength_m}<br><br>

    <b>Net Concrete Volume:</b> {round(net_volume * 1e6, 2)} cm³<br><br>

    <b>Materials Required:</b><br>
    - Cement: {cement} kg<br>
    - Sand: {sand} kg<br>
    - Aggregate: {aggregate} kg<br>
    - Water: {water} liters<br><br>

    <b>Recommended Formwork Dimensions:</b><br>
    {f_length} mm x {f_width} mm x {f_height} mm
    """
    return report
