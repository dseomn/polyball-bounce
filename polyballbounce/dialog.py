import math
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
  def cb_hazard_size(self, widget, index):
    if index == 0:
      self.config.hazard['size'] = (widget.get_value(), self.config.hazard['size'][1])
    elif index == 1:
      self.config.hazard['size'] = (self.config.hazard['size'][0], widget.get_value())
  def cb_player(self, widget, player):
    for k, v in self.config.player['type_name'].iteritems():
      if v == widget.get_model()[widget.get_active()][0]:
        self.config.paddle['paddle_type'][player] = k
        return
  def cb_paddle_curvature(self, widget):
    self.config.paddle['curvature'] = widget.get_value()

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

    vbox_labels.pack_start(gtk.Label('Corner width'))
    adj = gtk.Adjustment(self.config.hazard['size'][0], 0, math.floor((self.config.size[0] - self.config.paddle['size_horizontal'][0] - 2*self.config.pixel_margin)/2), 1)
    scale = gtk.HScale(adj)
    scale.connect('value-changed', self.cb_hazard_size, 0)
    vbox_controls.pack_start(scale)

    vbox_labels.pack_start(gtk.Label('Corner height'))
    adj = gtk.Adjustment(self.config.hazard['size'][1], 0, math.floor((self.config.size[1] - self.config.paddle['size_vertical'][1] - 2*self.config.pixel_margin)/2), 1)
    scale = gtk.HScale(adj)
    scale.connect('value-changed', self.cb_hazard_size, 1)
    vbox_controls.pack_start(scale)

    for player in self.config.PLAYER_ALL:
      vbox_labels.pack_start(gtk.Label(self.config.player['name'][player]))
      liststore = gtk.ListStore(str)
      cbox = gtk.ComboBox(liststore)
      cell = gtk.CellRendererText()
      cbox.pack_start(cell)
      cbox.add_attribute(cell, 'text', 0)
      for p_type in self.config.PLAYER_TYPES_ALL:
        treeiter = liststore.append([self.config.player['type_name'][p_type]])
        if p_type == self.config.paddle['paddle_type'][player]:
          cbox.set_active_iter(treeiter)
      cbox.connect('changed', self.cb_player, player)
      vbox_controls.pack_start(cbox)

    vbox_labels.pack_start(gtk.Label('Paddle curvature'))
    range = float(self.config.paddle['curvature_range'][1]-self.config.paddle['curvature_range'][0])
    num_steps = 1000
    num_pages = 100
    adj = gtk.Adjustment(self.config.paddle['curvature'], self.config.paddle['curvature_range'][0], self.config.paddle['curvature_range'][1], range/num_steps, range/num_pages)
    scale = gtk.HScale(adj)
    scale.set_digits(int(max(0,-math.log(range/num_steps, 10))))
    scale.connect('value-changed', self.cb_paddle_curvature)
    vbox_controls.pack_start(scale)

    but = gtk.Button(stock=gtk.STOCK_OK)
    but.connect_object('clicked', gtk.Widget.destroy, window)
    hbox_bottom.pack_end(but, expand=False)

    window.show_all()
    gtk.main()
