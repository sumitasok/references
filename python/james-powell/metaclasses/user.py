from library import Base

# if not covered by test
assert hasattr(Base, 'foo'), "You broke it you fool"

class Derived(Base):
    def bar(self):
        return self.foo()

    def bar2(self):
        return 'bar'