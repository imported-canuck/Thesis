from shape_library import *
from spectrum_alignment import *
#import os
#os.environ["CUDA_VISIBLE_DEVICES"]="1"

params = OptimizationParams()
params.min_eval_loss = 0.0001
params.evals = [20]
params.numsteps = 3000
params.volume_reg = 1e3 ## Modified

[VERT, TRIV] = load_mesh('data/round_cuber_1000/');
mesh = prepare_mesh(VERT,TRIV,'float32')

[VERT_t, TRIV_t] = load_mesh('data/bunny/')
evals_t = calc_evals(VERT_t,TRIV_t)

run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/bunny_disp', params = params)
