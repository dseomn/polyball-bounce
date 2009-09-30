import pygtk
pygtk.require('2.0')
import gtk

class ConfigDialog(object):
  def __init__(self, config, levels):
    self.config = config
    self.levels = levels

  def cb_ball_num(self, widget):
    self.config.ball['num'] = widget.get_value_as_int()
  def cb_level(self, widget):
    self.levels[widget.get_model()[widget.get_active()][0]].init(self.config)

  def show(self):
    window = gtk.Window()
    window.set_title('Configure ' + self.config.name)
    window.set_icon_from_file(self.config.icon_file)
    window.connect('delete_event', lambda widget, data=None: False)
    window.connect('destroy', lambda widget, data=None: gtk.main_quit())

    # set up boxes
    vbox_outer = gtk.VBox(False, 10)
    vbox_outer.set_border_width(10)
    window.add(vbox_outer)

    hbox = gtk.HBox(False, 10)
    vbox_outer.pack_start(hbox)

    hbox_bottom = gtk.HBox(False, 10)
    vbox_outer.pack_start(hbox_bottom)

    vbox_labels = gtk.VBox(True, 10)
    hbox.pack_start(vbox_labels)

    vbox_controls = gtk.VBox(True, 10)
    hbox.pack_start(vbox_controls)

    # set up widgets in boxes
    vbox_labels.pack_start(gtk.Label('Balls'))
    adj = gtk.Adjustment(self.config.ball['num'], 1, self.config.ball['num_max'], 1)
    spin = gtk.SpinButton(adj)
    spin.set_wrap(False)
    spin.connect('value-changed', self.cb_ball_num)
    vbox_controls.pack_start(spin)

    vbox_labels.pack_start(gtk.Label('Level'))
    liststore = gtk.ListStore(str)
    cbox = gtk.ComboBox(liststore)
    cell = gtk.CellRendererText()
    cbox.pack_start(cell)
    cbox.add_attribute(cell, 'text', 0)
    for level_name in self.levels.iterkeys():
      treeiter = liststore.append([level_name])
      if level_name == self.config.level_name:
        cbox.set_active_iter(treeiter)
    cbox.connect('changed', self.cb_level)
    vbox_controls.pack_start(cbox)

    but = gtk.Button(stock=gtk.STOCK_OK)
    but.connect_object('clicked', gtk.Widget.destroy, window)
    hbox_bottom.pack_end(but, expand=False)

    window.show_all()
    gtk.main()
