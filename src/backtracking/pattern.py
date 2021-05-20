'''正则表达式匹配'''
class Pattern(object):

    def __init__(self, pattern) -> None:
        super().__init__()
        self.matched = False
        self.pattern = pattern
        self.p_len = len(pattern)

    def match(self, text) -> bool:
        t_len = len(text)
        self.pattern_match(0, 0, t_len, text)
        return self.matched

    def pattern_match(self, pi, ti, t_len, text):
        if self.matched:
            return
        if pi == self.p_len:
            if ti == t_len:
                self.matched = True
            return
        if self.pattern[pi] == '*':
            for i in range(t_len-ti+1):
                self.pattern_match(pi+1, ti+i, t_len, text)
        elif self.pattern[pi] == '?':
            self.pattern_match(pi+1, ti, t_len, text)
            self.pattern_match(pi+1, ti+1, t_len, text)
        elif ti < t_len and self.pattern[pi] == text[ti]:
            self.pattern_match(pi+1, ti+1, t_len, text)