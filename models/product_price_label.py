from odoo import models

class ReportPriceLabel(models.AbstractModel):
    """
    ReportPriceLabel is an abstract model that generates dynamic price label reports 
    based on configurable paper dimensions and product data.
    It calculates font sizes and barcode image dimensions based on the specified paper size.
    """
    _name = 'report.product_price_label.product_price_label_template'
    _description = 'Dynamic Price Label Report'


    def _get_report_values(self, docids, data=None):
        
        products = self.env['product.template'].browse(docids)
        config = self.env['ir.config_parameter'].sudo()

        width = float(config.get_param('product_price_label.paper_width', default='43'))
        height = float(config.get_param('product_price_label.paper_height', default='35'))

        paperformat_name = f'Dynamic Label {width}x{height} mm'
        paperformat = self.env['report.paperformat'].search([('name', '=', paperformat_name)], limit=1)

        if not paperformat:
            paperformat = self.env['report.paperformat'].create({
                'name': paperformat_name,
                'format': 'custom',
                'page_width': width,
                'page_height': height,
                'orientation': 'Portrait',
                'margin_top': 0,
                'margin_bottom': 0,
                'margin_left': 0,
                'margin_right': 0,
                'header_line': False,
                'dpi': 90,
            })

        # Update report to use this paper format
        # Retrieve the report action for the product price label
        report_action = self.env.ref('product_price_label.action_product_price_label')
        # Assign the dynamically created paper format to the report action
        report_action.paperformat_id = paperformat.id

        # Calculate the font size for the product name based on paper dimensions
        x = (height * 13) / 35
        y = (height * 13) / 43
        font_name = round((x + y) / 2)

        # Calculate the font size for the barcode based on paper dimensions
        x = (height * 12) / 35
        y = (height * 12) / 43
        font_barcode = round((x + y) / 2)

        # Calculate the font size for the price based on paper dimensions
        x = (height * 18) / 35
        y = (height * 18) / 43
        font_price = round((x + y) / 2)

        # Calculate the dimensions of the barcode image based on paper dimensions
        barcode_img_width = round((width * 150) / 43)
        barcode_img_height = round((height * 50) / 35)

        # Return the calculated values and product data to the report template
        return {
            'docs': products,
            'font_name': font_name,
            'font_barcode': font_barcode,
            'font_price': font_price,
            'barcode_img_width': barcode_img_width,
            'barcode_img_height': barcode_img_height,
            # Calculate the scaled image dimensions for rendering
            'img_width': round((barcode_img_width * 400) / 150),
            'img_height': round((barcode_img_height * 100) / 50),
        }
