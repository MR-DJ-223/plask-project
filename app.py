from flask import Flask,redirect,url_for
import jinja2,os


landing_zone=Flask(__name__)

def render_template(template, **kwargs):return jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)))).get_template(template).render(**kwargs)

@landing_zone.route('/HOME/')
def useless():
    return  render_template("./lz.html")
    

@landing_zone.route('/')
def starting():
    # return render_template("./templates/lz.html")
    return render_template('./templates/lz.html')


# landing_zone.add_url_rule('/landingZone',"LZ",landing_zone)

if __name__=="__main__":
    landing_zone.run(debug=True)



