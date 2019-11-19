# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class CreateFundWizard(models.TransientModel):

    _name = "account.pettycash.fund.create"
    _description = "Petty Cash Fund Creation Wizard"

    # Fields
    #
    fund_name = fields.Char(required=True)
    fund_code = fields.Char(required=True)
    fund_amount = fields.Monetary(string="Monto", required=True)
    custodian_id = fields.Many2one("res.partner", required=True)
    account = fields.Many2one("account.account", required=True)
    payable_account = fields.Many2one(
        "account.account", required=True, domain=[("type", "=", "payable")]
    )
    effective_date = fields.Date(required=True)
    payable_move = fields.Many2one("account.move", string="Journal Entry")
    fund = fields.Many2one("account.pettycash.fund")

    @api.multi
    def initialize_fund(self):

        # Create the petty cash fund
        #
        FndObj = self.env["account.pettycash.fund"]
        for wizard in self:
            fnd = FndObj.create_fund(
                wizard.fund_amount,
                wizard.fund_name,
                wizard.fund_code,
                wizard.custodian,
                wizard.account,
            )

            desc = _("Establish Petty Cash Fund (%s)" % (wizard.fund_name))

            # Create payable account entry and post it
            #
            move = fnd.create_payable_journal_entry(
                fnd,
                wizard.payable_account.id,
                wizard.effective_date,
                wizard.fund_amount,
                desc,
            )
            wizard.payable_move = move
            wizard.fund = fnd
