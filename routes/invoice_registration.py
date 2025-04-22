from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask
from models.invoice_registration import InvoiceRegistration

invoice_registration_route = Blueprint('invoice', __name__)

@invoice_registration_route.route("/insert-invoice", methods=["GET"])
def form_invoice():
    """formulario para cadastrar uma nota fiscal"""
    return render_template("invoice_registration.html")

@invoice_registration_route.route("/insert-invoice", methods=["POST"])
def insert_invoice():
        data = request.form
        try:
            new_invoice = InvoiceRegistration.create(
                    item_category=data['item_category'], 
                    number_invoice=data['number_invoice'],
                    product_name=data['product_name'],   
                    quantity=data['quantity'],
                    sector=data['sector'],
                    value=data['value'],
                    description=data['description'],
                    identification_document=data['identification_document'],
                    company_name=data['company_name'],
                    address=data['address'],
                    date_issue=data['date_issue'],
                    payment_date=data['payment_date']
                )
            flash('Nota fiscal cadastrada com sucesso!', "success")
            return redirect(url_for('invoice.form_invoice', invoice=new_invoice))
        except:
            flash('Erro ao cadastrar a nota fiscal!', "danger")
            return redirect(url_for('invoice.insert_invoice'))