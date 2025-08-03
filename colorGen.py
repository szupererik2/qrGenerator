import random
import colorsys

def calculateGammaCorrection(c):
    # Apply gamma correction to a normalized color component.
    if c <= 0.03928:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4

def calculateLuminance(color):
    # Calculate the relative luminance of an RGB color.
    # Normalize RGB values to 0-1 range
    r, g, b = (color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)
    
    # Apply gamma correction
    r_corr = calculateGammaCorrection(r)
    g_corr = calculateGammaCorrection(g)
    b_corr = calculateGammaCorrection(b)
    
    # Calculate luminance using standard coefficients
    luminance = 0.2126 * r_corr + 0.7152 * g_corr + 0.0722 * b_corr
    return luminance

def calculateContrastRate(color1, color2):
    # Calculate contrast ratio between two RGB colors.
    l1 = calculateLuminance(color1)
    l2 = calculateLuminance(color2)
    # Ensure l1 is the lighter luminance
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)

def generateColor():
    # Generate a random RGB color.
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def adjustValueForContrast(h, s, v, base_lum, target_lum, min_contrast=4.6):
    # Adjust the value (brightness) of the HSV color to meet the minimum contrast ratio.
    # Returns adjusted RGB color.

    # Binary search for appropriate value 'v' in [0,1]
    low, high = 0.0, 1.0
    best_v = v
    
    for _ in range(20):  # 20 iterations for precision
        mid = (low + high) / 2
        r, g, b = colorsys.hsv_to_rgb(h, s, mid)
        rgb = (int(r * 255), int(g * 255), int(b * 255))
        lum = calculateLuminance(rgb)
        contrast = (max(base_lum, lum) + 0.05) / (min(base_lum, lum) + 0.05)
        
        if contrast >= min_contrast:
            best_v = mid
            if lum < base_lum:
                low = mid  # try brighter
            else:
                high = mid  # try darker
        else:
            if lum < base_lum:
                high = mid
            else:
                low = mid

    r, g, b = colorsys.hsv_to_rgb(h, s, best_v)
    return (int(r * 255), int(g * 255), int(b * 255))

def generateComplementer(color, min_contrast=4.6):
    # Generate a complementary color by rotating hue 180 degrees and adjusting brightness
    # to ensure minimum contrast ratio with the base color.

    # Convert RGB to HSV
    r_norm, g_norm, b_norm = (c / 255.0 for c in color)
    h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
    
    # Calculate luminance of the base color
    base_lum = calculateLuminance(color)
    
    # Complementary hue (180 degrees = 0.5 in normalized HSV hue)
    comp_h = (h + 0.5) % 1.0
    
    # Adjust the complementary color's value (brightness) to meet contrast requirement
    comp_rgb = adjustValueForContrast(comp_h, s, v, base_lum, None, min_contrast)
    return comp_rgb

def generateColors():
    primary = generateColor()
    complement = generateComplementer(primary)

    return {primary, complement}
