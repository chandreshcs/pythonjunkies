from flask import Flask, render_template, request

app = Flask(__name__)


def convert_number(num_str):
    num_str = num_str.strip().lower()

    # Decimal float
    if "." in num_str:
        value = float(num_str)
        return {
            "Binary": "N/A",
            "Octal": "N/A",
            "Decimal": value,
            "Hexadecimal": "N/A"
        }

    # Integer (prefix-based)
    value = int(num_str, 0)

    return {
        "Binary": bin(value)[2:],
        "Octal": oct(value)[2:],
        "Decimal": value,
        "Hexadecimal": hex(value)[2:].upper()
    }


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        num_str = request.form["number"]

        try:
            result = convert_number(num_str)
        except ValueError:
            error = "Invalid number format"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
