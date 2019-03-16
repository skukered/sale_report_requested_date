# -*- coding: utf-8 -*-
# Copyright 2018 Iterativo - Rubén Bravo <rubenred18@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    requested_date = fields.Datetime('Requested Date', readonly=True)

    def _select(self):

        select_str = super(SaleReport, self)._select()
        select_str += ", s.requested_date as requested_date"
        return select_str

    def _group_by(self):
        group_by_str = super(SaleReport, self)._group_by()
        group_by_str += ", s.requested_date"
        return group_by_str
