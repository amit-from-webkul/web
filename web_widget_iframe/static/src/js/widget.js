openerp.web_widget_iframe = function (instance) {


    instance.web.form.widgets.add('iframe', 'instance.web.form.FieldIFrame');

    instance.web.search.fields.add('iframe', 'instance.web.search.CharField');

    instance.web.form.FieldIFrame = instance.web.form.FieldChar.extend({
        template: 'FieldIFrame',
        widget_class: 'oe_form_field_iframe',

        render_value: function () {
            var show_value = this.format_value(this.get('value'), '');
            this.$el.find('iframe').attr('src', show_value);
        },

        initialize_content: function() {
            var self = this;
            this.$('.oe_iframe_switch').click(function() {
                self.$el.toggleClass('oe_iframe_fullscreen');
                self.$el.find('.oe_iframe_switch').toggleClass('fa-expand fa-compress');
                self.view.$el.find('.oe_chatter').toggle();
                $('#oe_main_menu_navbar').toggle();
            });
            this.render_value();
        }

    });
};
