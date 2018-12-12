import controller as c
import model as m
import view as v

ctrl = c.Controller(v.View(), m.Model())

ctrl.start()