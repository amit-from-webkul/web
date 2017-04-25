/* Copyright 2017 Therp BV, ACSONE SA/NV
 *  * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define('web.web_ir_actions_act_window_message', function (require) {
    "use strict";

    var ActionManager = require('web.ActionManager'),
        core = require('web.core'),
        _ = require('_'),
        Dialog = require('web.Dialog');

    var _t = core._t;

    ActionManager.include({
        ir_actions_act_window_message: function(action, options) {
            var self = this;
            var def = $.Deferred();
            options = _.extend(
                {
                    size: 'medium',
                    title: action.title,
                    $content: $('<div>', {
                        text: action.message,
                    }),
                    buttons: [
                        {
                            text: _t('Close'),
                            click: function() { this.close() }, //TODO: a better way to refresh parent view after the dialog close
                            oe_link_class: 'oe_highlight',
                        },
                    ],
                },
                options
            );
            new Dialog(self, options).open();
            return def.promise();
        }
    });
});
