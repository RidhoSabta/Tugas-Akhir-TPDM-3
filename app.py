from flask import Flask, request, render_template
import pickle
import numpy

app = Flask(__name__)

model_file = open('gold.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', Price=0)

@app.route('/predict', methods=['POST'])
def predict():

    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
   
    Open, High, Low = [x for x in request.form.values()]






    data = []

    data.append(float(Open))
    data.append(float(High))
    data.append(float(Low))




    prediction = model.predict([data])
    output = round(float(prediction[0]),2)
    
    return render_template('index.html', Price=output, Open=Open, High=High, Low=Low)

if __name__ == '__main__':
    app.run(debug=True)
