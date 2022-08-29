import numpy as np

parameters = [
  dict( #1
    # number of particles                   unitless
    N = 5000,
    # size of the mesh                      length
    size = 10,
    # size of the grid step                 length
    dx = 0.1,
    # size of the time step                 time
    dt = 0.0006,
    # diffusion rate                        length^2/time
    alpha = 3,
    # chemical decay rate                   1/time
    beta = 32,
    # time in active state                  time
    t_a = 0.004,
    # time in recovery state                time
    t_r = 0.06,
    # emission rate                         concentration/time
    gamma = 6_000,
    # emission rate of pacemaker particles  concentration/time
    gamma_pacemaker = 15_000,
    # excitation threshold                  concentration
    tau = 1.5,
    # random movement distance              length
    movement_random = 0.03,
    # movement distance                     length
    movement_distance = 0.03,
    # movement threshold                    concentration/length
    movement_threshold = 1,
    # max time                              time
    T = 3,
    # pacemaker particles (x, y, s)
    pacemakers = [
      (
        2.5,
        5,
        0.004
      )
    ],
    # particle distribution
    distribution = np.concatenate([[(r := np.sqrt(np.random.rand(5000) * 15 + 1)) * np.sin(phi := np.random.rand(5000) * 2 * np.pi) + 5], [r * np.cos(phi) + 5]], axis=0).T,
    # time step to do in a single frame
    time_steps_per_frame = 10,
    # dpi of the output image
    dpi = 100,
  ),
  dict( #2
    # number of particles                   unitless
    N = 5000,
    # size of the mesh                      length
    size = 10,
    # size of the grid step                 length
    dx = 0.1,
    # size of the time step                 time
    dt = 0.0006,
    # diffusion rate                        length^2/time
    alpha = 3,
    # chemical decay rate                   1/time
    beta = 32,
    # time in active state                  time
    t_a = 0.004,
    # time in recovery state                time
    t_r = 0.06,
    # emission rate                         concentration/time
    gamma = 6_000,
    # emission rate of pacemaker particles  concentration/time
    gamma_pacemaker = 15_000,
    # excitation threshold                  1/length^2
    tau = 1.5,
    # random movement distance              length
    movement_random = 0.03,
    # movement distance                     length
    movement_distance = 0.03,
    # movement threshold                    concentration/length
    movement_threshold = 1,
    # max time                              time
    T = 3,
    # pacemaker particles (x, y, s)
    pacemakers = [
      (
        2.5,
        5,
        0.004
      )
    ],
    # particle distribution
    distribution = np.concatenate([[(r := np.random.rand(5000) * 4) * np.sin(phi := np.random.rand(5000) * 2 * np.pi) + 5], [r * np.cos(phi) + 5]], axis=0).T,
    # time step to do in a single frame
    time_steps_per_frame = 10,
    # dpi of the output image
    dpi = 100,
  ),
  dict( #3
    # number of particles                   unitless
    N = 5000,
    # size of the mesh                      length
    size = 10,
    # size of the grid step                 length
    dx = 0.1,
    # size of the time step                 time
    dt = 0.0006,
    # diffusion rate                        length^2/time
    alpha = 3,
    # chemical decay rate                   1/time
    beta = 32,
    # time in active state                  time
    t_a = 0.004,
    # time in recovery state                time
    t_r = 0.06,
    # emission rate                         concentration/time
    gamma = 6_000,
    # emission rate of pacemaker particles  concentration/time
    gamma_pacemaker = 15_000,
    # excitation threshold                  1/length^2
    tau = 1.5,
    # random movement distance              length
    movement_random = 0.03,
    # movement distance                     length
    movement_distance = 0.03,
    # movement threshold                    concentration/length
    movement_threshold = 1,
    # max time                              time
    T = 3,
    # pacemaker particles (x, y, s)
    pacemakers = [
      (
        2.5,
        5,
        0.004
      )
    ],
    # particle distribution
    distribution = np.concatenate([[(r := (np.random.rand(5000) * 64) ** (1 / 3)) * np.sin(phi := np.random.rand(5000) * 2 * np.pi) + 5], [r * np.cos(phi) + 5]], axis=0).T,
    # time step to do in a single frame
    time_steps_per_frame = 10,
    # dpi of the output image
    dpi = 100,
  ),
  dict( #4
    # number of particles                   unitless
    N = 5000,
    # size of the mesh                      length
    size = 10,
    # size of the grid step                 length
    dx = 0.1,
    # size of the time step                 time
    dt = 0.0006,
    # diffusion rate                        length^2/time
    alpha = 3,
    # chemical decay rate                   1/time
    beta = 32,
    # time in active state                  time
    t_a = 0.004,
    # time in recovery state                time
    t_r = 0.06,
    # emission rate                         concentration/time
    gamma = 6_000,
    # emission rate of pacemaker particles  concentration/time
    gamma_pacemaker = 15_000,
    # excitation threshold                  1/length^2
    tau = 1.5,
    # random movement distance              length
    movement_random = 0.03,
    # movement distance                     length
    movement_distance = 0.03,
    # movement threshold                    concentration/length
    movement_threshold = 1,
    # max time                              time
    T = 3,
    # pacemaker particles (x, y, s)
    pacemakers = [
      (
        2.5,
        5,
        0.004
      )
    ],
    # particle distribution
    distribution = np.concatenate([[(r := (np.random.rand(5000) * 256) ** (1 / 4)) * np.sin(phi := np.random.rand(5000) * 2 * np.pi) + 5], [r * np.cos(phi) + 5]], axis=0).T,
    # time step to do in a single frame
    time_steps_per_frame = 10,
    # dpi of the output image
    dpi = 100,
  ),
  dict( #5
    # number of particles                   unitless
    N = 5000,
    # size of the mesh                      length
    size = 10,
    # size of the grid step                 length
    dx = 0.1,
    # size of the time step                 time
    dt = 0.0006,
    # diffusion rate                        length^2/time
    alpha = 3,
    # chemical decay rate                   1/time
    beta = 32,
    # time in active state                  time
    t_a = 0.004,
    # time in recovery state                time
    t_r = 0.06,
    # emission rate                         concentration/time
    gamma = 6_000,
    # emission rate of pacemaker particles  concentration/time
    gamma_pacemaker = 15_000,
    # excitation threshold                  1/length^2
    tau = 1.5,
    # random movement distance              length
    movement_random = 0.03,
    # movement distance                     length
    movement_distance = 0.03,
    # movement threshold                    concentration/length
    movement_threshold = 1,
    # max time                              time
    T = 6,
    # pacemaker particles (x, y, s)
    pacemakers = [
      (
        5,
        5,
        0.004
      )
    ],
    # particle distribution
    distribution = np.concatenate([[x := np.random.rand(5000) * 8 + 1], [3 * (np.sin(5 * (x - 5)) + 1) + 2 + np.random.rand(5000) * 1.5 - 0.75]], axis=0).T,
    # time step to do in a single frame
    time_steps_per_frame = 10,
    # dpi of the output image
    dpi = 100,
  ),
  dict( #6
    # number of particles                   unitless
    N = 5000,
    # size of the mesh                      length
    size = 10,
    # size of the grid step                 length
    dx = 0.1,
    # size of the time step                 time
    dt = 0.0006,
    # diffusion rate                        length^2/time
    alpha = 3,
    # chemical decay rate                   1/time
    beta = 32,
    # time in active state                  time
    t_a = 0.004,
    # time in recovery state                time
    t_r = 0.06,
    # emission rate                         concentration/time
    gamma = 6_000,
    # emission rate of pacemaker particles  concentration/time
    gamma_pacemaker = 15_000,
    # excitation threshold                  1/length^2
    tau = 1.5,
    # random movement distance              length
    movement_random = 0.03,
    # movement distance                     length
    movement_distance = 0.03,
    # movement threshold                    concentration/length
    movement_threshold = 1,
    # max time                              time
    T = 3,
    # pacemaker particles (x, y, s)
    pacemakers = [
      (
        2.5,
        5,
        0.004
      )
    ],
    # particle distribution
    distribution = np.concatenate([[(r := (np.random.rand(5000) * 2) ** 2) * np.sin(phi := np.random.rand(5000) * 2 * np.pi) + 5], [r * np.cos(phi) + 5]], axis=0).T,
    # time step to do in a single frame
    time_steps_per_frame = 10,
    # dpi of the output image
    dpi = 100,
  ),
  dict( #7
    # number of particles                   unitless
    N = 5000,
    # size of the mesh                      length
    size = 10,
    # size of the grid step                 length
    dx = 0.1,
    # size of the time step                 time
    dt = 0.0006,
    # diffusion rate                        length^2/time
    alpha = 3,
    # chemical decay rate                   1/time
    beta = 32,
    # time in active state                  time
    t_a = 0.004,
    # time in recovery state                time
    t_r = 0.06,
    # emission rate                         concentration/time
    gamma = 6_000,
    # emission rate of pacemaker particles  concentration/time
    gamma_pacemaker = 15_000,
    # excitation threshold                  1/length^2
    tau = 1.5,
    # random movement distance              length
    movement_random = 0.03,
    # movement distance                     length
    movement_distance = 0.03,
    # movement threshold                    concentration/length
    movement_threshold = 1,
    # max time                              time
    T = 5,
    # pacemaker particles (x, y, s)
    pacemakers = [
      (
        2.5,
        5,
        0.004
      ),
      (
        7.5,
        5,
        0.004
      )
    ],
    # particle distribution
    distribution = np.random.rand(5000, 2) * 8 + 1,
    # time step to do in a single frame
    time_steps_per_frame = 10,
    # dpi of the output image
    dpi = 100,
  ),
  dict( #8
    # number of particles                   unitless
    N = 5000,
    # size of the mesh                      length
    size = 10,
    # size of the grid step                 length
    dx = 0.1,
    # size of the time step                 time
    dt = 0.0006,
    # diffusion rate                        length^2/time
    alpha = 3,
    # chemical decay rate                   1/time
    beta = 32,
    # time in active state                  time
    t_a = 0.004,
    # time in recovery state                time
    t_r = 0.06,
    # emission rate                         concentration/time
    gamma = 6_000,
    # emission rate of pacemaker particles  concentration/time
    gamma_pacemaker = 15_000,
    # excitation threshold                  1/length^2
    tau = 1.5,
    # random movement distance              length
    movement_random = 0.03,
    # movement distance                     length
    movement_distance = 0.03,
    # movement threshold                    concentration/length
    movement_threshold = 1,
    # max time                              time
    T = 5,
    # pacemaker particles (x, y, s)
    pacemakers = [
      (
        2.5,
        5,
        0.004
      ),
      (
        7.5,
        5,
        -0.06
      )
    ],
    # particle distribution
    distribution = np.random.rand(5000, 2) * 8 + 1,
    # time step to do in a single frame
    time_steps_per_frame = 10,
    # dpi of the output image
    dpi = 100,
  ),
]