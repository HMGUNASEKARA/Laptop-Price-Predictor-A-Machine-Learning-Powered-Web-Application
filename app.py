from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)

def prediction(lst):
    filename = 'Model/Predicttor.pickle'
    with open(filename,'rb') as file:
        model = pickle.load(file)
    pred_value =model.predict([lst])
    return pred_value

@app.route('/',methods=['POST','GET'])
def index():
    pred = 0
    if request.method == 'POST':
         ram = request.form['ram']
         weight = request.form['weight']
         company = request.form['company']
         typename = request.form['typename']
         opsys = request.form['opsys']
         cpu = request.form['cpuname']
         gpu = request.form['gpuname']
         touchscreen = request.form.getlist('touchscreen')
         ips = request.form.getlist('ips')

                 
         
         feature_list = []
         feature_list.append(int(ram))
         feature_list.append(float(weight))
         feature_list.append(len(touchscreen ))
         feature_list.append(len(ips))

         company_list =["acer","apple","asus","dell","hp","lenovo","msi","toshiba","other"]
         tyname_list = ["2in1convertible","gaming","netbook","notebook","ultrabook","workstation"]
         opsays_list = ["windows","mac","linux","other"]
         cpu_list = ["intelcorei3","intelcorei5","intelcorei7","amd","other"]
         gpu_list = ["intel","amf","nvidia"]

        
         def get_list(lst,value):
          for item in lst:
             if item == value:
                 feature_list.append(1)
             else:
                 feature_list.append(0)
         

         get_list(company_list,company)
         get_list(tyname_list,typename)
         get_list(opsays_list,opsays_list)
         get_list(cpu_list,cpu)
         get_list(gpu_list,gpu)
    
         #print(feature_list)

         pred = (prediction(feature_list)*344)-400000
         pred = np.round(pred[0])
    return render_template("index.html",pred = pred)


if __name__ == '__main__':
    app.run(debug=True)

    