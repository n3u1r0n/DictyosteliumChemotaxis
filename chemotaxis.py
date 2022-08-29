import imageio
import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import numpy as np
import os
import scipy.sparse
import scipy.sparse.linalg
from time import time

from tex import *
from parameters import *

# do a simulation for given parameters
def simulation(animation_name, N, size, dx, dt, alpha, beta, t_a, t_r, gamma, gamma_pacemaker, tau, movement_random, movement_distance, movement_threshold, T, pacemakers, distribution, time_steps_per_frame, dpi):
  global C, particle_locations, particle_states, pacemaker_locations, pacemaker_states
  gridsize = int(size / dx)

  # setup for the solver of the implicit euler step
  up =     - np.ones(gridsize * gridsize - gridsize)   * dt * alpha / (dx ** 2)      # cell up
  left =   - np.ones(gridsize * gridsize - 1)          * dt * alpha / (dx ** 2)      # cell to the left
  center =   np.ones(gridsize * gridsize) * (4 * alpha / (dx ** 2) + beta) * dt + 1  # main
  right =  - np.ones(gridsize * gridsize - 1)          * dt * alpha / (dx ** 2)      # cell to the right
  down =   - np.ones(gridsize * gridsize - gridsize)   * dt * alpha / (dx ** 2)      # cell down
  left[::gridsize] = 0
  right[-1::-gridsize] = 0
  A = scipy.sparse.diags([up, left, center, right, down], [-gridsize, -1, 0, 1, gridsize], format='csc')
  solver = scipy.sparse.linalg.factorized(A)

  # setup concentration and particles
  C = np.zeros((gridsize, gridsize))
  particle_locations = distribution
  particle_states = np.zeros(N)

  # setup pacemakers
  pacemaker_locations = np.array([pacemaker[:2] for pacemaker in pacemakers])
  pacemaker_states = np.array([pacemaker[2] for pacemaker in pacemakers])

  # do one time step
  def do_time_step():
    global C, particle_locations, particle_states, pacemaker_locations, pacemaker_states

    # get cell indices the particles and the pacemaker particles are in
    particle_indices = np.clip(np.round(particle_locations / dx).astype(int), 0, gridsize - 1)
    pacemaker_indices = np.clip(np.round(pacemaker_locations / dx).astype(int), 0, gridsize - 1)

    C_emitted = np.zeros((gridsize, gridsize))

    # calculate the gradient and the gradient norm of the concentration
    gradient_direction = np.zeros((gridsize, gridsize, 2))
    gradient_direction[1:-1, 1:-1, 0] = (C[2:, 1:-1] - C[:-2, 1:-1]) / (2 * dx)
    gradient_direction[1:-1, 1:-1, 1] = (C[1:-1, 2:] - C[1:-1, :-2]) / (2 * dx)
    gradient_norm = np.sqrt(gradient_direction[:, :, 0] ** 2 + gradient_direction[:, :, 1] ** 2)
    gradient_norm[gradient_norm == 0] = 1
    gradient_direction[:,:,0] = gradient_direction[:,:,0] / gradient_norm
    gradient_direction[:,:,1] = gradient_direction[:,:,1] / gradient_norm
    particle_gradient_norm = gradient_norm[(particle_indices.T[0], particle_indices.T[1])]
    particle_gradient_direction = gradient_direction[(particle_indices.T[0], particle_indices.T[1])]

    # get the particles of given states
    active_particles = particle_states > 0
    recovering_particles = particle_states < 0
    inactive_particles = particle_states == 0
    activating_particles = inactive_particles * (C[particle_indices.T[0], particle_indices.T[1]] > tau)
    moving_particles = activating_particles * (particle_gradient_norm > movement_threshold)

    # activate and move particles which are above the threshold
    particle_states[activating_particles] = t_a
    particle_locations[moving_particles] += movement_distance * particle_gradient_direction[moving_particles]

    # update and emit from active particles
    particle_states[active_particles] -= dt
    particle_states[active_particles * (particle_states <= 0)] = -t_r
    C_emitted[particle_indices[active_particles].T[0], particle_indices[active_particles].T[1]] += gamma * dt
    
    # update recovering particles
    particle_states[recovering_particles] += dt
    particle_states[recovering_particles * (particle_states > 0)] = 0

    # get the pacemaker particles of given states
    active_pacemakers = pacemaker_states >= 0
    recovering_pacemakers = pacemaker_states < 0

    # update and emit from active pacemaker particles
    pacemaker_states[active_pacemakers] -= dt
    pacemaker_states[active_pacemakers * (pacemaker_states < 0)] = -t_r
    C_emitted[pacemaker_indices[active_pacemakers].T[0], pacemaker_indices[active_pacemakers].T[1]] += gamma_pacemaker * dt

    # update recovering pacemaker particles
    pacemaker_states[recovering_pacemakers] += dt
    pacemaker_states[recovering_pacemakers * (pacemaker_states >= 0)] = t_a

    # move particles randomly
    particle_locations += (np.random.rand(N, 2) * 2 - 1) * movement_random * np.sqrt(dt)

    # update C with emitted C alpha and diffuse
    C += C_emitted
    C = solver(C.flatten()).reshape(gridsize, gridsize)
    return active_particles, recovering_particles, inactive_particles


  # animation setup
  colors = matplotlib.colors.LinearSegmentedColormap.from_list('C', ['white', 'blue'])
  fig, ax = matplotlib.pyplot.subplots()
  c_plot = matplotlib.pyplot.imshow(C.T, vmin=0, vmax=16, cmap=colors, interpolation='bilinear')
  active_particles_plot, = matplotlib.pyplot.plot([], [], 'bo', ms=1)
  inactive_particles_plot, = matplotlib.pyplot.plot([], [], 'ko', ms=1, alpha=0.2)
  recovering_particles_plot, = matplotlib.pyplot.plot([], [], 'ko', ms=1)
  pacemaker_plot, = matplotlib.pyplot.plot([], [], 'yo', ms=2)

  def init():
    ax.set_xlim([1, gridsize])
    ax.set_ylim([gridsize, 1])

  def update(i):
    # do the time step
    for _ in range(time_steps_per_frame - 1):
      do_time_step()
    active, recovering, inactive = do_time_step()

    # plot particles and the concentration
    ax.axis('off')
    ax.set_title('{:.3f} s'.format(i * dt * time_steps_per_frame))
    c_plot.set_data(C.T)
    active_particles_plot.set_data(particle_locations[active,0] / dx, particle_locations[active,1] / dx)
    inactive_particles_plot.set_data(particle_locations[inactive,0] / dx, particle_locations[inactive,1] / dx)
    recovering_particles_plot.set_data(particle_locations[recovering,0] / dx, particle_locations[recovering,1] / dx)
    pacemaker_plot.set_data(pacemaker_locations[:,0] / dx, pacemaker_locations[:,1] / dx)

  # do and animate the simulation
  animation = matplotlib.animation.FuncAnimation(fig, update, init_func=init, frames=int(T / (dt * time_steps_per_frame)), repeat=True, interval=1, blit=False)
  animation.save(animation_name, fps=30, writer='imagemagick', dpi=dpi)


# run simulations for the parameters given in the parameters file
def main():
  global parameters
  start_point = 1
  for i, parameters in enumerate(parameters[start_point - 1:]):
    # create folder for this simulation if it doesn't exist yet
    folder = 'simulation/{}'.format(i + start_point)
    if not os.path.exists(folder):
      os.makedirs(folder)
    
    # clear folder
    for file in os.listdir(folder):
      os.remove(os.path.join(folder, file))

    # run simulation
    start = time()
    print('Simulating {}'.format(i + start_point))
    simulation(os.path.join(folder, 'animation.gif'), **parameters)
    print('Done in {} s'.format(time() - start))

    # extract a few frames of the animation and save it as a png
    frames = np.round(np.linspace(0, parameters['T'] / (parameters['dt'] * parameters['time_steps_per_frame']) - 1, 8)).astype(int)
    with imageio.get_reader(os.path.join(folder, 'animation.gif')) as reader:
      for frame in frames:
        image = reader.get_data(frame)
        # crop the image
        image = image[25:415, 145:515, :]
        imageio.imwrite(os.path.join(folder, 'frame_{}.png'.format(frame)), image)
    print('Saved images')

    # save tex output to folder
    with open(os.path.join(folder, 'tex.tex'), 'w') as f:
      f.write(tex([os.path.join(folder, 'frame_{}.png'.format(frame)) for frame in frames]))

main()