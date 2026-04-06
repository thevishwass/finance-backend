def calculate_summary(records):

    income = sum(r.amount for r in records if r.type == "income")
    expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income": income,
        "total_expenses": expense,
        "net_balance": income - expense
    }

# for summary of income and expenses