from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    salary = float(request.form['salary'])
    rent = float(request.form['rent'])
    utilities = float(request.form['utilities'])
    miscellaneous = float(request.form['miscellaneous'])
    goal = float(request.form['goal'])

    # Calculate total income and expenses
    total_income = salary
    total_expense = rent + utilities + miscellaneous

    # Calculate the necessary savings to reach the goal
    necessary_savings = total_income - goal if total_income > goal else goal - total_income

    # Create the expense breakdown
    expenses = {
        'Rent': rent,
        'Utilities': utilities,
        'Miscellaneous': miscellaneous
    }

    # Plot expense breakdown
    plt.figure(figsize=(10, 6))
    plt.bar(expenses.keys(), expenses.values(), color='salmon')
    plt.title('Current Expenses by Category')
    plt.savefig('static/expense_plot.png')
    plt.close()

    # Calculate savings per category to meet the goal
    total_expense_value = sum(expenses.values())
    savings_per_category = {k: v / total_expense_value * necessary_savings for k, v in expenses.items()}

    # Plot savings plan
    plt.figure(figsize=(10, 6))
    plt.bar(savings_per_category.keys(), savings_per_category.values(), color='green')
    plt.title('Required Savings by Category')
    plt.savefig('static/savings_plot.png')
    plt.close()

    # Pass results to the summary page
    report = {
        'total_income': total_income,
        'total_expense': total_expense,
        'necessary_savings': necessary_savings,
        'savings_per_category': savings_per_category
    }

    plots = {
        'expense_plot': 'static/expense_plot.png',
        'savings_plot': 'static/savings_plot.png'
    }

    return render_template('summary.html', report=report, plots=plots)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
