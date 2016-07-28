"use strict";
openerp.web_calendar_description = function(instance) {
    var _t = instance.web._t, QWeb = instance.web.qweb;

    instance.web_calendar.CalendarView.include({

        view_loading : function(fv) {
            var self = this;
            var res = self._super(fv);
            if (self.dataset.context.calendar_description != undefined) {
                var model = new instance.web.Model('ir.config_parameter');
                var key = self.dataset.context.calendar_description;
                model.call('get_param', [ key ]).then(
                        function(calendar_description) {
                            if (calendar_description) {
                                self.$el.parent().prepend(
                                        "<div><b>" + calendar_description
                                                + "</b><div>");
                            }
                        });
            }
            return res;
        },
    });
}
