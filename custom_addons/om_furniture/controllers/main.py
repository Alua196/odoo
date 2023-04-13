from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post)
        print("res.....", res.qcontext)
        # print("Inherited...", res, type(res))
        return res


class Furniture(http.Controller):
    @http.route([
        '''/furniture/products/''',
        '''/furniture/products/page/<int:page>'''
    ], auth='public', website=True)
    def furniture_products(self, page=1, **kw):
        products = request.env['furniture.products']
        total_p = products.search_count([])
        page_det = pager(url='/furniture/products/', total=total_p, page=page, step=5)
        pr = products.search([], limit=5, offset=page_det['offset'])
        values = {'pr': pr,
                  'page_name': 'items_list',
                  'pager': page_det}
        return request.render("om_furniture.products_page", values)
        # return request.render("om_furniture.products_page", {})