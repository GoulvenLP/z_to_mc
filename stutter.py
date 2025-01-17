

class Stutter:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


    def execute(self, action, config):
        left_step, right_action = action
        left_config, right_config = config

        right_targets = self.rhs.execute(right_action, left_step, right_config)

        # for each target obtained on the right side, map it
        left_config, left_action, left_target = left_step

        targets = map(lambda right_target: (left_target, right_target), right_targets)
        return list(targets)
