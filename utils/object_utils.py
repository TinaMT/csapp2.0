class ObjectUtils:

    def equal_str(key, exp_value, act_value):
        assert str(exp_value) == str(act_value), f"[{key}], expected: {exp_value}, but actual: {act_value}"