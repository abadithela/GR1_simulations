import logging
from tulip import spec
from tulip import synth
from tulip.transys import machines
from tulip import dumpsmach

logging.basicConfig(level=logging.WARNING)

env_vars = {}
sys_vars = {}
env_vars['b'] = (1,3)
sys_vars['r'] = (1,4)

env_init = {'b=2'}
sys_init = {'r=1'}

env_safe = {
            'b=1 -> X(b=2)', 
            'b=2 -> X(b=1 || b=3)', 
            'b=3 -> X(b=2)',
           }

sys_safe = {
            'r = 1 -> X(r=1 || r=2 || r=3)',
            'r = 2 -> X(r=4)',
            'r = 3 -> X(r=4)',
            'r = 4 -> X(r=4)',
           }

# Avoid collision:
sys_safe |= {
             '(b=2 -> !(r=2))',
             '(b=3 -> !(r=3))'
}

env_prog = {}
sys_prog = {'r=4'}

# Create a GR(1) specification
specs = spec.GRSpec(env_vars, sys_vars, env_init, sys_init, env_safe, sys_safe, env_prog, sys_prog)
# Print specifications:
print(specs.pretty())
#
# Controller synthesis
#
# The controller decides based on current variable values only,
# without knowing yet the next values that environment variables take.
# A controller with this information flow is known as Moore.
specs.moore = True
# Ask the synthesizer to find initial values for system variables
# that, for each initial values that environment variables can
# take and satisfy `env_init`, the initial state satisfies
# `env_init /\ sys_init`.
specs.qinit = r'\E \A'  # i.e., "there exist sys_vars: forall env_vars"

# At this point we can synthesize the controller
# using one of the available methods.
strategy = synth.synthesize(specs)
assert strategy is not None, 'unrealizable'

dumpsmach.write_python_case('rb.py', strategy, classname='runner')
