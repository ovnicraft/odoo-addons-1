# -*- coding: utf-8 -*-

{
    "name": "Petty Cash",
    "summary": "Automated management of petty cash funds",
    "description": """
    """,
    "author": "Sucros Clear Information Technologies PLC, Cristian Salamea",
    "website": "http://www.clearict.com/",
    "license": "AGPL-3",
    "version": "10.0.1.0.0",
    "category": "Accounting & Finance",
    "depends": ["l10n_ec_withholding", "account_voucher"],
    "data": [
        "security/petty_cash.xml",
        "security/ir.model.access.csv",
        # "wizard/change_fund_view.xml",
        # "wizard/close_fund_view.xml",
        # "wizard/create_fund_view.xml",
        # "wizard/issue_voucher_view.xml",
        # "wizard/reconcile_view.xml",
        # "wizard/reopen_view.xml",
        "views/petty_cash_view.xml",
    ],
    "installable": True,
    "active": True,
}
