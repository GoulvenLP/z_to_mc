class StepSemanticsIntersection:

    def init(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


    def initial(self):
        cs = []
        for lc in self.lhs.initial():
            for rc in self.rhs.initial:
                cs.append((lc, rc))
        return cs


    def actions(self, config):
        """
            @config: the submitted config
        """
        left_config, right_config = config
        synchronous_actions = []
        left_actions = self.lhs.actions(left_config)
        n_actions = len(left_actions) # number of produced actions
        
        # first: assemble the left step
        for left_action in left_actions:
            left_targets = self.lhs.execute(left_action, left_config)
            if len(left_targets) == 0: # an action was not successful: leads to nothing
                n_actions -= 1
            for left_target in left_targets:
                left_step = (left_config, left_action, left_target)
                
                # work on the right side now to assemble the right step
                right_actions = self.rhs.actions(left_step, right_config)
                synchronous_actions.extends(map(lambda right_action : (left_step, right_action), right_actions))
        if n_actions == 0:
            left_step = (left_config, stutter(), left_config)
            right_actions = self.rhs.actions(left_step, right_config)
            synchronous_actions.extends(map(lambda right_action: (left_step, right_action), right_actions))
        return synchronous_actions

