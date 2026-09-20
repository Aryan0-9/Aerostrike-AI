import math

# --- STEP 1: TRACKING DATA LIST ---
# The exact coordinates your Day 3 tracker generated

# Combined and cleaned: No duplicate frames allowed!

# Insert this clean flight path into Step 1 of your kinematics script
# The true frame-by-frame progression (Duplicates removed)
# The isolated, real ball tracking data from your console log
pixel_data = [
    (899, 858), 
    (919, 856), 
    (935, 855), 
    (965, 834), 
    (992, 847), 
    (1037, 832), 
    (1026, 828), 
    (1049, 841), 
    (1069, 837), 
    (1089, 835)
]
# --- STEP 2: PHYSICS CONSTANTS ---
FPS = 30
TIME_STEP = 1.0 / FPS      # 0.0333 seconds per frame
METERS_PER_PIXEL = 0.010722

print("=== DAY 4: KINEMATICS ANALYSIS REPORT ===")
print("Analyzing data points...")
print("")

# Extract our very first tracked position (Index 0)
x0_pixel = pixel_data[0][0]
y0_pixel = pixel_data[0][1]

# Extract our last tracked position (Index -1)
xN_pixel = pixel_data[-1][0]
yN_pixel = pixel_data[-1][1]

# --- STEP 3: CALCULATE DISPLACEMENTS ---
delta_x_pixels = xN_pixel - x0_pixel
# Screen Y goes down, so we invert this to get a positive upward displacement
delta_y_pixels = y0_pixel - yN_pixel 

# Convert pixel changes into real-world meters
displacement_x = delta_x_pixels * METERS_PER_PIXEL
displacement_y = delta_y_pixels * METERS_PER_PIXEL
total_time = (len(pixel_data) - 1) * TIME_STEP

print("Horizontal Displacement (Dx): " + str(round(displacement_x, 2)) + " meters")
print("Vertical Displacement (Dy): " + str(round(displacement_y, 2)) + " meters")
print("Total Flight Duration: " + str(round(total_time, 3)) + " seconds")
print("")

# --- STEP 4: CALCULATE TRUE INITIAL VELOCITY COMPONENTS ---
# Horizontal speed remains mostly constant (ignoring minor air resistance)
velocity_x = displacement_x / total_time

# Vertical speed accounts for gravity pulling it down during flight
GRAVITY = 9.80665   # acceleration in m/s^2
velocity_y0 = (displacement_y + (0.5 * GRAVITY * (total_time ** 2))) / total_time

# --- STEP 5: VECTOR RESOLUTION ---
# Calculate total initial speed using the true initial vertical component
total_velocity = math.sqrt((velocity_x ** 2) + (velocity_y0 ** 2))

# Convert meters per second to kilometers per hour
velocity_kmh = total_velocity * 3.6

# Calculate true launch angle using initial velocity components
launch_angle_radians = math.atan2(velocity_y0, velocity_x)
launch_angle_degrees = math.degrees(launch_angle_radians)

print("--- TRUE INITIAL RESULTANT VECTORS (WITH GRAVITY) ---")
print("Horizontal Velocity (Vx): " + str(round(velocity_x, 2)) + " m/s")
print("Initial Vertical Velocity (Vy0): " + str(round(velocity_y0, 2)) + " m/s")
print("TRUE INITIAL LAUNCH VELOCITY: " + str(round(total_velocity, 2)) + " m/s (" + str(round(velocity_kmh, 1)) + " km/h)")
print("LAUNCH ANGLE: " + str(round(launch_angle_degrees, 1)) + " degrees above horizontal")
print("=========================================")