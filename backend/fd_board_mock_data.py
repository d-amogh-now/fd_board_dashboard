from datetime import date

def get_mock_fd_data():
    return {
        "profile": {
            "name": "Amogh Desai",
            "dob": "1991-05-20",
            "pan": "ABCDE1234F"
        },
        "summary": {
            "deposits": [
                {
                    "bank_name": "HDFC Bank",
                    "account_type": "Term Deposit",
                    "account_number": "123456789",
                    "currency": "INR",
                    "principal_amount": 300000,
                    "interest_rate": 6.5,
                    "maturity_amount": 348000,
                    "maturity_date": "2026-04-01"
                },
                {
                    "bank_name": "SBI",
                    "account_type": "Term Deposit",
                    "account_number": "987654321",
                    "currency": "INR",
                    "principal_amount": 200000,
                    "interest_rate": 6.8,
                    "maturity_amount": 238000,
                    "maturity_date": "2025-10-01"
                }
            ]
        }
    }