import controller
import model
import view

m = model.Model()
cards = m.create_cards()
v = view.View(cards)

ctrl = controller.Controller(v,m)

ctrl.start()