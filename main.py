from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Create an empty DataFrame to store user data
data_df=pd.read_csv('static/dftocsv.csv')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    
    sentence = request.form['sentence']
    sentiment = request.form['sentiment']

    # Convert sentiment to 1 for positive, 0 for negative
    sentiment_value = 1 if sentiment.lower() == 'positive' else 0

    # Append data to the DataFrame
    global data_df
    data_df = data_df._append({'Sentence': sentence, 'Sentiment': sentiment_value}, ignore_index=True)
    data_df.to_csv('static/dftocsv.csv',index=False)
    return render_template('form.html', message="Data submitted successfully!")

@app.route('/data')
def show_data():
    return data_df.to_html()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)