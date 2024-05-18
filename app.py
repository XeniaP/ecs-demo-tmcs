from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

s3 = boto3.client('s3')
BUCKET_NAME = 'tu-bucket-s3'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    s3.put_object(Bucket=BUCKET_NAME, Key='data.txt', Body=data)
    return 'Datos guardados en S3'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
