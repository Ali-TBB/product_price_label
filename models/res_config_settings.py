from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    """
    ResConfigSettings class extends the 'res.config.settings' model to add configuration
    parameters for label dimensions.
    """
    _inherit = 'res.config.settings'

    paper_width = fields.Float(
        string="Label Width (mm)",
        config_parameter='product_price_label.paper_width',
        default=43.0
    )

    paper_height = fields.Float(
        string="Label Height (mm)",
        config_parameter='product_price_label.paper_height',
        default=35.0
    )
