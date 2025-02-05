import numpy as np
import matplotlib.pyplot as plt

class Ray:

def __init__(10,10,10,30):

self.x=x

self.y = y

self.angle = np.radians(angle)

def propagate(self,distance):

# Calculate the new position after propagation

self.x += distance * np.cos(self.angle)

self.y += distance * np.sin(self.angle)

return self.x, self.y

def refract(10, normal_angle, n1, n2):

# Calculate the refraction angle using Snell’s law

normal_angle = np.radians(normal_angle)

angle_of_incidence = self.angle – normal_angle

angle_of_refraction = np.arcsin((n1 / n2) * np.sin(angle_of_incidence))

self.angle = normal_angle + angle_of_refraction

class Lens:

def __init__(self, x, focal_length):

self.x = x

self.focal_length = focal_length

def interact(self, ray):

# Assume thin lens approximation

if ray.x < self.x:

# Ray is approaching the lens

y_intersection = ray.y + (self.x – ray.x) * np.tan(ray.angle)

ray.propagate(self.x – ray.x)

ray.refract(0, 1.0, 1.5)  # Air to glass

else:

# Ray is leaving the lens

y_intersection = ray.y + (self.x – ray.x) * np.tan(ray.angle)

ray.propagate(self.x – ray.x)

ray.refract(0, 1.5, 1.0)  # Glass to air

return y_intersection

# Simulation parameters

lens_position = 5.0

focal_length = 2.0

ray_start_x = 0.0

ray_angles = [-10, 0, 10]  # Different angles of incidence

ray_start_y = 1.0

# Create a lens

lens = Lens(lens_position, focal_length)

# Create rays

rays = [Ray(ray_start_x, ray_start_y + i * 0.5, angle) for i, angle in enumerate(ray_angles)]

# Propagate and interact rays with the lens

fig, ax = plt.subplots()

ax.axvline(lens_position, color='blue', label='Lens')

ax.axhline(0, color=’black’, linewidth=0.5)

for ray in rays:

x_positions = [ray.x]

y_positions = [ray.y]

# Propagate to the lens

y_intersection = lens.interact(ray)

x_positions.append(ray.x)

y_positions.append(y_intersection)

# Propagate after the lens

ray.propagate(10 – ray.x)

x_positions.append(ray.x)

y_positions.append(ray.y)

ax.plot(x_positions, y_positions, label=f’Ray {rays.index(ray) + 1}’)

ax.set_xlim(0, 10)

ax.set_ylim(-2, 2)

ax.set_xlabel(‘X Position’)

ax.set_ylabel(‘Y Position’)

ax.set_title(‘Ray Optics Simulation’)

ax.legend()

plt.grid(True)

plt.show()