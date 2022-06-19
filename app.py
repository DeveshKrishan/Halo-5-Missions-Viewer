from flask import Flask, render_template
import halo
    
app = Flask(__name__)

@app.route("/")
def home():
    #Grab the data from the HALO API formatted.
    mission_list = halo.get_data(halo.main())
    #Use template to render out page.
    return render_template("index.html", Mission1=mission_list[0], Mission2=mission_list[1], Mission3=mission_list[2], Mission4=mission_list[3], Mission5=mission_list[4], Mission6=mission_list[5], Mission7=mission_list[6], Mission8=mission_list[7], Mission9=mission_list[8], Mission10=mission_list[9], Mission11=mission_list[10], Mission12=mission_list[11], Mission13=mission_list[12], Mission14=mission_list[13], Mission15=mission_list[14])

if __name__ == "__main__":
    #Run the app and allow changes with "debug=True"
    app.run(debug=True)