class BaseRule():
    # Base class for all driving rules derived from traffic signs
    pass


class SpeedLimitRule(BaseRule):
    # Rule for limiting vehicle speed
    RULE_TYPE = "speed_limit"

    def __init__(self, value):
        self.value = value


class AccessRestrictionRule(BaseRule):
    # Rule for restricting vehicle movement in specific direction
    RULE_TYPE = "access_restriction_rule"

    def __init__(self, direction):
        self.direction = direction  # Direction is 'straight' for no-entry sign


class MandatoryTurnRule(BaseRule):
    # Rule for enforcing mandatory turn
    RULE_TYPE = "mandatory_turn_rule"

    def __init__(self, direction):
        self.direction = direction


class TrafficLightRule(BaseRule):
    # Rule for representing traffic light state
    RULE_TYPE = "traffic_light"

    def __init__(self, state):
        self.state = state  


class CautionRule(BaseRule):
    # Indicated warning or hazard ahead
    RULE_TYPE = "caution"

    def __init__(self, warning):
        # Warning types are 'speed_bump_ahead', 'hazard', 'yield', 'stop', 'roundabout'
        self.warning = warning  