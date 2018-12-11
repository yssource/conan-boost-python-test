#!/usr/bin/env python
import libclasses as classes

t = classes.World()
t.set("bom dia!")
print(t.greet())

t.many(['Good Morning', 'Buon giorno', 'Kali mera'])
print(t.greet())
