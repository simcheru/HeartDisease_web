from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main_page.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':

        clf = joblib.load('/Users/simcheol-u/Desktop/project3/model2.pkl')

        BMI = request.form.get('BMI')
        Smoking	= request.form.get('Smoking')
        AlcoholDrinking	= request.form.get('AlcoholDrinking')
        Sex	= request.form.get('Sex')
        AgeCategory	= request.form.get('AgeCategory')
        PhysicalActivity = request.form.get('PhysicalActivity')
        GenHealth = request.form.get('GenHealth')
        SleepTime = request.form.get('SleepTime')
        Race = request.form.get('Race')
        Race_Asian = 0
        Race_Black = 0
        Race_Hispanic = 0
        Race_Other = 0
        Race_White = 0
        
        if Race == 'Asian':
            Race_Asian += 1
        elif Race == 'Black':
            Race_Black += 1
        elif Race == 'Hispanic':
            Race_Hispanic += 1
        elif Race == 'Other':
            Race_Other += 1
        elif Race == 'White':
            Race_White += 1

        X = [[BMI, 
                Smoking, 
                AlcoholDrinking, 
                Sex, 
                AgeCategory,
                PhysicalActivity,
                GenHealth,
                SleepTime, 
                Race_Asian, 
                Race_Black, 
                Race_Hispanic, 
                Race_Other, 
                Race_White]]

        prediction = clf.predict(X)
        
        return render_template('result.html', result = prediction)

if __name__ == '__main__':
    app.run(debug=True)


# import pickle

# with open('model2.pkl', 'rb') as pickle_file:
#     model = pickle.load(pickle_file)

# X_test = [[20, 0, 0, 0, 77, 1, 3, 7, 0, 0, 0, 0, 1]]

# y_pred = model.predict(X_test)

# print(y_pred)